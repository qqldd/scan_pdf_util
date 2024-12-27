# Merging Double-Sided Scanned PDFs with Reversed Back Pages 

 Merge two PDFs from scanner without duplex ability like Epson-3850

 The scanner with ADF but without duplex feature will generate have two PDFs:
 * PDF 1 (front.pdf): Contains the front sides of the pages (1, 3, 5, ...).
 * PDF 2 (back.pdf): Contains the back sides of the pages in reverse order (..., 6, 4, 2).
 The goal is to create a single PDF with the correct page order (1, 2, 3, 4, 5, 6, ...).

# Tool Include

`pdf_merger.py`: Merge and rename two PDFs with Gemini API.

`pdf_renamer.py`: Rename signle PDF. After scan single page PDF, the name is random from scanner. This tool uses Gemini API to analysis the PDF and reanme it.

To use Gemini feature, a file called `gemini_api.key` needs to be provided in the same folder as the script.

