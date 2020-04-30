listOfThings = []
numberOfLines = int(raw_input())

#receive the quantity of lines to works and the list of words
if numberOfLines <= 100:
    for i in range(numberOfLines):
        incoming = sorted(raw_input().split())
        notRepeatedThing = []
        for index in incoming:
            #Delete the repeated words
            if index not in notRepeatedThing:
                notRepeatedThing.append(index)
        listOfThings.append(notRepeatedThing[:])
#print the list
for thing in listOfThings:
    print (' '.join(thing))



   
