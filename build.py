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

    if not os.path.exists("docs/index"):
        os.makedirs("docs/index")

    fpmkdocs = codecs.open("mkdocs.yml", mode="a+", encoding="utf-8")
    directory = u"docs"
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
                if category[0] == u"index":
                    continue
                path = path.replace(directory+"/", "", 1)
                print(path, category, title)
                page_item = u"    - ['" + unicode(path) + u"', '"+ category[0] + u"', '" + title[0] + u"']"
                print("Add:", page_item)
                list_item = (title[0], path)
                toc[category[0]].append(list_item)
                fpmkdocs.write(page_item+"\n")

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


    #create index.md of catory
    for k, v in toc.items():
        if k == u'首页':
            page_item = "    - ['" + "index.md" + "', '"+ "index" + "', '" + k + "']"
            print("Add:", page_item)
            fpmkdocs.write(page_item+"\n")
            continue
        indexfile="docs/index/"+k+".md"
        relativepath ="index/"+k+".md"
        index = u'''<!--Meta
title:{}
category:index
DO NOT Delete Meta Above-->

<div class="minecraft clearfix">\n
'''
        index = index.format(k)
        cate = '<div class="section section-api">\n'
        head = '\t<h3>' + k + '<h3>\n'
        cate += head
        cate += '\t<ul class="list-unstyled">\n'
        for item in v:
            if 0 == len(item[0]):
                continue
            cate += '\t\t<li><a href="/' + item[1][:-3]+ '">' + item[0]+ '</a></li>\n'
            item_count += 1
        cate += '\t</ul>\n'
        cate += '\t</div>\n'
        if 0 == item_count:
            cate = u''
        index += cate
        index += '</div>\n'
        index += '</div>\n'

        page_item = "    - ['" + relativepath + "', '"+ "index" + "', '" + k + "']"
        print("Add:", page_item)
        fpmkdocs.write(page_item+"\n")

        fp = codecs.open(indexfile, mode="w", encoding="utf-8")
        fp.write(index)
        fp.close()

    fp.close()
