a = int(input("Enter Number"))

if 1 <= a <= 20:
    counter = 0
    while counter < a:
        print(counter ** 2)
        counter += 1
