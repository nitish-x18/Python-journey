import csv

average = 0
highest = 0

with open("student.csv", "r") as file:
    reader = csv.reader(file)

    # for row in reader:
    #     print(row)

    for i in reader:
        math = int(i["math"])
        science = int(i["science"])
        english = int(i["english"])

        total = math + science + english
        average = total/3

        if average > highest:
            highest = average
        
        print(f"Total marks: {total}, Average marks: {average}")
        print(f"Highest marks: {highest}")