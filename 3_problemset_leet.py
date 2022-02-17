###################################  solution 1 ######################################
# def lengthOfLongestSubstring(s):

#     l = len(s)
#     max_len = 1

#     def checker(first, last):
#         ascii_track = [0]*128

#         for i in range(first, last+1):
#             c = ord(s[i])
#             ascii_track[c] = ascii_track[c] + 1
#             if ascii_track[c] > 1:
#                 return False
#         return True

#     for i in range(l):
#         for j in range(i, l):

#             if checker(i, j):

#                 max_len = max(max_len, j-i+1)

#     return max_len

###################################  solution 2 ######################################


# def lengthOfLongestSubstring(s):

#     l = len(s)
#     max_len = 0

#     for i in range(l):

#         ascii_track = [0] * 128

#         for j in range(i, l):

#             if (ascii_track[ord(s[j])] == 1):
#                 break

#             else:
#                 max_len = max(max_len, j - i + 1)
#                 ascii_track[ord(s[j])] = 1

#     return max_len

###################################  solution 3 ######################################

def lengthOfLongestSubstring(s):
    ln = len(s)
    right = left = max_len = 0
    ascii_track = [0]*128
    while(right < ln):
        r = s[right]
        ascii_track[ord(r)] += 1
        while ascii_track[ord(r)] > 1:
            l = s[left]
            ascii_track[ord(l)] -= 1
            left = left + 1

        max_len = max(max_len, right-left + 1)
        right = right + 1
    return max_len

s = "anasizhaan"
print(lengthOfLongestSubstring(s))
