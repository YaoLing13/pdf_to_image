### Time: 20190904
### Author: YaoLing
### Des: pdf convert to jpg

# -*- coding: UTF-8 -*-

from pdf2image import convert_from_path ## pip install pdf2image  or pip install --user pdf2image

pdf_name = "/home/yl/1.pdf"
jpg_name =pdf_name[:-4]+'.jpg'

pages = convert_from_path(pdf_name, 500)
for page in pages:
    page.save(jpg_name, 'JPEG')

