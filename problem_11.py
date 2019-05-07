'''
Implement an autocomplete system. That is, given a query string s and a set of all possible query strings, return all strings in the set that have s as a prefix.

For example, given the query string de and the set of strings [dog, deer, deal], return [deer, deal].

Hint: Try preprocessing the dictionary into a more efficient data structure to speed up queries.
'''

class Trie:
    def __init__(self):
        self._trie = {}

    def insert(self, word):
        trie = self._trie
        for char in word:
            if char not in trie:
                trie[char] = {}
            trie = trie[char]
        trie['*'] = True

    def suffixes(self, prefix):
        trie = self._trie
        for char in prefix:
            if char in trie:
                trie = trie[char]
            else:
                return []
        return self._elements(trie)

    def _elements(self, trie):
        result = []
        for c, v in trie.items():
            if c == '*':
                subresult = ['']
            else:
                subresult = [ c + s for s in self._elements(v)]
            result.extend(subresult)
        return result

# O(n)
def complete(words, prefix):
    words = sorted(words)
    print([s for s in words if s.startswith(prefix)])


if __name__ == '__main__':
    words = ['dog', 'deer', 'deal']
    complete(words, 'de')

    trie = Trie()
    for word in words:
        trie.insert(word)
    print(['de' + w for w in trie.suffixes('de')])

    words = ['able', 'abode', 'about', 'above', 'abuse', 'syzygy']
    complete(words, 'abo')

    trie = Trie()
    for word in words:
        trie.insert(word)
    print(['abo' + w for w in trie.suffixes('abo')])

