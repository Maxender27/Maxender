import xml.etree.ElementTree as ET
import argparse

def save_to_xml(data, file_path):
    """
    Save data to an XML file.
    
    :param data: Data to be saved (dictionary)
    :param file_path: Path to the XML file
    """
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
    parser = argparse.ArgumentParser(description="Save data to an XML file.")
    
    
    parser.add_argument(
        '-f', '--file', 
        required=True, 
        help='Path to the XML file'
    )
    
    args = parser.parse_args()
    
    
    data = {
        "name": "Jane Doe",
        "age": 25,
        "is_student": True,
        "courses": ["Physics", "Chemistry"]
    }
    
    save_to_xml(data, args.file)
    print(f"Data has been saved to {args.file}.")

if __name__ == "__main__":
    main()



