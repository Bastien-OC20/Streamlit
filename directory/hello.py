import os 
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import logging
from pathlib import Path


# Chemins des dossiers log/ et img/ au niveau n-1
# log_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '/log/')
# file_dir = os.path.dirname(os.path.abspath(__file__))
# print(file_dir)
# print(f"{Path(__file__).parent.parent}/img/")


img_dir = f"{Path(__file__).parent.parent}/img/"
# Création dossier s'ils n'existe pas
os.makedirs(img_dir, exist_ok=True)

st.markdown("""
<style>
    .reportview-container {
        background: #f0f0f5;
        display: flex;
        justify-content: center;  
        align-items: center;      
        height: 100vh;           
    }
    .main {
        width: 80%;              
        max-width: 1200px;      
    }
    .sidebar .sidebar-content {
        background: #f0f0f5;
    }
    .stButton>button {
        background-color: #4CAF50; 
        color: white; 
        border: none; 
        padding: 10px 20px; 
        text-align: center; 
        text-decoration: none; 
        display: inline-block; 
        font-size: 16px; 
        margin: 4px 2px; 
        cursor: pointer; 
    }
</style>
""", unsafe_allow_html=True)

st.title('Bienvenue sur l\'application Streamlit !')
st.header('Voici un exemple de Streamlit')
st.subheader('Affichage de texte et de données')
st.write('Streamlit permet de créer facilement des applications web pour le data science.')
st.markdown('[la documentation de streamlit](https://pypi.org/project/streamlit/)')


try:
    df = pd.read_csv('data/test.csv')
    logging.info("Données chargées depuis test.csv.")
except FileNotFoundError:
    logging.error("Le fichier 'test.csv' est introuvable.")
    st.error("Le fichier 'test.csv' est introuvable.")
    df = pd.DataFrame()

if not df.empty:
    st.write('Affichage du dataframe de test.csv')
    st.dataframe(df)
    st.write('Affichage du tableau test.csv (les 5 premières valeurs)')
    st.table(df.head(5))

df= pd.read_csv('data/test.csv')
st.write('Affichage du dataframe de text.csv')
st.dataframe(df)
st.write('Affichage du tableau text.csv (les 5 premières valeurs)')
st.table(df.head(5))

st.write("Cliquez sur le bouton.")
st.button('Mon premier button avec Streamlit')


st.checkbox('Case à cocher')
st.write(df)

texte= st.text_input('Entre un texte')
st.selectbox("Vous avez entré : ", texte )

selection = st.selectbox('Choisissez une option !' ,df.columns)
st.write(f"Vous avez selectionné : {selection}")

x = st.slider("Séléctinnez une valeur" )
st.write(x, "au carré : ", 1*100)


col1, col2, col3 = st.columns(3)
colonne1 = df.columns[0]  
colonne2 = df.columns[1]  
colonne3 = df.columns[2]
with col1 : 
    st.write("Colonnes du DataFrame dans la colonne 1 : PassengerId")
    st.write(df[colonne1])
with  col2:
    st.write("Colonnes du DataFrame dans la colonne 2 : Pclass")
    st.write(df[colonne2])
with col3:
    st.write("Colonnes du DataFrame dans la colonne 3 : Name")
    st.write(df[colonne3])
    

with st.expander("Cliquez pour en savoir plus"):
    st.write("Contenu extensible")



tab1, tab2 = st.tabs(["Onglet 1", "Onglet 2"])
with tab1:
    st.write("Contenu de l'onglet 1")
with tab2:
    st.write("Contenu de l'onglet 2")
    
    
df_iris = sns.load_dataset('iris')
st.title("Visualisation de données avec Matplotlib, Seaborn et Plotly")

st.header("Graphique Matplotlib")
fig, ax = plt.subplots()
ax.scatter(df_iris['sepal_length'], df_iris['sepal_width'], color='blue')
ax.set_title("Longueur vs Largeur des sépales (Matplotlib)")
ax.set_xlabel("Longueur des sépales")
ax.set_ylabel("Largeur des sépales")
st.pyplot(fig)

st.header("Graphique Seaborn")
sns.pairplot(df_iris, hue='species')
st.pyplot(plt.gcf())

st.header("Graphique Plotly")
fig_plotly = px.scatter(
    df_iris, 
    x='sepal_length', 
    y='sepal_width', 
    color='species', 
    title="Longueur vs Largeur des sépales (Plotly)"
    )
st.plotly_chart(fig_plotly)


st.title("Filtrage de données avec Matplotlib, Seaborn et Plotly")


st.sidebar.header("Filtres")
selected_columns = st.sidebar.multiselect(
    "Sélectionnez les colonnes à afficher", 
    options=df_iris.columns.tolist(), 
    default=['sepal_length', 'sepal_width']
)

st.write("Données filtrées :")
st.dataframe(df_iris[selected_columns])


st.sidebar.header("Informations détaillées")
selected_species = st.sidebar.selectbox("Choisissez une espèce", df_iris['species'].unique())
filtered_data = df_iris[df_iris['species'] == selected_species]

st.write(f"Détails pour l'espèce sélectionnée : {selected_species}")
st.dataframe(filtered_data)



@st.cache_data
def load_data():
    return sns.load_dataset('iris')

df_iris=load_data()




st.title("Visualisation des données Iris avec filtres et interactions")

species_filter = st.selectbox("Choisissez une espèce : ", df_iris['species'].unique())
st.session_state.selected_species= species_filter

filtered_df = df_iris[df_iris ['species'] == st.session_state.selected_species]
st.write('Données filtrées : ', filtered_df)

st.header("Graphique Plotly")
fig_plotly = px.scatter(
    df_iris, 
    x='sepal_length', 
    y='sepal_width', 
    color='species', 
    title=f"Longueur vs Largeur des sépales ({st.session_state.selected_species})"
    )
st.plotly_chart(fig_plotly)

def display_details():
    st.write(f"Détails pour l'espèce : {st.session_state.selected_species}")
    st.write(filtered_df.describe())


if st.button("Afficher des détails", on_click=display_details):
    pass
    
st.header("Graphique Seaborn")
sns.boxplot(data=filtered_df, x='species', y='sepal_length')
st.pyplot(plt.gcf()) 


st.header("Graphique Matplotlib")
fig, ax = plt.subplots()
ax.hist(filtered_df['sepal_length'], bins=10, color='lightblue', edgecolor='black')
ax.set_title(f"Histogramme de la longueur des sépales ({st.session_state.selected_species})")
ax.set_xlabel("Longueur des sépales")
ax.set_ylabel("Fréquence")
st.pyplot(fig)

if st.checkbox("Afficher les données brutes"):
    st.write(df_iris)



st.title('Gestion des fichiers avec streamlit')

upload_file= st.file_uploader('Télécharger un fichier CSV', type=["csv"])    
if upload_file is not None:
    df = pd.read_csv(upload_file)
    logging.info("Données chargées depuis le fichier téléchargé.")
    st.write('Données chargées : ')
    st.dataFrame(df)
    
st.write("Noms de colonnes :", df.columns.tolist())

column_to_plot = st.selectbox("Choisissez la colonne pour l'histogramme", df.columns)
    
plt.figure(figsize=(10,5))
sns.histplot(df[column_to_plot].dropna(), bins=30)
plt.title('Histogramme de Ma colonne')

st.pyplot(plt.gcf())

image_path = os.path.join(img_dir, "histogramme.png")
plt.savefig(image_path)
st.success("Graphique enregistré sous histogramme.png")

with open(image_path, "rb") as file:
    st.download_button("Télécharger le graphique", file, "histogramme.png", "image/png")
    
logging.info("L'application a été exécutée avec succès.")





