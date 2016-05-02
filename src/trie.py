# import json


class Trie(object):
    """
    Turn words into graph objects... so "Norton", "North", "Integer", "Interesting", "Int" becomes ->.

    {
        *: {
            "n": {
                "o": {
                    "r": {
                        "t": {
                            "h": {$:$},
                            "o": {
                                "n": {$:$},
                            }
                        }
                    }
                }
            },
            "i": {
                "n": {
                    "t": {
                        $:$,
                        "e": {
                            "g": {
                                "e": {
                                    "r": {$:$}
                                }
                            },
                            "r": {
                                "e": {
                                    "s": {
                                        "t": {
                                            "i": {
                                                "n": {
                                                    "g": {*:$}
                                                }
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }

    """

    allowed_chars = 'abcdefghijklmnopqrstuvwxyz-\''

    def __init__(self, init_graph=None):
        """Init Trie Instance."""
        self.children = init_graph or {}
        self._terminated = False

    def insert(self, word):
        """Insert word into Trie."""
        focus = self
        for char in word.lower():
            if char in self.allowed_chars:
                focus.children.setdefault(char, Trie())
                focus = focus.children[char]
        focus._terminated = True

    def _traverse(self, start):
        """Helper method to traverse tree."""
        if self._terminated:
            yield start
        for key, value in self.children.items():
            for result in value._traverse(start + key):
                yield result

    def traversal(self, start):
        """Return generator of words in tree from starting point."""
        return self._contains(start)._traverse(start)

    def autocomplete(self, token):
        """Return list of the next 4 words based on letter provided."""
        pointer = self._contains(token)
        if not pointer:
            return []
        return [x for x in sorted(pointer._traverse(token))][:4]

    def _contains(self, value):
        """Return dictionary of last character in value."""
        focus = self
        for letter in value.lower():
            focus = focus.children.get(letter)
            if not focus:
                return False
        return focus

    def __contains__(self, value):
        """Return Boolean value of _contains.

        Checks if word in trie.
        """
        focus = self._contains(value)
        return bool(focus) and focus._terminated

    # def __str__(self):
    #     """String representation of trie."""
    #     return json.dumps(self.children, indent=2).replace('"', "").replace("  ", "| ")
