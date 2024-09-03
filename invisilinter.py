import ast

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

def fuck_up_name(vname):
    if vname in keyword.kwlist + dir(builtins) + ["var"]:
        return vname
    new_name = ""
    added = False
    for letter in vname:
        if (not added) and (letter in evildict.keys()):
            new_name += evildict[letter]
            added=True
        else:
            new_name += letter
        
    return new_name


class toLower(ast.NodeTransformer):
    def visit_alias(self, node):
        return ast.alias(**{**node.__dict__, 'asname':fuck_up_name(node.asname)})

    def visit_Name(self, node):
        return ast.Name(**{**node.__dict__, 'id':fuck_up_name(node.id)})


def wreak_havoc(src_code):
    '''Call this function! Pass the code as parameter.'''
    return ast.unparse(toLower().visit(ast.parse(src_code)))