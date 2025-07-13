from collections import Counter
import string
import os

DATA_PATH = os.path.join(os.path.dirname(__file__), '..', 'data', 'alice_in_wonderland.txt')

def load_stopwords():
    return {"the", "and", "to", "of", "a", "i", "it", "in", "or", "is", "that", "on", "for", "with", "as", "was", "he", "she"}

def analyze_text():
    with open(DATA_PATH, 'r', encoding='utf-8') as file:
        text = file.read()
        
    lines = text.splitlines()
    words = text.lower().translate(str.maketrans('', '', string.punctuation)).split()
    stopwords = load_stopwords()
    
    filtered_words = [word for word in words if word not in stopwords]
    word_counts = Counter(filtered_words).most_common(10)
    
    report = [
        f'File summary \'{DATA_PATH}\':',
        f'- String count: {len(lines)}',
        f'- Words count: {len(words)}',
        f'- Symbols count: {len(text)}',
        '',
        '10 most popular words (w/o stopwords):'
    ]
    for i, (word, count) in enumerate(word_counts, 1):
        report.append(f"{i}. {word} — {count}")

    with open('report.txt', 'w', encoding='utf-8') as output:
        output.write('\n'.join(report))

    print("✅ Analyze complete. Final report stored in report.txt")


if __name__ == "__main__":
    analyze_text()