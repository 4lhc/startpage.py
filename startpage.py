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
htm_p1 = """

<!DOCTYPE html>
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<title>start</title>

<link rel="stylesheet" type="text/css" href="css/search.css" />



</head>

<body>

<div id="page">

    <form target="_blank" id="searchForm" method="get" action="https://www.google.com/search">
        <fieldset>

            <input id="s" type="text" name="q" value=""/>

            <input type="submit" value="Submit" id="submitButton" />

            <ul class="icons">
                <li class="google" title="google" queryurl="https://www.google.com/search" >google</li>
                <li class="deviant" title="deviantart" queryurl="http://www.deviantart.com/browse/all/?q=">deviantart</li>
                <li class="imdb" title="IMDB" queryurl="http://www.imdb.com/find?s=all&q=">imdb</li>
                <li class="youtube" title="Youtube" queryurl="https://www.youtube.com/results?search_query=">youtube</li>
                <li class="torrentz" title="TorrentZ" queryurl="http://torrentz.com/search?q=">torrentz</li>
<!--                <li class="amazon" title="amazon" queryurl="http://www.amazon.in/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords=">Amazon.in</li>
-->
<!--                when adding more search engines, note to update their attributes in style.css too -->

            </ul>

        </fieldset>
    </form>
</div>


<section id="categoryhold" class="body">

"""
htm_p2 = """



</section>


<!-- It would be great if you leave the link back to the tutorial. Thanks! -->
<div id="con">
<div id="filler"> </div>
<p class="credit">
    <a id="orange" href="#">credits:</a>
    <a href="http://tutorialzine.com/2010/09/google-powered-site-search-ajax-jquery/">based on: tutorialzine</a>
    <a href="http://www.deviantart.com/art/KMay-Start-Page-184915031">design: defined04 @ deviantart</a>
    <a href="http://dakirby309.deviantart.com/art/Metro-UI-Icon-Set-725-Icons-280724102">icons by dAKirby309</a>
    <a href="https://github.com/4lhc">python and mods ~4lhc</a>
</p>
</div>
<script src="http://ajax.googleapis.com/ajax/libs/jquery/1.4.2/jquery.min.js"></script>
<script src="js/search.js"></script>

</body>
</html>
"""
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

htm = htm_p1 + "".join(dict_list) + htm_p2

with open(out_htm, 'w') as fp:
    fp.write(htm)

