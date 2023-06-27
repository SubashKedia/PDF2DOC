from pdf2docx import Converter

old_pdf = "Assignment_7.pdf"
new_doc = "Assignment_7.docx"

obj = Converter(old_pdf)
obj.convert(new_doc)
obj.close()