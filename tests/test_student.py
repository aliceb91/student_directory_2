from lib.student import Student

def test_create_student():
    # Given the required data
    # It produces a Student object with that data at contents.
    student = Student(1, "Test Student", 4)
    assert student.id == 1
    assert student.student_name == "Test Student"
    assert student.cohort_id == 4

def test_compare_students():
    # Given two instances of Student
    # It compares the contents of the two.
    student_1 = Student(1, "Test Student", 4)
    student_2 = Student(1, "Test Student", 4)
    assert student_1 == student_2

def test_outputs_string_of_contents():
    # Given a Student object
    # It outputs a string of it's contents when called.
    student = Student(1, "Test Student", 4)
    assert str(student) == "1, Test Student, 4"
