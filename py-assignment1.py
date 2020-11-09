num_of_courses = int(input('How many courses did you finish?'))


course_marks = []

count = 1
while count < num_of_courses:
    course_marks.append(int(input(f'Enter your marks for course {str(count)}:')))
    count += 1

    
