import pytest
import time

from ftimecache import ftimecache
from ftimecache import _make_safe


def test_dict_to_sorted_list():
    d = {"c": {"d": 3}, "b": 2, "a": 1}
    d = _make_safe(d)

    assert d == (("a", 1), ("b", 2), ("c", (("d", 3),)))


def test_timecache_cached_okay(generator):
    @ftimecache(milliseconds=300)
    def testf():
        return next(generator)

    # initialized
    assert testf() == 0
    # cached
    assert testf() == 0
    # reset cache
    time.sleep(0.3)
    # next element
    assert testf() == 1


def test_timecache_with_kwargs(generator):
    @ftimecache(milliseconds=300)
    def testf(kwargs):
        return next(generator)

    d1 = {"a": 1, "b": {"c": 2}}
    d2 = {"a": 2, "b": {"c": 2}}

    assert testf(d1) == 0
    assert testf(d1) == 0
    assert testf(d2) == 1


def test_list_and_set(generator):
    @ftimecache(milliseconds=300)
    def testf(*args):
        return next(generator)

    l = [1]
    s = {2}

    assert testf(l, s) == 0
    assert testf(l, s) == 0
    time.sleep(0.3)
    assert testf(l, s) == 1
