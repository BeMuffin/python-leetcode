# Given a string s, find the length of the longest
# substring
# without repeating characters.

s = "dvdf"
substr = ""
substr_arr = []
for l in s:
    if l not in substr:
        substr+=l
        substr_arr.append(substr)
    else:
        substr = l
        continue
    

print(len(max(substr_arr,key=len)))
print(max(substr_arr,key=len))
# s = "     "
# print (len(s.split()))