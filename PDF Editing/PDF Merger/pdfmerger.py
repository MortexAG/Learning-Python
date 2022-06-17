import PyPDF2
print("Enter The Names of The First PDF")
pdf1 = input()
pdf1file = (pdf1 + ".pdf")
print("Enter The Names of The Second PDF")
pdf2 = input()
pdf2file = (pdf2 + ".pdf")
pdfs = [pdf1file, pdf2file]
merger = PyPDF2.PdfMerger()

for pdf in pdfs:
        merger.append(pdf)
merger.write("result.pdf")
merger.close()
input("Done Press Enter To Exit")