# returns hamming distance value

def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise ValueError('Strands are not equal lengths.')

    distance = 0

    if strand_a == strand_b:
        return distance
    else:
        for i in range(len(strand_a)):
            if strand_a[i] != strand_b[i]:
                distance += 1
        return distance
