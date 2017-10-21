#!python3

#This function breaks a list into sublists based on specified delimiter
def mysplit(stringarg, delimiter):
    subsList = []
    while len(stringarg) > 0:
        idx = stringarg.find(delimiter)
        if idx < 0:
            subsList += [stringarg[:]]
            stringarg = ""
        else:
            subsList += [stringarg[0:idx]]
            stringarg = stringarg[idx+len(delimiter):].lstrip()
    return subsList
