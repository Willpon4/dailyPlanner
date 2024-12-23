# AUTHOR: Will Ponczak
# DATE: 12/22/24
# VERSION: 1.0



class Order:

    homework = Homework()
    date = Date()
    course = Course()

    def __init__(self, date, homework, course):
        self.homework = homework
        self.date = date
        self.course = course
