# simple rank
# rank the runners up
n = int(input("Enter Number Of Students: "))
arr = map(int, input("Enter Marks: ").split(","))
arr_ = list(arr)
if len(arr_) > n and n < 2:
    print("Out of range")
else:
    arr_.sort(reverse=True)
    n = 1
    max_ = arr_[0]
    while n <= len(arr_) - 1:
        next_ = arr_[n]
        if next_ != max_:
            print(next_)
            break
        else:
            pass
        n += 1



