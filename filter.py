import os
import xml.etree.ElementTree as ET

import xml.etree.ElementTree as ET

def filter_tags(file_path, output_file):
    # Parse the XML file into an ElementTree object
    tree = ET.parse(file_path)
    root = tree.getroot()
    namespaces = {'wp': 'http://wordpress.org/export/1.2/'}
    for channel in root.findall(".//channel", namespaces):
        for item in channel.findall("item", namespaces):
            title = item.find("title", namespaces)
            print(f"Processing item: {title.text}")
            for comment in item.findall("wp:comment", namespaces):
                to_remove = []
                for meta in comment.findall("wp:commentmeta", namespaces):
                    key = meta.find("wp:meta_key", namespaces)
                    if key is not None:
                        if key.text.startswith('_') or 'akismet' in key.text or 'jabber' in key.text:
                            to_remove.append(meta)
                for meta in to_remove:
                    comment.remove(meta)
                if to_remove:
                    print(f"removed {len(to_remove)} commentmetas.")
            to_remove = []
            for meta in item.findall("wp:postmeta", namespaces):
                key = meta.find("wp:meta_key", namespaces)
                if key is not None:
                    if key.text.startswith('_wp') and key.text not in ['_wp_attached_file', '_wp_attachment_metadata']:
                        to_remove.append(meta)
            for meta in to_remove:
                item.remove(meta)
            if to_remove:
                print(f"removed {len(to_remove)} postmetas.")

    # Save the modified tree to the output file
    tree.write(output_file, encoding='utf-8', xml_declaration=True)

# Example usage
input_file = 'out.xml'
output_file = 'out-clean-meta.xml'

filter_tags(input_file, output_file)

