def main():
   course_numbers = [];
   units = [];
   grade = [];
   points = [];

   while True:
       line = input("Enter course number, units, and grade, separated by spaces \n");
       if len(line) == 0:
           break;
       space = line.split(" ");
       course_numbers.append(space[0]);
       units.append(int(space[1]));
       grade.append(space[2]);
   for i in range(0, len(grade)):
       Points = grade_points(grade[i]);
       Points = Points * units[i];
       points.append(Points);
   GPA = sum(points) / sum(units);   
   print("The GPA is %.2f \n" %(GPA));
  
def grade_points(grade):
   c_points = 0;
   gradepoints_value = {'A': 4, 'B': 3, 'C': 2, 'D': 1, 'F': 0};
  
   letter = '';
   symbol = '';
   if len(grade) == 2:
       letter = grade[0];
       symbol = grade[1];
   else:
       letter = grade;
   c_points = gradepoints_value[letter];
   if symbol == '+' and letter != 'A':
       c_points = c_points + 0.3;
   if symbol == '-' and letter != 'F':
       c_points = c_points - 0.3;
   return c_points;
main();
