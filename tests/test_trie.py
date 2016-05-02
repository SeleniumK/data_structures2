from src.trie import Trie
import pytest

AUTOCOMPLETE = [
    ('n', ['no', 'nord', 'north', 'norton']),
    ('no', ['no', 'nord', 'north', 'norton']),
    ('nor', ['nord', 'north', 'norton', 'nortron']),
    ('nort', ['north', 'norton', 'nortron']),
    ('nortr', ['nortron']),
    ('north', ['north']),
    ('q', [])
]

def test_termination(simple_trie):
    assert simple_trie._contains("no")._terminated is True


def test_trie_init():
    goddamn = Trie()
    assert goddamn.children == {}


def test_trie_contains(simple_trie):
    assert 'norton' in simple_trie
    assert 'north' in simple_trie
    assert 'nortron' in simple_trie
    assert 'nord' in simple_trie


def test_trie_contains_not_subwords(simple_trie):
    assert 'nor' not in simple_trie


def test_trie_contains_subwords_after(simple_trie):
    simple_trie.insert('no')
    assert 'no' in simple_trie
    assert 'norton' in simple_trie
    assert 'north' in simple_trie
    assert 'nortron' in simple_trie
    assert 'nord' in simple_trie


def test_traversal(simple_trie):
    assert sorted(list(simple_trie.traversal('no'))) == sorted(["no", "norton", "north", "nord", "nortron"])


@pytest.mark.parametrize('a, b', AUTOCOMPLETE)
def test_autocomplete(simple_trie, a, b):
    assert simple_trie.autocomplete(a) == b
