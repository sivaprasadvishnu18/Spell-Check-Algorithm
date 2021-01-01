class LanguageHelper():
    language = set()
    
    def __init__(self, words):
        for w in words:
            self.language.add(w)

    def __contains__(self, query):
        return query in self.language

    def getSuggestions(self, query):
        testWord = ''
        matchingWords = []
        alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','-',"\'"]
        for words in self.language:
            if len(words) == len(query) + 1:  #If length of word is 1 more
                for x in range(len(words)):
                    testWord = words.replace(words[x],'',1) #Delete each letter to match query
                    if testWord.lower() == query.lower(): #Check to see if testWord is the same as query
                        matchingWords.append(words)
                        
            elif len(query) == len(words) + 1: #if length of query is 1 more
                for x in range(len(query)):
                    testWord = query.replace(query[x], '',1) #Delete each letter to match word
                    if testWord.lower() == words.lower(): #Check to see if testWord is in words
                        matchingWords.append(testWord)
                        
            elif len(query) == len(words):  #If lengh of query and word are equal
                for x in range(len(query)):
                    for letter in alphabet:
                        testWord = query.replace(query[x],letter,1) #Replace letter of query with a letter from the alphabet once each time
                        if testWord == words.lower(): #Check if it equals word from the list
                            matchingWords.append(words)
                            
                    if x == 0:                 #If the first value is 0
                        testWord = query[1] + query[0] + query[2:] #The first two characters are going to switch places
                    else:
                        testWord = query[:x] + query[x+1:x - 1:-1] + query[x + 2:] #This will swap two characters in the rest of the query 
                    if testWord.lower() == words.lower(): #Check if this word is in the list 
                        if len(query) == len(testWord):
                            matchingWords.append(words)
                            
        total = []             #This will delete duplicates and make the list in alphabetical order
        for items in matchingWords:
            if items not in total:
                if query[0].isupper():
                    total.append(items.capitalize())
                else:
                     total.append(items)
        return sorted(total) 
    
