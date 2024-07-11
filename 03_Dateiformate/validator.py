from lxml import etree


def validate(xml_path: str, xsd_path: str) -> bool:
    """Prüfung der XML-Datei nach XSD"""

    xmlschema_doc = etree.parse(xsd_path)
    xmlschema = etree.XMLSchema(xmlschema_doc)

    xml_doc = etree.parse(xml_path)
    result = xmlschema.validate(xml_doc)

    return result
