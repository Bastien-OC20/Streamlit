from dataclasses import dataclass

# from abc import ABC

@dataclass
class Personne():
    email:str=""
    def __init__(self, email:str) -> None:
        self.email = email
