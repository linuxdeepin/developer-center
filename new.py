#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
import locale

meta = '''Title:   My Document
Summary: A brief description of my document.
Authors: Waylan Limberg
         Date:    October 2, 2007
'''

def usage():
    help = u'''Use new.py like:
new.py category title path-to-file

example:
    new.py 深度截图 入门指南 deepin-shot/guide.md

    it will create a file at "docs/deepin-shot/guide.md" with this content:

title:
category:首页

    '''
    print(help)


if __name__=="__main__":
    if len(sys.argv)!= 4:
        usage()
        sys.exit(1)

    encoding = locale.getdefaultlocale()[1]
    meta = {}
    category = sys.argv[1].decode(encoding, 'ignore')
    title = sys.argv[2].decode(encoding, 'ignore')
    file = sys.argv[3]

    if not file.endswith(".md"):
        print ("path-to-file must end with .md\n")
        usage()
        sys.exit(2)

    meta["category"]=category
    meta["title"]=title

    mdmeta = "<!--Meta\n"
    for k, v in meta.items():
        mdmeta += k+":"+v+"\n"
    mdmeta += "DO NOT Delete Meta Above -->\n"

    path = "docs/" + file
    try:
        dir, name = os.path.split(path)
        os.makedirs(dir)
    except:
        pass

    fp = open(path, "w")
    fp.writelines(mdmeta.encode('utf8', 'ignore'))
    fp.close()
