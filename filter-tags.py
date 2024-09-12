import os
import xml.etree.ElementTree as ET

import xml.etree.ElementTree as ET

def filter_tags(file_path, output_file):
    # Parse the XML file into an ElementTree object
    tree = ET.parse(file_path)
    root = tree.getroot()
    namespaces = {'wp': 'http://wordpress.org/export/1.2/'}
    for channel in root.findall(".//channel", namespaces):
        # Loop through the children of <channel> to track the parent of each <wp:comment>
        to_remove = []
        for category in channel.findall("wp:category", namespaces):
            to_remove.append(category)
        for tag in channel.findall("wp:tag", namespaces):
            to_remove.append(tag)
        for item in channel.findall("item", namespaces):
            cut = []
            for pm in item.findall(".//wp:postmeta", namespaces):
                if pm.find("wp:meta_value", namespaces).text == "{{unknown}}":
                    cut.append(pm)
            for c in cut:
                item.remove(c)
        for item in to_remove:
            channel.remove(item) 

    # Save the modified tree to the output file
    tree.write(output_file, encoding='utf-8', xml_declaration=True)

# Example usage
input_file = 'filtered.xml'
output_file = 'filtered-2.xml'

filter_tags(input_file, output_file)

