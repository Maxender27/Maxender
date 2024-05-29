import argparse
import json
import yaml
import xml.etree.ElementTree as ET
import os

def load_json(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file {file_path} does not exist.")
    with open(file_path, 'r', encoding='utf-8') as file:
        try:
            data = json.load(file)
        except json.JSONDecodeError as e:
            raise ValueError(f"Invalid JSON syntax in file {file_path}: {e}")
    return data

def save_to_json(data, file_path):
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

def load_yaml(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file {file_path} does not exist.")
    with open(file_path, 'r', encoding='utf-8') as file:
        try:
            data = yaml.safe_load(file)
        except yaml.YAMLError as e:
            raise ValueError(f"Invalid YAML syntax in file {file_path}: {e}")
    return data

def save_to_yaml(data, file_path):
    with open(file_path, 'w', encoding='utf-8') as file:
        yaml.dump(data, file, default_flow_style=False, allow_unicode=True)

def load_xml(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file {file_path} does not exist.")
    try:
        tree = ET.parse(file_path)
        return tree
    except ET.ParseError as e:
        raise ValueError(f"Invalid XML syntax in file {file_path}: {e}")

def save_to_xml(data, file_path):
    person = ET.Element("person")
    name = ET.SubElement(person, "name")
    name.text = data.get("name", "")
    age = ET.SubElement(person, "age")
    age.text = str(data.get("age", ""))
    is_student = ET.SubElement(person, "is_student")
    is_student.text = str(data.get("is_student", ""))
    courses = ET.SubElement(person, "courses")
    for course in data.get("courses", []):
        course_element = ET.SubElement(courses, "course")
        course_element.text = course
    tree = ET.ElementTree(person)
    tree.write(file_path, encoding='utf-8', xml_declaration=True)

def main():
    parser = argparse.ArgumentParser(description="Handle data in JSON, YAML, and XML formats.")
    parser.add_argument('--load-json', help='Path to load JSON file')
    parser.add_argument('--save-json', help='Path to save JSON file')
    parser.add_argument('--load-yaml', help='Path to load YAML file')
    parser.add_argument('--save-yaml', help='Path to save YAML file')
    parser.add_argument('--load-xml', help='Path to load XML file')
    parser.add_argument('--save-xml', help='Path to save XML file')
    parser.add_argument('--data', help='Data to save in JSON format', type=json.loads)
    args = parser.parse_args()

    if args.load_json:
        try:
            data = load_json(args.load_json)
            print("Loaded JSON data:", data)
        except (FileNotFoundError, ValueError) as e:
            print(e)

    if args.save_json and args.data:
        save_to_json(args.data, args.save_json)
        print(f"Data has been saved to {args.save_json}.")

    if args.load_yaml:
        try:
            data = load_yaml(args.load_yaml)
            print("Loaded YAML data:", data)
        except (FileNotFoundError, ValueError) as e:
            print(e)

    if args.save_yaml and args.data:
        save_to_yaml(args.data, args.save_yaml)
        print(f"Data has been saved to {args.save_yaml}.")

    if args.load_xml:
        try:
            tree = load_xml(args.load_xml)
            root = tree.getroot()
            print("Loaded XML data:", ET.tostring(root, encoding='utf-8').decode('utf-8'))
        except (FileNotFoundError, ValueError) as e:
            print(e)

    if args.save_xml and args.data:
        save_to_xml(args.data, args.save_xml)
        print(f"Data has been saved to {args.save_xml}.")

if __name__ == "__main__":
    main()




