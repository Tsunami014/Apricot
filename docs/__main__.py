import griffe
from collections import deque
import os
import re

# <!-- module.object --> Documentation here
# <!--!  = ending for multiline (auto added)
# <!--1  = only print that object's docs, not any of its properties

def parseDoc(doc):
    return doc

MOD = griffe.load('apricot')
def getDoc(path, pref):
    obj = MOD[path]
    if obj.is_alias:
        obj = obj.final_target

    if pref == '1':
        doc = obj.docstring
        return parseDoc(doc) if doc is not None else ''

    ann = getattr(obj, "annotation", None)
    if not isinstance(ann, griffe.Expr):
        return ''
    try:
        cls = MOD[ann.canonical_path.removeprefix("apricot.")]
        if cls.is_alias:
            cls = cls.final_target
    except KeyError:
        return ''

    lines = []
    for memb in cls.all_members.values():
        doc = memb.docstring
        lines.append(f'- `{memb.name}`' + (f': {parseDoc(doc.value)}' if doc is not None else ''))
    return '\n'.join(lines)

_parseRe = re.compile(r'<!--([!1]?) (\S+) -->')
def parseMd(file):
    with open(file) as f:
        fc = f.read()
    groups = deque(_parseRe.finditer(fc))
    while groups:
        g = groups.pop()
        nam = g.group(2)
        pref = g.group(1)
        if pref == '!':
            nxt = groups[-1]
            if groups and nxt.group(2) == nam:
                fc = fc[:nxt.end()]+fc[g.end():]
            continue
        out = getDoc(nam, pref)
        if pref and pref in '1':
            end = fc.find('\n', g.end())
            fc = fc[:g.end()] + out + (fc[end:] if end != -1 else "")
        else:
            fc = fc[:g.end()] + f'\n{out}\n<!--! {nam} -->' + fc[g.end():]
    with open(file, 'w+') as f:
        f.write(fc.strip())

if __name__ == '__main__':
    import sys
    sys.path.append(os.getcwd())

    for pth, _, files in os.walk('./docs'):
        for f in files:
            if f.endswith('.md'):
                print(f"Parsing {f}...")
                parseMd(os.path.join(pth, f))
    print("Done!")
