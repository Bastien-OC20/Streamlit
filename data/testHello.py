import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import pytest
import logging

@pytest.fixture(autouse=True)
def caplog(caplog):
    """Fixture pour capturer les logs."""
    logging.basicConfig(level=logging.INFO)
    yield caplog
    
    
@st.cache_data
def load_data():
    return sns.load_dataset('iris')
    
def test_load_data(mocker):
    """Test de la fonction load_data pour vérifier le chargement des données."""
    # Objet Mock de sns.load_dataset clone du dataFrame pour ne pas rentrer les données soit même
    mock_data = pd.DataFrame({
        'sepal_length': [5.1, 4.9, 4.7],
        'sepal_width': [3.5, 3.0, 3.2],
        'species': ['setosa', 'setosa', 'setosa']
    })
    mocker.patch('seaborn.load_dataset', return_value=mock_data)
    
df_iris = load_data()  # Remplacez par l'appel de votre fonction

# print(df_iris)

assert not df_iris.empty
assert df_iris.shape[0] == 150
assert 'sepal_length' in df_iris.columns
assert 'species' in df_iris.columns


def test_file_not_found_log(caplog):
    """Test pour vérifier le log lorsqu'un fichier est introuvable."""
    with caplog.at_level(logging.ERROR):
        try:
            df = pd.read_csv('non_existent_file.csv')
        except FileNotFoundError:
            logging.error("Le fichier 'non_existent_file.csv' est introuvable.")

    assert "Le fichier 'non_existent_file.csv' est introuvable." in caplog.text


def test_display_details(mocker):
    """Test de la fonction display_details."""
    mocker.patch('streamlit.write')
    mocker.patch('streamlit.session_state', new={'selected_species': 'setosa'})
    
    # Mock de DataFrame
    filtered_df = pd.DataFrame({
        'sepal_length': [5.1, 4.9],
        'sepal_width': [3.5, 3.0],
        'species': ['setosa', 'setosa']
    })
    
    # Appel de la fonction display_details
    display_details()  # Remplacez par l'appel de votre fonction

    # Vérifiez que les détails ont été affichés
    assert st.write.call_count == 2  # Vérifiez le nombre d'appels à st.write


def test_upload_file(mocker):
    """Test pour vérifier le chargement d'un fichier CSV."""
    mock_data = "sepal_length,sepal_width,species\n5.1,3.5,setosa\n4.9,3.0,setosa\n"
    mock_file = StringIO(mock_data)
    mocker.patch('pandas.read_csv', return_value=pd.read_csv(mock_file))

    upload_file = st.file_uploader('Télécharger un fichier CSV', type=["csv"])
    
    # Simulez le téléchargement du fichier
    df = pd.read_csv(upload_file)
    
    assert df.shape[0] == 2
    assert 'sepal_length' in df.columns


if __name__ == "__main__":
    pytest.main()