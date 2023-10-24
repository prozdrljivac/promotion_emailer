import csv
import os
import unittest

from tempfile import NamedTemporaryFile

from apps.employee.services import Employee, get_employees_from_csv


class TestEmployeeService(unittest.TestCase):
    def setUp(self):
        self.csv_file = NamedTemporaryFile(
            delete=False,
            mode="w",
            newline="",
        )
        self.csv_writer = csv.DictWriter(
            self.csv_file,
            fieldnames=Employee.__annotations__.keys(),
        )
        self.csv_writer.writeheader()
        self.csv_writer.writerow(
            {
                "first_name": "John",
                "last_name": "Doe",
                "gender": "Male",
                "position": "Manager",
                "email": "johndoe@example.com",
            }
        )
        self.csv_file.close()

    def tearDown(self):
        os.remove(self.csv_file.name)

    def test_get_employees_from_csv(self):
        # Test reading employees from a CSV file
        employees = get_employees_from_csv(self.csv_file.name)

        # Check if the returned data matches the expected Employee object
        self.assertEqual(len(employees), 1)
        employee = employees[0]
        self.assertEqual(employee.first_name, "John")
        self.assertEqual(employee.last_name, "Doe")
        self.assertEqual(employee.gender, "Male")
        self.assertEqual(employee.position, "Manager")
        self.assertEqual(employee.email, "johndoe@example.com")

    def test_get_employees_from_csv_file_not_found(self):
        # Test handling a file not found error
        non_existent_file = "non_existent_file.csv"
        employees = get_employees_from_csv(non_existent_file)

        # Check if the function returns an empty list
        self.assertEqual(len(employees), 0)


if __name__ == "__main__":
    unittest.main()
