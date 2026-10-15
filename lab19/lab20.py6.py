student=[
("Asha",88),
("Ravi",72),
("meera",95),
("karan",59),
("divya",81)
]
total =0
highest_name = student[0][0]
highest_marks = student[0] [1]
lowest_name = student[0][0]
lowest_marks = student[0][1]
for name , marks in student:
    total += highest_marks
    if marks >=90:
        grade = "A"
    elif marks >=80:
        grade = "B"
    elif marks >=70:
        grade = "c"
    elif marks >=60:
        grade = "D"
    else:
        

     print(name,":",marks,"grade =", grade)
    if marks > highest_marks:
       highest_marks = marks
       highest_name = name
    if marks < lowest_marks:
        lowest_marks = marks
        lowest_name = name
average = total / len(student)
print("class average:",average)
print("Top scorer:",highest_name,highest_marks)
print("Bottom scorer:",lowest_name,lowest_marks)



