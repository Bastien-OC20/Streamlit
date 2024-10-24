import os 
import logging
import streamlit as st
import directory as pg
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler, FileSystemEventHandler

from services.haschService import haschService
from services.connectionService import ConnectService
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
    if st.button("Ajouter un utilisateur"):
        pass

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

register_page = st.Page(
    "directory/register.py",title="REgister", icon=":material/account_circle:"
)
# print(f" -- st.session_state.logged_in : {st.session_state.logged_in}")
if st.session_state.logged_in:

    pg = st.navigation(
        {
            "Account": [logout_page],
            "Accueil": [home_page, hello_page],
            "Tools": [fonctionAffine_page],
            "Documentation": [documentation_page],
            "Compte utilisateur":[register_page]
        }
    )
    # print(f" login-- st.session_state.logged_in : {st.session_state.logged_in}")

else:
    default = True        
    print(f" logout-- st.session_state.logged_in : {st.session_state.logged_in}")
    
    left, right = st.columns(2)
    def myLeftBt()->bool:
        return right.button("login", icon="🔥", use_container_width=True)
    
    if left.button("Nouvel utilisateur", icon="😃", use_container_width=True):
        default = False
        pg = st.navigation([register_page])
    if myLeftBt() or default:
    # if right.button("login", icon="🔥", use_container_width=True):
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
