def count_substring(string, sub_string):
    counter = 0
    for i in range(len(string)):
        if sub_string in string[i:]:
            counter += 1


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)