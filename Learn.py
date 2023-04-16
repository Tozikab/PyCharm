import math
def disemvowel(string_):
    strio = []
    for i in range(len(string_)):
        if string_[i] not in "euiojaEUIOJA":
            strio.append(string_[i])
    string_ = ''.join(strio)
    return string_
print(disemvowel("No offense but,\nYour writing is among the worst I've ever read"))
