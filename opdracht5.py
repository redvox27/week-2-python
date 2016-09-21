def intersect(seq1, seq2):
 res = set()
 for x in seq1:
    if x in seq2:
        res.add(x)
    return res


print(intersect('beer', 'burger'))
print(intersect((1,2,3,4),(1,4,2,5)))