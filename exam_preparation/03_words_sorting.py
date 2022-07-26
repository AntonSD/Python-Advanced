def words_sorting(*args):
    words = {}

    for word in args:
        ord_counter = 0
        for chr in word:
            number = ord(chr)
            ord_counter += number
        words[word] = ord_counter

    for word, number in words.items():



print(
    words_sorting(
        'escape',
        'charm',
        'mythology'
  ))
