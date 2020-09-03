import re
from pathlib import Path

path_txt = '../txt/'

for p in Path(path_txt).rglob('*.txt'):
    path_md = str(p).replace('.txt', '.md').replace('/txt/', '/md/')
    text = open(str(p), 'r').read()
    verses = re.findall("\[[0-9]+\:[0-9]+\]", text)
    for v in verses:
        md_verse = v.replace("[", "**<<").replace("]", ">>**")
        text = text.replace(v, md_verse)
    text = text.replace("<<", "[").replace(">>", "]").replace("\n", "\n\n")

    text = "# "+text
    with open(path_md, 'w') as md:
        md.write(text)
        md.close()
