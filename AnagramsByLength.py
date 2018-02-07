import collections

wordClean = sorted(list(set(word.strip().lower() for word in open('words', 'r'))))

wordsBySig = collections.defaultdict(list)
wordsByLen = collections.defaultdict(list)

anagramsByLength = {}

def signature(word):
    return ''.join(sorted(word))

def anagrams(word):
    return wordsBySig[signature(word)]

for word in wordClean:
    wordsBySig[signature(word)].append(word)

for word in wordClean:
    wordsByLen[len(word)].append(word)

for length, words in wordsByLen.items():
    anagramsByLength[length] = {word: anagrams(word) for word in words if len(anagrams(word)) > 1}

allAnagrams = {word : anagrams(word) for word in wordClean if len(anagrams(word)) > 1}

print(anagramsByLength)

