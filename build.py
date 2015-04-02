#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import shutil
import markdown
import codecs
from collections import defaultdict


if __name__ == "__main__":
    print("Genarator mkdocs.yml")
    shutil.copyfile("mkdocs.yml.base","mkdocs.yml")

    fp = codecs.open("mkdocs.yml", mode="a+", encoding="utf-8")
    directory = "docs"
    toc = defaultdict(list)
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.md'):
                path = root + "/" + file
                with codecs.open(path, mode="r", encoding="utf-8") as fin:
                    data = fin.read().splitlines(True)
                data = data[1:]
                text = ""
                for l in data:
                    text += l
                md = markdown.Markdown(extensions = ['meta'])
                md.convert(text)
                if not md.Meta.has_key("category"):
                    continue
                category = md.Meta["category"]
                title = md.Meta["title"]
                path = path.replace(directory+"/", "", 1)
                page_item = "    - ['" + path + "', '"+ category[0] + "', '" + title[0] + "']"
                print("Add:", page_item)
                list_item = (title[0], path)
                toc[category[0]].append(list_item)
                fp.write(page_item+"\n")
    fp.close()

    index = u'''<!--Meta
title:
category:首页
DO NOT Delete Meta Above-->

<div class="minecraft clearfix">\n
'''
    for k, v in toc.items():
        item_count = 0
        cate = u'<div class="section section-api">'
        head = '\t<h3>' + k + '<h3>\n'
        cate += head
        cate += '\t<ul class="list-unstyled">\n'
        for item in v:
            if 0 == len(item[0]):
                continue
            cate += '\t\t<li><a href="' + item[1][:-3]+ '">' + item[0]+ '</a></li>\n'
            item_count += 1
        cate += '\t</ul>\n'
        cate += '\t</div>\n'
        if 0 == item_count:
            cate = u''
        index += cate
    index += '</div>\n'

    fp = codecs.open("docs/index.md", mode="w", encoding="utf-8")
    fp.write(index)
    fp.close()
