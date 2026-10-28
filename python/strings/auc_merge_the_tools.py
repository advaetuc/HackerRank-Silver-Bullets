def merge_the_tools(string, k):

    for i in range(0, len(string), k):

        t = string[i:i+k]

        u = "".join(dict.fromkeys(t))

        print(u)
