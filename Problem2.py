total_marks = 0
for i in range(0,5):
   obt_marks = int(input("Add Marks for Subject{}\n".format(i+1)))
   total_marks+=obt_marks

percentage = round(total_marks/500*100)
grade = "C" if percentage <50 else "B" if percentage == 50 or percentage <80 else "A"
print(f"Total Marks {total_marks} Percentage {percentage} Grade {grade}")