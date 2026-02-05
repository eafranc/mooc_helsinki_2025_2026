# # 1- MY SOLUTION - NOT IMPROVED FOR PERFORMANCE, BUT IT WORKS
# # text =  "We use ptython to make a spell checker"
# # text = "This is acually a good and usefull program"
# text = input("Write text: ")
# words = text.split(" ")
# for word in words:
#     is_on_wordlist = False
#     with open("wordlist.txt") as new_file:
#         for line in new_file:
#             line = line.strip()
#             if word.lower() == line:
#                 is_on_wordlist = True
#                 break
#         if is_on_wordlist == False:
#             word = f"*{word}*"
#     print(f"{word} ", end = "")

# # 2 - OTHER SOLUTION - BETTER, FASTER
def wordlist():
    words = []
    with open("wordlist.txt") as new_file:
        for line in new_file:
            words.append(line.strip())
    return words

words    = wordlist()
sentence = input("Write text: ")
# sentence =  "We use ptython to make a spell checker"
# sentence = "This is acually a good and usefull program"
for word in sentence.split(" "):
    if word.lower() in words:
        print(f"{word} ", end = "")
    else:
        print(f"*{word}* ", end = "")

# SAMPLE OUTPUTS:
# Write text: We use ptython to make a spell checker
# We use *ptython* to make a spell checker

# Write text: This is acually a good and usefull program
# This is *acually* good and *usefull* program

