from jinja2 import Environment, FileSystemLoader

from apps.employee.services import get_employees_from_csv
from apps.email.services import TestEmailService, BasicEmailService
from settings import EMAIL_SERVICE

env = Environment(loader=FileSystemLoader("apps/email/templates"))
template = env.get_template("promotion_template.txt")

email_service = {
    "test": TestEmailService,
}.get(
    EMAIL_SERVICE,
    None,
)


def main():
    employees = get_employees_from_csv("test.csv")
    for employee in employees:
        render_email = template.render(
            {
                "full_name": employee.full_name,
                "position": employee.position,
            }
        )
    es: BasicEmailService = email_service()
    # for employee in employees:
    #     es.send_email(
    #         subject="Promotion!",
    #         body="promotion.txt",
    #         sender="ceo@test.com",
    #         receiver=[employee],
    #     )


if __name__ == "__main__":
    main()
