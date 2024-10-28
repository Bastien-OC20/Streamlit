# from faker import Faker # https://faker.readthedocs.io/en/master/
from datetime import datetime
from enum import Enum

# Définition de l'énumération des rôles
class Roles(Enum):
    SuperAdmin = 0
    Admin = 1
    User = 2

