from src.trie import Trie


def test_trie_graph_insert(simple_trie):
    assert simple_trie.graph_dict == {
        "n": {
            "o": {
                "r": {
                    "t": {
                        "o": {
                            "n": {"*": "$"}
                        },
                        "h": {"*": "$"},
                        "r": {
                            "o": {
                                "n": {"*": "$"}
                            }
                        }
                    },
                    "d": {'*': '$'}
                }
            }
        }
    }


def test_trie_insert():
    assert Trie().graph_dict == {}


def test_trie_contains(simple_trie):
    assert 'norton' in simple_trie
    assert 'north' in simple_trie
    assert 'nortron' in simple_trie
    assert 'nord' in simple_trie


def test_trie_contains_not_subwords(simple_trie):
    assert 'no' not in simple_trie


def test_trie_contains_subwords_after(simple_trie):
    simple_trie.insert('no')
    assert 'no' in simple_trie
    assert 'norton' in simple_trie
    assert 'north' in simple_trie
    assert 'nortron' in simple_trie
    assert 'nord' in simple_trie
