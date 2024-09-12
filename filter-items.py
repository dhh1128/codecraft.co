import os
import xml.etree.ElementTree as ET

import xml.etree.ElementTree as ET

def filter_items(file_path, output_file):
    # Parse the XML file into an ElementTree object
    tree = ET.parse(file_path)
    root = tree.getroot()
    namespaces = {'wp': 'http://wordpress.org/export/1.2/', 'ns2': 'http://purl.org/rss/1.0/modules/content/'}
    for channel in root.findall(".//channel", namespaces):
        to_remove = []
        for item in channel.findall("item", namespaces):
            link = item.find("link", namespaces)
            if link is None: continue
            if 'post_type=feedback' not in link.text: continue
            print('found feedback')
            encoded = item.find("ns2:encoded", namespaces)
            if encoded is None: continue
            print(encoded.text)
            user_input = input("Keep this feedback? (Yes/no): ").strip().lower()
            if user_input.startswith('n'):
                to_remove.append(item)
        for item in to_remove:
            channel.remove(item)

    # Save the modified tree to the output file
    tree.write(output_file, encoding='utf-8', xml_declaration=True)

# Example usage
input_file = 'out-clean-meta.xml'
output_file = 'out-clean-items.xml'

filter_items(input_file, output_file)

