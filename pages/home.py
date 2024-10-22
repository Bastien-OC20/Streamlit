import streamlit as st

def show_home():
    # Titre principal
    st.title("Projet Streamlit : Initiation")

    # Section sur le projet
    st.header("Ce projet vous guidera pas à pas dans la création d'un dashboard interactif avec Streamlit.")
    st.write("Vous commencerez par les bases et progresserez vers des fonctionnalités plus avancées, "
            "pour finalement obtenir une application complète de visualisation et d'analyse de données.")

    # Jeu de données
    st.subheader("Jeu de données")
    st.write("Pour ce projet, vous pouvez utiliser un jeu de données de votre choix. Voici quelques suggestions :")
    st.write("- [Données sur le Titanic](https://www.kaggle.com/c/titanic/data)")
    st.write("- [Données sur les ventes d'une entreprise](https://www.kaggle.com/datasets/kyanyoga/sample-sales-data)")

    # Points à aborder
    st.subheader("Points à aborder")
    points = [
        "1. Installation et configuration",
        "2. Chargement et affichage de données",
        "3. Widgets interactifs",
        "4. Visualisation de données",
        "5. Filtres et interactions",
        "6. Caching",
        "7. États de session",
        "8. Callbacks",
        "9. Thèmes et personnalisation",
        "10. Gestion des fichiers",
        "11. Intégration avec d'autres bibliothèques",
        "12. Tests unitaires",
        "13. Documentation",
        "14. Amélioration de l'interface utilisateur",
        "15. Versionner votre code",
        "16. Sécurité",
        "17. Maintenance et mises à jour",
        "18. Déploiement",
        "19. Conseils"
    ]
    for point in points:
        st.write(point)

    # Section des Streamlit Pages
    st.header("Streamlit Pages")
    st.subheader("Titre du projet : Visualisation interactive d'une fonction affine avec Streamlit")
    st.write("**Objectif :** Apprendre à visualiser des fonctions affines de manière interactive.")
    st.write("**Fonctionnalités :**")
    st.write("- Afficher des graphes de fonctions affines.")
    st.write("- Interagir avec les paramètres de la fonction.")
    st.write("**Instructions :** Suivez les étapes dans les pages correspondantes.")
    st.write("**Bonus :** Ajoutez des fonctionnalités supplémentaires selon vos idées.")

    st.subheader("Titre du projet : Création d'un outil d'analyse de données interactif avec Streamlit")
    st.write("**Objectif :** Développer un outil d'analyse de données interactif.")
    st.write("**Fonctionnalités :**")
    st.write("- Chargement de jeux de données variés.")
    st.write("- Visualisations interactives.")
    st.write("**Instructions :** Consultez les pages détaillées pour chaque étape.")
    st.write("**Bonus :** Implémentez des fonctionnalités avancées d'analyse.")

    # Aller plus loin
    st.header("Aller plus loin! Au-delà de Streamlit!")
    st.subheader("Alternative")
    st.write("Explorez d'autres bibliothèques pour créer des visualisations ou des dashboards.")

    st.subheader("Amélioration pour ceux qui sont en avance")
    st.write("Reprenez le code de fonction affine et ajoutez des fonctionnalités supplémentaires.")
    st.write("**Étape 1:** Ajouter un nouveau paramètre.")
    st.write("**Étape 2:** Implémenter un filtre.")
    st.write("**Étape 3:** Créer un graphique dynamique.")

    # Instructions de fin
    st.write("Ce projet vous permettra d'acquérir une solide compréhension de Streamlit et de ses fonctionnalités. "
            "N'hésitez pas à explorer et à expérimenter pour créer une application qui répond à vos besoins et à vos intérêts.")
    

show_home()