import json

class Trie(object):
    """
    Turn words into graph objects... so "Norton", "North", "Integer", "Interesting", "Int" becomes ->

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
    children = 'abcdefghijklmnopqrstuvwxyz-\''

    def __init__(self):
        self.graph_dict = {}

    def insert(self, word):
        focus = self.graph_dict
        for char in word.lower():
            if char in self.children:
                focus.setdefault(char, {})
                focus = focus[char]
        focus['*'] = '$'

    def traversal(self, start):
        start = 'n'


        def give_me_your_children(start, word=[]):
            import pudb; pudb.set_trace()
            if start == '$':
                yield "".join(word)
            else:
                for key, value in start.items():
                    if key != '*':
                        word.append(key)
                    for result in give_me_your_children(value, word):
                        yield result
                    # yield word + list(give_me_your_children(value, word))

        return list(give_me_your_children(self.graph_dict))

        # flattened = give_me_your_children(self.graph_dict)
        # import json
        #
        # print(list(flattened))
        # print(json.dumps(list(chain.from_iterable(flattened)), indent=2).replace('\"', ''))

        # while stack:
        #     print(word)
        #     for key, value in stack.pop().items():
        #         if key == '*' and value == '$':
        #             yield ''.join(word)
        #         else:
        #             word.append(key)
        #             stack.append(value)
        # print(word)


    # def delete(self, word):
    #     focus = self.graph_dict
    #     remove_index = None
    #     for i, letter in enumerate(word.lower() + '*'):
    #         try:
    #             if len(focus.keys()) == 1 and not remove_index:
    #                 remove_index = i
    #             elif len(focus.keys()) > 1:
    #                 remove_index = None
    #             focus = focus[letter]
    #         except KeyError:
    #             return False
    #
    #     return remove_index

    def _contains(self, value):
        focus = self.graph_dict
        for letter in value.lower():
            focus = focus.get(letter)
            if not focus:
                return False
        return focus

    def __contains__(self, value):
        return bool(self._contains(value + '*'))


    def __str__(self):
        return json.dumps(x.graph_dict, indent=2).replace('"', "").replace("  ", "| ")


x = Trie()
x.insert("Norton")
x.insert("No")
x.insert("North")
x.insert("Nortron")
x.insert("Selena")
x.insert("Kent")
print(x.traversal('asdf'))
# x.insert("Integer")
# x.insert("Interest")
# x.insert("Int")
# x.insert('immutable')
# x.insert("Norton")
# x.insert("No")
# x.insert("Noon")
# x.insert("North")
# x.insert("Norway")
# x.insert("Nocturne")
# x.insert("Legend")
# x.insert("League")
# x.insert("Leashed")
# x.insert("Leash")
# print(x)
