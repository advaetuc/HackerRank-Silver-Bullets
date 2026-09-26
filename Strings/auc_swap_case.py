def swap_case(s):
    swapped_test = ""
    if 0 < len(s) < 1000:
        swapped_test = s.swapcase()
    return swapped_test

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
