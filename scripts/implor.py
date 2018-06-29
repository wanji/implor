#!/usr/bin/env python
# coding: utf-8
"""
   File Name: image_viewer.py
      Author: Wan Ji
      E-mail: wanji@live.com
  Created on: Sun 04 Jun 2017 10:29:34 PM CST
 Description:
"""
import os
import sys
from flask import Flask, request    # , redirect


app = Flask(__name__)


def gen_img_html(name, img_names, start, num, width=0, height=0):
    num_images = len(img_names)
    has_prev = start > 0
    has_next = start + num < num_images

    html = """
    <style>
        div.img_holder figure
        {
            float: left;
        }
    </style>
    """

    size_params = ""
    size_params += "&h={}".format(height) if height > 0 else ""
    size_params += "&w={}".format(width) if width > 0 else ""

    head_html = ""

    if has_prev:
        prev_start = max(start - num, 0)
        prev_num = num
        prev_href = "/{}?s={}&n={}{}".format(name, prev_start, prev_num,
                                             size_params)
        head_html += "<a href='{}'>Prev</a>".format(prev_href)
    else:
        head_html += "Prev"

    head_html += "&nbsp|&nbsp"

    if has_next:
        next_start = start + num
        next_num = num  # min(num, num_images - start - num)
        next_href = "/{}?s={}&n={}{}".format(name, next_start, next_num,
                                             size_params)
        head_html += "<a href='{}'>Next</a>".format(next_href)
    else:
        head_html += "Next"

    head_html += "&nbsp&nbsp{}&nbsp-&nbsp{}".format(start, start+num-1)

    html += head_html
    html += "<hr />"

    for img_id, img_name in enumerate(img_names[start:start+num]):
        img_url = "/static/{}/{}".format(name, img_name)
        img_html = "<img src='{}' title='{}' {} {} />\n".format(
            img_url, img_name,
            "height={}".format(height) if height > 0 else "",
            "width={}".format(width) if width > 0 else "")
        cap_html = "<a href='{}'><figcaption>{}</figcaption></a>".format(
            img_url, img_name)
        if has_next:
            img_html = "<a href='{}'>{}</a>".format(next_href, img_html)
        img_html = """
        <div class='img_holder'>
            <figure>{}{}</figure>
        </div>""".format(
            img_html, cap_html)
        html += img_html
    # html += "<hr />"
    # html += head_html
    return html


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def image_viewer(path=None):
    if path == 'favicon.ico':
        return ""

    img_dir = os.path.join(os.getcwd(), "static", "" if path is None else path)
    img_names = sorted([img_name for img_name in os.listdir(img_dir)
                        if img_name.split(".")[-1].lower()
                        in ['jpg', 'png', 'jpeg']])
    if len(img_names) == 0:
        list_html = ""
        for d in os.listdir(img_dir):
            href = "/".join([path, d]) if path != "" else d
            list_html += "<a href='/{}'>{}</a><br>".format(href, d)
        return list_html

    start = int(request.args.get('s', '0'))
    num = int(request.args.get('n', '1'))
    width = int(request.args.get('w', '0'))
    height = int(request.args.get('h', '0'))

    return gen_img_html(path, img_names, start, num, width=width, height=height)

if __name__ == "__main__":
    app.run(host=sys.argv[1], port=int(sys.argv[2]))
