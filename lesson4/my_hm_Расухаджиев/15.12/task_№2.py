class SchoolClass:

     def __init__(self, name, form,students=[],marks=[]):
          self.name = name
          self.form = form
          self.students = students
          self_marks = marks

     def math_mark(self, mark,all=0, marks=[],middle=0,):
         for i in range(0,len(marks)):
             all = all + marks[i]
         middle = all//len(marks)
         mark = middle
         self.mark = mark

     def sort_by_marks(self):
          for i in range(len(self.students)):
               for f in range(len(self.students)-1):
                    if self.mark[f] > self.mark[f+1]:
                         self.students[f], self.students[f+1] = self.students[f+1] , self.students[f]
                         self.mark[f], self.mark[f+1] = self.mark[f+1] , self.mark[f]
                         self.form[f], self.form[f+1] = self.form[f+1], self.form[f]
     
     def best_pupils(self):
          for i in range(len(self.students)):
               for j in range(4,5):
                    if self.mark == j:
                         print(self.students,end = " ")
                         print(self.mark, end = " ")
                         print(self.form)

students = ["Rasukhadjiev B.A.","Gritchenko N.A.","Rozarev E.A.","Skolkov A.V.","Otrashkevich S.A.","Nemchinov K.V.","Chizhikova O.S.","Gustov D.K.","Unin S.A.","Calinin S.B."]
marks =[5,4,5,5,4],[4,4,3,5,4],[3,3,4,5,4],[5,5,4,3,3],[2,4,5,3,5],[5,3,2,5,4],[4,2,5,3,4],[3,4,5,3,4],[4,5,4,5,3],[4,5,2,3,4]
form = [9,8,10,6,7,8,9,11,8,7]

print(students)
group = SchoolClass("School № 1530",form, students, marks)

