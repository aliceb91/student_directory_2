from lib.cohort import Cohort
from lib.student import Student

class CohortRepository():
    def __init__(self, connection):
        # Stores connection data and other variables.
        #
        # Parameters:
        #   connection: A Connection object.
        self._connection = connection

    def find_with_students(self, cohort_id):
        # Returns a cohort object, alongside a list of student objects that relate to this cohort.
        rows = self._connection.execute(
            '''
            SELECT students.id AS students_id, students.student_name, students.cohort_id, cohorts.id AS cohorts_id, cohorts.cohort_name
            FROM students JOIN cohorts 
            ON students.cohort_id = cohorts.id 
            WHERE cohorts.id = %s''', [cohort_id]
        )
        students = []
        for row in rows:
            student = Student(row['students_id'], row['student_name'], row['cohort_id'])
            students.append(student)
        return Cohort(rows[0]['cohorts_id'], rows[0]['cohort_name'], students)
