def word_count(words):
    counter = {}
    for w in words:
        if w not in counter:
            counter[w] = 1
        else:
            counter[w] += 1
    print(len(counter))
    lst = sorted(list(counter.values()), reverse=True)
    print(lst)


word_count(['bcdef', 'abcdefg', 'bcde', 'bcdef'])
