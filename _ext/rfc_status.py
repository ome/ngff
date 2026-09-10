import os
import posixpath
import yaml
from docutils import nodes
from docutils.parsers.rst import Directive
from sphinx import addnodes

# Display-only labels for the state codes of the (non-normative) table under
# resources/rfc-status-codes. The code in an RFC's front matter stays the source
# of truth; this only spells it out for readers.
STATE_LABELS = {
    "D1": "Initial idea",
    "D2": "Initial idea",
    "D3": "PR open",
    "D4": "PR open",
    "D5": "Editor decision",
    "D6": "Closed",
    "R1": "Under review",
    "R2": "Under review",
    "R3": "Replying to reviews",
    "R4": "Replying to reviews",
    "R5": "Under review",
    "R6": "Under review",
    "R7": "Under review",
    "R8": "Replying to reviews",
    "R9": "Withdrawn",
    "S0": "Accepted; SPEC updates",
    "S1": "Accepted; SPEC updates",
    "S2": "Clarification",
    "S3": "Implementation",
    "S4": "Adopted",
}

STATE_CODES_DOC = "/resources/rfc-status-codes/index"


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


def _status_nodes(meta):
    """The status line of an RFC, e.g. "S4 – Adopted (update implementations)".

    Everything comes from the RFC's front matter: `manual_status` holds the state
    code, `status_note` an optional fragment explaining it. Editors set the code
    by hand when they move an RFC along; it is never guessed here from the
    reviews or responses that happen to be on disk. The code links to the table
    of status codes; a code that is not in STATE_LABELS (say "N/A" for the
    historical RFC-0) is shown without a label.
    """
    code = str(meta.get("manual_status", "")).strip()
    if not code:
        return []
    result = [_doc_reference(code, STATE_CODES_DOC)]
    label = STATE_LABELS.get(code.upper())
    if label:
        result.append(nodes.Text(f" \u2013 {label}"))
    note = str(meta.get("status_note", "")).strip()
    if note:
        result.append(nodes.Text(f" ({note})"))
    return result


def _state_text(meta):
    """The state as plain text, e.g. "S4 (Adopted)", for the RFC listing."""
    code = str(meta.get("manual_status", "")).strip()
    if not code:
        return ""
    label = STATE_LABELS.get(code.upper())
    return f"{code} ({label})" if label else code


def _doc_reference(text, docname):
    """Link to another page, resolved by the builder so the URL is always right."""
    return addnodes.pending_xref(
        "",
        nodes.inline("", text),
        refdomain="std",
        reftype="doc",
        reftarget=docname,
        refexplicit=True,
        refwarn=True,
    )


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

        all_dates = [
            str(m.get("date", ""))
            for _, m in (reviews + comments + responses)
            if m.get("date")
        ]
        last_update = max(all_dates) if all_dates else str(central.get("date", ""))

        result = []

        status = _status_nodes(central)
        if status:
            line = nodes.paragraph(classes=["rfc-status-state"])
            line += nodes.strong("", nodes.Text("Status: "))
            line.extend(status)
            result.append(line)

        reference_pr = str(central.get("reference_pr", "")).strip()
        if reference_pr:
            number = reference_pr.rstrip("/").rsplit("/", 1)[-1]
            label = f"#{number}" if number.isdigit() else reference_pr
            pr = nodes.paragraph(classes=["rfc-status-reference-pr"])
            pr += nodes.Text("Reference PR: ")
            pr += nodes.reference("", label, refuri=reference_pr)
            result.append(pr)

        summary = nodes.paragraph(classes=["rfc-status-summary"])
        summary += nodes.Text(
            f"As of the last update, {last_update}: "
            f"{_thread_count(comments)} comments, "
            f"{_thread_count(reviews)} reviews, "
            f"{_thread_count(responses)} responses, "
        )
        result.append(summary)
        result.append(nodes.title(text="Authors, editors, and endorsers"))
        result.append(self._people_table(central))
        if reviews or comments or responses:
            result.append(nodes.title(text="Reviews, comments, and responses"))
            result.append(
                self._activity_table(
                    reviews, comments, responses, posixpath.dirname(env.docname)
                )
            )
        return result

    # ---- Table 1: Authors + Editors + Endorsers----

    def _people_table(self, central):
        cols = ["Role", "Name", "GitHub", "Institution", "Date", "Status"]
        table, tbody = self._new_table(cols, (10, 22, 20, 22, 10, 16))
        for person in central.get("authors", []):
            tbody += self._person_row(person, "Author")
        for person in central.get("editors", []):
            tbody += self._person_row(person, "Editor")
        for person in central.get("endorsers", []):
            tbody += self._person_row(person, "Endorser")
        return table

    def _person_row(self, person, role):
        row = nodes.row()
        row += self._text_entry(role, "bold")
        row += self._text_entry(person.get("name", ""))
        gh = person.get("github")
        row += self._github_entry([gh] if gh else [])
        row += self._affiliation_entry(
            [(person.get("affiliation", ""), person.get("affiliation_url"))]
        )
        row += self._text_entry(str(person.get("date", "")))
        # Endorsers always read "endorse", linked to the endorsement document when
        # a reference is given; everyone else shows their role as text.
        if role == "Endorser":
            reference = person.get("reference", "")
            if reference:
                row += self._linked_entry("endorse", reference)
            else:
                row += self._text_entry(person.get("role") or "endorse")
        else:
            row += self._text_entry(person.get("role", ""))

        return row

    # ---- Table 2: Reviews + Comments + Responses (one row per round) ----

    def _activity_table(self, reviews, comments, responses, rfc_docdir):
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
                    f"{rfc_docdir}/{section}/{label}/index",
                )
        return table

    def _activity_row(self, meta, link_text, link_docname):
        authors = meta.get("authors", [])
        names = ", ".join(a.get("name", "") for a in authors if a.get("name"))
        handles = [a["github"] for a in authors if a.get("github")]
        affils = []
        for a in authors:
            aff = a.get("affiliation")
            if aff and aff not in [x for x, _ in affils]:
                affils.append((aff, a.get("affiliation_url")))
        recommendation = str(meta.get("recommendation") or "").replace("_", " ")

        row = nodes.row()
        row += self._doc_entry(link_text, link_docname)
        row += self._text_entry(names)
        row += self._github_entry(handles)
        row += self._affiliation_entry(affils)
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

    def _text_entry(self, text, style=None):
        entry = nodes.entry()
        para = nodes.paragraph()
        if style == "bold":
            para += nodes.strong("", nodes.Text(text or ""))
        elif style == "italic":
            para += nodes.emphasis("", nodes.Text(text or ""))
        else:
            para += nodes.Text(text or "")
        entry += para
        return entry

    def _doc_entry(self, text, docname):
        """Cell linking to another document."""
        entry = nodes.entry()
        para = nodes.paragraph()
        para += _doc_reference(text, "/" + docname)
        entry += para
        return entry

    def _affiliation_entry(self, affiliations):
        """Comma-separated institutions, linked when an `affiliation_url` is given."""
        entry = nodes.entry()
        para = nodes.paragraph()
        for i, (name, uri) in enumerate(a for a in affiliations if a[0]):
            if i:
                para += nodes.Text(", ")
            if uri:
                para += nodes.reference("", name, refuri=uri)
            else:
                para += nodes.Text(name)
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

    def _linked_entry(self, text, target, style=None):
        entry = nodes.entry()
        para = nodes.paragraph()
        if target:
            para += nodes.reference("", text, refuri=target)
        else:
            if style == "bold":
                para += nodes.strong("", nodes.Text(text or ""))
            elif style == "italic":
                para += nodes.emphasis("", nodes.Text(text or ""))
            else:
                para += nodes.Text(text or "")
        entry += para
        return entry


class RFCListing(RFCStatus):
    """The table of all RFCs, built from each RFC's own front matter.

    Subclasses RFCStatus only to reuse its table builders; it renders the
    overview table for rfc/index.md rather than a single RFC's record.
    """

    def run(self):
        env = self.state.document.settings.env
        base = os.path.dirname(env.doc2path(env.docname))
        docdir = posixpath.dirname(env.docname)

        rfcs = []
        for name, subdir in _numbered_subdirs(base):
            index_path = os.path.join(subdir, "index.md")
            if name.isdigit() and os.path.isfile(index_path):
                rfcs.append((int(name), _read_front_matter(index_path)))
        rfcs.sort()

        cols = ["RFC", "Description", "Date", "Status", "Note", "OME-Zarr Version"]
        table, tbody = self._new_table(cols, (8, 26, 8, 20, 26, 12))
        table.insert(0, nodes.title(text="RFC Listing"))
        for number, meta in rfcs:
            date = str(meta.get("date", ""))
            row = nodes.row()
            row += self._doc_entry(f"RFC-{number}", f"{docdir}/{number}/index")
            row += self._text_entry(meta.get("description", ""))
            row += self._text_entry(date[:4] if date else "TBD")
            row += self._text_entry(_state_text(meta) or "TBD")
            row += self._text_entry(str(meta.get("status_note", "")))
            row += self._text_entry(str(meta.get("ome_zarr_version", "")))
            tbody += row
        return [table]


def setup(app):
    app.add_directive("rfc-status", RFCStatus)
    app.add_directive("rfc-listing", RFCListing)
    return {"parallel_read_safe": True, "parallel_write_safe": True}
