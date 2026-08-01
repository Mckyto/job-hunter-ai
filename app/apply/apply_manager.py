import re
from pathlib import Path

class ApplyManager:
    """
    Gestionează crearea dosarelor și înregistrarea aplicațiilor trimise.
    """
    def __init__(self, base_dir="applications"):
        self.base_dir = Path(base_dir)
        self.base_dir.mkdir(exist_ok=True)

    def sanitize_name(self, name) -> str:
        r"""
        Elimină caracterele interzise în Windows dintr-un text pentru a putea deveni nume de folder valid.
        Caractere interzise în Windows: < > : " / \ | ? *
        """
        if not name:
            return "job_application"
        # Înlocuiește caracterele nepermise cu Underline sau spațiu
        clean_name = re.sub(r'[<>:"/\\|?*]', '_', str(name))
        # Curăță spațiile multiple sau caracterele ciudate rămase
        clean_name = re.sub(r'\s+', ' ', clean_name).strip()
        return clean_name[:100]  # Limitează lungimea maximă pentru siguranță

    def create_application(self, job, cv_path):
        try:
            # Construim un nume sigur pentru folder folosind compania și titlul curățate
            safe_company = self.sanitize_name(getattr(job, 'company', 'Company'))
            safe_title = self.sanitize_name(getattr(job, 'title', 'Job'))
            
            folder_name = f"{safe_company}_{safe_title}"
            folder = self.base_dir / folder_name
            
            # Creează folderul în siguranță
            folder.mkdir(parents=True, exist_ok=True)
            
            # Salvează detaliile jobului într-un fișier text în interiorul folderului
            info_file = folder / "job_details.txt"
            with open(info_file, "w", encoding="utf-8") as f:
                f.write(f"Titlu: {getattr(job, 'title', 'N/A')}\n")
                f.write(f"Companie: {getattr(job, 'company', 'N/A')}\n")
                f.write(f"Locație: {getattr(job, 'location', 'N/A')}\n")
                f.write(f"Salariu: {getattr(job, 'salary', 'N/A')}\n")
                f.write(f"Link: {getattr(job, 'url', 'N/A')}\n")

            print(f"✅ Aplicație salvată cu succes în folderul: {folder}")
            return True
        except Exception as e:
            print(f"❌ Eroare la crearea aplicației: {e}")
            return False