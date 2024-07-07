# URL to Wordlist Tool

This tool extracts text from a list of URLs and generates a wordlist by removing common words and duplicates. The wordlist can be used for various purposes such as text analysis, word frequency studies, or creating custom dictionaries.

## Features

- Fetches text content from multiple URLs.
- Removes common English words.
- Generates a wordlist with unique words.
- Allows specifying input URLs file and output wordlist file via command-line arguments.

## Requirements

- Python 3.x
- `requests` library
- `beautifulsoup4` library

## Installation

1. **Clone the repository or download the script.**

2. **Install the required Python libraries.**

   ```bash
   pip install -r requirements.txt

## Usage

To use the tool, run the script with the following command-line arguments:

- '-u' or '--urls': File containing the list of URLs (one URL per line).
- '-o' or '--output': Output file name for the generated wordlist.

   ```bash
   python code.py -u urls.txt -o output.txt

## Example

   ```bash
   python code.py -u example_urls.txt -o wordlist.txt
   ```

## help

To display help information about the script, use the -h or --help flag:

  ```bash
    python code.py -h
  ```


This `README.md` provides a comprehensive guide on how to use the tool, including installation instructions, usage, examples, and help information.

