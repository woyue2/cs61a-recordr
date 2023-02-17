# class Student:
#     def __init__(self,name,learnindex,yuwen,shuxue,english):
#         self.name = name
#         self.learnindex = learnindex
#         self.yuwen = yuwen
#         self.shuxue= shuxue
#         self.english = english
#     def print(self,subject):
#         print(f"分数是{self.subject}")
#     def printAll(self):
#         print(self.yuwen,self.shuxue,self.english)
'''LearingFrom https://youtu.be/6c4yOoJNhPI'''
class Student:
    def __init__(self, name, student_id) :
        self.name = name
        self.student_id = student_id
        self.grades = {"语":0,"数":0,"英":0}

    def set_grade(self,course,grade):
        if course in self.grades:
            self.grades[course] = grade

    def print_grades(self):
        for course in self.grades:
            print(f"{course}分数是：{self.grades[course]}分")
            
ming = Student("小明",1)
print(ming.grades,ming.name,ming.student_id)
ming.set_grade('语',10)
ming.set_grade('数',110)
print(ming.grades)
ming.print_grades()