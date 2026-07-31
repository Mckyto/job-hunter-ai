from pathlib import Path
import shutil
import json


class ApplyManager:

    def __init__(self):

        self.output = Path("applications")

        self.output.mkdir(exist_ok=True)


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

        job_data = {
            "title": job.title,
            "company": job.company,
            "location": job.location,
            "salary": job.salary,
            "source": job.source,
            "url": job.url,
            "score": job.score
        }

        with open(
            folder / "job.json",
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(
                job_data,
                file,
                ensure_ascii=False,
                indent=4
            )

        return folder