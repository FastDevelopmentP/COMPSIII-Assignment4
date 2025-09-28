class Student:
    # Constructor method
    def __init__(self, name: str, major: str, gpa_for_semesters: list):
        self.name = name
        self.major = major
        self.__gpa_for_semesters = gpa_for_semesters  # private attribute

    # String representation
    def __str__(self) -> str:
        return f"{self.name} is studying {self.major}."

    # Getter for GPA list
    def get_gpa(self) -> list:
        return self.__gpa_for_semesters

    # Setter for GPA list
    def set_gpa(self, new_value: list):
        self.__gpa_for_semesters = new_value

    # Calculates average GPA
    def calculate_average_gpa(self) -> float:
        if len(self.__gpa_for_semesters) == 0:
            return 0.0
        return sum(self.__gpa_for_semesters) / len(self.__gpa_for_semesters)

    # Checks if student is in good standing
    def is_in_good_standing(self, threshold: float = 3.0) -> str:
        avg = self.calculate_average_gpa()
        if avg >= threshold:
            return f"{self.name} is a student in good standing."
        else:
            return f"{self.name} is not in good standing."


    
class UndergraduateStudent(Student):
    def __init__(self, name: str, major: str, gpa_for_semesters: list, set_gpa: float):
        super().__init__(name, major, gpa_for_semesters)
        self.set_gpa(set_gpa)

class GraduateStudent(Student):
    def __init__(self, name: str, major: str, gpa_for_semesters: list, set_gpa: float):
        super().__init__(name, major, gpa_for_semesters)
        self.set_gpa(set_gpa)