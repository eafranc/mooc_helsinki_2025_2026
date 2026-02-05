def find_segments(data):
    last_char = ""
    counter = 1
    segments = []
    for i in range(len(data)):
        if data[i] == last_char:
            counter += 1
        else:
            if last_char != "":
                segments.append((counter, last_char))
            last_char = data[i]
            counter = 1

        if i == len(data) - 1:
            last_char = data[i]
            segments.append((counter, last_char))
    return segments

if __name__ == "__main__":
    print(find_segments("aaabbccdddd"))
    # [(3, 'a'), (2, 'b'), (2, 'c'), (4, 'd')]

    print(find_segments("aaaaaaaaaaaaaaaaaaaa"))
    # [(20, 'a')]

    print(find_segments("abcabc"))
    # [(1, 'a'), (1, 'b'), (1, 'c'), (1, 'a'), (1, 'b'), (1, 'c')]

    print(find_segments("kissa"))
    # [(1, 'k'), (1, 'i'), (2, 's'), (1, 'a')]
