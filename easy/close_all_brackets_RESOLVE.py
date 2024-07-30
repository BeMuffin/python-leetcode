s = "([]{})"

br_dict = {
    "(" : 0,
    ")" :0,
    "[" :0,
    "]" :0,
    "{" :0,
    "}" :0

}


for br in s:
    br_dict[br] +=1

if br_dict["("] == br_dict[")"] and br_dict["["] == br_dict["]"] and br_dict["{"] == br_dict["}"]:
    print(True)
else:
    print (False)
