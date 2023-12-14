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
        
grade_format = "20s11sf"
def pack_grade(grade):
    return struct.pack(grade_format, grade.course.encode(), grade.roll_no.encode(), grade.percent_marks)

def unpack_grade(data):
    unpacked_data = struct.unpack(grade_format, data)
    course, roll_no, percent_marks = unpacked_data
    return Grade(course.decode().rstrip('\x00'), roll_no.decode().rstrip('\x00'), percent_marks)

student_format = "11s30s2sIf11s"
def pack_student(student):
    return struct.pack(student_format, student.roll_no.encode(), student.name.encode(), student.dept_code.encode(),
                       student.semester, student.last_sem_percent, student.phone.encode())

def unpack_student(data):
    unpacked_data = struct.unpack(student_format, data)
    roll_no, name, dept_code, semester, last_sem_percent, phone = unpacked_data
    return Student(roll_no.decode().rstrip('\x00'), name.decode().rstrip('\x00'), dept_code.decode().rstrip('\x00'),
                   semester, last_sem_percent, phone.decode().rstrip('\x00'))

def write_data(file_name, data, pack_func):
    with open(file_name, 'wb') as file:
        for item in data:
            file.write(pack_func(item))


def read_data(file_name, unpack_func, fmt):
    with open(file_name, 'rb') as file:
        data = []
        format_size = struct.calcsize(fmt)
        while True:
            chunk = file.read(format_size)
            if not chunk:
                break
            data.append(unpack_func(chunk))
    return data

def quit_system():
    print("Quitting the management system.")
    exit()

def add_student(students, new_student, student_data_file):
    flag = 1
    for existing_student in students:
        if existing_student.roll_no == new_student.roll_no:
            print(f"Duplicate entry! Student with roll number {new_student.roll_no} already exists.")
            flag = 0
            break
    if flag == 1:
        students.append(new_student)
        print(f"Student with roll number {new_student.roll_no} added successfully!")
        write_data(student_data_file, students, pack_student)
        

def view_student_by_roll_no(students, roll_no):
    flag = 1
    for student in students:
        if student.roll_no == roll_no:
            print(f"Roll No: {student.roll_no}, Name: {student.name}, Dept Code: {student.dept_code}, "
                  f"Semester: {student.semester}, Last Sem Percent: {student.last_sem_percent}, Phone: {student.phone}")
            flag = 0
            break
    if flag == 1:
        print(f"No student found with roll number {roll_no}.")

def edit_student_by_roll_no(students, new_student_data, student_data_file):
    flag =1 
    for student in students:
        if student.roll_no == new_student_data.roll_no:
            student.name = new_student_data.name
            student.dept_code = new_student_data.dept_code
            student.semester = new_student_data.semester
            student.last_sem_percent = new_student_data.last_sem_percent
            student.phone = new_student_data.phone
            write_data(student_data_file, students, pack_student)
            print(f'Updated successfully\nRoll no: {new_student_data.roll_no}, name: {new_student_data.name}, dept_code: {new_student_data.dept_code}, '
                  f'semester: {new_student_data.semester}, last_sem_percent: {new_student_data.last_sem_percent}, phone: {new_student_data.phone}')
            flag = 0
            break
    if flag == 1:
        print(f'No student find with roll no {roll_no} ')

def del_student(students, roll_no, student_data_file):
    for student in students:
        if student.roll_no == roll_no:
            students.remove(student)
            print(f"Student with roll number {roll_no} deleted successfully")
            write_data(student_data_file, students, pack_student)
            break

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

def add_grade(grades, new_grade, grade_data_file):
    flag = 1
    for grade in grades:
        if (grade.roll_no == new_grade.roll_no and grade.course==new_grade.course):
            print(f"Duplicate entry! course {new_grade.course} already exist")
            flag = 0
            break
    if flag == 1:
        grades.append(new_grade)
        print(f"grade  for course {new_grade.course} added successfully!")
        write_data(grade_data_file, grades, pack_grade)

def import_grade(file_name, grades, grade_data_file):

    with open(file_name, 'r') as file:
        file.readline()
        for line in file:
            flag = 1
            roll_no, course, percent_marks = line.strip().split('\t')
            new_grade = Grade(roll_no, course, float(percent_marks))
            for grade in grades:
                if grade.roll_no == new_grade.roll_no and grade.course == new_grade.course:
                    print(f"Duplicate entry! roll no: {new_grade.roll_no} and course {new_grade.course}")
                    flag = 0
                    break
            if flag == 1:
                add_grade(grades, new_grade, grade_data_file)
                print(f"Grade for course {new_grade.course} added successfully!")
                    
def view_grade_by_course(grades, course):
    for grade in grades:
        if grade.course == course:
            print(f"Roll No: {grade.roll_no}, course:{grade.course} Percent_marks: {grade.percent_marks}")

def edit_grade_for_course(grades, new_grade_data, grade_data_file):
    flag =1 
    for grade in grades:
        if grade.course==new_grade_data.course and grade.roll_no==new_grade_data.roll_no:
            grade.percent_marks = new_grade_data.percent_marks
            write_data(grade_data_file, grades, pack_grade)
            print(f"Data updated successfully\nRoll no: {new_grade_data.roll_no}, "
                  f"course: {new_grade_data.course}, percent_marks: {new_grade_data.percent_marks}")
            flag = 0
            break
    if flag == 1:
        print(f'No grade found for Roll number {grade.roll_no} and Course {grade.course}.')

def del_grade(grades, roll_no, course, grade_data_file):
    for grade in grades:
        if grade.roll_no == roll_no and grade.course == course:
            grades.remove(grade)
            print(f"grade with Roll no {roll_no} and Course {course} removed successfully")
            write_data(grade_data_file, grades, pack_grade)
            break

def list_student_marks_for_each_course(grades, roll_no):
    print(f"\nRoll no: {roll_no}")
    for grade in grades:
        if grade.roll_no == roll_no:
            print(f"Course: {grade.course}, Percent marks: {grade.percent_marks}")
    
def list_course_marks(grades, course):
    print(f"\nCourse: {course}")
    for grade in grades:
        if grade.course == course:
            print(f"Roll no: {grade.roll_no}, Percent_marks: {grade.percent_marks}")
            
def award_sheet(grades, students):
    unique_courses = set(grade.course for grade in grades)
    for course in unique_courses:
        print(f"\nCourse: {course}\n")
        for grade in grades:
            for student in students:
                if grade.course == course and grade.roll_no == student.roll_no:
                    print(f"Roll No: {student.roll_no}  (Name: {student.name}, Dept Code: {student.dept_code},"
                          f" Semester: {student.semester}, Last Sem Percent: {student.last_sem_percent}, Phone: {student.phone})-{grade.percent_marks}")

def summary_sheet(grades):
    unique_courses = set(grade.course for grade in grades)
    for course in unique_courses:
        print(f"\nCourse: {course.upper()}")
        for grade in grades:
            if grade.course == course:
                print(f"Roll no: {grade.roll_no}, Percent marks: {grade.percent_marks}")

def generate_transcript(student, grades):
    print(f"Transcript for {student.name} (Roll No: {student.roll_no}):")
    
    for grade in grades:
        if grade.roll_no == student.roll_no:
            print(f"- Course: {grade.course}, Percent Marks: {grade.percent_marks}%")

def main():
    file_1 = "students.dat"
    file_2 = "grades.dat"
    new_student1 = Student('bsdsf22a039', 'muqadsa qudoos', 'ds', 2, 3.61, '03027615626')
    new_student2 = Student('bsdsf22a044', 'rabbiya Bukhari', 'ds', 2, 3.65, '12345678912')
    new_student3 = Student('bsdsf22a032', 'bisma ', 'ds', 2, 3.61, '03145678912')
    new_student4 = Student('bscsf22a031', 'hamna', 'cs', 5, 3.98, '12345678912')
    new_student5 = Student('bscsf22a030', 'ayesha', 'cs', 5, 3.45, '13456978912')
    new_student6 = Student('bscsf22a038', 'mahnum', 'cs', 5, 3.90, '04527816526')
    new_student7 = Student('bssef22a036', 'kashaf Abbas', 'se', 2, 3.78, '04527816526')
    new_student8 = Student('bssef22a015', 'khalood', 'se', 2, 3.34, '12345609876')
    new_student9 = Student('bssef22a014', 'tehreem fatima', 'cs', 2, 3.98, '03892716526')

    students = read_data(file_1, unpack_student, student_format)
    # add student
    print("adding students:")
    add_student(students, new_student1, file_1)
    add_student(students, new_student2, file_1)
    add_student(students, new_student3, file_1)
    add_student(students, new_student4, file_1)
    add_student(students, new_student5, file_1)
    add_student(students, new_student6, file_1)
    add_student(students, new_student7, file_1)
    add_student(students, new_student8, file_1)
    add_student(students, new_student9, file_1)
    
    #view student
    print("\nView Students:")
    view_student_by_roll_no(students, "bsdsf22a039")

    #edit student
    print("\nedit Student:")
    new_student5 = Student('bssef22a014', 'tehreem fatima', 'cs', 2, 4.00, '03892716526')
    edit_student_by_roll_no(students, new_student5, file_1)
    

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
    new_grade1 = Grade("oop","bsdsf22a039",73.8)
    new_grade2 = Grade("dld","bsdsf22a039",79.8)
    grades = read_data(file_2, unpack_grade, grade_format)

    #add grade
    print("\nadding grades")
    add_grade(grades, new_grade1, file_2)
    add_grade(grades, new_grade2, file_2)

    #import grade from text file
    print("\nimport grades from text file")
    import_grade('tabed_text_file.txt', grades, file_2)

    #view grade
    print("\nView grades:")
    view_grade_by_course(grades,"oop")

    #edit grade
    print("\nedit grade:")
    new_grade3 = Grade("probability","bsdsf22a039",90.0)
    edit_grade_for_course(grades, new_grade3, file_2)

    #list each course for 1 studnet
    list_student_marks_for_each_course(grades, 'bsdsf22a031')

    #list marks for 1 course
    list_course_marks(grades, "dld")

    #award sheet
    print("AWARD SHEET")
    award_sheet(grades, students)

    #summarysheet
    print("\nSUMMARY SHEET")
    summary_sheet(grades)

    #transcript
    print("\nTRANSCRIPT OF STUDENT")
    generate_transcript(new_student1, grades)
    

main()
