class Student():
    def __init__(self, id, student_name, cohort_id):
        # Creates a student object.
        #
        # Parameters:
        #   id: int
        #   student_name: string
        #   cohort_id: int
        self.id = id
        self.student_name = student_name
        self.cohort_id = cohort_id

    def __eq__(self, other):
        # Compares the contents of two objects.
        return self.__dict__ == other.__dict__

    def __repr__(self):
        # Returns a string of contents when the object is called.
        return f"{self.id}, {self.student_name}, {self.cohort_id}"
