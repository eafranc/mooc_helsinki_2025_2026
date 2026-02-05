# Write your solution here
def get_wordlist():
    wordlist = []
    with open("words.txt") as read_file:
        for line in read_file:
            line = line.strip()
            wordlist.append(line)
        return wordlist

def find_words(search_term: str):
    wordlist    = get_wordlist()
    found_words = []
    dot         = "."
    star        = "*"

    for word in wordlist:
        if len(word) < len(search_term):
            continue
        for i in range(len(search_term)):
            if i == len(search_term) - 1:
                if (search_term[i] == word[i] or search_term[i] == dot) and len(search_term) == len(word):
                    found_words.append(word)
                elif search_term[i] == star:
                    parts = search_term.split(star)
                    if word.startswith(parts[0]):
                        found_words.append(word)
                    break
            else:
                if search_term[i] == word[i]:
                    continue
                else:
                    if search_term[i] == dot:
                        continue
                    elif search_term[i] == star:
                        parts = search_term.split(star)
                        if i == 0:
                            if word.endswith(parts[1]):
                                found_words.append(word)
                        elif word.startswith(parts[0]) and word.endswith(parts[1]):
                            found_words.append(word)
                        break
                    else:
                        break
    return found_words

if __name__ == "__main__":
    found_words = find_words("ca.")
    print(found_words)
