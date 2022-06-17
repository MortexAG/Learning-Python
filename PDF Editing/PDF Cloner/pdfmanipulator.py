import PyPDF2
#Enter The PDF Name
print("Type the Name of The pdf file to Make a copy from")
pdffirst = input()
pdforiginal = (pdffirst + ".pdf")
#Enter The Resulting pdf Name
print("Enter The Resulting Pdf Name")
pdfresult = input()
pdfnew = (pdfresult + ".pdf")
# Copy All Pages of the PDF
pdffileobj = open(pdforiginal, "rb")
pdfreader = PyPDF2.PdfFileReader(pdffileobj)
pdfwrite = PyPDF2.PdfFileWriter()
pagesnumber = pdfreader.numPages
for pagesnum in range(pagesnumber):
    pdfwrite.addPage(pdfreader.getPage(pagesnum))
# Creat the New PDf
pdfoutputfile = open(pdfnew, "wb")
pdfwrite.write(pdfoutputfile)
pdfoutputfile.close()
pdffileobj.close()
