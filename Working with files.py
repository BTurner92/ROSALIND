##file = open("dummy_text.txt", "r")
##result = ""
##for line in file:
##    file.readline(str(line))
##    file.write(str(line) +"\n")
##    result+= str(line)
##
##print(result)

#Reads each line of a file, only prints every even numbered line (assuming 1 base counting
#therefore counts every second line
file = open("rosalind_ini5.txt", "r")
result = ""
for line in file:
    result += file.readline()
print(result)

    
