# coding=utf-8

__author__ = 'Shyam'

# from polyglot.text import Text


def tokenizer(raw_text, lang):
    # print(raw_text)
    # text = Text(raw_text, hint_language_code=lang)
    # return text.words
    return raw_text.split(" ")
