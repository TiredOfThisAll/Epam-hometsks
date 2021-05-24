"""
File `data/students.csv` stores information about students in CSV format.
This file contains the student’s names, age and average mark.

1. Implement a function get_top_performers which receives file path and
returns names of top performer students.
Example:
def get_top_performers(file_path, number_of_top_students=5):
    pass

print(get_top_performers("students.csv"))

Result:
['Teresa Jones', 'Richard Snider', 'Jessica Dubose', 'Heather Garcia',
'Joseph Head']

2. Implement a function write_students_age_desc which receives the file path
with students info and writes CSV student information to the new file in
descending order of age.
Example:
def write_students_age_desc(file_path, output_file):
    pass

Content of the resulting file:
student name,age,average mark
Verdell Crawford,30,8.86
Brenda Silva,30,7.53
...
Lindsey Cummings,18,6.88
Raymond Soileau,18,7.27
"""


class StudentsModel:
    def __init__(self, student_name, age, average_mark):
        self.student_name = student_name
        self.age = age
        self.average_mark = average_mark

    def from_tuple(students_tuple):
        return StudentsModel(*students_tuple)

    def to_tuple(self):
        return self.student_name, self.age, self.average_mark

    def __str__(self):
        return f"{self.student_name},{self.age},{self.average_mark}"


def get_top_performers(file_path, number_of_top_students=5):
    with open(file_path, "r+") as file:
        students_csv = file.read().split("\n")
    students = []
    for student in students_csv[1:]:
        students.append(StudentsModel.from_tuple(student.split(",")))
    sorted_by_marks = sorted(students, key=lambda student: float(student.average_mark), reverse=True)
    return list(map(lambda x: x.student_name, sorted_by_marks[:number_of_top_students]))


def write_students_age_desc(file_path, output_file):
    with open(file_path, "r+") as file:
        students_csv = file.read().split("\n")
    students = []
    for student in students_csv[1:]:
        students.append(StudentsModel.from_tuple(student.split(",")))
    sorted_by_marks = sorted(students, key=lambda student: int(student.age), reverse=True)
    result = "student name,age,average mark\n" + "".join(list(map(lambda student: ",".join(student.to_tuple()) + "\n", sorted_by_marks)))
    with open(output_file, "w+") as file:
        file.write(result)
