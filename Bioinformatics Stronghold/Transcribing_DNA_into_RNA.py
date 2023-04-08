#File takes a DNA sequence and returns it as an RNA sequence
import sys

DNA_sequence = input("insert nucleotide sequence here: ")
RNA_sequ = DNA_sequence.replace("T", "U")
print(str(RNA_sequ))

