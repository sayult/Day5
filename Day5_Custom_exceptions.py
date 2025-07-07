class Grade_Error(Exception):   #自定义成绩异常类(定义一个异常)
    def __init__(self, grade):
        self.grade = grade
        super().__init__(f'无效成绩！{grade}(成绩应在0-100之间)')


def check_grade(grade):
    if not 0 <= grade <= 100:
        raise Grade_Error(grade)
    return grade

try:
    check_grade(1065)
except Grade_Error as e:
    print(e)


