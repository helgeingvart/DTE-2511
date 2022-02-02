# %% [markdown]
# # Litt om file IO.
# 
# File IO er en fellesbetegnelse for fil-operasjoner, der man kan tenke seg å jobbe med input og output operasjoner i parallell. Konseptuelt kan man forestille seg at man leser fra "strømmer" og skriver til andre "strømmer", gjerne til/fra en fil, men kanskje også fra en nettverks-kobling eller en terminal. Man kan til og med strømme data til/fra strenger.
# 
# De viktige kallene når man skal "spole" fram og tilbake i en slik strøm er kallet seek() og tell() på en filpeker. Ellers er det bare å bruke read() og write() som vanlig.

# %%
import os
import shutil

print(os.getcwd())
fo = open("fileIO.txt", "r+", encoding="utf-8")
pos1 = fo.tell()  # Start of file, but if append mode, it's in the end!
fo.seek(0) # Ensure positioning at the beginning.
pos2 = fo.tell()  # Should be at the start
fo.seek(40)  # Step 40 characters into the file
pos3 = fo.tell()  
str = fo.read(3)
posAfterReadingDog = fo.tell()
fo.seek(40) # Go back to start of position for dog
fo.write("cat") # Overwrite "dog" with "cat"
fo.seek(40)
strCat = fo.read(3)
fo.flush()  # For små data-endringer som dette, trenger man egentlig ikke dette kallet..

# Lesing fra slutten av fila
fo.seek(0,2)  # Tallet 2 på slutten angir at man begynner på slutten av fila.
fileSize = fo.tell()
fo.seek(fileSize - 10) 
endString = fo.read(10)

byts = bytes(endString, 'utf-8')
print(endString)
for b in byts :
    print(b, end=" ")






