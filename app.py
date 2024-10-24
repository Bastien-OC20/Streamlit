import os 
import logging
import streamlit as st
import directory as pg
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler, FileSystemEventHandler

from directory.services.haschService import haschService
from directory.services.connectionService import ConnectService
# from directory.services.sessionService import sessionService


# Configuration de la page
st.set_page_config(page_title="Fonction affine", initial_sidebar_state="expanded", page_icon="📊")

# Ajouter un logo
logo_path = "img/logo.png" 
st.image(logo_path, width=450)

# st.markdown(
#     f"""
#     <div style="display: flex; justify-content: center;">
#     </div>
#     """, unsafe_allow_html=True
# )
################################################################# login
myHaschService = haschService()
myHaschService.check()
myConectionService = ConnectService()


myEmail = "my@mail.fr"
myPassord = "password"
myHash = myHaschService.HashPassord(myPassord)

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

def login(mail:str, passord:str, hash:str):

    if not myConectionService.verifyConnect(mail,passord, hash):
        return None
    if st.button("Log in"):
        st.session_state.logged_in = True

        st.rerun()

def logout():
    if st.button("Log out"):

        st.session_state.logged_in = False
        st.rerun()

def myLoginTrue(): login(myEmail, myPassord, myHash)

################################################################# menu
# icone : https://mui.com/material-ui/material-icons/
login_page = st.Page((myLoginTrue), title="Log in", icon=":material/login:")
logout_page = st.Page(logout, title="Log out", icon=":material/logout:")

documentation = st.Page(
    "directory/documentation.py", title="Documentation", icon=":material/dashboard:"
)
fonctionAffine = st.Page(
    "directory/fonctionAffine.py", title="Fonction affine", icon=":material/functions:"
)
hello = st.Page(
    "directory/hello.py", title="Hello", icon=":material/waving_hand:"
)
home = st.Page(
    "directory/home.py", title="Home", default=True, icon=":material/home:"
)
print(f" -- st.session_state.logged_in : {st.session_state.logged_in}")
if st.session_state.logged_in:

    pg = st.navigation(
        {
            "Account": [logout_page],
            "Accueil": [home, hello],
            "Tools": [fonctionAffine],
            "Documentation": [documentation],
        }
    )
    print(f" login-- st.session_state.logged_in : {st.session_state.logged_in}")

else:
    print(f" logout-- st.session_state.logged_in : {st.session_state.logged_in}")
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

for module in logger_blocklist:
    observer.schedule(event_handler, module, recursive=False)
