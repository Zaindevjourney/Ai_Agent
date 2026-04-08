from pypdf import PdfWriter, PdfReader
import os

class PDFManager:
    def __init__(self):
        pass

    def merge_pdfs(self, input_paths, output_path):
        """
        Merges multiple PDF files into a single PDF.
        """
        merger = PdfWriter()
        
        for path in input_paths:
            if not os.path.exists(path):
                print(f"Warning: File not found: {path}")
                continue
            try:
                merger.append(path)
                print(f"Added: {path}")
            except Exception as e:
                print(f"Error adding {path}: {e}")

        try:
            with open(output_path, "wb") as f_out:
                merger.write(f_out)
            print(f"Successfully merged {len(input_paths)} files into {output_path}")
            return True, f"Successfully merged items into {output_path}"
        except Exception as e:
            return False, f"Error saving output file: {e}"
        finally:
            merger.close()

    def split_pdf(self, input_path, output_dir):
        """
        Splits a PDF into individual pages.
        """
        if not os.path.exists(input_path):
            return False, "Input file not found."
            
        try:
            reader = PdfReader(input_path)
            base_name = os.path.splitext(os.path.basename(input_path))[0]
            
            if not os.path.exists(output_dir):
                os.makedirs(output_dir)

            for i, page in enumerate(reader.pages):
                writer = PdfWriter()
                writer.add_page(page)
                output_filename = f"{base_name}_page_{i+1}.pdf"
                output_path = os.path.join(output_dir, output_filename)
                
                with open(output_path, "wb") as f_out:
                    writer.write(f_out)
            
            return True, f"Successfully split into {len(reader.pages)} pages in {output_dir}"
        except Exception as e:
            return False, f"Error splitting PDF: {e}"

    def rotate_pdf(self, input_path, output_path, rotation):
        """
        Rotates all pages in a PDF by the specified angle (90, 180, 270).
        """
        if not os.path.exists(input_path):
            return False, "Input file not found."
            
        try:
            reader = PdfReader(input_path)
            writer = PdfWriter()

            for page in reader.pages:
                writer.add_page(page)
                writer.pages[-1].rotate(rotation)

            with open(output_path, "wb") as f_out:
                writer.write(f_out)
                
            return True, f"Successfully rotated PDF and saved to {output_path}"
        except Exception as e:
            return False, f"Error rotating PDF: {e}"
