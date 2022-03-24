
import io
from PIL import Image

import pymupdf

file = "/home/paindr/PycharmProjects/pythonProject1/crt anonymisation.pdf"

# jonas ici on ouvre le fichier pdf
pdf_file = fitz.open(file)

# on itere dans le pdfs
for page_index in range(len(pdf_file)):


    page = pdf_file[page_index]
    image_list = page.getImageList()


    if image_list:
        print(f"[+]il y a   {len(image_list)} images isur la page {page_index}")
    else:
        print("[il n'y a aucune image dur la page", page_index)
    for image_index, img in enumerate(page.getImageList(), start=1):

        xref = img[0]
        print(xref)

        base_image = pdf_file.extractImage(xref)
        image_bytes = base_image["image"]


        image_ext = base_image["ext"]
