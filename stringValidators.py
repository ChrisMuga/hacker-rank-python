S = input("Enter String")
print(any(map(str.isalnum, S)))
print(any(map(str.isalpha, S)))
print(any(map(str.isdigit, S)))
print(any(map(str.islower, S)))
print(any(map(str.isupper, S)))


