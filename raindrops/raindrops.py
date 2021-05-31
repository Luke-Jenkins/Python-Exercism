def convert(number):
    responses = {3: 'Pling', 5: 'Plang', 7: 'Plong'}
    results = []
    raindrop = ''
    for factor in responses:
        if number % factor == 0:
            results.append(factor)
    if not results:
        return str(number)
    else:
        for result in results:
            raindrop += responses[result]
        return raindrop
