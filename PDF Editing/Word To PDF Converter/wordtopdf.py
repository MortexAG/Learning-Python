import docx2pdf
from docx2pdf import convert
print("Type Word File Name Here")
word = input()
wordfile = (word + ".docx")
pdffile = (word + ".pdf")
convert(wordfile, pdffile)
convert("my_docx_folder/")