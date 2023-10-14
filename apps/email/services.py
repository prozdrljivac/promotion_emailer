from abc import ABC, abstractmethod
from typing import List, Self


class BasicEmailService(ABC):
    @abstractmethod
    def send_email(
        self: Self,
        subject: str,
        body: str,
        sender: str,
        receiver: List[str],
    ) -> None:
        pass


class TestEmailService(BasicEmailService):
    def send_email(
        self: Self,
        subject: str,
        body: str,
        sender: str,
        receiver: List[str],
    ) -> None:
        print("Subject: ", subject)
        print("Body: ", body)
        print("Sender: ", sender)
        print("receiver: ", receiver)
        print("Email Sent")
