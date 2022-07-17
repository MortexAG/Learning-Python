import docx2pdf
import os
from docx2pdf import convert
print("Please Make Sure there's only one word file in the folder wordfile")
input("Press Enter To Continue")
import glob
word_list = []
for filename in glob.glob('wordfile/*.docx'): #assuming docx
    wordfile = (filename)
    pdfname = "wordfile/" + filename + ".pdf"
    print(pdfname)
    pdf_pre = filename.replace('.docx','')
    pdffile = (pdf_pre + ".pdf")
#pdffile = ("wordfile/result.pdf")
convert(wordfile, pdffile)
convert("my_docx_folder/")
