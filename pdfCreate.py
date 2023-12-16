#Tutorial: https://blog.aspose.com/pdf/create-pdf-files-in-python/
#Installation: pip install aspose-pdf

import aspose.pdf as ap

# Initialize document object
document = ap.Document()

# Add page
page = document.pages.add()

# Initialize textfragment object
text_fragment = ap.text.TextFragment("Hello, world!")

# Add text fragment to new page
page.paragraphs.add(text_fragment)

# Save updated PDF
document.save("output.pdf")