# import pandas as pd
# import uuid
# import random
# from faker import Faker
# from datetime import datetime, timedelta
# import Roles as Roles

# # Initialiser Faker avec une locale française pour des noms plus réalistes
# fake = Faker('fr_FR')

# # Générer un code postal de Marseille
# marseille_postal_codes = [f"130{str(i).zfill(2)}" for i in range(1, 17)]

# # Fonction pour générer des timestamps
# def generer_timestamp(date):
#     return date.timestamp() # TODO intervals de dates réalistes

# # Fonction pour générer n données
# def generer_donnees(n):
#     data = []
    
#     for _ in range(n):
#         user_id = str(uuid.uuid4())
#         nom = fake.last_name()
#         mot_de_passe = fake.password(length=10)
#         email = fake.email()
#         code_postal = random.choice(marseille_postal_codes)
#         age = random.randint(18, 80)
#         taille = round(random.uniform(1.5, 2.0), 2)  # Taille en mètres
#         poids = random.randint(50, 120)  # Poids en kg
        
#         # Sélection aléatoire d'un rôle parmi l'énumération Roles
#         role = random.choice(list(Roles)).name
        
#         # Création de la date de création
#         created_date = fake.date_time_between(start_date="-5y", end_date="now")
#         created_timestamp = generer_timestamp(created_date)
        
#         # Génération de la date de mise à jour avec une probabilité de 45%
#         updated_timestamp = None
#         if random.random() <= 0.45:
#             updated_date = fake.date_time_between(start_date=created_date, end_date="now")
#             updated_timestamp = generer_timestamp(updated_date)
        
#         # Génération de la date de suppression avec une probabilité de 20%
#         deleted_timestamp = None
#         if random.random() <= 0.20:
#             deleted_date = fake.date_time_between(start_date=created_date, end_date="now")
#             deleted_timestamp = generer_timestamp(deleted_date)
        
#         # Ajouter les données dans la liste
#         data.append({
#             "UserId": user_id,
#             "nom": nom,
#             "mot_de_passe": mot_de_passe,
#             "email": email,
#             "code_postal": code_postal,
#             "age": age,
#             "taille": taille,
#             "poids": poids,
#             "role": role,
#             "CreatedDate": created_timestamp,
#             "UpdatedDate": updated_timestamp,
#             "DeletedDate": deleted_timestamp
#         })
    
#     return pd.DataFrame(data)

# # Fonction pour écrire les données dans un fichier CSV
# def ecrire_donnees_csv(n, filename):
#     df = generer_donnees(n)
#     df.to_csv(filename, index=False)

# # Exemple d'utilisation
# ecrire_donnees_csv(100, "marseille_users_data.csv")