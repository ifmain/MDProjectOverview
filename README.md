# MDRepoSnapshot

MDRepoSnapshot is a tool for generating a detailed overview of a project's structure and file contents, presented in Markdown format.

## Overview

MDRepoSnapshot scans a given repository directory and generates two main sections in the Markdown report:

1. **Project Structure**: Displays the directory structure of the project, excluding specified directories and files according to the configuration.
   
2. **File Contents**: Provides the content of each detected file along with the detected programming language (using syntax highlighting), or indicates errors for unreadable or binary files.

## Features

- **Configurable Ignored Directories and Files**: Customize which directories and files to exclude from the report using a configuration file (`config.json`).
- **Markdown Output**: Output the generated report directly in Markdown format, suitable for documentation or further processing.
- **Language Detection**: Automatically detects programming languages for syntax highlighting in code snippets.

## Usage

To generate a report for a repository:

```bash
python repolist.py path_to_repo
```

Replace `path_to_repo` with the path to the repository you want to analyze.

## Installation

1. Clone the repository:

```bash
git clone https://github.com/your_username/MDRepoSnapshot.git
cd MDRepoSnapshot
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

## Configuration

The tool uses a `config.json` file to define directories and files to ignore during scanning. If `config.json` is not found, it creates one with default settings:

```json
{
    "ignore_dirs": [
        ".*",
        "__*"
    ],
    "ignore_files": [
        "*.json"
    ]
}
```

Modify these lists to suit your specific project structure and requirements.

## Dependencies

- Python 3.x
- Required Python packages (see `requirements.txt`)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
