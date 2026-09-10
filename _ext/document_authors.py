import yaml
from docutils import nodes
from docutils.parsers.rst import Directive

ORCID_ICON = "https://orcid.org/assets/vectors/orcid.logo.icon.svg"
GITHUB_ICON = "https://github.githubassets.com/favicons/favicon.svg"
EMAIL_ICON = "https://raw.githubusercontent.com/twbs/icons/main/icons/envelope-fill.svg"


def _icon_link(uri, src, alt):
    """A hyperlink wrapping a small inline image."""
    ref = nodes.reference("", "", refuri=uri)
    img = nodes.image(
        uri=src,
        alt=alt,
        classes=["rfc-author-icon"],
    )
    ref += img
    return ref


class DocumentAuthors(Directive):
    def run(self):
        env = self.state.document.settings.env
        src = env.doc2path(env.docname)
        with open(src, encoding="utf-8") as f:
            text = f.read()

        parts = text.split("---", 2)
        if len(parts) < 3:
            raise self.error("rfc-authors: no YAML front matter found")
        meta = yaml.safe_load(parts[1]) or {}

        authors = meta.get("authors", [])
        if not authors:
            raise self.error("rfc-authors: no 'authors' in front matter")

        # Number unique affiliations in first-seen order
        affils, order = {}, []
        for a in authors:
            aff = a.get("affiliation")
            if aff and aff not in affils:
                order.append(aff)
                affils[aff] = len(order)

        para = nodes.paragraph(classes=["rfc-authors"])
        for i, a in enumerate(authors):
            if i:
                para += nodes.Text(" and " if i == len(authors) - 1 else ", ")

            para += nodes.Text(a["name"])

            aff = a.get("affiliation")
            if aff:
                para += nodes.superscript(text=str(affils[aff]))

            orcid = a.get("orcid")
            if orcid:
                uri = (
                    orcid
                    if str(orcid).startswith("http")
                    else f"https://orcid.org/{orcid}"
                )
                para += nodes.Text(" ")
                para += _icon_link(uri, ORCID_ICON, "ORCID")

            gh = a.get("github")
            if gh:
                uri = gh if str(gh).startswith("http") else f"https://github.com/{gh}"
                para += nodes.Text(" ")
                para += _icon_link(uri, GITHUB_ICON, "GitHub")

            email = a.get("email")
            if email:
                uri = email if str(email).startswith("mailto:") else f"mailto:{email}"
                para += nodes.Text(" ")
                para += _icon_link(uri, EMAIL_ICON, "Email")

        result = [para]

        for aff in order:
            p = nodes.paragraph(classes=["rfc-affiliation"])
            p += nodes.superscript(text=str(affils[aff]))
            p += nodes.Text(" " + aff)
            result.append(p)

        return result


def setup(app):
    app.add_directive("document-authors", DocumentAuthors)
    return {"parallel_read_safe": True, "parallel_write_safe": True}
