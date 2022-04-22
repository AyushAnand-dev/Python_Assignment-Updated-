import PyPDF2
import csv

a = PyPDF2.PdfFileReader('File.pdf')
# print(a.getNumPages())
string = ""


for i in range(a.getNumPages()):
    string += a.getPage(i).extractText()
# print(string)
with open("text1.txt", "w", encoding='utf-8') as f:
    f.write(string)
