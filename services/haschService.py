from argon2 import PasswordHasher

from dataclasses import dataclass

@dataclass
class haschService():

    __ph = PasswordHasher()

    def HashPassord(self,password:str)->str:

        return self.__ph.hash(password)
    
    def checkPassorwd(self, password:str, hash:str)->bool:
        try:
            if self.__ph.verify(hash, password):
                # Best practice to check – and if necessary rehash – passwords after each successful authentication.
                # https://argon2-cffi.readthedocs.io/en/stable/api.html#argon2.PasswordHasher.check_needs_rehash
                self.__ph.check_needs_rehash(hash) 
                return True
        except Exception as e:
            print(f"checkPassorw => An error occurred: {e}")
            return False

    def check(self):
        hash = self.__ph.hash("correct horse battery staple")
        hash  # doctest: +SKIP
        '$argon2id$v=19$m=65536,t=3,p=4$MIIRqgvgQbgj220jfp0MPA$YfwJSVjtjSU0zzV/P3S9nnQ/USre2wvJMjfCIjrTQbg'