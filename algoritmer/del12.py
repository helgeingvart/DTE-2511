# %% [markdown]
# # Søking i strenger
# 
# Vi er ute etter etter en algoritme som kan finne en søkestreng `pattern` i en viss streng `text`. Først, la oss se på tilfellet "brute force"
# 
# ![brute](../resources/img/brute-force.png)
# 
# Denne metoden sjekker at det alle bokstavene i mønsteret gjentar seg på et visst sted der man søker i teksten. Før vi går videre og implementerer denne algoritmen, definerer vi noen variable/konstanter:
# 
# * m = len(pattern)
# * n = len(text)
# * i: nåværende indeks i text
# * k: næværende indeks i pattern

# %%
def search(text, pattern) :
    m = len(pattern)
    n = len(text)

    positions = []
    if (m >= n) : raise RuntimeError("Pattern must be shorter than text searched")
    for i in range(n-m+1) :  # For every position i, check for match
        found = True
        for k in range(m) :
            if pattern[k] != text[i+k] :
                found = False
                break
        if (found) :
            positions.append(i)

    return positions

text = "HelgeFred"
pattern = "s"

search(text, pattern)

# %% [markdown]
# Så, dette var vel enkelt og greit? Well, algoritmen er ikke så effektiv, siden man kan risikere å søke etter `pattern` hele `n-m` ganger dersom match skjer helt på slutten av `text`, noe som er ganske inefektivt. Dette vil bli i størrelsesorde $O(nm)$ operasjoner. 
# 
# En bedre algoritme er den såkalte Boyer-Moore, se egen presentasjon for denne...

# %%
def searchBoyerMoore(text, pattern) :
    i = 0
    n = len(text)
    m = len(pattern)
    while (i < n-m+1) :
        misMatch = False
        k = m-1  # Start at the end of the pattern string
        while (k >= 0) :
            if pattern[k] != text[i+k] :
                misMatch = True
                break
            k-=1
        if misMatch :  # Need to look for next occurance backwards in pattern!
            char = text[i+k]   
            numSteps = 0
            foundElsewere = False
            while (k >= 0) :
                if pattern[k] != char :
                    k -= 1
                    numSteps += 1
                else :
                    foundElsewere = True
                    break
            if not foundElsewere :
                i = i + m   # Move the whole length of searchString
            else :
                i = i + numSteps  # Move that many steps necessary
        else :
            return i

    return -1

text    = "GCTTCTGCTACCTTTTGCGCGCGCT"
pattern = "CGCT"

searchBoyerMoore(text, pattern)



