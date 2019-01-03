import time
import codecs

word = input("Please enter a word to guess: ")
wordList = input("Please enter the wordlist to use: ")

guessed = 0

try:
    with codecs.open(wordList, "r", encoding='utf-8', errors='ignore') as f:
        start = time.time()
        lines = f.read().splitlines()
        for line in lines:
            print(f"Trying '{line}'")
            if line == word:
                end = time.time() - start
                print("SUCCESS!")
                print(f"[!] Guessed: {line}")
                print(f"[?] Finished in {end} seconds")
                print(f"[?] Guessed {guessed/end} words per second")
                break
            elif line != word:
                print("Failed!")
                guessed += 1
            elif guessed == len(lines):
                print("[!] NO WORDS MATCHED :(")
                print(f"[?] Finished in {end} seconds")
                print(f"[?] Guessed {guessed/end} words per second")
except Exception as e:
    print(f"[!] ERROR: {e}")
    print("[!] Did you enter the full file name and is it in the same directory as this script?")