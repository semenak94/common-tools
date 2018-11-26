import os
import img2pdf

path_to_img = os.getcwd()
with open("result.pdf", "wb") as f:
    f.write(img2pdf.convert([i for i in os.listdir(path_to_img) if i.endswith(".jpg")]))
