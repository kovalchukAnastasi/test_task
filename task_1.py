from operator import itemgetter
import string

text = "The European languages are members of the same family. Their separate existence is a myth. For science, music, sport, etc, Europe uses the same vocabulary. The languages only differ in their grammar, their pronunciation and their most common words. Everyone realizes why a new common language would be desirable: one could refuse to pay expensive translators. To achieve this, it would be necessary to have uniform grammar, pronunciation and more common words. If several languages coalesce, the grammar of the resulting language is more simple and regular than that of the individual languages. The new common language will be more simple and regular than the existing European languages. It will be as simple as Occidental; in fact, it will be Occidental. To an English person, it will seem like simplified English, as a skeptical Cambridge friend of mine told me what Occidental is."

# TASK 1) Find the number of times each word in the paragraph is used. Print the top 3 most used words.
def top_3_words(text):
    myDict1 = {}
    lowerText = text.lower()
    myList1 = lowerText.split()
    for word in myList1:
        stripWord = word.strip(string.punctuation)
        if stripWord in myDict1:
            myDict1[stripWord] += 1
        else:
            myDict1.update({stripWord : 1})
    myListFromDict=list(myDict1.items())
    sortedListFromDict = sorted(myListFromDict, key=itemgetter(1), reverse=True)
    #print(sortedListFromDict)
    return sortedListFromDict[:3]

print('TASK 1 solution:', top_3_words(text))


# TASK 2) Find the shortest sentence from the paragraph. Print the sentence and the number of words in that sentence.
def shortest_sent_and_num_of_words(text):
    myList2 = text.split('. ')
    myDict2 = {}
    for sentence in myList2:
        senList=sentence.split()
        myDict2.update({sentence : len(senList)})
    senDictList=list(myDict2.items())
    sortedSenDictList = sorted(senDictList, key=itemgetter(1))
    return sortedSenDictList[:1]

print('TASK 2 solution:', shortest_sent_and_num_of_words(text))


# TASK 3) Print a version of the paragraph in which the first and every other letter from every word is capitalized.
def capitalized_through_one(text):
    lowerText = text.lower()
    myList1 = lowerText.split()
    myList3 = []
    for word in myList1:
        listedWord=list(word)
        for (index, elem) in enumerate(listedWord):
            if index==0 or index%2==0:
                listedWord[index] = elem.capitalize()
        joinedWord = "".join(listedWord)
        myList3.append(joinedWord)
    changedText = " ".join(myList3)
    return changedText

print('TASK 3 solution:')
print(capitalized_through_one(text), '\n')


# TASK 4). Print a version of the paragraph in which all words are in reversed order. 
def reversed_text(text):
    myList4 = text.split()
    myList4.reverse()
    revText = ' '.join(myList4)
    return revText

print('TASK 4 solution:', reversed_text(text), '\n')