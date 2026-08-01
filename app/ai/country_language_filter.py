class CountryLanguageFilter:
    """
    Filtrează joburile în funcție de țară și limbă.
    Exclude pozițiile fizice din alte țări, menținând România și joburile remote.
    """

    def is_valid(self, job) -> bool:
        location = str(getattr(job, 'location', '')).lower()
        
        # Țări străine fizice care nu ne interesează (dacă nu sunt remote)
        foreign_countries = [
            "germany", "france", "usa", "united states", 
            "spain", "italy", "poland", "uk", "united kingdom",
            "netherlands", "sweden", "switzerland"
        ]

        # Dacă jobul este fizic într-o țară străină, îl respingem
        if any(country in location for country in foreign_countries) and "remote" not in location:
            print(f"🚫 Job respins (locație fizică externă - '{location}'): {job.title}")
            return False

        return True