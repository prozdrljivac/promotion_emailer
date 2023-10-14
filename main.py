from apps.employee.services import get_employees_from_csv


def main():
    # Get List of Employees
    employees = get_employees_from_csv("test.csv")
    # Send them promotion email
    # Create EmailService so it is easy to test and can use different email configurations


if __name__ == "__main__":
    main()
