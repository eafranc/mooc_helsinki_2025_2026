# Write your solution here
from string import ascii_letters, digits, whitespace
def change_case(orig_string: str):
    new_string = ""
    for ch in orig_string:
        if ch.islower():
            new_string += ch.upper()
        else:
            new_string += ch.lower()
    return new_string

def split_in_half(orig_string: str):
    return (orig_string[:len(orig_string) // 2], orig_string[len(orig_string) // 2:])

def remove_special_characters(orig_string: str):
    new_string = ""
    for ch in orig_string:
        if ch not in ascii_letters and ch not in whitespace and ch not in digits:
            continue
        else:
            new_string += ch
    return new_string

if __name__ == "__main__":
    import string_helper
    my_string = "Well hello there!"
    print(string_helper.change_case(my_string))
    p1, p2 = string_helper.split_in_half(my_string)
    print(p1)
    print(p2)
    m2 = string_helper.remove_special_characters("This is a test, lets see how it goes!!!11!")
    print(m2)
    m3 = string_helper.remove_special_characters("Thi§ is a test: test?")
    print(m3)
    # wELL HELLO THERE!
    # Well hel
    # lo there!
    # This is a test lets see how it goes11
    # Thi is a test test
