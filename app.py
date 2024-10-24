import os 
import logging
import streamlit as st
import directory as pg
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler, FileSystemEventHandler
from collections.abc import Iterable

from directory.services.haschService import haschService
from directory.services.connectionService import ConnectService
from directory.services.sessionService import sessionService

from argon2 import PasswordHasher






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
# sessionServ = sessionService()
# testSession = sessionServ.testSessionLoggedIn()

myEmail = "my@mail.fr"
myPassord = "password"
myHash = myHaschService.HashPassord(myPassord)

# print("sessionService.sessionState")
# print(sessionService.sessionState)
# if (not isinstance(sessionService.sessionState, Iterable)):
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
    # sessionServ.logged_in = False
# else:
#     if "logged_in" not in sessionService.sessionState:
#         sessionServ.logged_in = False

    # st.session_state.logged_in = False
def login(mail:str, passord:str, hash:str):
# def login():
    # if myHaschService.checkPassorwd()
    if not myConectionService.verifyConnect(mail,passord, hash):
        return None
    if st.button("Log in"):
        # sessionServ.logged_in = True
        st.session_state.logged_in = True
        # print(f"st.session_state.logged_in : {st.session_state.logged_in}")
        # print(st.session_state.logged_in)
        # st.session_state.logged_in = myConectionService.verifyConnect(myEmail,myPassord, myHash)
        # st.session_state.logged_in = True
        st.rerun()
# login = connectServ.login()

def logout():
    if st.button("Log out"):
        # print(sessionServ.logged_in)
        # sessionServ.logged_in = False
        # print("2")
        st.session_state.logged_in = False
        # print(sessionServ.logged_in)
        st.rerun()

def myLoginTrue(): login(myEmail, myPassord, myHash)
# logout = connectServ.logout()
################################################################# menu
# icone : https://mui.com/material-ui/material-icons/
login_page = st.Page((myLoginTrue), title="Log in", icon=":material/login:")
# login_page = st.Page(connectServ.login(), title="Log in", icon=":material/login:")
logout_page = st.Page(logout, title="Log out", icon=":material/logout:")
# logout_page = st.Page(connectServ.logout(), title="Log out", icon=":material/logout:")

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
# if sessionService.logged_in:
    # sessionServ.logged_in = True
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
    # sessionServ.logged_in = False
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
# path = '.'  # Surveiller le répertoire courant
# for module in logger_blacklist :
#     observer.schedule(event_handler, path, recursive=True)  # Planifier l'observateur
observer.start()  # Démarrer l'observateur

logger_blocklist = [
    ".",
    "directory",
    "data",
    "img",
]

for module in logger_blocklist:
    observer.schedule(event_handler, module, recursive=False)


# ph = PasswordHasher()

# hash = ph.hash("correct horse battery staple")
# hash  # doctest: +SKIP
# '$argon2id$v=19$m=65536,t=3,p=4$MIIRqgvgQbgj220jfp0MPA$YfwJSVjtjSU0zzV/P3S9nnQ/USre2wvJMjfCIjrTQbg'
# print(ph.verify(hash, "correct horse battery staple"))
# # True
# print(ph.check_needs_rehash(hash))
# print(ph.verify(hash, "correct horse battery staple"))
# False
# # ph.verify(hash, "Tr0ub4dor&3")