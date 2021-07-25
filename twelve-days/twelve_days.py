def recite(start_verse, end_verse):
    chorus = ''
    song = []
    day = [
        'first', 'second', 'third', 'fourth',
        'fifth', 'sixth', 'seventh', 'eighth',
        'ninth', 'tenth', 'eleventh', 'twelfth'
    ]
    gifts = [
            'a Partridge in a Pear Tree.',
            'two Turtle Doves,',
            'three French Hens,',
            'four Calling Birds,',
            'five Gold Rings,',
            'six Geese-a-Laying,',
            'seven Swans-a-Swimming,',
            'eight Maids-a-Milking,',
            'nine Ladies Dancing,',
            'ten Lords-a-Leaping,',
            'eleven Pipers Piping,',
            'twelve Drummers Drumming,'
    ]

    gift = gifts[0:end_verse]
    gift.reverse()

    for i in range(1, end_verse + 1):
        if i == 1:
            chorus = gift[end_verse - i]
        elif i == 2:
            chorus = gift[end_verse - i] + ' and ' + chorus
        else:
            chorus = gift[end_verse - i] + ' ' + chorus

        if i >= start_verse:
            refrain = f'On the {day[i - 1]} day of Christmas my true love gave to me: '
            song.append(refrain + chorus)

    return song
