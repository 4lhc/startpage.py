#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  startpage.py
#
#  author : shelldoor
#  email  : echo $(base64 -d <<< NDQ0bGhjCg==)@gmail.com
#  date   : Sat 08 Nov 2014 02:06:33 IST
#  ver    : 0.0.1

#todo :
#       * rss ticker, search engines


import json

###configs###
new_tab = not True #open urls in newtab?
life_purpose = True #

###end of configs###


links = "data/links.json"
out_htm = "index.html"
htm_p1 = "data/part-1.html"
htm_p2 = "data/part-2.html"
tb = 'target="_blank"'
if not new_tab:
    tb = ''



with open(links, 'rb') as fp:
    link_dict = json.loads(fp.read().decode('utf-8'))

dict_list = [""] * link_dict.__len__()


for item in link_dict:
    id = link_dict[item]['id']
    htm = """   <div id="category{}">
      <h3>{}</h3>
         <ul>\n""".format(id, item)

    for key, value in link_dict[item]['links'].items():
        htm += """            <li><a {} href="{}">{}</a></li>\n""".format(tb, value, key)
    htm += """         </ul>
    </div>\n"""
    dict_list[id-1] = htm
#print("<!--" + "---"*15 + "-->")
#print("".join(dict_list))
with open(htm_p1, 'r') as p1, open(htm_p2, 'r') as p2:
    htm = p1.read() + "".join(dict_list) + p2.read()

with open(out_htm, 'w') as fp:
    fp.write(htm)

