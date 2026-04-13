import json
import sys
import os

def merge_json_files(file1, file2, output_file):
    if not os.path.exists(file1) or not os.path.exists(file2):
        print("Error: One or both input files do not exist.")
        return

    try:
        with open(file1, "r", encoding="utf-8") as f1:
            data1 = json.load(f1)
            
        with open(file2, "r", encoding="utf-8") as f2:
            data2 = json.load(f2)
            
        # Merging dictionaries. data2 keys will overwrite data1 keys if there's a conflict
        merged_data = {**data1, **data2}
        
        with open(output_file, "w", encoding="utf-8") as out:
            json.dump(merged_data, out, indent=4)
            
        print(f"Successfully merged '{file1}' and '{file2}' into '{output_file}'.")

    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON format. {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Create some dummy config files if they don't exist to make it easier to test
def create_dummies():
    if not os.path.exists("config1.json"):
        with open("config1.json", "w") as f: json.dump({"host": "localhost", "port": 8080}, f)
    if not os.path.exists("config2.json"):
        with open("config2.json", "w") as f: json.dump({"port": 9000, "debug": True}, f)

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Usage: python merger.py <file1.json> <file2.json> <merged.json>")
        print("Creating sample files 'config1.json' and 'config2.json' for you to test.")
        create_dummies()
        print("Now try running: python merger.py config1.json config2.json output.json")
    else:
        merge_json_files(sys.argv[1], sys.argv[2], sys.argv[3])
