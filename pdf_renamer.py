import base64
import os
import sys
import google.generativeai as genai

def genai_filename(input_pdf):
    output = input_pdf
    gemini_key_file = "gemini_api.key"
    if not os.path.isfile("gemini_api.key"):
        print(f"No {gemini_key_file}, return original name.")
        return output
    
    with open("gemini_api.key", "r") as f:
        gemini_key = f.read()
    genai.configure(api_key=gemini_key)
    model = genai.GenerativeModel("gemini-1.5-flash")
    with open(input_pdf, "rb") as doc_file:
        doc_data = base64.standard_b64encode(doc_file.read()).decode("utf-8")
        prompt = "Just return the best file name for this document under 10 words with pdf extension within one line"
        response = model.generate_content([{'mime_type': 'application/pdf', 'data': doc_data}, prompt])
        print("GenAI renamed pdf name: ", response.text)
        output=response.text
    return output


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: Drag and drop ONE PDF files onto this executable.")
        print("Or run from command line: script.exe <input.pdf>")
        input("Press Enter to exit...")
        sys.exit(1)

    input_pdf = sys.argv[1]

    if not os.path.exists(input_pdf):
        print(f"Error: Input PDF file does not exist: {input_pdf}")
        input("Press Enter to exit...")
        sys.exit(1)

    try:
        renamed_pdf_name = genai_filename(input_pdf)
        full_renamed_path = os.path.join(os.path.dirname(input_pdf), renamed_pdf_name.strip())
        os.rename(input_pdf, full_renamed_path)

        print(f"PDFs renamed to: {renamed_pdf_name}")
        input("Press Enter to exit...")
    except Exception as e:
        print(f"An error occurred: {e}")
        input("Press Enter to exit...")
        sys.exit(1)