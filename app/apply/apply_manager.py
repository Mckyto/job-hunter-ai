from pathlib import Path
import shutil
import json

from app.ai.cover_letter import CoverLetterGenerator


class ApplyManager:

    def __init__(self):

        self.output = Path("applications")
        self.output.mkdir(exist_ok=True)

        self.cover = CoverLetterGenerator()


    def create_application(self, job, cv_path):

        folder_name = (
            f"{job.company}_{job.title}"
            .replace("/", "-")
            .replace("\\", "-")
        )

        folder = self.output / folder_name

        folder.mkdir(exist_ok=True)


        shutil.copy(
            cv_path,
            folder / "CV.pdf"
        )


        with open(folder / "job.json", "w", encoding="utf-8") as file:

            json.dump(
                job.__dict__,
                file,
                indent=4,
                ensure_ascii=False
            )


        letter = self.cover.generate(job)

        with open(folder / "CoverLetter.txt", "w", encoding="utf-8") as file:

            file.write(letter)


        return folder