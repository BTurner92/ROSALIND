#GIVEN a string of a few hundred words
#RETURN the number of occurrences of each unique word, case inclusive, in
    #a nice list
file = []
file = input("insert string here: ")
dictionary = {}
i=0
for word in file.split(" "):
    if word not in dictionary:
        dictionary[word] = i   
    if word in dictionary:
        dictionary[word] +=1

for word, occurrences in dictionary.items():
    print(word, occurrences)

