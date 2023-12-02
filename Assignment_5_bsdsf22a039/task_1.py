import struct

class Student:
    def __init__(self, roll_no, name, dept_code, semester, last_sem_percent, phone):
        self.roll_no = roll_no
        self.name = name
        self.dept_code = dept_code
        self.semester = semester
        self.last_sem_percent = last_sem_percent
        self.phone = phone

class Grade:
    def __init__(self, course, roll_no, percent_marks):
        self.course = course
        self.roll_no = roll_no
        self.percent_marks = percent_marks

def pack_student(student):
    return struct.pack('11s30s2sIf11s', student.roll_no.encode('utf-8'), student.name.encode('utf-8'),
                       student.dept_code.encode('utf-8'), student.semester, student.last_sem_percent,
                       student.phone.encode('utf-8'))

def unpack_student(data):
    unpacked_data = struct.unpack('11s30s2sIf11s', data)
    roll_no, name, dept_code, semester, last_sem_percent, phone = unpacked_data
    return Student(roll_no.decode('utf-8'), name.decode('utf-8'), dept_code.decode('utf-8'),
                   semester, last_sem_percent, phone.decode('utf-8'))

def pack_grade(grade):
    return struct.pack('20s11sf', grade.course.encode('utf-8'), grade.roll_no.encode('utf-8'), grade.percent_marks)

def unpack_grade(data):
    unpacked_data = struct.unpack('20s11sf', data)
    course, roll_no, percent_marks = unpacked_data
    return Grade(course.decode('utf-8'), roll_no.decode('utf-8'), percent_marks)

def write_data(file_name, data, pack_func):
    with open(file_name, 'ab') as file:
        for item in data:
            file.write(pack_func(item))

def read_data(file_name, unpack_func):
    try:
        with open(file_name, 'rb') as file:
            data = []
            while True:
                chunk = file.read(struct.calcsize(unpack_func.__code__.co_argcount * 'sIf'))
                if not chunk:
                    break
                data.append(unpack_func(chunk))
    except FileNotFoundError:
        data = []
    return data
def add_student(students, new_student):
    for student in students:
        if student.roll_no == new_student.roll_no:
            print(f"Duplicate entry! Student with roll number {new_student.roll_no} already exists.")
            return
    students.append(new_student)
    print(f"Student with roll number {new_student.roll_no} added successfully.")



def view_student_by_roll_no(students, roll_no):
    for student in students:
        if student.roll_no == roll_no:
            print(f"Student found with roll number {roll_no}:")
            print(f"Roll No: {student.roll_no}, Name: {student.name}, Dept Code: {student.dept_code}, "
                  f"Semester: {student.semester}, Last Sem Percent: {student.last_sem_percent}, Phone: {student.phone}")
            return
    print(f"No student found with roll number {roll_no}.")

def edit_student_by_roll_no(students, roll_no, new_student_data):
    for i, student in enumerate(students):
        if student.roll_no == roll_no:

            for other_student in students:
                if other_student.roll_no == new_student_data.roll_no and other_student.roll_no != roll_no:
                    print(f"Duplicate entry! Another student with roll number {new_student_data.roll_no} already exists.")
                    return

            students[i] = new_student_data
            print(f"Student with roll number {roll_no} edited successfully.")
            return

    print(f"No student found with roll number {roll_no}.")
def delete_student_by_roll_no(students, roll_no):
    for i, student in enumerate(students):
        if student.roll_no == roll_no:
            del students[i]
            print(f"Student with roll number {roll_no} deleted successfully.")
            return

    print(f"No student found with roll number {roll_no}.")
def list_students_by_semester(students, target_semester):
    found_students = [student for student in students if student.semester == target_semester]

    if found_students:
        print(f"Students in semester {target_semester}:")
        for student in found_students:
            print(f"Roll No: {student.roll_no}, Name: {student.name}, Dept Code: {student.dept_code}, "
                  f"Semester: {student.semester}, Last Sem Percent: {student.last_sem_percent}, Phone: {student.phone}")
    else:
        print(f"No students found in semester {target_semester}.")
def list_students_by_name(students, target_name):
    found_students = [student for student in students if target_name.lower() in student.name.lower()]

    if found_students:
        print(f"Students with name containing '{target_name}':")
        for student in found_students:
            print(f"Roll No: {student.roll_no}, Name: {student.name}, Dept Code: {student.dept_code}, "
                  f"Semester: {student.semester}, Last Sem Percent: {student.last_sem_percent}, Phone: {student.phone}")
    else:
        print(f"No students found with name containing '{target_name}'.")
def add_grade(grades, new_grade):
    for grade in grades:
        if grade.roll_no == new_grade.roll_no and grade.course == new_grade.course:
            print(f"Duplicate entry! Grade for course '{new_grade.course}' already exists for student with roll number {new_grade.roll_no}.")
            return
    grades.append(new_grade)
    print(f"Grade for course '{new_grade.course}' added successfully for student with roll number {new_grade.roll_no}.")

def import_grades_from_file(file_name, course, grades_list):
    try:
        with open(file_name, 'r') as file:
            for line in file:
                data = line.strip().split('\t')
                if len(data) == 2:  
                    roll_no, percent_marks_str = data
                    percent_marks = float(percent_marks_str)

                   
                    for grade in grades_list:
                        if grade.roll_no == roll_no and grade.course == course:
                            print(f"Duplicate entry! Grade for course '{course}' already exists for student with roll number {roll_no}.")
                            return

                    
                    grades_list.append(Grade(course, roll_no, percent_marks))
                    print(f"Grade for course '{course}' added successfully for student with roll number {roll_no}.")

    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found.")

def main():
    students_data_file = 'students.dat'
    grades_data_file = 'grades.dat'

    # Sample student and grade data
    new_student = Student('55555555555', 'Alice Wonderland', 'ME', 1, 92.3, '98765432102')
    new_grade = Grade('History', '55555555555', 85.5)

    # Read existing student and grade data
    students = read_data(students_data_file, unpack_student)
    grades = read_data(grades_data_file, unpack_grade)

    # Add a new student and grade
    add_student(students, new_student)
    add_grade(grades, new_grade)

    # View student by roll number
    roll_no_to_view = '55555555555'
    view_student_by_roll_no(students, roll_no_to_view)

    # Edit student by roll number
    updated_student_data = Student('55555555555', 'Alice Updated', 'CE', 2, 88.5, '98765432103')
    edit_student_by_roll_no(students, roll_no_to_view, updated_student_data)

    # List students by semester
    target_semester_to_list = 2
    list_students_by_semester(students, target_semester_to_list)

    # List students by name
    target_name_to_list = 'Alice'
    list_students_by_name(students, target_name_to_list)

    # Delete student by roll number
    roll_no_to_delete = '55555555555'
    delete_student_by_roll_no(students, roll_no_to_delete)

    # Import grades from a file
    grades_to_import_file = 'grades_to_import.txt'
    course_to_import = 'Physics'
    grades_to_import = []
    import_grades_from_file(grades_to_import_file, course_to_import, grades_to_import)

    # Write updated student and grade data back to files
    write_data(students_data_file, students, pack_student)
    write_data(grades_data_file, grades, pack_grade)

if __name__ == "__main__":
    main()

