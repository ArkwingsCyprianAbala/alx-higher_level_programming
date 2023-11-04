#!/usr/bin/python3
def multiple_returns(sentence):
    if not sentence:
        sentence = None
    if sentence:
        senlen = len(sentence)
    else:
        senlen = 0
    return (senlen, sentence if not sentence else sentence[:1])
