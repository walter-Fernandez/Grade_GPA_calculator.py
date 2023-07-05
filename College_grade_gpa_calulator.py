#submit your three midterms grade and your final and the system will output your grade and GPA
#each midterm is 15% of your grade and your final exam is 55%
def student():
    midterm_1 = int(input("what is your grade 1: "))
    midterm_2 = int(input("what is your grade 2: "))
    midterm_3 = int(input("what is your grade 3: "))
    final = int(input("what is your grade on your final exam: "))
    final_grade = midterm_1*.15+midterm_2*.15+midterm_3*.15+final*.55
    print("your final grade is: ",final_grade)

    if final_grade>= 93 and final_grade<= 100:
        print("A+ : your GPA is 4.0")
    elif final_grade>= 90 and final_grade<= 92.9:
        print("A- : your GPA is 3.7")
    elif final_grade>= 87 and final_grade<= 89.9:
        print("B+ : your GPA is 3.3")
    elif final_grade>= 80 and final_grade<= 82.9:
        print("B- : your GPA is 2.7")
    else:
        print("C-: your GPA is 1.7")



student()


