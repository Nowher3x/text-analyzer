# 📖 Text Analyzer ![License](https://img.shields.io/badge/license-MIT-green) ![Python](https://img.shields.io/badge/python-3.7%2B-blue)

A lightweight Python script that analyzes text files: counts lines, words, and characters, and finds the **top 10 most frequent words** (excluding stopwords).

The analysis result is saved to `report.txt` 📄

---

## 🚀 Features
✨ **Key Highlights**
- 📌 Counts total **lines**, **words**, and **characters**
- 🗂 Filters out common **stopwords** (like "the", "and", "to")
- 📊 Displays **Top 10 most frequent words**
- 💾 Saves results to a nicely formatted `report.txt`
- 📝 Clean, beginner-friendly Python code

---

## 📂 Project Structure
```
text-analyzer/
├── data/
│   └── alice_in_wonderland.txt   # Source text file
├── text_analyzer.py              # Main script
├── report.txt                    # Generated report
├── .gitignore
└── README.md
```

---

## ⚙️ Requirements
- Python **3.7+**
- No external dependencies (uses built-in `os`, `string`, `collections`)

---

## 🚀 Quick Start

Clone the repository and run the script:
```bash
git clone https://github.com/Nowher3x/text-analyzer.git
cd text-analyzer
python text_analyzer.py
```

Or place your own text file into `data/` and edit `DATA_PATH` in `text_analyzer.py`.

---

## 📊 Sample Output
```
File summary '../data/alice_in_wonderland.txt':
- String count: 6523
- Words count: 27346
- Symbols count: 144623

10 most popular words (w/o stopwords):
1. alice — 356
2. said — 298
3. queen — 210
4. time — 187
5. little — 176
6. king — 162
7. mock — 150
8. turtle — 146
9. hatter — 143
10. gryphon — 141
```

---

## 🛠 Customization
Want to analyze another file? Just update `DATA_PATH` in `text_analyzer.py`:
```python
DATA_PATH = "data/your_file.txt"
```
Change stopwords in `load_stopwords()` to fit your language or needs.

---

## 📜 License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## 🌟 Star This Project!
If you find this useful, leave a ⭐️ on [GitHub](https://github.com/Nowher3x/text-analyzer)!
