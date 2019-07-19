# -*- coding: utf 8 -*-
"""
Define a suite a tests for the Lexicon module.
"""
from striplog import Lexicon


def test_lexicon():
    """All the tests...
    """
    lexicon = Lexicon.default()
    s = lexicon.__str__()
    assert s is not ''
    assert lexicon.__repr__() is not ''
    assert lexicon.find_synonym('Halite') == 'salt'
    assert len(lexicon.categories) == 4

    s = "lt gn ss w/ sp gy sh"
    answer = 'lighter green sandstone with spotty gray shale'
    assert lexicon.expand_abbreviations(s) == answer

    fname = "tutorial/lexicon.json"
    l = Lexicon.from_json_file(fname)
    assert l.__repr__() is not ''


def test_lexicon_dates():
    """ slashes in date/time formats are not replaced by 'with'
    """
    lexicon = Lexicon.default()
    s = "SHALE - DEEPENED 01/02/2002"
    answer = s
    assert lexicon.expand_abbreviations(s) == answer

