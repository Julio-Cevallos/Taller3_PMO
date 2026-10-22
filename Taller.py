
class Student:
    """Manage a student's information and grades."""

    def __init__(self, student_id, name):
        if not isinstance(student_id, str) or not student_id.strip():
            raise ValueError("Student ID cannot be empty.")

        if not isinstance(name, str) or not name.strip():
            raise ValueError("Student name cannot be empty.")

        self.student_id = student_id.strip()
        self.name = name.strip()
        self.grades = []

    def add_grade(self, grade):
        """Add a grade between 0 and 100."""
        if isinstance(grade, bool) or not isinstance(
            grade, (int, float)
        ):
            raise ValueError("Grade must be numeric.")

        if not 0 <= grade <= 100:
            raise ValueError("Grade must be between 0 and 100.")

        self.grades.append(float(grade))

    def calculate_average(self):
        """Calculate the average of all grades."""
        if not self.grades:
            return None

        return sum(self.grades) / len(self.grades)

    def get_letter_grade(self):
        """Return the letter grade based on the average."""
        average = self.calculate_average()

        if average is None:
            return "N/A"
        if average >= 90:
            return "A"
        if average >= 80:
            return "B"
        if average >= 70:
            return "C"
        if average >= 60:
            return "D"
        return "F"

    def get_status(self):
        """Return the student's pass/fail status."""
        average = self.calculate_average()

        if average is None:
            return "N/A"

        return "Passed" if average >= 60 else "Failed"

    def is_honor_roll(self):
        """Check whether the student qualifies for Honor Roll."""
        average = self.calculate_average()
        return average is not None and average >= 90

    def remove_grade_by_index(self, index):
        """Remove a grade using its zero-based index."""
        if not isinstance(index, int) or isinstance(index, bool):
            raise ValueError("Index must be an integer.")

        if not 0 <= index < len(self.grades):
            raise IndexError("Grade index is out of range.")

        return self.grades.pop(index)

    def remove_grade_by_value(self, grade):
        """Remove the first grade matching the given value."""
        if isinstance(grade, bool) or not isinstance(
            grade, (int, float)
        ):
            raise ValueError("Grade must be numeric.")

        try:
            self.grades.remove(float(grade))
        except ValueError as error:
            raise ValueError("Grade not found.") from error

    def generate_report(self):
        """Generate a formatted student summary report."""
        average = self.calculate_average()
        average_text = (
            f"{average:.2f}" if average is not None else "N/A"
        )
        honor_roll = "Yes" if self.is_honor_roll() else "No"

        return (
            "\n--- Student Summary Report ---\n"
            f"Student ID: {self.student_id}\n"
            f"Student Name: {self.name}\n"
            f"Number of Grades: {len(self.grades)}\n"
            f"Average Grade: {average_text}\n"
            f"Letter Grade: {self.get_letter_grade()}\n"
            f"Pass/Fail Status: {self.get_status()}\n"
            f"Honor Roll: {honor_roll}\n"
            "------------------------------"
        )


def main():
    """Run the student grade management system."""
    students = {}

    while True:
        print("\n=== Student Grade Management System ===")
        print("1. Add student")
        print("2. Add grade")
        print("3. Remove grade")
        print("4. Generate student report")
        print("5. Exit")

        option = input("Choose an option: ").strip()

        if option == "1":
            student_id = input("Enter student ID: ").strip()
            name = input("Enter student name: ").strip()

            try:
                student = Student(student_id, name)

                if student_id in students:
                    print("Error: Student ID already exists.")
                    continue

                students[student_id] = student
                print("Student added successfully.")

            except ValueError as error:
                print(f"Error: {error}")

        elif option == "2":
            student_id = input("Enter student ID: ").strip()
            student = students.get(student_id)

            if student is None:
                print("Error: Student not found.")
                continue

            try:
                grade = float(input("Enter grade (0-100): "))
                student.add_grade(grade)
                print("Grade added successfully.")

            except ValueError as error:
                print(f"Error: {error}")

        elif option == "3":
            student_id = input("Enter student ID: ").strip()
            student = students.get(student_id)

            if student is None:
                print("Error: Student not found.")
                continue

            print("1. Remove by index")
            print("2. Remove by value")
            method = input("Choose a method: ").strip()

            try:
                if method == "1":
                    print(f"Current grades: {student.grades}")
                    index = int(input("Enter zero-based index: "))
                    removed = student.remove_grade_by_index(index)
                    print(f"Removed grade: {removed:g}")

                elif method == "2":
                    grade = float(input("Enter grade to remove: "))
                    student.remove_grade_by_value(grade)
                    print("Grade removed successfully.")

                else:
                    print("Error: Invalid removal method.")

            except (ValueError, IndexError) as error:
                print(f"Error: {error}")

        elif option == "4":
            student_id = input("Enter student ID: ").strip()
            student = students.get(student_id)

            if student is None:
                print("Error: Student not found.")
            else:
                print(student.generate_report())

        elif option == "5":
            print("Exiting the system.")
            break

        else:
            print("Error: Please choose a valid option.")


if __name__ == "__main__":
    main()
