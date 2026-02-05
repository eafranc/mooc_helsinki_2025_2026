# Write your solution here
def longest(strings: list):
    """ Function returns most longest of the strings;
        If there are more than 1 string that could be labeled as longest,
        this function will choose the first longest one in the list given as argument
    """
    longest_string = strings[0]
    for string in strings:
        if len(string) > len(longest_string):
            longest_string = string
    return longest_string

if __name__ == "__main__":
    strings = ["hi", "hiya", "hello", "howdydoody", "hi there"]
    print(longest(strings)) # howdydoody