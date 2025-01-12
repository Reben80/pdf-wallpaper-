import fitz  # PyMuPDF
import os

def pdf_to_svg(pdf_file):
    # Get the directory and base name of the PDF file
    directory = os.path.dirname(pdf_file)
    base_name = os.path.splitext(os.path.basename(pdf_file))[0]
    # Define the output SVG file path
    output_svg = os.path.join(directory, f"{base_name}.svg")
    
    try:
        # Open the PDF file
        doc = fitz.open(pdf_file)
        
        # Extract the first page (or loop if needed for multiple pages)
        page = doc[0]  # First page (page numbers are zero-indexed)
        svg_content = page.get_svg_image()  # Get SVG content of the page
        
        # Write SVG content to the file
        with open(output_svg, 'w') as svg_file:
            svg_file.write(svg_content)
        
        print(f"SVG file saved as: {output_svg}")
        return output_svg
    
    except Exception as e:
        print(f"Error during conversion: {e}")
        return None

def convert_all_pdfs_to_svgs(base_path):
    sets = ['set1', 'set2', 'set3']
    
    for set_name in sets:
        set_path = os.path.join(base_path, set_name)
        for file_name in os.listdir(set_path):
            if file_name.endswith('.pdf'):
                pdf_file_path = os.path.join(set_path, file_name)
                pdf_to_svg(pdf_file_path)

# Define the base path to your directories
base_path = '/Users/Rebin/Documents/Wallapper_Group_Website/To Github/pdf'

# Convert all PDFs to SVGs
convert_all_pdfs_to_svgs(base_path)
