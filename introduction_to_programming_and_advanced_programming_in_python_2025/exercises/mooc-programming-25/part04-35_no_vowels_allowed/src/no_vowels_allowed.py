# 1 - MY SOLUTION USING REPLACE METHOD
# Write your solution here
# def no_vowels(text: str):
#     no_vowels_text = text
#     vowels = "aeiou"
#     for ch in no_vowels_text:
#         if ch in vowels:
#             no_vowels_text = no_vowels_text.replace(letter, "")
#     return no_vowels_text

# 2 - SIMPLER SOLUTION:
def no_vowels(text: str):
    vowels = "aeiou"
    no_vowels_text = ""
    for ch in text:
        if ch not in vowels:
            no_vowels_text += ch
    return no_vowels_text

if __name__ == "__main__":
    my_string = "this is an example" 
    print(no_vowels(my_string)) # ths s n xmpl