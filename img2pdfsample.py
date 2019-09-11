import img2pdf
from PIL import Image
import os

img_path="images"
pdf_path="pdffile/"

pdffile=open(pdf_path+"output.pdf","wb")
filelist=[]
for path,dir,files in os.walk(img_path):
    for file in files:
        filelist.append(img_path+"/"+file)
print(filelist)
#image=Image.open(img_path+"/"+file)
#print(img_path+"/"+file)
pdf_bytes=img2pdf.convert(filelist)
pdffile.write(pdf_bytes)
#image.close()
pdffile.close()
