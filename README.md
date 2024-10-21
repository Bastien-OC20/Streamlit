# Application Streamlit pour la Fonction Affine

Cette application permet de visualiser et de personnaliser le graphique d'une fonction affine de la forme \( y = ax + b \). L'utilisateur peut interagir avec des curseurs pour modifier les paramètres \( a \) et \( b \), ainsi que d'autres options de personnalisation comme la couleur de la courbe et les titres des axes.

## Fonctionnalités

- **Paramètres personnalisables**:
  - Ajustement des coefficients \( a \) et \( b \) via des curseurs.
  - Choix de la couleur de la courbe.
  - Modification du titre du graphique et des étiquettes des axes.

- **Affichage dynamique**:
  - Le graphique se met à jour en temps réel lorsque les utilisateurs modifient les valeurs des curseurs.

- **Tableau des valeurs**:
  - Affiche un tableau avec les valeurs calculées de \( x \) et \( y \).

## Installation

Pour exécuter cette application, assurez-vous d'avoir Python installé sur votre machine. Vous aurez également besoin des bibliothèques suivantes:

```bash
pip install streamlit numpy pandas matplotlib
```

## Utilisation

1. Clonez ce dépôt ou téléchargez le fichier `0_fonction_affine.py`.
2. Naviguez dans le répertoire contenant le fichier dans votre terminal.
3. Exécutez l'application avec la commande suivante:

```bash
streamlit run 0_fonction_affine.py
```

4. Une fois l'application lancée, un onglet s'ouvrira dans votre navigateur avec l'interface de la fonction affine.

## Explication du Code

### Imports

```python
import streamlit as st  # Importation de la bibliothèque Streamlit pour créer une interface web
import numpy as np  # Importation de NumPy pour manipuler les tableaux de nombres
import pandas as pd  # Importation de Pandas pour la manipulation des données sous forme de tableaux
import matplotlib.pyplot as plt  # Importation de Matplotlib pour créer des graphiques
```

### Fonction Principale

```python
def fonction_affine():
    # Titre de l'application
    st.title('Personnalisation du graphique de la fonction affine')
```

La fonction principale gère toute l'interaction utilisateur et la création de graphiques.

### Curseurs

```python
a = st.slider('Choisissez une valeur pour a', min_value=-10.0, max_value=10.0, value=1.0, step=0.1)
b = st.slider('Choisissez une valeur pour b', min_value=-20.0, max_value=20.0, value=0.0, step=0.5)
```

Les curseurs permettent aux utilisateurs de sélectionner les valeurs pour les coefficients \( a \) et \( b \) de la fonction affine.

### Calculs

```python
x_values = np.linspace(x_min, x_max, 100)
y_values = a * x_values + b
```

Cette partie génère les valeurs \( y \) correspondant aux \( x \) basées sur les coefficients choisis.

### Affichage des Résultats

```python
st.dataframe(df)
st.pyplot(fig)
```

Affiche le tableau des valeurs et le graphique de la fonction affine.

## Documentation et Ressources Utiles

- [Streamlit Documentation](https://docs.streamlit.io)
- [NumPy Documentation](https://numpy.org/doc/stable/)
- [Pandas Documentation](https://pandas.pydata.org/pandas-docs/stable/)
- [Matplotlib Documentation](https://matplotlib.org/stable/contents.html)

## Contribution

Les contributions sont les bienvenues! N'hésitez pas à soumettre une demande de tirage pour des améliorations.

## License

Ce projet est sous licence MIT.
