import PyPDF2

# Create a PDF merger object
pdf_merger = PyPDF2.PdfMerger()

# Add the first PDF file to the merger
pdf_merger.append("1.pdf")

# Add the second PDF file to the merger
pdf_merger.append("2.pdf")

# Output merged PDF to a new file
pdf_merger.write("merged.pdf")

# Close the merger
pdf_merger.close()

