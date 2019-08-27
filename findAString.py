string = "WoW!TestCaseTestCase"
substring  = "CaseT"
str1 = ""
# find index 1 of substring
substring_index = substring[0]
substring_length = len(substring)
if substring in string:
    c = string.index(substring)
    counter = c
    match_count = 0
    while counter < len(string)-1:
        if string[counter] == substring_index:
            c_ = 0
            for i in range(0,substring_length):
                try:
                    str1 += string[counter + c_]
                except:
                    str1 = ""
                if len(str1) == substring_length and str1 == substring:
                    print(counter)
                    print("found", str1)
                    match_count += 1
                c_ += 1
        str1 = ""
        counter += 1
else:
    match_count = 0

print(match_count)

