# 14. Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".

# Input: strs = ["flower","flow","flight"]
# Output: "fl"
import re

strs = [""]
        
def longestCommonPrefix( strs):
    """
    :type strs: List[str]
    :rtype: str
    """


    words_counter = len(strs)
    str_from_list = " ".join(strs)
    result = ""
    search_str = ""
    if words_counter == 1:
        return str_from_list
    for l in str_from_list:
        search_str += l
        pattern = r'\b{}\w*'.format(search_str)
        result_search = re.findall(pattern, str_from_list)
        if len(result_search) == words_counter:
            result +=l
        else:
            return result


print(longestCommonPrefix(strs))


if (len(strs) == 0):
    print("")
        
prefix = strs[0]
        
for i in range(1, len(strs)):
    while not (strs[i].startswith(prefix)):
        prefix = prefix[:-1]
        if (len(prefix) == 0):
            print("")
                
print(prefix)