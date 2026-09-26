def count_substring(string, sub_string):
    count = 0
    sub_len = len(sub_string)

    if 1 <= len(string) <= 200 and string.isascii():
        for index in range(len(string)):
            if index + sub_len > len(string):
                break
            if string[index] == sub_string[0]:
                match_letters = 1
                for j in range(1, sub_len):
                    if string[index + j] == sub_string[j]:
                        match_letters += 1
                if match_letters == sub_len:
                    count += 1

    return count

string = input().strip()
sub_string = input().strip()

count = count_substring(string, sub_string)
print(count)
