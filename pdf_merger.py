import sys
import os
from pypdf import PdfReader, PdfWriter
from pdf_renamer import genai_rename

def reverse_pdf(input_path, output_path):
    reader = PdfReader(input_path)
    writer = PdfWriter()
    for page_num in range(len(reader.pages) - 1, -1, -1):
        page = reader.pages[page_num]
        writer.add_page(page)
    with open(output_path, "wb") as outfile:
        writer.write(outfile)

def interleave_pdfs(pdf1_path, pdf2_path, output_path):
    pdf1 = PdfReader(pdf1_path)
    pdf2 = PdfReader(pdf2_path)
    writer = PdfWriter()
    min_len = min(len(pdf1.pages), len(pdf2.pages))
    for i in range(min_len):
        writer.add_page(pdf1.pages[i])
        writer.add_page(pdf2.pages[i])

    # Add remaining pages if one PDF is longer
    for i in range(min_len, len(pdf1.pages)):
        writer.add_page(pdf1.pages[i])
    for i in range(min_len, len(pdf2.pages)):
        writer.add_page(pdf2.pages[i])
    with open(output_path, "wb") as outfile:
        writer.write(outfile)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: Drag and drop TWO PDF files onto this executable.")
        print("Or run from command line: script.exe <front.pdf> <back.pdf>")
        input("Press Enter to exit...")
        sys.exit(1)

    front_pdf_path = sys.argv[1]
    back_pdf_path = sys.argv[2]

    if not os.path.exists(front_pdf_path) or not os.path.exists(back_pdf_path):
        print("Error: One or both input files do not exist.")
        input("Press Enter to exit...")
        sys.exit(1)

    try:
        reversed_back_pdf_path = "back_reversed.pdf"
        reverse_pdf(back_pdf_path, reversed_back_pdf_path)
        interleave_pdfs(front_pdf_path, reversed_back_pdf_path, "combined.pdf")
        os.remove(reversed_back_pdf_path)
        genai_rename("combined.pdf")

        print(f"PDFs merged successfully!")
        input("Press Enter to exit...")
    except Exception as e:
        print(f"An error occurred: {e}")
        input("Press Enter to exit...")
        sys.exit(1)

