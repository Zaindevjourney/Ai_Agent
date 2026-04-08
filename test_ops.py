from pypdf import PdfWriter
import os
from merger import PDFManager

def create_dummy_pdf(filename):
    writer = PdfWriter()
    writer.add_blank_page(width=72, height=72)
    with open(filename, "wb") as f:
        writer.write(f)
    print(f"Created {filename}")

def test_manager():
    manager = PDFManager()
    
    # Setup
    f1 = "test1.pdf"
    f2 = "test2.pdf"
    create_dummy_pdf(f1)
    create_dummy_pdf(f2)
    
    # Test Merge
    output_merge = "merged_test.pdf"
    success, msg = manager.merge_pdfs([f1, f2], output_merge)
    print(f"Merge: {success} - {msg}")
    
    # Test Split
    output_split_dir = "split_output"
    success, msg = manager.split_pdf(output_merge, output_split_dir)
    print(f"Split: {success} - {msg}")
    
    # Test Rotate
    output_rotate = "rotated_test.pdf"
    success, msg = manager.rotate_pdf(f1, output_rotate, 90)
    print(f"Rotate: {success} - {msg}")

    # Cleanup (Optional)
    # os.remove(f1)
    # os.remove(f2)
    # os.remove(output_merge)
    # os.remove(output_rotate)

if __name__ == "__main__":
    test_manager()
