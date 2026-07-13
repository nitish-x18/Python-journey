# class student:
#     def __init__(self,name,roll_num,marks):
#         self.name = name
#         self.roll_num = roll_num
#         self.marks = marks
#         # self.clas = clas
#         # self.sec = sec

#         def set_data():
#             for i in range(5):
#                 name = input("enter your name: ")
#                 roll_num = input("enter your roll_num: ")
#                 marks = input("enter your marks: ")

#         def display():
#             print(name)
#             print(roll_num)
#             print(marks)

# s1 = student()
# s1.set_data()

with open("text.txt", "w") as f:
    for i in range(5):
        name = input("enter your name: ")
        roll_num = input("enter your roll_num: ")
        marks = input("enter your marks: ")

    f.write(f"{name},{roll_num},{marks}")