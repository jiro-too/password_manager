import sys
import os
import encryption

class File:
    def __init__(self,db_path:str) -> bool:
        self.path = db_path
        if os.path.exists(db_path):
            self.db = open(db_path,"w+")
            return True
        else:
            return False

    def create_db(self, masterkey:str):
        pass
    def load_key(self,username:str):
        uname_hex = encryption.Sha256(bytes(username)).hexdigest()
        uname_p_list = self.path.readlines()
        for entry in uname_p_list:
            if entry.split(":")[0] == uname_hex:
                print("FOUND")
            else:
                print("NOT FOUND")
        
        return 0
    
    def enter_key(self,username:str,password:str):
        uname_hex = encryption.Sha256(bytes(username)).hexdigest()
        self.db.write(f"\n{")

if __name__ == "__main__":












