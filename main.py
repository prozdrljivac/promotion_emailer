from apps.employee.services import get_employees_from_csv
from apps.email.services import TestEmailService, BasicEmailService
from settings import EMAIL_SERVICE

email_service = {
    "test": TestEmailService,
}.get(
    EMAIL_SERVICE,
    None,
)


def main():
    employees = get_employees_from_csv("test.csv")
    # Fill template with user data
    # Send email to employee
    es: BasicEmailService = email_service()
    for employee in employees:
        es.send_email(
            subject="Promotion!",
            body="promotion.txt",
            sender="ceo@test.com",
            receiver=[employee],
        )


if __name__ == "__main__":
    main()
