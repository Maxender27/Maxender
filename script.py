import json
import argparse
import os

def load_json(file_path):
    """
    Load JSON data from a file and validate its syntax.
    
    :param file_path: Path to the JSON file
    :return: Parsed JSON object
    :raises: ValueError if JSON syntax is invalid
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file {file_path} does not exist.")
    
    with open(file_path, 'r', encoding='utf-8') as file:
        try:
            data = json.load(file)
        except json.JSONDecodeError as e:
            raise ValueError(f"Invalid JSON syntax in file {file_path}: {e}")
    
    return data

def main():
    parser = argparse.ArgumentParser(description="Load and validate JSON file.")
    
    
    parser.add_argument(
        '-f', '--file', 
        required=True, 
        help='Path to the JSON file'
    )
    
    args = parser.parse_args()
    
    try:
        data = load_json(args.file)
        print("JSON file loaded and validated successfully.")
        print(data)
    except (FileNotFoundError, ValueError) as e:
        print(e)

if __name__ == "__main__":
    main()

