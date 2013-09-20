#!/usr/bin/env python
#encoding: utf-8

import os


class Pinyin(object):
    """docstring for Pinyin"""

    p = None

    def __init__(self):
        dictpath = os.path.join(os.path.dirname(__file__), "data", "Mandarin.dat")
        with open(dictpath, 'r') as fp:
            self.table = dict([line.rstrip('\n').split(',')
                            for line in fp])

    def to_unicode(self, value):
        """Converts a string argument to a unicode string.
        If the argument is already a unicode string or None, it is returned
        unchanged.  Otherwise it must be a byte string and is decoded as utf8.
        """
        if isinstance(value, (unicode, type(None))):
            return value
        assert isinstance(value, bytes)
        try:
            return unicode(value, "utf8")
        except:
            return value.encode("utf8").decode("utf8")

    def translate(self, chars, splitter=' '):
        """docstring for translate"""
        results = []
        is_english = False

        chars = self.to_unicode(chars)
        for char in chars:
            key = repr(char)[4:-1].upper()
            if key in self.table:
                if is_english:
                    results.append(splitter)
                results.append(self.table[key].strip().split(" ", 1)[0][0:-1].lower())
                results.append(splitter)
                is_english = False
            else:
                results.append(char)
                is_english = True
        return "".join(results).strip(splitter)

    @classmethod
    def t(self, chars, splitter=' '):
        """docstring for t"""

        if not self.p:
            self.p = Pinyin()

        return self.p.translate(chars, splitter)

if __name__ == "__main__":
    print Pinyin.t("hi梁小波")
