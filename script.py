import yaml
import argparse

def save_to_yaml(data, file_path):
    """
    Save data to a YAML file.
    
    :param data: Data to be saved
    :param file_path: Path to the YAML file
    """
    with open(file_path, 'w', encoding='utf-8') as file:
        yaml.dump(data, file, default_flow_style=False, allow_unicode=True)

def main():
    parser = argparse.ArgumentParser(description="Save data to a YAML file.")
    
    
    parser.add_argument(
        '-f', '--file', 
        required=True, 
        help='Path to the YAML file'
    )
    
    args = parser.parse_args()
    
    
    data = {
        "name": "Jane Doe",
        "age": 25,
        "is_student": True,
        "courses": ["Physics", "Chemistry"]
    }
    
    save_to_yaml(data, args.file)
    print(f"Data has been saved to {args.file}.")

if __name__ == "__main__":
    main()


