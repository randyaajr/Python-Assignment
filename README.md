# Python-Assignment
-------------------


## This assignment demonstrats my skills in the following:
   * Creating variable following Python naming convention
   * Reading/output data from/to VS Code Terminal
   * Converting string data type to integer
   * Using the two types of loop: While and For
   * Arithmetic operations with BEDMAS Rules
   * Using lists (Like Arrays in JavaScript)
   * If elif condition with logical operators


## Assignment Instructions:
Create a new Python and save it as .py file as “py-assignment1.py”
like py-assignment1.py
1. You will use print() to print the output in the terminal window
2. The assignment was designed to be similar like the challenges that you have been using by adding hints
     and notes about the solution
3. This assignment document contains screen shot for the output to give a better understanding and a
     clear idea about the final result
4. Please feel free to use any other ways or logic you prefer or you like since you will get the same
     results at the end

### Part 1:
1.  You will ask the user to enter how many courses did he/she finish using the input() built-in function:
    * The text to be displayed with the print: “How many courses did you finish?”
    * Declare a variable named “num_of_courses” to save the number of courses (which is the value
      that will be returned from the print function based on the user’s input). The “num_of_course”
      should be just an int variable (variable with integer value). 
    * Make sure that the input value (which is string) is converted into number (numeric) using the
      appropriate Python built-in function that we covered in our lectures

2.  Declare an empty list (empty array in JS), this array variable will be used to contain the course marks
      (later) named “course_marks”. This “course_marks” will be just an empty list exactly as we did in 

3.  You will use “while loop” loop for a specific number of times based on your variable num_of_courses, for
     example if num_of _courses value is 5 as shown in the image above, you will make the loop iterate for 5
     times. In each iteration of the loop, you will ask the user to enter his/her course mark. This mark will be
     inserted into the list “course_marks” immediately (instantly), so you will populate this list with the user
     input through this while loop.

Notice that You need to modify the course number in the print message for every iteration throughout the
loop as shown below (Hint: you can user the same while loop counter since it starts with 1):
   * For the first time: Enter your mark for course 1
   * For the second time: Enter your mark for course 2
   * And so on for the x time: Enter your mark for course x
   * Course_marks list will be updated inside the loop in each iteration to add (save) the current user input
      which represents the current course mark. Don’t forget that lists in Python have a nice method to input
      value into them (please refer to the logic to get more hints and help)

#### **The Logic:**

**Outside the while loop**
   * You can use While Loop with this condition (the loop counter < num_of_courses)
   * Don’t forget to declare a loop counter with its initial value before the loop (Hint: You can definitely go with
      initial value of 1 because in this while loop we NOT will loop through the array index)
      Then (inside the loop): 
   * You will populate (putting the values from the user input) course_marks list (array in JS) on the fly
      (throughout the loop iteration) by adding the user input to the list with append() method 
   * Using input() method (function) that contain the course mark question ending with (concatenating to) the
      loop counter variable to show the question and course 1, course 2, course 3 etc.
   * Remember that the append() method in Python has the same action like push() method in JS 😊). It will
      just append/push the current value at the end of our list (array):
   * Don’t forget to Increment the while loop counter

**Hints**
   * The input() function should be nested inside the append() method
   * You will need to use the appropriate Python function to convert the user input into a numeric value,
      which means the input() function also need to be nested inside the python method for converting string
      number to an integer number
   * Remember that we used two functions to convert string into a number

4. After the user finish inserting all their value into our list “course_marks”, use “for loop” to print the items
     of course_marks list:

