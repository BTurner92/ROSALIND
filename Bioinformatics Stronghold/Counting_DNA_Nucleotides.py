#File takes a DNA sequence and counts the number of occurrences of each nucleotide.
import sys

sequence = input("insert nucleotide sequence here: ")
A = 0
C = 0
G = 0
T = 0

len_sequence = len(sequence)
i=0

while i<len_sequence:
    nuc = sequence[i]
    if nuc == "A":
        A+=1
        i+=1
    if nuc == "C":
        C+=1
        i+=1
    if nuc == "G":
        G+=1
        i+=1
    if nuc == "T":
        T+=1
        i+=1

print(str(A)+" "+str(C)+" "+str(G)+" "+str(T))
    

