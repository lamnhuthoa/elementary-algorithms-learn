# Bai 5
# Searching Students
class Student:
    def __init__(self, student_id, math, literature):
        self.student_id = student_id
        self.math = math
        self.literature = literature
        
    
class StudentSearcher:
    def __init__(self, students):
        self.students = students
        
    def add_student(self, student):
        self.students.append(student)

    def search_by_student_id(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                return student
        return None
    
    def return_students_scores_by_id(self, student_id):
        student = self.search_by_student_id(student_id)
        if student:
            return (student.math, student.literature)
        else:
            return None
        
num_of_students, num_of_queries = map(int, input().split())

students = []
for _ in range(num_of_students):
    student_id, math, literature = input().split()
    students.append(Student(student_id, float(math), float(literature)))
    
searcher = StudentSearcher(students)
scores = []
for _ in range(num_of_queries):
    query_id = input().strip()
    score_tuple = searcher.return_students_scores_by_id(query_id)
    scores.append(score_tuple) if score_tuple else scores.append((0, 0))
    

for score in scores:
    print(f"{score[0]:.2f} {score[1]:.2f}")