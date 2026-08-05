import streamlit as st
from app.romania_portals import RomaniaPortalsSearcher
from app.linkedin_indeed import LinkedInIndeedSearcher
from app.agent import JobHunterAgent
from app.cover_letter import CoverLetterGenerator
from app.email_generator import EmailGenerator

st.set_page_config(page_title="Job Hunter AI - Gabriela Usurelu", page_icon="🤖", layout="wide")

st.title("🤖 Job Hunter AI - Panou de Control")
st.markdown("Bine ai venit, **Gabriela**! De aici poți rula căutările și poți gestiona oportunitățile identificate.")

# Sidebar pentru setări
st.sidebar.header("Setări Căutare")
platforma_selectata = st.sidebar.multiselect(
    "Alege platformele:",
    ["Portaluri România (eJobs, BestJobs, OLX, Ia Job)", "LinkedIn & Indeed"],
    default=["Portaluri România (eJobs, BestJobs, OLX, Ia Job)", "LinkedIn & Indeed"]
)

if st.button("🚀 Pornește Căutarea Acum", type="primary"):
    with st.spinner("Se caută joburi pe platforme... Te rog așteaptă."):
        searchers = []
        if "Portaluri România (eJobs, BestJobs, OLX, Ia Job)" in platforma_selectata:
            searchers.append(RomaniaPortalsSearcher())
        if "LinkedIn & Indeed" in platforma_selectata:
            searchers.append(LinkedInIndeedSearcher())
            
        # Colectăm joburile
        all_jobs = []
        for s in searchers:
            jobs = s.search()
            if jobs:
                all_jobs.extend(jobs)
                
        st.session_state['jobs'] = all_jobs
        st.success(f"Găsite cu succes {len(all_jobs)} joburi!")

# Afișare rezultate dacă există
if 'jobs' in st.session_state and st.session_state['jobs']:
    st.markdown("---")
    st.subheader("📋 Lista Joburilor Găsite")
    
    letter_gen = CoverLetterGenerator()
    email_gen = EmailGenerator()
    
    for idx, job in enumerate(st.session_state['jobs']):
        with st.expander(f"{job.title} — *{job.company}* ({job.location})"):
            st.write(f"**Link Anunț:** [Deschide jobul în pagină]({job.url})")
            st.write(f"**Salariu:** {job.salary}")
            
            col1, col2 = st.columns(2)
            
            with col1:
                if st.button(L"📄 Generează Scrisoare", key=f"cl_{idx}"):
                    scrisoare = letter_gen.generate(job)
                    st.text_area("Scrisoare de intenție:", scrisoare, height=200, key=f"txt_cl_{idx}")
                    
            with col2:
                if st.button(L"✉️ Generează Email", key=f"em_{idx}"):
                    email_text = email_gen.generate(job)
                    st.text_area("Mesaj Email:", email_text, height=200, key=f"txt_em_{idx}")
else:
    st.info("Apasă pe butonul de pornire de mai sus pentru a genera lista de joburi.")
