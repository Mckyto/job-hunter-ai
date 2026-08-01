class ProfileJobFilter:
    """
    Filtrează joburile menținând strict:
    - Domeniile dorite (Call Center, Data Entry, Cosmetice)
    - Exclusiv limba română
    - Exclusiv în BUCUREȘTI sau REMOTE
    """

    def is_relevant(self, job) -> bool:
        title = str(getattr(job, 'title', '')).lower()
        location = str(getattr(job, 'location', '')).lower()
        
        # 1. Respingem instantaneu joburile care cer limbi străine
        foreign_languages = [
            "bulgara", "bulgarian", "rusa", "russian", "ukrainian", 
            "german", "deutsch", "french", "francais", "spanish", 
            "italian", "hungarian", "maghiara", "polona"
        ]
        for lang in foreign_languages:
            if lang in title or lang in location:
                print(f"🚫 Job respins (necesită limbă străină - '{lang}'): {job.title}")
                return False

        # 2. Filtrare strictă după locație: Doar București sau Remote / România
        other_cities = [
            "cluj", "timisoara", "iasi", "constanta", "brasov", "sibiu", 
            "craiova", "galati", "ploiesti", "oradea", "arad", "pitesti", 
            "bacau", "targu mures", "baia mare", "suceava", "piatra neamt"
        ]
        
        is_remote_or_bucharest = (
            "bucuresti" in location or 
            "bucharest" in location or 
            "remote" in location or 
            "romania" in location or
            "la distanta" in location or
            "de acasa" in location
        )

        for city in other_cities:
            if city in location and not ("bucuresti" in location or "bucharest" in location or "remote" in location):
                print(f"🚫 Job respins (locație fizică în alt oraș - '{city}'): {job.title} | Locație: {job.location}")
                return False

        # 3. Cuvinte cheie permise pentru domeniile tale
        allowed_keywords = [
            # Call Center / Suport / Chat
            "call center", "callcenter", "customer support", "suport clienti", 
            "relatii cu clientii", "support agent", "chat support", "operator", 
            "customer service", "helpdesk", "asistent", "virtual assistant",
            "romana", "română", "suport",
            
            # Data Entry / Introducere date
            "data entry", "introducere date", "operare date", "data specialist", "analist",
            
            # Cosmetice / Parfumerie / Beauty / Retail
            "parfumerie", "cosmetice", "beauty", "advisor", "consultant", 
            "parfum", "makeup", "make-up", "retail", "vanzator", "vânzător", "seller"
        ]

        match_found = False
        for keyword in allowed_keywords:
            if keyword in title:
                match_found = True
                break

        if not match_found:
            print(f"🚫 Job respins (în afara domeniilor dorite): {job.title}")
            return False

        return True