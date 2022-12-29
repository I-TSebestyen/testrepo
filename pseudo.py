def make_matrix(m, n, sentence):
    output = []
    for i in range(0, len(sentence), n):
        sub_str = sentence[i:i+n]
        print(sub_str)
        output.append(list(sub_str))

    for e in output:
        if len(e) < n:
            e.append('.')

    return output


print(make_matrix(6, 2, 'Raise sails'))
