import csv

from dataclasses import dataclass
from typing import List, Self


@dataclass
class Employee:
    first_name: str
    last_name: str
    gender: str
    position: str

    @property
    def full_name(self: Self) -> str:
        return f"{self.first_name} {self.last_name}"


def get_employees_from_csv(file_path: str) -> List[Employee]:
    with open(file_path, newline="") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        return [Employee(**data) for data in csv_reader]
