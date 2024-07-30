# Given a string s consisting of words and spaces, return the length of the last word in the string.

# A word is a maximal
# substring
# consisting of non-space characters only.

string ="    fly me   to   the moon    "
str_to_arr = string.split()
result_list = list(filter(lambda item: item!=" ",str_to_arr ))
max = 0
print( len(result_list[len(result_list)-1])) or 0


# OR

string ="    fly me   to   the moon    "
str_to_arr = string.split()
print(len(str_to_arr[-1]))