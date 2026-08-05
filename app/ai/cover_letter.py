from datetime import datetime


class CoverLetterGenerator:

    def __init__(self):

        self.template = """
Stimate departament de recrutare {company},

Vă contactez pentru poziția de {title}.

Experiența mea în relația cu clienții, comunicare și utilizarea
instrumentelor digitale mă recomandă pentru această oportunitate.

Sunt o persoană organizată, atentă la detalii și orientată spre
rezolvarea problemelor. Îmi doresc să contribui la succesul echipei
dumneavoastră și să aduc valoare prin seriozitate și implicare.

Consider că abilitățile mele se potrivesc cerințelor acestui rol și
aș aprecia oportunitatea unei discuții pentru a prezenta mai multe
detalii despre experiența mea.

Vă mulțumesc pentru timpul acordat.

Cu stimă,
Gabriela Usurelu

Generat automat: {date}
"""

    def generate(self, job):

        return self.template.format(
            company=job.company,
            title=job.title,
            date=datetime.now().strftime("%d.%m.%Y")
        )
