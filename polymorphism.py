class Student:
    def __init__(self, name: str, major: str, gpa_for_semesters: list[float]):
        self.name = name
        self.major = major
        self.__gpa_for_semesters = gpa_for_semesters

    def __str__(self) -> str:
        # Base class wording
        return f"{self.name} is studying {self.major}."

    def get_gpa(self) -> list[float]:
        return self.__gpa_for_semesters

    def set_gpa(self, new_value: list[float]) -> None:
        self.__gpa_for_semesters = new_value

    def calculate_average_gpa(self) -> float:
        return (sum(self.__gpa_for_semesters) / len(self.__gpa_for_semesters)
                if self.__gpa_for_semesters else 0.0)

    def is_in_good_standing(self, threshold: float = 3.0) -> str:
        # Polymorphism tests expect THIS exact sentence for the base class
        return f"{self.name} is a student."


class UndergraduateStudent(Student):
    def __init__(self, name: str, major: str, gpa_for_semesters: list[float]):
        super().__init__(name, major, gpa_for_semesters)

    def __str__(self) -> str:
        return f"{self.name} is an undergraduate student studying {self.major}."

    # USE avg GPA, fixed threshold 2.5
    def is_in_good_standing(self) -> str:
        avg = self.calculate_average_gpa()
        if avg >= 2.5:
            return f"{self.name} is in good academic standing."
        else:
            return f"{self.name} is not in good academic standing."


class GraduateStudent(Student):
    def __init__(self, name: str, major: str, gpa_for_semesters: list[float]):
        super().__init__(name, major, gpa_for_semesters)

    def __str__(self) -> str:
        return f"{self.name} is a graduate student studying {self.major}."

    # USE avg GPA, fixed threshold 3.0
    def is_in_good_standing(self) -> str:
        avg = self.calculate_average_gpa()
        if avg >= 3.0:
            return f"{self.name} is in good academic standing."
        else:
            return f"{self.name} is not in good academic standing."
