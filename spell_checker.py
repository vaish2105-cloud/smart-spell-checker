import os
import string


# -------------------------------
# Auto-generate Dictionary (if missing)
# -------------------------------
def generate_default_dictionary(filename):

    default_words = [
        "the", "be", "to", "of", "and", "a", "in", "that", "have", "it",
        "for", "not", "on", "with", "he", "as", "you", "do", "at", "this",
        "but", "his", "by", "from", "they", "we", "say", "her", "she", "or",
        "an", "will", "my", "one", "all", "would", "there", "their", "what",
        "so", "up", "out", "if", "about", "who", "get", "which", "go", "me",
        "when", "make", "can", "like", "time", "no", "just", "him", "know",
        "take", "people", "into", "year", "your", "good", "some", "could",
        "them", "see", "other", "than", "then", "now", "look", "only",
        "come", "its", "over", "think", "also", "back", "after", "use",
        "two", "how", "our", "work", "first", "well", "way", "even", "new",
        "want", "because", "any", "these", "give", "day", "most", "us",
        "python", "programming", "computer", "science", "student", "college",
        "project", "code", "dictionary", "spell", "checker", "word", "sentence"
    ]

    with open(filename, "w", encoding="utf-8") as file:
        for word in sorted(default_words):
            file.write(word + "\n")

    print("No dictionary found. A default dictionary.txt has been created with",
          len(default_words), "common words.")
    print("You can add more words anytime using option 3.\n")


# -------------------------------
# Load Dictionary
# -------------------------------
def load_dictionary(filename):

    if not os.path.exists(filename):
        generate_default_dictionary(filename)

    words = []

    try:

        with open(filename, "r", encoding="utf-8") as file:

            for line in file:

                word = line.strip().lower()

                if word:

                    words.append(word)

    except FileNotFoundError:

        print("Dictionary file not found.")
        return []

    return words


# -------------------------------
# Exact Search
# -------------------------------
def search_word(dictionary_set, word):

    return word in dictionary_set


# -------------------------------
# Edit Distance
# -------------------------------
def edit_distance(word1, word2):

    m = len(word1)
    n = len(word2)

    dp = [[0 for j in range(n + 1)] for i in range(m + 1)]

    for i in range(m + 1):
        dp[i][0] = i

    for j in range(n + 1):
        dp[0][j] = j

    for i in range(1, m + 1):

        for j in range(1, n + 1):

            if word1[i - 1] == word2[j - 1]:

                cost = 0

            else:

                cost = 1

            dp[i][j] = min(

                dp[i - 1][j] + 1,

                dp[i][j - 1] + 1,

                dp[i - 1][j - 1] + cost

            )

    return dp[m][n]


# -------------------------------
# Suggestions
# -------------------------------
def get_suggestions(dictionary, word):

    candidates = []

    for w in dictionary:

        if len(w) == 0:
            continue

        if w[0] != word[0]:
            continue

        if abs(len(w) - len(word)) > 2:
            continue

        distance = edit_distance(word, w)

        candidates.append((distance, w))

    candidates.sort()

    return candidates[:5]


# -------------------------------
# Sentence Checker
# -------------------------------
def check_sentence(dictionary, dictionary_set):

    sentence = input("\nEnter Sentence : ").lower()

    words = sentence.translate(
        str.maketrans('', '', string.punctuation)
    ).split()

    print("\nChecking...\n")

    for word in words:

        if search_word(dictionary_set, word):

            print(word, "\u2713 Correct")

        else:

            print(word, "\u2717 Incorrect")

            suggestions = get_suggestions(dictionary, word)

            if suggestions:

                print("Suggestions:")

                for distance, suggestion in suggestions:

                    print("   -", suggestion)

            print()


# -------------------------------
# Add New Word
# -------------------------------
def add_word(dictionary, dictionary_set):

    word = input("\nEnter New Word : ").strip().lower()

    if word == "" or not word.isalpha():

        print("Please enter a valid alphabetic word.")
        return

    if search_word(dictionary_set, word):

        print("Word already exists.")
        return

    dictionary.append(word)

    dictionary_set.add(word)

    dictionary.sort()

    with open("dictionary.txt", "a", encoding="utf-8") as file:

        file.write(word + "\n")

    print("Word Added Successfully.")


# -------------------------------
# Check Single Word
# -------------------------------
def check_word(dictionary, dictionary_set):

    word = input("\nEnter Word : ").strip().lower()

    if word == "":
        print("Please enter a word.")
        return

    if not word.isalpha():
        print("Please enter only alphabetic words.")
        return

    if search_word(dictionary_set, word):

        print("\nCorrect Spelling.")

    else:

        print("\nWord Not Found.")

        suggestions = get_suggestions(dictionary, word)

        if suggestions:

            print("\nDid you mean:\n")

            for i, (distance, suggestion) in enumerate(suggestions, start=1):

                print(f"{i}. {suggestion}")

        else:

            print("No Suggestions Found.")


# -------------------------------
# Main
# -------------------------------
def main():

    dictionary = load_dictionary("dictionary.txt")

    dictionary_set = set(dictionary)

    print("Dictionary Loaded Successfully.")
    print("Total Words :", len(dictionary))

    while True:

        print("\n========== SPELL CHECKER ==========")
        print("1. Check Word")
        print("2. Check Sentence")
        print("3. Add New Word")
        print("4. Exit")

        choice = input("\nEnter Choice : ")

        if choice == "1":

            check_word(dictionary, dictionary_set)

        elif choice == "2":

            check_sentence(dictionary, dictionary_set)

        elif choice == "3":

            add_word(dictionary, dictionary_set)

        elif choice == "4":

            print("\nThank You.")
            break

        else:

            print("\nInvalid Choice.")


if __name__ == "__main__":
    main()
