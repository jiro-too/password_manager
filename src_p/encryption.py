import hashers

def get_md5(string:str):
    mdstr = "".join(format(i,'x') for i in hashers.md5sum(string))
    return mdstr

