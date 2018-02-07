# finds the number of anagrams given a file of
# words separated by the new line character 

#needed for the defaultdict
import collections

# clean and sort input
wordClean = sorted(list(set(word.strip().lower() for word in open('words', 'r'))))

# creates 'signature' of a word to be used as a key
# in the dictionary for anagram comparison 
def signature(word):
    return ''.join(sorted(word))

# the defaultdict will create an empty list in the
# case that a key cannot be used
wordsBySig = collections.defaultdict(list)

# populate the dictionary
for word in wordClean:
    wordsBySig[signature(word)].append(word)

# function to return a list of anagrams when a word
# is passed in as a parameter
def anagrams(word):
    return wordsBySig[signature(word)]

# creates a dictionary with the key of each word that 
# has a list of greater size than one (a word other than itself)
allAnagrams = {word : anagrams(word) for word in wordClean if len(anagrams(word)) > 1}

# print out the number of anagrams!
print(len(allAnagrams))