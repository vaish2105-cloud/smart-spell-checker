# Smart Spell Checker

A Python-based spell checker that detects misspelled words and suggests the closest matching words using the Levenshtein Edit Distance algorithm. The application supports word checking, sentence checking, custom dictionary management, and optimized searching using a large English dictionary.

---

## Features

- Check the spelling of individual words
- Check the spelling of complete sentences
- Suggest the top 5 closest matching words
- Add new words permanently to the dictionary
- Fast exact word lookup using Python sets
- Optimized candidate filtering based on first letter and word length
- Displays search execution time
- Input validation for invalid entries

---

## Technologies Used

- Python
- Dynamic Programming
- Levenshtein Edit Distance Algorithm
- File Handling
- Lists
- Sets
- String Processing

---

## Project Structure

```
smart-spell-checker/
│── spell_checker.py
│── dictionary.txt
│── README.md
```

---

## How to Run

1. Clone the repository.

```bash
git clone https://github.com/vaish2105-cloud/smart-spell-checker.git
```

2. Open the project folder.

```bash
cd smart-spell-checker
```

3. Ensure `dictionary.txt` is present in the project directory.

4. Run the program.

```bash
python spell_checker.py
```

---

## Sample Output

### Check Word

Input

```
progamming
```

Output

```
Word Not Found.

Did you mean:

1. programming
2. programmer
3. program

Search Time: 0.15 seconds
```

### Check Sentence

Input

```
I am lerning python
```

Output

```
i ✓ Correct
am ✓ Correct
lerning ✗ Incorrect
Suggestions:
- learning

python ✓ Correct
```

### Add New Word

Input

```
chatgpt
```

Output

```
Word Added Successfully.
```

The new word is permanently stored in `dictionary.txt`.

---

## Algorithm

The project uses the **Levenshtein Edit Distance** algorithm to calculate the minimum number of insertions, deletions, and substitutions required to transform one word into another. To improve performance, candidate words are filtered using the first letter and word length before computing edit distances.

---
