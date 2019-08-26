s = "www.HackerRank.com"

def swap_case(s):
    if 0 <= len(s) <= 1000:
        swapped_string = ""
        for char in s:
            if char.isupper() :
                swapped_string += char.lower()
            else:
                swapped_string += char.upper()
        return swapped_string

s = input("Enter message: ")
print(swap_case(s))