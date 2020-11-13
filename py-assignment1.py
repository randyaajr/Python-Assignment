# Variable declared whick asks for user input and stores the value entered.
num_of_courses = int(input('How many courses did you finish?'))

# This empty variable store the values entered by the user.
course_marks = []

# This while loop iterates through the inputed amount of courses completed.
count = 1
while (count <= num_of_courses):
    course_marks.append(
        int(input(f'Enter your marks for course {count}: ')))
        #int(input(f'Enter your marks for course {str(count}:'))) ** Removed str as it is not needed
    count += 1

# The for loop here then prints (to the terminal) the inputed values.
for item in course_marks:
    print(item)

# Here is where the values are added. 
continuer = 0
for mark in course_marks:
    continuer = continuer + mark

# Now continuer is devided with the number of courses entered.
average = round(continuer / num_of_courses, 1)
print(f'Your average for your {num_of_courses} courses is: {average}')

# Last but not least, the if statment which determines the overall alphabetical grade.
if average >= 90 and average <= 100:
    print('Your grade is A')
elif average >= 80 and average <= 89:
   print('Your grade is B')
elif average >= 70 and average <= 79:
    print('Your grade is C')
elif average >= 60 and average <= 69:
    print('your grade is D')
else:
    print('Your grade is F')


# End of loop