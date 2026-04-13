import sys

def convert_to_html(input_file, output_file):
    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        html_lines = ["<html>\n<head><title>Converted Output</title></head>\n<body>\n"]
        
        for line in lines:
            line = line.strip()
            if not line:
                html_lines.append("<br/>\n")
            elif line.startswith("# "):
                html_lines.append(f"<h1>{line[2:]}</h1>\n")
            elif line.startswith("## "):
                html_lines.append(f"<h2>{line[3:]}</h2>\n")
            else:
                # Basic bolding replacement
                if "**" in line:
                    parts = line.split("**")
                    # Even indices are normal text, odd indices are bolded text (if paired properly)
                    new_line = ""
                    for i, part in enumerate(parts):
                        if i % 2 != 0: 
                            new_line += f"<strong>{part}</strong>"
                        else:
                            new_line += part
                    line = new_line
                html_lines.append(f"<p>{line}</p>\n")
        
        html_lines.append("</body>\n</html>\n")
        
        with open(output_file, 'w', encoding='utf-8') as f:
            f.writelines(html_lines)
            
        print(f"Successfully converted {input_file} to {output_file}!")
        
    except FileNotFoundError:
        print(f"Error: The file {input_file} was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python converter.py <input.md> <output.html>")
    else:
        convert_to_html(sys.argv[1], sys.argv[2])
