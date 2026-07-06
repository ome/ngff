import os
import yaml
from docutils import nodes
from docutils.parsers.rst import Directive


def _read_front_matter(path):
    try:
        with open(path, encoding="utf-8") as f:
            text = f.read()
    except OSError:
        return {}
    parts = text.split("---", 2)
    if len(parts) < 3:
        return {}
    try:
        return yaml.safe_load(parts[1]) or {}
    except yaml.YAMLError:
        return {}


def _numbered_subdirs(base):
    if not os.path.isdir(base):
        return
    for e in os.listdir(base):
        p = os.path.join(base, e)
        if os.path.isdir(p) and e != "index":
            yield e, p


def _folder_sort_key(label):
    """'1' -> (1, ''), '1b' -> (1, 'b'), so rounds sort after their round 1."""
    num = "".join(c for c in label if c.isdigit())
    suffix = "".join(c for c in label if not c.isdigit())
    return (int(num) if num else 0, suffix)


def _thread_stem(label):
    """'1b' -> '1', '12c' -> '12'. Used to count threads, not documents."""
    i = len(label)
    while i > 0 and label[i - 1].isalpha():
        i -= 1
    return label[:i] or label


def _collect_section(rfc_dir, section):
    """Return list of (label, meta), sorted by folder key (round-aware)."""
    base = os.path.join(rfc_dir, section)
    rows = []
    for label, subdir in _numbered_subdirs(base):
        index_path = os.path.join(subdir, "index.md")
        if not os.path.isfile(index_path):
            continue
        rows.append((label, _read_front_matter(index_path)))
    rows.sort(key=lambda r: _folder_sort_key(r[0]))
    return rows


def _thread_count(rows):
    return len({_thread_stem(label) for label, _ in rows})


def _count_versions(rfc_dir):
    base = os.path.join(rfc_dir, "versions")
    return sum(1 for _ in _numbered_subdirs(base)) if os.path.isdir(base) else 0


class RFCStatus(Directive):
    SECTION_LABELS = {
        "reviews": ("Reviewer", "Review"),
        "comments": ("Commenter", "Comment"),
        "responses": ("Author", "Response"),
    }

    def run(self):
        env = self.state.document.settings.env
        src = env.doc2path(env.docname)
        rfc_dir = os.path.dirname(src)
        central = _read_front_matter(src)

        reviews = _collect_section(rfc_dir, "reviews")
        comments = _collect_section(rfc_dir, "comments")
        responses = _collect_section(rfc_dir, "responses")
        n_versions = _count_versions(rfc_dir)

        all_dates = [
            str(m.get("date", ""))
            for _, m in (reviews + comments + responses)
            if m.get("date")
        ]
        last_update = max(all_dates) if all_dates else str(central.get("date", ""))

        result = []

        summary = nodes.paragraph(classes=["rfc-status-summary"])
        summary += nodes.Text(
            f"As of the last update, {last_update}: "
            f"{_thread_count(comments)} comments, "
            f"{_thread_count(reviews)} reviews, "
            f"{_thread_count(responses)} responses, "
        )
        result.append(summary)
        result.append(nodes.Text("\n Authors and editors:"))
        result.append(self._people_table(central))
        result.append(nodes.Text("\n Reviews, comments, and responses:"))
        result.append(self._activity_table(reviews, comments, responses))
        return result

    # ---- Table 1: Authors + Editors ----

    def _people_table(self, central):
        cols = ["Role", "Name", "GitHub", "Institution", "Date", "Status"]
        table, tbody = self._new_table(cols, (10, 22, 20, 22, 10, 16))
        for person in central.get("authors", []):
            tbody += self._person_row(person, "Author")
        for person in central.get("editors", []):
            tbody += self._person_row(person, "Editor")
        return table

    def _person_row(self, person, role):
        row = nodes.row()
        row += self._text_entry(role)
        row += self._text_entry(person.get("name", ""))
        gh = person.get("github")
        row += self._github_entry([gh] if gh else [])
        row += self._text_entry(person.get("affiliation", ""))
        row += self._text_entry(str(person.get("date", "")))
        row += self._text_entry(person.get("role", ""))
        return row

    # ---- Table 2: Reviews + Comments + Responses (one row per round) ----

    def _activity_table(self, reviews, comments, responses):
        cols = ["Link", "Name", "GitHub", "Institution", "Date", "Rec."]
        table, tbody = self._new_table(cols, (12, 22, 18, 20, 12, 16))
        for section, rows in (
            ("reviews", reviews),
            ("comments", comments),
            ("responses", responses),
        ):
            _, link_label = self.SECTION_LABELS[section]
            for label, meta in rows:
                tbody += self._activity_row(
                    meta,
                    f"{link_label}\u00a0{label}",  # non-breaking space
                    f"./{section}/{label}/index",
                )
        return table

    def _activity_row(self, meta, link_text, link_target):
        authors = meta.get("authors", [])
        names = ", ".join(a.get("name", "") for a in authors if a.get("name"))
        handles = [a["github"] for a in authors if a.get("github")]
        affils = []
        for a in authors:
            aff = a.get("affiliation")
            if aff and aff not in affils:
                affils.append(aff)
        recommendation = str(meta.get("recommendation", "")).replace("_", " ")

        row = nodes.row()
        row += self._status_entry(link_text, link_target)
        row += self._text_entry(names)
        row += self._github_entry(handles)
        row += self._text_entry(", ".join(affils))
        row += self._text_entry(str(meta.get("date", "")))
        row += self._text_entry(recommendation)
        return row

    # ---- shared builders ----

    def _new_table(self, cols, widths):
        table = nodes.table()
        tgroup = nodes.tgroup(cols=len(cols))
        table += tgroup
        for w in widths:
            tgroup += nodes.colspec(colwidth=w)
        thead = nodes.thead()
        tgroup += thead
        hrow = nodes.row()
        for c in cols:
            hrow += self._text_entry(c)
        thead += hrow
        tbody = nodes.tbody()
        tgroup += tbody
        return table, tbody

    def _text_entry(self, text):
        entry = nodes.entry()
        para = nodes.paragraph()
        para += nodes.Text(text or "")
        entry += para
        return entry

    def _github_entry(self, handles):
        entry = nodes.entry()
        para = nodes.paragraph()
        for i, gh in enumerate(handles):
            if i:
                para += nodes.Text(", ")
            para += nodes.reference("", gh, refuri=f"https://github.com/{gh}")
        entry += para
        return entry

    def _status_entry(self, text, target):
        entry = nodes.entry()
        para = nodes.paragraph()
        if target:
            para += nodes.reference("", text, refuri=target)
        else:
            para += nodes.Text(text or "")
        entry += para
        return entry


def setup(app):
    app.add_directive("rfc-status", RFCStatus)
    return {"parallel_read_safe": True, "parallel_write_safe": True}
