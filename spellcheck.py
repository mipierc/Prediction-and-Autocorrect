import re
def words(text): return re.findall(r'\w+', text.lower())

WORDS = words(open('big.txt').read())
words = []

def one_edit_distance(word):
    letters    = 'abcdefghijklmnopqrstuvwxyz'
    splits     = [(word[:i], word[i:])    for i in range(len(word) + 1)]
    deletes    = [L + R[1:]               for L, R in splits if R]
    transposes = [L + R[1] + R[0] + R[2:] for L, R in splits if len(R)>1]
    replaces   = [L + c + R[1:]           for L, R in splits if R for c in letters]
    inserts    = [L + c + R               for L, R in splits for c in letters]
    return set(deletes + transposes + replaces + inserts)

def two_edit_distance(word): 
    "All edits that are two edits away from `word`."
    return (e2 for e1 in one_edit_distance(word) for e2 in one_edit_distance(e1))

def known(words): 
    "The subset of `words` that appear in the dictionary of WORDS."
    return set(w for w in words if w in WORDS)

def before_and_after(word):
    # for x in WORDS:
    #     if x is word:
    #         a = tuple(x - 1, x + 1)
    #         words.insert(0, a)
    for index, s in enumerate(WORDS):
        if s == word:
            a = (WORDS[index-1], WORDS[index+1])
            words.append(a)
        else:
            continue


if __name__ == '__main__':
    #print(one_edit_distance("speling"))
    print(known(one_edit_distance("speling")))
    print(len(known(two_edit_distance('something'))))
    print(words)
