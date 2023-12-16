#Tutorial: https://stackoverflow.com/questions/3444645/merge-pdf-files
#Installation: pip install pypdf

from pypdf import PdfMerger

pdfs = ['pdf1-output.pdf', 'pdf2-output.pdf']

merger = PdfMerger()

for pdf in pdfs:
    merger.append(pdf)

merger.write("pdf3-compiled.pdf")
merger.close()