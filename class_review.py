class Course:
    def __init__(self, name, course_number, pre_reqs):
        self.name = name
        self.course_number = course_number
        self.pre_reqs = pre_reqs

    def list_all_pre_reqs(self):
        #for index in range(0,len(self.pre_reqs)):
            #print(self.pre_reqs[index])

        for course in self.pre_reqs:
            print(course)

#Create an array of prereq courses

calculus1 = Course("Calculus1", "3012", [])
calculus2 = Course("Calculus2", "3022", [calculus1])
linear_Algebra = Course("Linear Algebra", "3025", [])

course = Course("Calculus 3", "3045", [calculus2])

course.list_all_pre_reqs()



class Student:
    def __init__(self, first_name, last_name, student_id):
        self.first_name = first_name
        self.last_name = last_name
        self.student_id = student_id


student1 = Student("John", "Doe", "25154")
print(student1)