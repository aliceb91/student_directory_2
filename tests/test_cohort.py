from lib.cohort import Cohort
from unittest.mock import Mock

def test_create_cohort():
    # Given the required data
    # It produces a Student object with that data at contents.
    student = Mock()
    cohort = Cohort(1, "Test Cohort", [student])
    assert cohort.id == 1
    assert cohort.cohort_name == "Test Cohort"
    assert cohort.students == [student]

def test_compare_cohorts():
    # Given two instances of Student
    # It compares the contents of the two.
    student = Mock()
    cohort_1 = Cohort(1, "Test Cohort", [student])
    cohort_2 = Cohort(1, "Test Cohort", [student])
    assert cohort_1 == cohort_2

def test_outputs_string_of_contents():
    # Given a Student object
    # It outputs a string of it's contents when called.
    student = Mock()
    student.student_name = "Test Student"
    cohort = Cohort(1, "Test Cohort", [student])
    assert str(cohort) == "1, Test Cohort, Test Student"
