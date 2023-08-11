class Cohort():
    def __init__(self, id, cohort_name, students):
        # Creates a cohort object.
        #
        # Parameters:
        #   id: int
        #   cohort_name: string
        #   students: A list of student objects that match the cohort's ID.
        self.id = id
        self.cohort_name = cohort_name
        self.students = students

    def __eq__(self, other):
        # Compares the contents of two objects.
        return self.__dict__ == other.__dict__

    def __repr__(self):
        # Returns a string of contents when the object is called.
        name_list = ""
        for student in self.students:
            student_name = student.student_name
            name_list += f"{student_name}, "
        return f"{self.id}, {self.cohort_name}, {name_list[:-2]}"
