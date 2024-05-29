import json
import argparse

def save_to_json(data, file_path):
    """
    Save data to a JSON file.
    
    :param data: Data to be saved
    :param file_path: Path to the JSON file
    """
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

def main():
    parser = argparse.ArgumentParser(description="Save data to a JSON file.")
    
    
    parser.add_argument(
        '-f', '--file', 
        required=True, 
        help='Path to the JSON file'
    )
    
    args = parser.parse_args()
    
    
    data = {
        "name": "Jane Doe",
        "age": 25,
        "is_student": True,
        "courses": ["Physics", "Chemistry"]
    }
    
    save_to_json(data, args.file)
    print(f"Data has been saved to {args.file}.")

if __name__ == "__main__":
    main()

