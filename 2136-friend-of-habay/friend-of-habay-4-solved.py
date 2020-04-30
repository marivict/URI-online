enroll = []
answerYes = []
answerNo = []
participants = []
notRepeatedNames=[]
notRepeatedAnswer = []
lenghtElements = []
majorLenghtElement = 0

while True:
    incoming = raw_input()
    if incoming == "FIM":
        break
    enroll.append(incoming.split())
    #print 'enroll: ' + str(enroll)
    
#Separte friend from say YES or NO
for answer in enroll:
    if answer[1] == "YES":
        answerYes.append(answer[0])
    else:
        answerNo.append(answer[0])
        
#add sorted names        
participants = sorted(answerYes) + sorted(answerNo)

#delete the repeated names
for names in participants:
    if names not in notRepeatedNames:
        notRepeatedNames.append(names)

#Display the names 
for participant in notRepeatedNames:
    print str(participant)

#deleted repeated names from yes list
for index in answerYes:
    if index is not notRepeatedAnswer:
        notRepeatedAnswer.append(index)
        
#Add the length of the element in notRepeatedName    
for index in notRepeatedAnswer:
    lenghtElements.append(len(index))

majorLenghtElement = max(lenghtElements)

#Choose a winner for a friend of Habay
for sortedIndex in notRepeatedAnswer:
    if len(sortedIndex) == majorLenghtElement:
        print "\nAmigo do Habay:\n" + str(sortedIndex)
        break
