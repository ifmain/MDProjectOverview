import os
import sys
import json

CONFIG_FILE = 'config.json'
DEFAULT_CONFIG = {
    "ignore_dirs": [".*", "__*"],
    "ignore_files": []
}

def load_config():
    if not os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, 'w', encoding='utf-8') as f:
            json.dump(DEFAULT_CONFIG, f, indent=4)
        return DEFAULT_CONFIG
    else:
        with open(CONFIG_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)

def should_ignore(name, patterns):
    import fnmatch
    return any(fnmatch.fnmatch(name, pattern) for pattern in patterns)

def get_project_structure(path, config):
    project_structure = []
    for root, dirs, files in os.walk(path):
        # Filter directories and files
        dirs[:] = [d for d in dirs if not should_ignore(d, config['ignore_dirs'])]
        files = [f for f in files if not should_ignore(f, config['ignore_files'])]
        
        level = root.replace(path, '').count(os.sep)
        indent = ' ' * 4 * level
        project_structure.append('{}{}/'.format(indent, os.path.basename(root)))
        sub_indent = ' ' * 4 * (level + 1)
        for f in files:
            project_structure.append('{}{}'.format(sub_indent, f))
    return project_structure

def get_file_content(path):
    try:
        with open(path, 'r', encoding='utf-8') as file:
            content = file.read()
        return content
    except UnicodeDecodeError:
        return None

def detect_language(file_path, file_content):
    from pygments.lexers import guess_lexer_for_filename
    try:
        lexer = guess_lexer_for_filename(file_path, file_content)
        return lexer.name.lower()
    except Exception:
        return 'text'

def generate_report(path):
    config = load_config()
    project_structure = get_project_structure(path, config)
    
    # Print project structure
    print("### Project structure")
    print("```")
    for line in project_structure:
        print(line)
    print("```")
    print()
    
    # Print content of each file with detected language
    for root, dirs, files in os.walk(path):
        # Filter directories and files
        dirs[:] = [d for d in dirs if not should_ignore(d, config['ignore_dirs'])]
        files = [f for f in files if not should_ignore(f, config['ignore_files'])]
        
        for f in files:
            file_path = os.path.join(root, f)
            file_content = get_file_content(file_path)
            if file_content is not None:
                language = detect_language(file_path, file_content)
                print(f"### {f}")
                print(f"```{language}")
                print(file_content)
                print("```")
            else:
                print(f"### {f}")
                print("```")
                print(f"Error reading file or binary file detected")
                print("```")
            print()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python repolist.py path_to_repo")
    else:
        path_to_repo = sys.argv[1]
        generate_report(path_to_repo)
