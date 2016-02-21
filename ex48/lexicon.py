lexicon = {
    "north": 'direction',
    "south": 'direction',
    "east": 'direction',
    "west": 'direction',  # study drill 2
    "go": 'verb',
    "kill": 'verb',
    "eat": 'verb',
    "the": 'stop',
    "in": 'stop',
    "of": 'stop',
    "bear": 'noun',
    "princess": 'noun',
    "1234": 'number',
    "3": 'number',
    "91234": 'number',
    "ASDFADFASDF": 'error',
    "IAS": 'error'
}

'''
lexicon = {
    "north": ('direction', 'north'),
    "south": ('direction', 'south'),
    "east": ('direction', 'east'),
    "go": ('verb', 'go'),
    "kill": ('verb', 'kill'),
    "eat": ('verb', 'eat'),
    "the": ('stop', 'the'),
    "in": ('stop', 'in'),
    "of": ('stop', 'of'),
    "bear": ('noun', 'bear'),
    "princess": ('noun', 'princess'),
    "1234": ('number', 1234),
    "3": ('number', 3),
    "91234": ('number', 91234),
    "ASDFADFASDF": ('error', 'ASDFADFASDF'),
    "IAS": ('error', 'IAS')
}
这个词典是我自己顺着题意写的，看了视频后发现，还是作者的方法比较好，代码量少！
为了避免该注释变成docstring。我把作者的代码写在上面！不过作者似乎忘记字符串和数字的转换了！！！
'''


def scan(sentence):
    result = []
    words = sentence.split()
    for word in words:
        if word.isdigit():
            pair = (lexicon[word], float(word))  # study drill 4
        else:
            pair = (lexicon[word], word)
        result.append(pair)

    return result

