# %% [markdown]
# # Litt mer om file.open() og ulike formater
# 
# Generell syntax for å åpne filer:
# ```<file> = open(<path>, mode='<mode>', encoding=None, newline=None)```
# 
# * 'encoding=None' means that the default encoding is used, which is platform dependent. Best practice is to use 'encoding="utf-8"' whenever possible.
# * 'newline=None' means all different end of line combinations are converted to '\n' on read, while on write all '\n' characters are converted to system's default line separator.
# * 'newline=""' means no conversions take place, but input is still broken into chunks by readline() and readlines() on either '\n', '\r' or '\r\n'.
# 
# Modes
# * 'r' - Read (default).
# * 'w' - Write (truncate).
# * 'x' - Write or fail if the file already exists.
# * 'a' - Append.
# * 'w+' - Read and write (truncate).
# * 'r+' - Read and write from the start.
# * 'a+' - Read and write from the end.
# * 't' - Text mode (default).
# * 'b' - Binary mode.
# 
# Exceptions
# * 'FileNotFoundError' can be raised when reading with 'r' or 'r+'.
# * 'FileExistsError' can be raised when writing with 'x'.
# * 'IsADirectoryError' and 'PermissionError' can be raised by any.
# * 'OSError' is the parent class of all listed exceptions.
# 
# Kilde: https://gto76.github.io/python-cheatsheet/#open
# 

# %%
text = "Dette er en vanlig tekst\nVi kan angi alle mulige strenger\n øæå¤§#"
with open("test.txt",'w', encoding="utf-8", newline='\n') as filePointer :
    filePointer.write(text)

with open("test.txt", 'r', encoding="utf-8") as filePointer :
    text = filePointer.read()

print(text)   # Alt vel.

# Funker det samme nå uten encoding spesifisert (dvs. vha systemets default encoding?)

with open("testDefaultEncoding.txt",'w') as filePointer :
    filePointer.write(text)

with open("testDefaultEncoding.txt", 'r') as filePointer :
    text = filePointer.read()

print(text)

# Ekstra sjekk: Se hva som skjer i de to tilfellene i notepad og notepad++ på Windows


# %%
import pickle

class Foo:
    strings = ["Hei", "Hå", "Yalla", "hopp og sprett"]
    __squares = [i*i for i in range(1,100)]  # List comprehension
    __dictionary= {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5} 
    __doubleDict = {k:v*2 for (k,v) in __dictionary.items()}  # Dictionary comprehension

    @property
    def squares(self) :
        return self.__squares

    @property
    def doubles(self) :
        return self.__doubleDict

bar = Foo()
with open("persistence.dat", "wb") as file :
    pickle.dump(bar, file)

with open("persistence.dat", "rb") as file :
    foo = pickle.load(file)
    if (isinstance(foo,Foo)):
        # for s in foo.strings :
        #     print(s)
        # for square in foo.squares :
        #     print(square)
        for tall in foo.doubles.values() :
            print(tall)


# %% [markdown]
# # Litt om stier, også populært kalt "paths"
# 
# from os import getcwd, path, listdir
# from glob import glob
# 
# Paths can be either strings, Paths or DirEntry objects.
# 
# * <str>  = getcwd()                   # Returns the current working directory.
# * <str>  = path.join(<path>, ...)     # Joins two or more pathname components.
# * <str>  = path.abspath(<path>)       # Returns absolute path.
# * <str>  = path.basename(<path>)      # Returns final component of the path.
# * <str>  = path.dirname(<path>)       # Returns path without the final component.
# * <tup.> = path.splitext(<path>)      # Splits on last period of the final component.
# * <list> = listdir(path='.')          # Returns filenames located at path.
# * <list> = glob('<pattern>')          # Returns paths matching the wildcard pattern.
# * <bool> = path.exists(<path>)        # Or: <Path>.exists()
# 
# * <bool> = path.isfile(<path>)        # Or: <DirEntry/Path>.is_file()
# * <bool> = path.isdir(<path>)         # Or: <DirEntry/Path>.is_dir()
# 
# # Litt om filsystem og håndtering av dette i forhold til filer
# 
# import os
# import shutil
# 
# * os.chdir(<path>)                    # Changes the current working directory.
# * os.mkdir(<path>, mode=0o777)        # Creates a directory. Mode is in octal.
# * os.makedirs(<path>, mode=0o777)     # Creates all directories in the path.
# * shutil.copy(from, to)               # Copies the file. 'to' can exist or be a dir.
# * shutil.move(from, to)               # Moves a file/directory to a new dir
# * os.rename(from, to)                 # Renames/moves the file or directory.
# * os.replace(from, to)                # Same, but overwrites 'to' if it exists.
# * os.remove(<path>)                   # Deletes the file.
# * os.rmdir(<path>)                    # Deletes the empty directory.
# * shutil.rmtree(<path>)               # Deletes the directory.

# %%
from os import getcwd, path, listdir, mkdir
import shutil

# Lag en fil text.x på working directory

with open("text.x", "x") :
    pass

workingDir = getcwd()
print(workingDir)

# Lag underkatalog temp og flytt text.x til denne
tempPath = path.join(workingDir,"temp")
mkdir(tempPath)
shutil.move("text.x", tempPath)



