from encodings import utf_8
import PyPDF2

x = PyPDF2.PdfFileReader("eng.pdf")

#print(x.getNumPages())
#print(x.getDocumentInfo())
str=""
for i in range (0,6):
       str += x.getPage(i).extractText()
with open ("text.txt","w") as f :
    f.write(str)
