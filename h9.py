number_of_entries = int(input("Enter number of students "))
counter = 0
students = []
if 2 <= number_of_entries <= 10:
    while counter < number_of_entries:
        i = input("Enter Input").split(" ")
        name = i[0]
        maths = float(i[1])
        physics = float(i[2])
        chemistry = float(i[3])
        print(i)
        breakpoint()
        if 0 <= (maths and physics and chemistry) <= 100:
            student = {
                "name": name,
                "maths": maths,
                "physics": physics,
                "chemistry": chemistry
            }
            students.append(student)
        counter += 1
    print(students)
    query = input("Search For... ")
    for std in students:
        if std.get("name") == query:
            total = std.get("maths") + std.get("physics") + std.get("chemistry")
            avg = total / 3
            print(format(avg, ".2f"))


