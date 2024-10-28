from dataclasses import dataclass
import pandas as pd
from Entity.User import User
import os
import uuid
from pathlib import Path
from Entity.Roles import Roles

# ,UserId,Name,Password,Email,Role,Age,Taille,Poids,Postal,CreatedDate,UpdatedDate,DeletedDate
# 0,0,Anthony,scrypt:32768:8:1$vdpjk472agafbAtC$225570d1468228415be6ca78545438be0dc17beded109deb2ed7b0f4a8d53735df7deafa9b58b54a0e79266075f1a72bcf18df6672d9589be742bd3cdb2d86e1,admin@test.com," ""ROLE_SUPERADMIN""",25,220,110,13009

@dataclass
class UserRepositoryCSV():
    __file = "/DataBase/user.csv"
    __filePath = None
    __header:pd.DataFrame = None

    def __init__(self):
        self.__filePath = f"{Path(__file__).parent.parent.parent}/DataBase/user.csv" #TODO
        # print("self.__filePath")
        # print(self.__filePath)
        # absolutepath = os.path.abspath(__file__)
        # fileDirectory = os.path.dirname(absolutepath)
        # parentDirectory = os.path.dirname(fileDirectory)
        # parentDirectory = parentDirectory.replace('\\', '/')
        # pathParentDirectory = Path(parentDirectory)
        # secondParentDirectory = pathParentDirectory.parent.parent
        # secondParentDirectory = str(secondParentDirectory).replace('\\', '/') 
        # self.__filePath = secondParentDirectory + self.__file
        # self.__header = self.__getHeaderDataFrameFromCSV()
        # print("Path CSV Data" + "="*80)
        # print(self.__filePath)
        # print("")

    def __getFileCSV(self) -> str:
        return self.__filePath
    
    def __getHeaderCSV(self):
        return self.__header
    
    def __setHeader(self):
        self.__header = self.__getHeaderDataFrameFromCSV()
    
    def __getHeaderDataFrameFromCSV(self) -> pd.DataFrame: # READ
        try:
            df = pd.read_csv(self.__getFileCSV())
            header = df.head(0)
            return header
        except FileNotFoundError:
            print(f"File '{self.__getFileCSV()}' not found.")
            return None
        except pd.errors.EmptyDataError:
            print("The file is empty.")
            return None
        except Exception as e:
            print(f"__getHeaderDataFrameFromCSV => An error occurred: {e}")
            return None
    
    # ---------------------------------------------------------------- CRUD methods ----------------------------------------------------------------

    
    def FindAll(self) -> pd.DataFrame: # READ
        try:
            result = pd.read_csv(self.__getFileCSV(), index_col=False, header = 0, sep = ',')
            return result
        except FileNotFoundError:
            print(f"File '{self.__getFileCSV()}' not found.")
            return None
        except pd.errors.EmptyDataError:
            print("The file is empty.")
            return None
        except Exception as e:
            print(f"FindAll => An error occurred: {e}")
            return None
    
    
    def Create(self, user: User)-> User:
        """""
        Add user in CSV file if user type is User & email doesn't exist
        """""
        print("usr - DAL create " + "-"*80)
        # print(user)
        if not User.IsInstanceOfUser(user):
            #  return None
            raise ValueError("Erreur dasn les paramètres")
        
        # df = self.FindAll()
        # print("data frame")
        # print(df)
        # if (df['email'].isin([user.email]).any()) or df['nom'].isin([user.nom]).any():
        #     print("This user already exists, mail or name")
        #     raise ValueError(f"C'est utilisateur exsite déjà soit : \"{user.email}\", ou soit : \"{user.nom}\" est déjà présent.")
        
        result = self.__addUserInCSV(user)
        return result
    
    def Update(self, user: User) -> User:
        """Update user if if user type is User & user already exists

        Args:
            user (User): user for updating

        Returns:
            User: class User
        """
        if not self.__userIdExists(user):
            return None
        
        oldUser = self.__setUserValuesFromCVSToUserClassInstance(user)

        userUpdated = self.__updateUser(oldUser, user)

        return userUpdated
    
    
    def Delete(self, user: User) -> bool:
        """ Delete user into CSV if user type is User & user already exists

        Args:
            user (User): _description_

        Returns:
            bool: true if user marked as deleted in the DeleteDate column
        """
        
        if not self.__userIdExists(user):
            return None
        if not self.__deleteUser(user):
            return False
        return True
    
    
    def Remove(self, user: User) -> bool:
        """ user deleted from csv file

        Args:
            user (User): user class instance

        Returns:
            bool: true if user deleted
        """
        
        if not self.__userIdExists(user):
            return None
        if not self.__removeUser(user):
            return False
        return True
        
    
    
    
    def __addUserInCSV(self, user: User) -> User: # Write
        """
        Private fonction
        Write for a first time user un CSV File
        """
        try:
            myIndex = str(uuid.uuid4())
            user.UserId = myIndex
            user.set_CreatedDate()  
            myUser = pd.DataFrame(user.__dict__ , index=[0])
            myUser.to_csv(self.__getFileCSV(),mode='a', index=False, header=False)
            df = self.FindAll()
            lastIndex = df.index[-1]
            print(f"Data saved successfully in {self.__getFileCSV()} with index n°{lastIndex}.")
            return user
        except Exception as e:
            print(f"AddUserInCSV => An error occurred: {e}")
        return None

    
    def __updateUser(self, oldUser:User, newUser: User): # Update
        """
        Private fonction 
        Update optimist user in CSV File
        """
        newUser.UserId = oldUser.UserId
        
        df = self.FindAll()
        # selectedUserDf = df.loc[df['nom'] == oldUser.nom]
        result=User.ConstructUserAllAttributsFrormDf(oldUser.UserId, oldUser.nom, oldUser.mot_de_passe, oldUser.email, oldUser.code_postal, oldUser.age, oldUser.taille, oldUser.poids, Roles(oldUser.role), oldUser.UpdatedDate, oldUser.email, oldUser.code_postal)
        indexOldUser = df.index.get_loc(df[df["nom"]==oldUser.nom].index[0])
        mofified = False
        if newUser.UserId != oldUser.UserId:
            if df['email'].isin([newUser.email]).any():
                print(f"l'email modifier {newUser.email} pour l'utilisateur {oldUser.nom} est déjà utilisé, veuillez en rentrer un autre")
                return None

        if oldUser.email != newUser.email:
            # selectedUserDf.at[oldUser.UserId,'email'] = newUser.email
            result.email = newUser.email
            mofified = True

        # if oldUser.mot_de_passe != newUser.mot_de_passe:
        #     selectedUserDf.at[oldUser.UserId,'mot_de_passe'] = newUser.mot_de_passe
        #     result.mot_de_passe = newUser.mot_de_passe
        #     mofified = True
            
        if oldUser.role!= newUser.role:
            # selectedUserDf.at[oldUser.UserId,'role'] = newUser.role.value
            result.role = newUser.role
            mofified = True

        if oldUser.age!= newUser.age:
            # selectedUserDf.at[oldUser.UserId,'age'] = newUser.age
            result.age = newUser.age
            mofified = True
            
        if oldUser.taille!= newUser.taille:
            # selectedUserDf.at[oldUser.UserId,'taille'] = newUser.taille
            result.taille = newUser.taille
            mofified = True

        if oldUser.poids!= newUser.poids:
            # selectedUserDf.at[oldUser.UserId,'poids'] = int(newUser.poids)
            result.poids = int(newUser.poids)
            mofified = True

        if oldUser.code_postal!= newUser.code_postal:
            # selectedUserDf.at[oldUser.UserId,'code_postal'] = newUser.code_postal
            result.code_postal = newUser.code_postal
            mofified = True

        if not mofified:
            print("No modification detected.")
            return None
        

        newUser.CreatedDate = oldUser.CreatedDate
        newUser.set_UpdatedDate()
        newUser.poids = int(round(newUser.poids, 0))
        print(newUser.__dict__)
        try:
            self.__setHeader()
            df.drop(index=[indexOldUser], inplace = True)
            newUserDf = pd.DataFrame(newUser.__dict__ , index=[0])
            df = pd.concat([df, newUserDf],ignore_index=True)
            self.__getHeaderCSV().to_csv(self.__getFileCSV(), index=False)
            df.to_csv(self.__getFileCSV(), mode='a', index=False, header=False)
            print(f"Data updated successfully in '{self.__getFileCSV()}'.")
            return result
        except Exception as e:
            print(f"UpdateUser => An error occurred: {e}")
        return None
       
    
    def __deleteUser(self, user: User) -> bool: # TODO pas finie
        user.set_DeletedDate()
        try:
            user.set_DeletedDate()
            myUser = pd.DataFrame(user.__dict__)
            myUser.to_csv(self.__getFileCSV(), index=False)
            print(f"Data deleted successfully in '{self.__getFileCSV()}'.")
            return True
        except KeyError:
            print("User not found.")
        except Exception as e:
            print(f"DeleteUser => An error occurred: {e}")
        return False
    
    
    def __removeUser(self, user: User) -> bool: # TODO pas finie
        try:
            df = self.FindAll()
            df.drop(df.loc[df['UserId']==user.Get_Id].index,inplace=True)
            df.to_csv(self.__getFileCSV(), index=False)
            print(f"Data Removed successfully in '{self.__getFileCSV()}'.")
            return True
        except KeyError:
            print("User not found.")
        except Exception as e:
            print(f"RemoveUser => An error occurred: {e}")
        return False
    # ---------------------------------------------------------------- END CRUD methods ----------------------------------------------------------------

    
    def __setUserValuesFromCVSToUserClassInstance(self, user: User)-> User:
        """Create user instance from CSV file if user type is User
        Args:
            user (User): user for update
        Returns:
            _type_: User class instance
            _value_: User values from dataframe
        """
        df = self.FindAll()
        indexOldUser = df.index.get_loc(df[df["UserId"]==user.UserId].index[0])
        
        userId = df['UserId'].loc[df.index[indexOldUser]]
        nom = df['nom'].loc[df.index[indexOldUser]]
        mot_de_passe = df['mot_de_passe'].loc[df.index[indexOldUser]]
        email = df['email'].loc[df.index[indexOldUser]]
        code_postal = df['code_postal'].loc[df.index[indexOldUser]]
        age = df['age'].loc[df.index[indexOldUser]]
        taille = df['taille'].loc[df.index[indexOldUser]]
        poids = df['poids'].loc[df.index[indexOldUser]]
        role = df['role'].loc[df.index[indexOldUser]]
        CreatedDate = df['CreatedDate'].loc[df.index[indexOldUser]]
        UpdatedDate = df['UpdatedDate'].loc[df.index[indexOldUser]]
        DeletedDate = df['DeletedDate'].loc[df.index[indexOldUser]]
            
        result = User.ConstructUserAllAttributsFrormDf(userId, nom,mot_de_passe,email,code_postal,age,taille,poids, Roles(role), CreatedDate, UpdatedDate, DeletedDate)
        return result

    
    def __userIdExists(self, user: User)-> bool:
        """Does the user exist

        Args:
            user (User): User to check

        Returns:
            bool: True if the user exists
        """
        if not User.IsInstanceOfUser(user):
            print("This user is not an instance of User")
            return False
        df = self.FindAll()
        if not df['UserId'].isin([user.UserId]).any():
        # if not df['nom'].isin([user.nom]).any():
            print("This user doesn't exist")
            return False
        return True
    
    def FindUserByName(self, name: str) -> pd.DataFrame:
        df = self.FindAll()
        try:
            indexUser = df.index.get_loc(df[df["nom"]==name].index[0])
            return df.loc[df.index[indexUser]]
        except IndexError:
            return None
    
    def FindDfUserByEmail(self, email: str) -> pd.DataFrame:
        df = self.FindAll()
        try:
            indexUser = df.index.get_loc(df[df["email"]==email].index[0])
            return df.loc[df.index[indexUser]]
        except IndexError:
            return None
    
    def FindUserByEmail(self, email: str) -> User:
        df = self.FindAll()
        try:
            indexUser = df.index.get_loc(df[df["email"]==email].index[0])
            df_user = df.loc[df.index[indexUser]]
            myuser = User.UserFromRowDf(df_user)
            # return df.loc[df.index[indexUser]]
            return myuser
        except IndexError:
            return None
    
    def FindDfUserById(self, id: str) -> pd.DataFrame:
        df = self.FindAll()
        try:
            indexUser = df.index.get_loc(df[df["UserId"]==id].index[0])
            return df.loc[df.index[indexUser]]
        except IndexError:
            return None
    
    def FindUserById(self, id: str) -> User:
        df = self.FindAll()
        try:
            indexUser = df.index.get_loc(df[df["UserId"]==id].index[0])
            df_user = df.loc[df.index[indexUser]]
            myuser = User.UserFromRowDf(df_user)
            # return df.loc[df.index[indexUser]]
            return myuser
        except IndexError:
            return None
            
        