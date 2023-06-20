from pathlib import Path
import importlib
import borb.pdf
from borb.pdf import Document
from borb.pdf import Page
from borb.pdf import SingleColumnLayout
from borb.pdf import Paragraph
from borb.pdf import PDF
# create an empty Document
pdf = Document()
name = "：測試"

# add an empty Page
page = Page()
pdf.add_page(page)

# use a PageLayout (SingleColumnLayout in this case)
layout = SingleColumnLayout(page)

# add a Paragraph object
layout.add(Paragraph("Hello World!"))
layout.add(Paragraph("就是"))

# store the PDF
with open(Path("20230620.pdf"), "wb") as pdf_file_handle:
    PDF.dumps(pdf_file_handle, pdf)