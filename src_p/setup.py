from distutils.core import setup, Extension
def maths_setup():
    setup(name="maths",
          include_dirs= ["./src_c/"],
          version="1.0.0",
          description="Python interface for the sqrt C library function",
          author="Soham Nandy",
          author_email="soham.nandy2006@gmail.com",
          ext_modules=[Extension("maths", ["./src_c/mathsmodule.c"])]),
    

def crypt_setup():
      setup(name="hashers",
          include_dirs= ["./src_c/"],
          version="1.0.0",
          description="C implementation of MD5 algorithm",
          author="Soham Nandy",
          author_email="soham.nandy2006@gmail.com",
          ext_modules=[Extension("hashers", ["./src_c/md5sum.c"])]),
          

if __name__ == "__main__":
    maths_setup()
    crypt_setup()
