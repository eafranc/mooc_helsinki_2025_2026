# WRITE YOUR SOLUTION HERE:
class ListHelper:
    # Class Method - frequency_dictionary
    @classmethod
    def frequency_dictionary(cls, my_list: list):
        frequencies = {}
        for number in my_list:
            if number not in frequencies:
                frequencies[number] = 1
            else:
                frequencies[number] += 1
        return frequencies

    # Class Method - greatest_frequency
    @classmethod
    def greatest_frequency(cls, my_list: list):
        frequencies = ListHelper.frequency_dictionary(my_list)
        greatest_freq     = 0
        greatest_freq_key = ""
        for key in frequencies:
            if greatest_freq < frequencies[key]:
                greatest_freq     = frequencies[key]
                greatest_freq_key = key
        return greatest_freq_key

    # Class Method -doubles
    @classmethod
    def doubles(cls, my_list: list):
        frequencies = ListHelper.frequency_dictionary(my_list)
        doubles_counter = 0
        for number in frequencies:
            if frequencies[number] > 1:
                doubles_counter += 1
        return doubles_counter

if __name__ == "__main__":
    numbers = [1, 1, 2, 1, 3, 3, 4, 5, 5, 5, 6, 5, 5, 5]
    print(ListHelper.greatest_frequency(numbers)) # 5
    print(ListHelper.doubles(numbers)) # 3
