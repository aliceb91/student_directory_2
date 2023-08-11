from lib.cohort_repository import CohortRepository
from lib.cohort import Cohort
from lib.student import Student
import pytest

def test_finds_student_list(db_connection):
    # Given a target cohort_id
    # It returns a Cohort object containing the relevant Student objects of the cohort.
    db_connection.seed('seeds/student_directory_2.sql')
    repository = CohortRepository(db_connection)
    cohort = repository.find_with_students(1)
    student_1 = Student(1, "Joe Blogs", 1)
    student_2 = Student(2, "Boe Jlogs", 1)
    student_list = [student_1, student_2]
    test_cohort = Cohort(1, "March 2023", student_list)
    assert cohort == test_cohort
