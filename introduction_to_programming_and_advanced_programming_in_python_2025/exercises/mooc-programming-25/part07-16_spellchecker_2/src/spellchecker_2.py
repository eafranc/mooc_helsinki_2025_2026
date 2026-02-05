# Write your solution here
def get_wordlist():
    wordlist = []
    with open("wordlist.txt") as file:
        for line in file:
            wordlist.append(line.strip())
    return wordlist

def main():
    from difflib import get_close_matches
    wordlist = get_wordlist()

    if True:
        text = input("write text: ")
    else:
        # text = "We use ptython to make a spell checker"
        text = "This is acually a good and usefull program"

    close_matches = {}
    for word in text.split(" "):
        if word.lower() in wordlist:
            print(f"{word} ", end = "")
        else:
            print(f"*{word}* ", end = "")
            close_matches[word] = []
            close_matches[word] = get_close_matches(word, wordlist)
    if len(close_matches) != 0:
        print("\nsuggestions:")
        for word, matches in close_matches.items():
            print(f"{word}: {", ".join(matches)}")

main()

