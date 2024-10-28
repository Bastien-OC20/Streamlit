import os 
import logging
import streamlit as st
import directory as pg
import re
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler, FileSystemEventHandler

####################### LOGIN OK
# kiki@free.fr / 1234
# lol@free.fr /1234


# Configuration de la page
if "user_email" in st.session_state:
    st.set_page_config(page_title=f"user : {st.session_state.user_email}", initial_sidebar_state="expanded")
else:
    st.set_page_config(page_title="Steamlit projet", initial_sidebar_state="expanded")
# st.set_page_config(page_title="Fonction affine", initial_sidebar_state="expanded", page_icon="📊")

# Ajouter un logo
logo_path = "img/logo.png" 
st.image(logo_path, width=450)

# st.markdown(
#     f"""
#     <div style="display: flex; justify-content: center;">
#     </div>
#     """, unsafe_allow_html=True
# )

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "visibility" not in st.session_state:
    st.session_state.visibility = "visible"
    st.session_state.disabled = False
if "active_page" not in st.session_state:
    st.session_state.active_page = "login_page"

################################################################# menu
# icone : https://mui.com/material-ui/material-icons/
login_page = st.Page(("directory/connection/login.py"), title="Log in", icon=":material/login:")
logout_page = st.Page("directory/connection/logout.py", title="Log out", icon=":material/logout:")

documentation_page = st.Page(
    "directory/documentation.py", title="Documentation", icon=":material/dashboard:"
)
fonctionAffine_page = st.Page(
    "directory/fonctionAffine.py", title="Fonction affine", icon=":material/functions:"
)
hello_page = st.Page(
    "directory/hello.py", title="Hello", icon=":material/waving_hand:"
)
home_page = st.Page(
    "directory/home.py", title="Home", default=True, icon=":material/home:"
)

user_page = st.Page(
    "directory/user.py",title="REgister", icon=":material/account_circle:"
)

if st.session_state.logged_in:
    pg = st.navigation(
        {
            "Account": [logout_page],
            "Accueil": [home_page, hello_page],
            "Tools": [fonctionAffine_page],
            "Documentation": [documentation_page],
            "Compte utilisateur":[user_page]
        }
    )

else:
    if "user_email" in st.session_state:
        del st.session_state["user_email"]

    left, right = st.columns(2)

    if left.button("Nouvel utilisateur", icon="😃", use_container_width=True, key="new_user") or st.session_state.active_page == "user_page":
        st.session_state.active_page = "user_page"
        pg = st.navigation([user_page])

    if right.button("login", icon="🔥", use_container_width=True, key="login") or st.session_state.active_page == "login_page":
        pg = st.navigation([login_page])

pg.run()

################################################################# log
# Créer le dossier log s'il n'existe pas
if not os.path.exists('log'):
        os.makedirs('log')
# Configuration de la journalisation
logging.basicConfig(level=logging.INFO,  # Définir le niveau de journalisation
                    format='%(asctime)s - %(message)s',  # Format du message
                    datefmt='%Y-%m-%d %H:%M:%S',
                    filename='log/file_changes.log',  # Fichier journal
                    filemode='w')  # Mode d'écriture

# Gestionnaire d'événements pour la surveillance de fichiers
class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        logging.info(f'Modified: {event.src_path}')
    
    def on_created(self, event):
        logging.info(f'Created: {event.src_path}')
        
    def on_deleted(self, event):
        logging.info(f'Deleted: {event.src_path}')

# Configurer l'observateur pour surveiller les modifications dans le répertoire courant
event_handler = MyHandler()  # Créer une instance de LoggingEventHandler
observer = Observer()  # Créer un observateur

observer.start()  # Démarrer l'observateur

logger_blocklist = [ # Surveiller le répertoire suivant
    ".",
    "directory",
    "data",
    "img",
]

# for module in logger_blocklist:
#     observer.schedule(event_handler, module, recursive=False)
