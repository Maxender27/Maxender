import xml.etree.ElementTree as ET
import argparse
import os

def load_xml(file_path):
    """
    Load XML data from a file and validate its syntax.
    
    :param file_path: Path to the XML file
    :return: Parsed XML object (ElementTree)
    :raises: ValueError if XML syntax is invalid
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file {file_path} does not exist.")
    
    try:
        tree = ET.parse(file_path)
        return tree
    except ET.ParseError as e:
        raise ValueError(f"Invalid XML syntax in file {file_path}: {e}")

def main():
    parser = argparse.ArgumentParser(description="Load and validate XML file.")
    
    
    parser.add_argument(
        '-f', '--file', 
        required=True, 
        help='Path to the XML file'
    )
    
    args = parser.parse_args()
    
    try:
        tree = load_xml(args.file)
        print("XML file loaded and validated successfully.")
        root = tree.getroot()
        print(ET.tostring(root, encoding='utf-8').decode('utf-8'))
    except (FileNotFoundError, ValueError) as e:
        print(e)

if __name__ == "__main__":
    main()



