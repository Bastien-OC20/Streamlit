from dataclasses import dataclass
from pydantic import BaseModel # TODO https://docs.pydantic.dev/latest/
from Transiant.Personne import Personne

# @dataclass
class transiant_connection(Personne):
# class trs_connection(BaseModel):
    # email:str
    password:str

    def __init__(self, email:str, password:str):
        # self.email = mail
        self.password = password
        super().__init__(email)

