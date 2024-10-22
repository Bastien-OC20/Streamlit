import os 
import streamlit as st  
import numpy as np  
import pandas as pd  
import matplotlib.pyplot as plt
import time
import logging
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler, FileSystemEventHandler
from watchdog.observers import Observer


# Créer le dossier log s'il n'existe pas
if not os.path.exists('log'):
    os.makedirs('log')

# Configuration de la journalisation
logging.basicConfig(level=logging.INFO,  # Définir le niveau de journalisation
                    format='%(asctime)s - %(message)s',  # Format du message
                    datefmt='%Y-%m-%d %H:%M:%S',
                    filename='log/file_changes.log',  # Fichier journal
                    filemode='w')  # Mode d'écriture

logger_blacklist = [
    '.streamlist',
    'Log',
]

logger = logging.getLogger()  # Création d'un logger

# Gestionnaire d'événements pour la surveillance de fichiers
class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        logging.info(f'Modified: {event.src_path}')
    
    def on_created(self, event):
        logging.info(f'Created: {event.src_path}')
        
    def on_deleted(self, event):
        logging.info(f'Deleted: {event.src_path}')


# Fonction principale pour gérer la création du graphique de la fonction affine
def fonction_affine():
    # Titre de l'application dans la page Streamlit
    st.title('Graphique de la fonction affine')
    logger = logging.getLogger()  # Création d'un logger
    logger.info('Application démarrée avec succès. Youpie !')
    
     # Titre de la barre latérale
    st.sidebar.header('Paramètres de la fonction affine')

    # Sliders pour ajuster les paramètres a et b de la fonction affine y = ax + b
    # On peut glisser pour choisir les valeurs souhaitées
    a = st.sidebar.slider('Choisissez une valeur pour a', min_value=-10.0, max_value=10.0, value=1.0, step=0.1)
    b = st.sidebar.slider('Choisissez une valeur pour b', min_value=-20.0, max_value=20.0, value=0.0, step=0.5)
    logger.info(f'Valeurs choisies : a:{a}, b:{b}')

    # Sélecteur de couleur pour permettre à l'utilisateur de changer la couleur de la courbe
    color = st.sidebar.color_picker('Choisissez la couleur de la courbe', '#FF4B4C')  # Couleur par défaut : rouge-orangé (#FF4B4C)
    

    # Champs texte pour personnaliser le titre du graphique et les étiquettes des axes
    graph_title = st.sidebar.text_input('Titre du graphique', 'Graphique de la fonction affine')  # Titre par défaut
    xlabel = st.sidebar.text_input('Nom de l\'axe des x', 'x')  # Nom de l'axe des x par défaut
    ylabel = st.sidebar.text_input('Nom de l\'axe des y', 'y')  # Nom de l'axe des y par défaut

    # Sliders pour ajuster l'intervalle des valeurs de x
    x_min = st.sidebar.slider('Valeur minimale de x', min_value=-50.0, max_value=0.0, value=-10.0)
    x_max = st.sidebar.slider('Valeur maximale de x', min_value=0.0, max_value=50.0, value=10.0)
    logger.info(f'Intervalle de x choisi : Min : {x_min}, Max:{x_max}')

    # Générer un tableau de valeurs de x réparties entre x_min et x_max
    x_values = np.linspace(x_min, x_max, 100)

    # Calcul des valeurs correspondantes de y à l'aide de la formule de la fonction affine : y = ax + b
    y_values = a * x_values + b

    # Création d'un tableau (DataFrame) avec les valeurs de x et y pour afficher dans un tableau Streamlit
    df = pd.DataFrame({
        'x': x_values,  # Colonne des valeurs de x
        'y': y_values   # Colonne des valeurs de y
    })
    
    # Sélectionner uniquement les 10 premières valeurs
    df_first_ten = df.head(10)
    
    # Tableau horizontale avec la methode "T" qui transpose le tableau 
    df_horizontale = df_first_ten.T
    

    # Afficher le tableau contenant les valeurs de x et y dans l'interface Streamlit
    st.write("Tableau des valeurs de x et y :")
    st.dataframe(df_horizontale)  # Affiche le tableau dans l'interface web
    logger.info('Tableau des valeurs de x et y affichés.')

    # Création du graphique de la fonction affine y = ax + b
    st.write("Graphique de la fonction y = ax + b :")
    fig, ax = plt.subplots(figsize=(8, 4))  # Création de la figure et de l'axe du graphique
    ax.plot(x_values, y_values, label=f'y = {a}x + {b}', color=color)  # Tracer la courbe avec la couleur choisie
    ax.set_title(graph_title, color='white')  # Définir le titre du graphique
    ax.set_xlabel(xlabel, color='white')  # Définir l'étiquette de l'axe des x
    ax.set_ylabel(ylabel, color='white')  # Définir l'étiquette de l'axe des y
    
    
    # Personnaliser les repères et axes en blanc
    ax.spines['top'].set_color('white')
    ax.spines['bottom'].set_color('white')
    ax.spines['left'].set_color('white')
    ax.spines['right'].set_color('white')
    
    
    # Définir la couleur du texte en blanc
    ax.xaxis.label.set_color('white')
    ax.yaxis.label.set_color('white')
    ax.title.set_color('white')
    ax.tick_params(axis='x', colors='white')
    ax.tick_params(axis='y', colors='white')

    # Fond transparent pour le graphique
    fig.patch.set_alpha(0.0)  # Rendre la figure transparente
    ax.set_facecolor((0, 0, 0, 0))  # Fond de l'axe transparent

    # Ajouter une légende dans le coin supérieur droit
    ax.legend(loc='upper right',facecolor='black', edgecolor='white', labelcolor='white')

    # Afficher le graphique dans Streamlit
    st.pyplot(fig)
    logger.info('Graphique affiché avec succès !')
    
    
    # Configurer l'observateur pour surveiller les modifications dans le répertoire courant
event_handler = MyHandler()  # Créer une instance de LoggingEventHandler
observer = Observer()  # Créer un observateur
path = '.'  # Surveiller le répertoire courant
for module in logger_blacklist :
    observer.schedule(event_handler, path, recursive=True)  # Planifier l'observateur
observer.start()  # Démarrer l'observateur

# Appel de la fonction principale lorsque l'application Streamlit est exécutée
if __name__ == "__main__":
    try:
        fonction_affine()  # Exécuter la fonction
    except KeyboardInterrupt:
        observer.stop()  # Arrêter l'observateur si une interruption est reçue
    finally:
        observer.stop()  # Arrêter l'observateur
        observer.join()  # Joindre l'observateur