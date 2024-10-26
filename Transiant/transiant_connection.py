from dataclasses import dataclass
from pydantic import BaseModel # TODO https://docs.pydantic.dev/latest/

@dataclass
class trs_connection():
# class trs_connection(BaseModel):
    # email:str
    # password:str

    def __init__(self, mail:str, passw:str):
        self.email = mail
        self.password = passw

