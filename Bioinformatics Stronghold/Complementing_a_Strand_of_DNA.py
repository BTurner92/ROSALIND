#File takes a DNA sequence, reverses it then creates a complementary strand of the
#reversed sequence
import sys
DNA_sequ = []
reverse_DNA_sequ = []
DNA_sequ = input("Paste DNA sequence here: ")
reverse_DNA_sequ = DNA_sequ[::-1]
comp_sequ = []

len_sequence = len(reverse_DNA_sequ)
i=0
message = ""
while i<len_sequence:
    nuc = reverse_DNA_sequ[i]
    if nuc == "A":
        comp_sequ.append("T")
        message+="T"
        i+=1
    if nuc == "C":
        comp_sequ.append("G")
        message+="G"
        i+=1
    if nuc == "G":
        comp_sequ.append("C")
        message+="C"
        i+=1
    if nuc == "T":
        comp_sequ.append("A")
        message+="A"
        i+=1
        
print(str("Here is the complementary strand: \n")+message)
