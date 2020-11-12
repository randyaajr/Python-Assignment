num_of_courses = int(input('How many courses did you finish?'))


course_marks = []

count = 1
while (count <= num_of_courses):
    course_marks.append(
        int(input(f'Enter your marks for course {str(count)}:')))
    count += 1

for item in course_marks:
    print(item)

total = 0
for mark in course_marks:
    total = total + mark

average = round(total/num_of_courses, 2)
print(f'Ypur average for your {num_of_courses} courses in {average}')
