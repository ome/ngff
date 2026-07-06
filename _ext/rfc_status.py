import os
import yaml
from docutils import nodes
from docutils.parsers.rst import Directive, directives


def _read_front_matter(path):
    """Return parsed YAML front matter dict from a markdown file, or {}."""
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
    """Yield (label, subdir_path) for numbered subfolders."""
    if not os.path.isdir(base):
        return
    for e in os.listdir(base):
        p = os.path.join(base, e)
        if os.path.isdir(p) and e != "index":
            yield e, p


def _folder_sort_key(label):
    num = "".join(c for c in label if c.isdigit())
    suffix = "".join(c for c in label if not c.isdigit())
    return (int(num) if num else 0, suffix)


class RFCStatus(Directive):
    """
        Build the full RFC status table.

        Author/Editor rows come from the central page's own front matter.
        Reviewer/Commenter/Response rows are scanned from the reviews/,
        comments/, responses/ subfolders and sorted by date (folder number
        as tiebreaker).

        Usage in rfc/9/index.md:

    ```{rfc-status}
    ```
    """

    option_spec = {
        "sections": directives.unchanged,
    }

    SECTION_LABELS = {
        "reviews": ("Reviewer", "Review"),
        "comments": ("Commenter", "Comment"),
        "responses": ("Author", "Response"),
    }

    COLUMNS = ["Role", "Name", "GitHub Handle", "Institution", "Date", "Status"]

    def run(self):
        env = self.state.document.settings.env
        src = env.doc2path(env.docname)
        rfc_dir = os.path.dirname(src)

        central = _read_front_matter(src)

        sections = self.options.get("sections")
        if sections:
            sections = [s.strip() for s in sections.split(",")]
        else:
            sections = ["reviews", "comments", "responses"]

        table = nodes.table()
        tgroup = nodes.tgroup(cols=len(self.COLUMNS))
        table += tgroup
        for width in (10, 22, 20, 22, 10, 16):
            tgroup += nodes.colspec(colwidth=width)

        thead = nodes.thead()
        tgroup += thead
        thead += self._header_row(self.COLUMNS)

        tbody = nodes.tbody()
        tgroup += tbody

        # --- Author/Editor rows from central front matter ---
        for person in central.get("authors", []):
            tbody += self._person_row(person, "Author")
        for person in central.get("editors", []):
            tbody += self._person_row(person, "Editor")

        # --- Rows scanned from subfolders, date-sorted ---
        for section in sections:
            base = os.path.join(rfc_dir, section)
            role_label, link_label = self.SECTION_LABELS.get(
                section, (section.title(), section.title())
            )
            rows = []
            for label, subdir in _numbered_subdirs(base):
                index_path = os.path.join(subdir, "index.md")
                if not os.path.isfile(index_path):
                    continue
                meta = _read_front_matter(index_path)
                date = str(meta.get("date", ""))
                status_text = f"{link_label} {label}"
                status_target = f"./{section}/{label}/index"
                rows.append(
                    (
                        date,
                        _folder_sort_key(label),
                        meta,
                        role_label,
                        status_text,
                        status_target,
                    )
                )

            # sort by (date, folder number); blank dates sort last
            rows.sort(key=lambda r: (r[0] == "", r[0], r[1]))

            for _, _, meta, role_label, status_text, status_target in rows:
                tbody += self._grouped_row(meta, role_label, status_text, status_target)

        return [table]

    # ---- entry helpers ----

    def _header_row(self, cells):
        row = nodes.row()
        for c in cells:
            row += self._text_entry(c)
        return row

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

    def _grouped_row(self, meta, role, status_text, status_target):
        authors = meta.get("authors", [])
        names = ", ".join(a.get("name", "") for a in authors if a.get("name"))
        handles = [a["github"] for a in authors if a.get("github")]
        affils = []
        for a in authors:
            aff = a.get("affiliation")
            if aff and aff not in affils:
                affils.append(aff)
        institution = ", ".join(affils)
        date = str(meta.get("date", ""))

        row = nodes.row()
        row += self._text_entry(role)
        row += self._text_entry(names)
        row += self._github_entry(handles)
        row += self._text_entry(institution)
        row += self._text_entry(date)
        row += self._status_entry(status_text, status_target)
        return row


def setup(app):
    app.add_directive("rfc-status", RFCStatus)
    return {"parallel_read_safe": True, "parallel_write_safe": True}
