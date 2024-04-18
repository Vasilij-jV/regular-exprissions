# -*- config: utf-8 -*-

import re

sample_html = ("<img src='https://example.com/image1.jpg'> <img src='http://example.com/image2.png'> <img "
               "src='https://example.com/image3.gif'> <img src='https://example.com/image4.jpeg'> <img "
               "src='https://example.com/image5.jpe'> <img src='https://example.com/image6.jeg'>")


def extract_image_text(text_html):
    extension = r'\.(\bpng|\bjpg|\bjpeg|\bgif)'

    list_link = re.split(r'\s', text_html)

    img_link = []
    for lnk in list_link:
        one_link = re.search(extension, lnk)
        if one_link is not None:
            cleaned_url = re.search(r'http(\w|\d|:|/|\.)+', lnk)
            img_link.append(cleaned_url.group())
    return img_link


image_links = extract_image_text(sample_html)

if image_links:
    for image_link in image_links:
        print(image_link)
else:
    print("Нет ссылок с картинками в HTML тексте.")
