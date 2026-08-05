class EmailGenerator:
    """
    Generează un mesaj sau email personalizat pentru aplicarea la un job.
    """

    def generate(self, job) -> str:
        title = getattr(job, 'title', 'Poziția dorită')
        company = getattr(job, 'company', 'Compania')
        
        email_content = (
            f"Bună ziua,\n\n"
            f"Vă contactez cu mult interes pentru poziția de {title} la {company}. "
            f"Sunt o persoană motivată, cu experiență în suport și relații cu clienții, "
            f"pregătită să aduc valoare echipei dumneavoastră.\n\n"
            f"Atașat găsiți CV-ul meu pentru mai multe detalii.\n\n"
            f"O zi excelentă,\nGabriela Usurelu"
        )
        return email_content
