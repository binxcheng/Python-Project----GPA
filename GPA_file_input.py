file_name = input('Enter name of input file: ')
total_units = 0
total_score = 0
grade_points= {'A+':4.00,'A':4.0,'A-':3.70,'B+':3.30, 'B':3.00, 'B-':2.70, 'C+': 2.3, 'C':2.00, 'C-':1.70, 'D+':1.30, 'D':1.00, 'D-':0.70, 'F':0}
##def grade_points(grade):
##   c_points = 0;
##   gradepoints_value = {'A': 4, 'B': 3, 'C': 2, 'D': 1, 'F': 0};
##  
##   letter = '';
##   symbol = '';
##   if len(grade) == 2:
##       letter = grade[0];
##       symbol = grade[1];
##   else:
##       letter = grade;
##   c_points = gradepoints_value[letter];
##   if symbol == '+' and letter != 'A':
##       c_points = c_points + 0.3;
##   if symbol == '-' and letter != 'F':
##       c_points = c_points - 0.3;
##   return c_points;
try:
    with open(file_name,'r') as input_file: #r = reading
        output_file = open('GPA_output.txt','w')
        for student_record in input_file: 
            if (',' in student_record):
                student_name =student_record.strip('\n') #remove \n
                continue
            else:
                if (' ' in student_record):
                    student = student_record.split (' ')
                    total_units +=int(student[1])
                    total_score += int(student[1]) * grade_points[student[2].strip('\n')]
                    continue
                else:
                    if (total_units >0):
                        print('in')
                        GPA = total_score/total_units
                        output_file.write ('%-26s%.2f\n' % (student_name, GPA))
                        total_units = 0
                        total_score = 0
        output_file.close()
except Error:
  print('A problem occurred')
