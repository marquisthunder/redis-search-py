#!/usr/bin/env python
# encoding: utf-8

import json
import redis

from chinese_pinyin import Pinyin

from mmseg import seg_txt
from mmseg.search import seg_txt_search, seg_txt_2_dict

complete_max_length = 10
pinyin_match        = True
debug               = True

redis = redis.Redis()

def hmget(name, ids, sort_field='id'):
    """docstring for hmget"""
    if not ids:
        return []
    return [r for r in redis.hmget(name, ids) if r]

def mk_sets_key(name, word):
    """docstring for mk_sets_key"""
    return "%s:%s" % (name, word.lower())

def mk_score_key(name, id):
    """docstring for mk_score_key"""
    return "%s:_score_:%s" % (name, id)

def mk_condition_key(name, field, id):
    """docstring for mk_condition_key"""
    return "%s:_by:_%s:%s" % (name, field, id)

def mk_complete_key(name):
    """docstring for mk_complete_key"""
    return "Compl%s" % name

def split_pinyin(text):
    """docstring for split_pinyin"""
    return split_words(Pinyin.t(text))

def split_words(text):
    """docstring for split_words"""
    return [i for i in seg_txt_search(text)]

def utf8(value):
    if isinstance(value, (bytes, type(None))):
        return value
    assert isinstance(value, unicode)
    return value.encode("utf-8")
