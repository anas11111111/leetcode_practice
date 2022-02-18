MAX_CHAR = 26


def sortString(str):
    charCount = [0 for i in range(MAX_CHAR)]
    for i in range(0, len(str), 1):
        charCount[ord(str[i]) - ord("a")] += 1

    for i in range(0, MAX_CHAR, 1):
        for j in range(0, charCount[i], 1):
            print(chr(ord("a") + i), end="")


s = "anassikderjeem"
sortString(s)
