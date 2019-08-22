# TODO: Rank Students to trace penultimate score
number_of_entries = int(input("Enter number of students: "))
counter = 0
points = []
while counter < number_of_entries:
    name = input(f"Enter name {counter + 1}: ")
    score = float(input(f"Enter marks for {name}: "))
    points.append([name, score])
    counter += 1
ranked_list = sorted(points, key=lambda x: x[1], reverse=True)
length = len(ranked_list)
minimum_points = ranked_list[length - 1][1]
counter = length
penultimate = []
penultimate_points = None
while counter > 0:
    current = ranked_list[counter-1][1]
    if current > minimum_points:
        penultimate_points = current
        break
    counter -= 1
counter = 0
ranked_list.sort()
while counter < length:
    current = current = ranked_list[counter-1][1]
    if current == penultimate_points:
        print(ranked_list[counter-1][0], ranked_list[counter-1][1])
    counter += 1





