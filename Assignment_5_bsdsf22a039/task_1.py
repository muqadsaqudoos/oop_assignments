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
    return struct.pack("11s30s2sIf11s", student.roll_no.encode(), student.name.encode(), student.dept_code.encode(),
                       student.semester, student.last_sem_percent, student.phone.encode())

def unpack_student(data):
    unpacked_data = struct.unpack("11s30s2sIf11s", data)
    roll_no, name, dept_code, semester, last_sem_percent, phone = unpacked_data
    return Student(roll_no.decode().rstrip('\x00'), name.decode().rstrip('\x00'), dept_code.decode().rstrip('\x00'),
                   semester, last_sem_percent, phone.decode().rstrip('\x00'))


def pack_grade(grade):
    return struct.pack("20s11sf", grade.course.encode(), grade.roll_no.encode(), grade.percent_marks)

def unpack_grade(data):
    unpacked_data = struct.unpack("20s11sf", data)
    course, roll_no, percent_marks = unpacked_data
    return Grade(course.decode(), roll_no.decode(), percent_marks)

def write_data(file_name, data, pack_func):
    with open(file_name, 'wb') as file:
        for item in data:
            file.write(pack_func(item))


def read_data(file_name, unpack_func):
    with open(file_name, 'rb') as file:
        data = []
        format_size = struct.calcsize("11s30s2sIf11s")
        while True:
            chunk = file.read(format_size)
            if not chunk:
                break
            data.append(unpack_func(chunk))
    return data


def add_student(students, new_student, student_data_file):
    flag = 1
    for existing_student in students:
        if existing_student.roll_no == new_student.roll_no:
            print(f"Duplicate entry! Student with roll number {new_student.roll_no} already exists.")
            flag = 0
            return
    if flag == 1:
        students.append(new_student)
        print(f"Student with roll number {new_student.roll_no} added successfully!")
        write_data(student_data_file, students, pack_student)

def view_student_by_roll_no(students, roll_no):
    for student in students:
        if student.roll_no == roll_no:
            print(f"Roll No: {student.roll_no}, Name: {student.name}, Dept Code: {student.dept_code}, "
                  f"Semester: {student.semester}, Last Sem Percent: {student.last_sem_percent}, Phone: {student.phone}")
            return
    print(f"No student found with roll number {roll_no}.")

def edit_student_by_roll_no(students, roll_no, new_student_data, student_data_file):
    for student in students:
        if student.roll_no == roll_no:
            student.name = new_student_data.name
            student.dept_code = new_student_data.dept_code
            student.semester = new_student_data.semester
            student.last_sem_percent = new_student_data.last_sem_percent
            student.phone = new_student_data.phone

    write_data(student_data_file, students, pack_student)
    print('Data updated successfully')

def del_student(students, roll_no, student_data_file):
    for student in students:
        if student.roll_no == roll_no:
            students.remove(student)
            print(f"Student with roll number {roll_no} deleted successfully")
            write_data(student_data_file, students, pack_student)
            return

    print(f"Student with roll number {roll_no} does not exist")


def list_student_by_sem(students, sem):
    for student in students:
        if student.semester == sem:
            view_student_by_roll_no(students, student.roll_no)

def list_student_by_name(students, name):
    for student in students:
        if student.name == name:
            view_student_by_roll_no(students, student.roll_no)
            
def print_student_list(students):
    s = []
    for student in students:
        student_info = student.roll_no, student.name, student.dept_code, student.semester, student.last_sem_percent, student.phone
        s.append(student_info)
    print(s)
            

def main():
    file_name = "students.dat"
    new_student1 = Student('bsdsf22a039', 'muqadsa qudoos', 'ds', 2, 3.61, '03027615626')
    new_student2 = Student('abc12345678', 'John Doe', 'cs', 3, 3.75, '1234567890')
    new_student3 = Student('xyz98765432', 'Jane Smith', 'ee', 2, 3.85, '9876543210')

    students = read_data(file_name, unpack_student)
    # add student
    print("adding students:)")
    add_student(students, new_student1, file_name)
    add_student(students, new_student2, file_name)
    add_student(students, new_student3, file_name)
    
    #view student
    print("\nAll Students:")
    for student in students:
        view_student_by_roll_no(students, student.roll_no)

    # list students by semester
    semester = 2
    print(f"\nstudents with semester {semester} are:")
    list_student_by_sem(students, semester)

    #list student by name
    name = "muqadsa qudoos"
    print(f"\nstudents with name {name} is:")
    list_student_by_name(students, name)

    #print student list
    print("\nstudents list:")
    print_student_list(students)

main()

