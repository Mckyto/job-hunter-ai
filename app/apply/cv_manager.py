from pathlib import Path


class CVManager:

    def __init__(self):

        self.cv_path = Path("cv/CV.pdf")


    def exists(self):

        return self.cv_path.exists()


    def get_path(self):

        return self.cv_path