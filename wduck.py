import requests
from bs4 import BeautifulSoup
from collections import Counter
import re
import argparse

# List of common words to remove
common_words = [
    "a", "about", "above", "after", "again", "against", "all", "am", "an", "and", "any", "are", "aren't", "as", "at",
    "be", "because", "been", "before", "being", "below", "between", "both", "but", "by", "can't", "cannot", "could",
    "couldn't", "did", "didn't", "do", "does", "doesn't", "doing", "don't", "down", "during", "each", "few", "for",
    "from", "further", "had", "hadn't", "has", "hasn't", "have", "haven't", "having", "he", "he'd", "he'll", "he's",
    "her", "here", "here's", "hers", "herself", "him", "himself", "his", "how", "how's", "i", "i'd", "i'll", "i'm",
    "i've", "if", "in", "into", "is", "isn't", "it", "it's", "its", "itself", "let's", "me", "more", "most", "mustn't",
    "my", "myself", "no", "nor", "not", "of", "off", "on", "once", "only", "or", "other", "ought", "our", "ours",
    "ourselves", "out", "over", "own", "same", "shan't", "she", "she'd", "she'll", "she's", "should", "shouldn't",
    "so", "some", "such", "than", "that", "that's", "the", "their", "theirs", "them", "themselves", "then", "there",
    "there's", "these", "they", "they'd", "they'll", "they're", "they've", "this", "those", "through", "to", "too",
    "under", "until", "up", "very", "was", "wasn't", "we", "we'd", "we'll", "we're", "we've", "were", "weren't",
    "what", "what's", "when", "when's", "where", "where's", "which", "while", "who", "who's", "whom", "why", "why's",
    "with", "won't", "would", "wouldn't", "you", "you'd", "you'll", "you're", "you've", "your", "yours", "yourself",
    "yourselves"
]


def get_text_from_url(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        # Get text and clean it up
        text = soup.get_text()
        text = re.sub(r'\s+', ' ', text)  # Replace multiple whitespace with single space
        return text
    except Exception as e:
        print(f"Error fetching {url}: {e}")
        return ""


def create_wordlist(urls, output_file):
    all_words = Counter()

    for url in urls:
        text = get_text_from_url(url)
        words = re.findall(r'\b\w+\b', text.lower())  # Extract words and convert to lower case
        words = [word for word in words if word not in common_words]  # Remove common words
        all_words.update(words)

    # Remove duplicates
    unique_words = set(all_words.keys())

    with open(output_file, "w") as f:
        for word in sorted(unique_words):
            f.write(word + "\n")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate a wordlist from the content of URLs.")
    parser.add_argument("-u", "--urls", required=True, help="File containing the list of URLs")
    parser.add_argument("-o", "--output", required=True, help="Output file name for the wordlist")

    args = parser.parse_args()

    with open(args.urls) as f:
        urls = [line.strip() for line in f if line.strip()]

    create_wordlist(urls, args.output)
