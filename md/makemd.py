import os
import re

folders = os.listdir()

for folder in folders:
    if '.py' in folder:
        continue
    texts = os.listdir(folder)
    for textfile in texts:

        textpath = os.path.join(folder, textfile)
        if not '.txt' in textpath:
            continue


        #process
        matchtext = "(\[[0-9]+\:[0-9]+\])"
        text = open(textpath).read()

        text = "#"+text

        matches = re.findall( "(\[[0-9]+\:[0-9]+\])", text)

        for m in matches:
            placeholder = m.replace("[", "<<").replace("]", ">>")
            text = text.replace(m, placeholder)

        text = text.replace("<<", "**[").replace(">>", "]**")
        mdpath  = textpath.replace(".txt", ".md")
        with open(mdpath, "w") as f:
            f.write(text)
