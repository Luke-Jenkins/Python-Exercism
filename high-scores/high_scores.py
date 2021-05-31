def latest(scores):
    return scores[len(scores) - 1]


def personal_best(scores):
    scores.sort()
    return scores[len(scores) - 1]


def personal_top_three(scores):
    scores.sort(reverse=True)
    top_scores = []

    count = len(scores)
    if count > 3:
        count = 3

    for i in range(count):
        top_scores.append(scores[i])

    return top_scores
