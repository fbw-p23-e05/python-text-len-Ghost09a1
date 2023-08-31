def check_even_odd_string(input_string):
    length = len(input_string)
    if length % 2 == 0:
        return "even"
    else:
        return "odd"

test_strings = ["hello world", "hello planet", ""]
for test_string in test_strings:
    result = check_even_odd_string(test_string)
    print(f'"{test_string}" --> "{result}"')
