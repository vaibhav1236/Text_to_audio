import pyttsx3
import PyPDF2
book=open("data.pdf",'rb')
pdfreader=PyPDF2.PdfFileReader(book)
pages=pdfreader.numPages
print(pages)
speaker=pyttsx3.init()
for num in range(500):
    page=pdfreader.getPage(num)
    text=page.extractText()
    speaker.say(text)
    speaker.runAndWait()

