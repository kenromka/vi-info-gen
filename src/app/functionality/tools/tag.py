import xml.dom.minidom


def create_tag(name: str = None, text: str = None, attributes: dict = None, *, cdata: bool = False):
    doc = xml.dom.minidom.Document()

    if name is None:
        return doc

    tag = doc.createElement(name)

    if text is not None:
        if cdata is True:
            tag.appendChild(doc.createCDATASection(text))
        else:
            tag.appendChild(doc.createTextNode(text))

    if attributes is not None:
        for attribute, value in attributes.items():
            tag.setAttribute(attribute, str(value))

    return tag
