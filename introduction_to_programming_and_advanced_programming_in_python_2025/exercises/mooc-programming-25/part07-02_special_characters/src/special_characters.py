# Write your solution here
def separate_characters(my_string: str):
    from string import ascii_letters, punctuation
    ascii_str = punct_str = other_str = ""
    for ch in my_string:
        if ch in ascii_letters:
            ascii_str += ch
        elif ch in punctuation:
            punct_str += ch
        else:
            other_str += ch
    return (ascii_str, punct_str, other_str)

if __name__ == "__main__":
    parts = separate_characters("Olé!!! Hey, are ümläüts wörking?")
    print(parts[0]) # OlHeyaremltswrking
    print(parts[1]) # !!!,?
    print(parts[2]) # é  üäü ö
