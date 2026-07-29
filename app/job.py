from dataclasses import dataclass
from typing import Optional


@dataclass
class Job:
    title: str
    company: str
    location: str
    salary: Optional[str]
    source: str
    url: str
    score: int = 0

    def display(self):
        print(f"Titlu     : {self.title}")
        print(f"Companie  : {self.company}")
        print(f"Locație   : {self.location}")
        print(f"Salariu   : {self.salary or 'Nespecificat'}")
        print(f"Sursă     : {self.source}")
        print(f"Scor      : {self.score}")
        print(f"Link      : {self.url}")