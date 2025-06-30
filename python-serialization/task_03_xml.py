#!/usr/bin/python3
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import ElementTree


def serialize_to_xml(dictionary, filename):
    root = ET.Element("data")

    for key, value in dictionary.items():
        element = ET.SubElement(root, key)
        element.text = str(value)

    tree = ElementTree(root)
    tree.write(filename, encoding="utf-8", xml_declaration=True)


def deserialize_from_xml(filename):
    tree = ET.parse(filename)
    root = tree.getroot()
    result = {}
    for element in root:
        result[element.tag] = element.text
    return result
