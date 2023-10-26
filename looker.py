import nltk
import re
from nltk.tokenize import sent_tokenize, word_tokenize

# Download the NLTK data (if not already downloaded)
nltk.download("punkt")

# Define a list of common color words
color_words = [
  "dust",
  "dusty",
  "dirt",
  "dirty",
  "powder"
  "powdery"
]

# Read the text file
def read_text_file(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        text = file.read().replace("\n", " ")
    return text
# Read the text file
def read_text_file_with_n(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        text = file.read().split("\n")
    return text

# Extract color words and their sentences from the text
def extract_color_words_and_sentences(text):
    sentences = sent_tokenize(text)
    color_sentences = {}

    for sentence in sentences:
        for color in color_words:
            pattern = r'\b{}\b'.format(re.escape(color))
            if re.search(pattern, sentence, re.IGNORECASE):
                if color in color_sentences:
                    color_sentences[color].append(sentence)
                else:
                    color_sentences[color] = [sentence]

    return color_sentences

if __name__ == "__main__":
    file_path = "The Great Gatsby/ch6.txt"  # Replace with the path to your text file
    text = read_text_file(file_path)
    splittext = read_text_file_with_n(file_path)

    color_sentences = extract_color_words_and_sentences(text)

    for color, sentences in color_sentences.items():
        print(f"{color.capitalize()} sentences:")
        for sentence in sentences:
            words = sentence.split(" ")
            num_matches = -1
            num_words = 0
            lookahead = 0
            matchnum = 0
            while num_matches != 1:
                num_matches = 0
                matchnum = 0
                for i in range(len(splittext)):
                    if " ".join(words[0:num_words]) in " ".join(splittext[i:i+lookahead]):
                        if matchnum == 0:
                            matchnum = i+1
                        num_matches += 1
                num_words += 1
                if (num_words > len(words)):
                    lookahead += 1
                    num_words = 0
            print(f"- ({matchnum}) {sentence.strip()}")
        print()
