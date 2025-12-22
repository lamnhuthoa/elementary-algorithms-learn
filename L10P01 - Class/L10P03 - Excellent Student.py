# Bai 3: Excellent student
class Student:
  def __init__(self, name, math_score, writing_score):
    self.name = name
    self.math_score = math_score
    self.writing_score = writing_score
    
  def calc_gpa(self):
    return (self.math_score + self.writing_score) / 2

  
class ExcellentStudentCount:
    def __init__(self):
        self.students = []
        self.excellent_students = []
        
    def add_student(self, student):
        self.students.append(student)
        
    def add_excellent_student(self, student):
        self.excellent_students.append(student)
        
    def find_excellent_student(self):
        if not self.students:
            return []
        
        for student in self.students:
            gpa_current_student = student.calc_gpa()
            if gpa_current_student >= 9.0:
                self.add_excellent_student(student)
        
        return self.excellent_students
        
def main():
    n = int(input())
    counter = ExcellentStudentCount()
    
    for _ in range(n):
        student_name = input()
        student_scores = list(map(float, input().split()))
        
        student = Student(student_name, student_scores[0], student_scores[1])
        counter.add_student(student)
        
    excellent_students = counter.find_excellent_student()
    
    print(len(excellent_students))
        
        
if __name__ == '__main__':
    main()