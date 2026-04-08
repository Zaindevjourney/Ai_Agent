import argparse
import sys
import os
from merger import PDFManager
from gui import run_gui

def main():
    parser = argparse.ArgumentParser(description="Advanced PDF Manager Tool")
    
    # Mode selection
    group = parser.add_mutually_exclusive_group()
    group.add_argument("--merge", action="store_true", help="Merge mode (default if multiple inputs provided)")
    group.add_argument("--split", action="store_true", help="Split mode")
    group.add_argument("--rotate", type=int, choices=[90, 180, 270], help="Rotate mode (degrees)")
    
    parser.add_argument("-o", "--output", help="Output file or directory")
    parser.add_argument("inputs", nargs="*", help="Input PDF files")

    args = parser.parse_args()

    # If no inputs provided, switch to GUI
    if not args.inputs:
        print("No arguments detected. Launching GUI...")
        run_gui()
        return

    manager = PDFManager()

    # CLI Logic
    try:
        if args.rotate:
            if len(args.inputs) != 1:
                print("Error: Rotate mode requires exactly one input file.")
                return
            
            output = args.output
            if not output:
                base, ext = os.path.splitext(args.inputs[0])
                output = f"{base}_rotated_{args.rotate}{ext}"
            
            success, msg = manager.rotate_pdf(args.inputs[0], output, args.rotate)
            print(msg)

        elif args.split:
            if len(args.inputs) != 1:
                print("Error: Split mode requires exactly one input file.")
                return
            
            output = args.output if args.output else os.getcwd()
            success, msg = manager.split_pdf(args.inputs[0], output)
            print(msg)

        else:
            # Default to merge
            if len(args.inputs) < 2:
                print("Error: Merge mode requires at least two input files.")
                return
            
            output = args.output
            if not output:
                output = "merged_output.pdf"
            if not output.lower().endswith('.pdf'):
                output += '.pdf'
                
            success, msg = manager.merge_pdfs(args.inputs, output)
            print(msg)
            
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nOperation cancelled by user.")
    except Exception as e:
        import traceback
        traceback.print_exc()
        print(f"\nAn unexpected error occurred: {e}")


