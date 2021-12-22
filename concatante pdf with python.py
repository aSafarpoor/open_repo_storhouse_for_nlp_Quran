from PyPDF2 import PdfFileMerger, PdfFileReader

filename1 = 'nlp-lec-07.pdf' 
filename2 = 'nlp-lec-08.pdf'
filename3 = 'nlp-lec-09-10.pdf'
filename4 = 'nlp-lec-11-12.pdf'

merger = PdfFileMerger()

merger.append(PdfFileReader(open(filename1, 'rb')))
merger.append(PdfFileReader(open(filename2, 'rb')))
merger.append(PdfFileReader(open(filename3, 'rb')))
merger.append(PdfFileReader(open(filename4, 'rb')))


merger.write("merged.pdf")