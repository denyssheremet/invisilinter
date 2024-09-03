import ast
import keyword
import builtins
from dataclasses import dataclass


# PASTE CODE HERE:
src_code = """
# Your code here ... 

"""





aas = ["a", "а"]
oos = ['o', 'о']
xxs = ["x", "х"]
sneaky_letters = xxs
fill_len = 50

def binnify(i):
    return str(bin(i)[2:]).zfill(fill_len)

def oofy(i):
    b = binnify(i)
    r = ''
    for d in b:
        r += sneaky_letters[int(d)]
    return r

for i in range(10):
    print(oofy(i))


evildict = {"a": "а",
"c": "с",
"d": "ԁ",
"e": "е",
"i": "і",
"j": "ј",
"n": "ո",
"o": "о",
"p": "р",
"v": "ν",
"x": "х",
"y": "у"}

changed_names = {}

@dataclass
class Counter:
    count = 0
counter = Counter()

def fuck_up_name(vname, counter=None, do_oofy=False):
    if vname in keyword.kwlist + dir(builtins) + ["var"]:
        return vname
    
    # change one letter sneakily
    if not do_oofy:
        new_name = ""
        added = False
        for letter in vname:
            if (not added) and (letter in evildict.keys()):
                new_name += evildict[letter]
                added=True
            else:
                new_name += letter
        return new_name
    
    # make everything unreadable
    else: 
        if vname in changed_names.keys():
            return changed_names[vname]
        else: 
            new_name = oofy(counter.count)
            changed_names[vname] = new_name
            counter.count += 1
            return new_name



class toLower(ast.NodeTransformer):
    def visit_alias(self, node):
        return ast.alias(**{**node.__dict__, 'asname':fuck_up_name(node.asname, counter, do_oofy=True)})

    def visit_Name(self, node):
        return ast.Name(**{**node.__dict__, 'id':fuck_up_name(node.id, counter, do_oofy=True)})

counter = Counter()


def wreak_havoc(src_code):
    '''Call this function! Pass the code as parameter.'''
    return ast.unparse(toLower().visit(ast.parse(src_code)))

print(wreak_havoc(src_code))