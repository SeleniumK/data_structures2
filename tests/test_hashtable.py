from src.hashtable import HashTable
import pytest


def test_init_starts_up():
    H = HashTable()
    assert len(H._table) == 1024


def test_table_builds():
    H = HashTable(10)
    assert H._table == [[], [], [], [], [], [], [], [], [], []]


def test_hash_works_correctly():
    H = HashTable(6)
    assert H._hash("Hello World!") == 1085


def test_set_works_correctly():
    H = HashTable(6)
    H.set("Hello World!", "Bubbles")
    assert len(H._table[5]) == 1, H._table
    assert len(H._table[0]) == 0, H._table
    assert len(H._table[1]) == 0, H._table
    assert len(H._table[2]) == 0, H._table
    assert len(H._table[3]) == 0, H._table
    assert len(H._table[4]) == 0, H._table


def test_set_works_correctly_multiple_in_buckets():
    H = HashTable(1)
    H.set("Waffles", "value1")
    H.set("asdf", "value2")
    H.set("leu23", "value3")
    assert len(H._table[0]) == 3


def test_set_works_correctly_multiple_in_buckets_assert_value_is_right():
    H = HashTable(1)
    H.set("Waffles", "value1")
    H.set("asdf", "value2")
    H.set("leu23", "value3")
    assert H._table[0][0] == ('Waffles', 'value1')
    assert H._table[0][1] == ("asdf", "value2")
    assert H._table[0][2] == ("leu23", "value3")


def test_get_works_correctly():
    H = HashTable()
    H.set("hello world", "value")
    H.set("hello world2", "value2")
    assert H.get("hello world") == "value"
    assert H.get("hello world2") == "value2"


def test_a_ton_of_stuff():
    from random import shuffle
    H = HashTable()
    chars = "a b c d e f g h i j k l m n o p q r s t u v w x y z"
    chars += " " + chars.upper()
    chars += " " + "1 2 3 4 5 6 7 8 8 9 0"
    chars = chars.split()
    vals = {}
    for x in range(100):
        shuffle(chars)
        H.set("".join(chars[:5]), "".join(chars[-5:]))
        vals["".join(chars[:5])] = "".join(chars[-5:])
    for key in vals:
        assert H.get(key) == vals[key]

def test_get_is_none():
    H = HashTable(1)
    H.set("Waffles", "value1")
    H.set("asdf", "value2")
    H.set("leu23", "value3")
    assert H.get("foo") is None


def test_set_typeerror():
    h = HashTable(1)
    with pytest.raises(TypeError):
        h.set(1, "foo")


def test_get_typeError():
    H = HashTable(1)
    H.set("Waffles", "value1")
    H.set("asdf", "value2")
    H.set("leu23", "value3")
    with pytest.raises(TypeError):
        H.get(1)
