import yaml
import argparse
import os

def load_yaml(file_path):
    """
    Load YAML data from a file and validate its syntax.
    
    :param file_path: Path to the YAML file
    :return: Parsed YAML object
    :raises: ValueError if YAML syntax is invalid
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file {file_path} does not exist.")
    
    with open(file_path, 'r', encoding='utf-8') as file:
        try:
            data = yaml.safe_load(file)
        except yaml.YAMLError as e:
            raise ValueError(f"Invalid YAML syntax in file {file_path}: {e}")
    
    return data

def main():
    parser = argparse.ArgumentParser(description="Load and validate YAML file.")
    
    
    parser.add_argument(
        '-f', '--file', 
        required=True, 
        help='Path to the YAML file'
    )
    
    args = parser.parse_args()
    
    try:
        data = load_yaml(args.file)
        print("YAML file loaded and validated successfully.")
        print(data)
    except (FileNotFoundError, ValueError) as e:
        print(e)

if __name__ == "__main__":
    main()


