from dataclasses import dataclass
import re
import pandas as pd

from Entity import Roles

@dataclass
class VerificationsService:
    
    def IsCodePostal(self,Postal):
        __rePostalCode = re.compile(r"(\d{5})")
        try:
            if not re.match(__rePostalCode,Postal):
                return False
            return True
        except re.error as e:
            print("Error occurred:", e.msg)
            print("Pattern:", e.pattern)
            print("Position:", e.pos)
            return False
        
    def IsEmail(self,email:str):
        __reEmail = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
        try:
            if not re.match(__reEmail, email):
                # print("isemail vérif NO")
                return False
            return True

        except re.error as e:
            print("Error occurred:", e.msg)
            print("Pattern:", e.pattern)
            print("Position:", e.pos)
            return False

    def EmailInUse(self,email:str,df:pd.DataFrame):
        if not isinstance(email,str):
            return False
        if not isinstance(df,pd.DataFrame):
           return False
        if email not in df['email'].tolist() :
            return False
        return True
        
    def IsInt(self,userInput):
        if not isinstance(userInput,int):
            return False
        return True

    def IsName(self,name) -> bool:
        __reText = re.compile(r"([A-Za-z])\w+(\d)?")
        try:
            if not re.fullmatch(__reText, name):
                return False
            return True
        except re.error as e:
            print("Error occurred:", e.msg)
            print("Pattern:", e.pattern)
            print("Position:", e.pos)
            return False
    
    def IsAge(self,age) -> bool:
        __reAge = re.compile(r"(\d{1,3})")
        try:
            if not re.fullmatch(__reAge, age):
                return False
        except re.error as e:
            print("Error occurred:", e.msg)
            print("Pattern:", e.pattern)
            print("Position:", e.pos)
            return False
        if int(age) < 1 or int(age) > 120:
                print("L'age doit être comprise entre 1 et 120 ans")
                return False
        return True
    
    def IsWeight(self,weight) -> bool:
        __reWeight = re.compile(r"(\d{1,3})")
        try:
            if not re.fullmatch(__reWeight, weight):
                return False
        except re.error as e:
            print("Error occurred:", e.msg)
            print("Pattern:", e.pattern)
            print("Position:", e.pos)
            return False
        if int(weight) < 1 or int(weight) > 450:
                print("Le poids doit être comprise entre 1 et 450 kg")
                return False
        return True
    
    def IsSize(self,size) -> bool:
        __reSize = re.compile(r"([0-2]{1}(([.])[0-9]{1,2})?)")
        try:
            if not re.fullmatch(__reSize, size):
                return False
        except re.error as e:
            print("Error occurred:", e.msg)
            print("Pattern:", e.pattern)
            print("Position:", e.pos)
            return False
        if float(size) < 0.5 or float(size) > 3:
                print("Le poids doit être comprise entre 0.5 et 3 m")
                return False
        return True
    
    def IsRole(self,role:Roles) -> bool:
        # values = map(lambda x: x.key, Roles)
        values = list(Roles.Roles)
        print(values)
        # a = list(Roles)
        # print(a)
        # print(list(Roles.__members__.keys()))
        # values = list(Roles.__members__.keys())
        # values = [member.value for member in Roles]
        if role not in values:
            return True
        return True
        