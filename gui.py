import tkinter as tk
from tkinter import filedialog, messagebox
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import os
from merger import PDFManager

class PDFApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Advanced PDF Manager")
        self.root.geometry("800x600")
        
        # Apply a modern theme
        # Available themes: cosmo, flatly, journal, literal, lumen, minty, pulse, sandstone, united, yeti, darkly, cyborg, superhero, solar, vapor
        self.style = ttk.Style(theme="superhero") 
        
        self.manager = PDFManager()
        self.files = []
        
        self.create_widgets()

    def create_widgets(self):
        # Main Container with padding
        main_container = ttk.Frame(self.root, padding="20")
        main_container.pack(fill=BOTH, expand=True)

        # Header
        header_frame = ttk.Frame(main_container)
        header_frame.pack(fill=X, pady=(0, 20))
        
        title_lbl = ttk.Label(
            header_frame, 
            text="PDF MANAGER PRO", 
            font=("Helvetica", 24, "bold"),
            bootstyle="primary"
        )
        title_lbl.pack(side=LEFT)

        # Content Area - Split into Left (List) and Right (Actions)
        content_frame = ttk.Frame(main_container)
        content_frame.pack(fill=BOTH, expand=True)

        # --- Left Side: File List ---
        left_frame = ttk.Labelframe(content_frame, text="Selected Files", padding="15", bootstyle="info")
        left_frame.pack(side=LEFT, fill=BOTH, expand=True, padx=(0, 10))

        # Listbox with Scrollbar
        list_container = ttk.Frame(left_frame)
        list_container.pack(fill=BOTH, expand=True)

        self.file_listbox = tk.Listbox(
            list_container, 
            selectmode=tk.EXTENDED, 
            font=("Consolas", 10),
            bg="#2b3e50", # Dark background for listbox to match superhero theme feel
            fg="white",
            relief="flat",
            bd=0,
            highlightthickness=1,
            highlightbackground="#4e5d6c"
        )
        self.file_listbox.pack(side=LEFT, fill=BOTH, expand=True)
        
        scrollbar = ttk.Scrollbar(list_container, orient=VERTICAL, command=self.file_listbox.yview)
        scrollbar.pack(side=RIGHT, fill=Y)
        self.file_listbox.config(yscrollcommand=scrollbar.set)

        # File List Controls (Add/Remove/Clear)
        list_controls = ttk.Frame(left_frame, padding=(0, 10, 0, 0))
        list_controls.pack(fill=X)

        ttk.Button(list_controls, text="Add Files", bootstyle="success", command=self.add_files).pack(side=LEFT, padx=2)
        ttk.Button(list_controls, text="Remove", bootstyle="danger-outline", command=self.remove_files).pack(side=LEFT, padx=2)
        ttk.Button(list_controls, text="Clear", bootstyle="secondary-outline", command=self.clear_files).pack(side=LEFT, padx=2)
        
        ttk.Button(list_controls, text="↓", bootstyle="link", command=self.move_down).pack(side=RIGHT)
        ttk.Button(list_controls, text="↑", bootstyle="link", command=self.move_up).pack(side=RIGHT)

        # --- Right Side: Operations ---
        right_frame = ttk.Labelframe(content_frame, text="Operations", padding="15", bootstyle="warning", width=250)
        right_frame.pack(side=RIGHT, fill=BOTH, padx=(10, 0))
        
        # Operation Buttons
        ttk.Label(right_frame, text="Main Actions", font=("Helvetica", 10, "bold"), bootstyle="secondary").pack(anchor=W, pady=(0, 5))
        
        merge_btn = ttk.Button(
            right_frame, 
            text="MERGE FILES", 
            bootstyle="primary", 
            width=20,
            command=self.merge_files
        )
        merge_btn.pack(pady=5, fill=X)
        
        ttk.Separator(right_frame, bootstyle="secondary").pack(fill=X, pady=15)
        
        ttk.Label(right_frame, text="Single File Actions", font=("Helvetica", 10, "bold"), bootstyle="secondary").pack(anchor=W, pady=(0, 5))

        split_btn = ttk.Button(
            right_frame, 
            text="Split Selection", 
            bootstyle="info-outline", 
            width=20,
            command=self.split_file
        )
        split_btn.pack(pady=5, fill=X)

        # Rotation Controls
        rotate_frame = ttk.Labelframe(right_frame, text="Rotate Pages", padding="10", bootstyle="secondary")
        rotate_frame.pack(pady=15, fill=X)

        self.rotate_var = tk.IntVar(value=90)
        
        r90 = ttk.Radiobutton(rotate_frame, text="90°", variable=self.rotate_var, value=90, bootstyle="info-toolbutton")
        r90.pack(side=LEFT, expand=True, padx=2)
        r180 = ttk.Radiobutton(rotate_frame, text="180°", variable=self.rotate_var, value=180, bootstyle="info-toolbutton")
        r180.pack(side=LEFT, expand=True, padx=2)
        r270 = ttk.Radiobutton(rotate_frame, text="270°", variable=self.rotate_var, value=270, bootstyle="info-toolbutton")
        r270.pack(side=LEFT, expand=True, padx=2)
        
        rotate_btn = ttk.Button(
            rotate_frame, 
            text="Apply Rotation", 
            bootstyle="warning-outline", 
            command=self.rotate_file
        )
        rotate_btn.pack(fill=X, pady=(10, 0))

        # Status Bar
        self.status_var = tk.StringVar(value="Ready")
        status_bar = ttk.Label(main_container, textvariable=self.status_var, bootstyle="secondary", font=("Helvetica", 9))
        status_bar.pack(side=BOTTOM, fill=X, pady=(10, 0), anchor=W)

    def update_status(self, message):
        self.status_var.set(message)
        self.root.update_idletasks()

    def add_files(self):
        filenames = filedialog.askopenfilenames(filetypes=[("PDF Files", "*.pdf")])
        if filenames:
            count = 0
            for f in filenames:
                if f not in self.files:
                    self.files.append(f)
                    self.file_listbox.insert(tk.END, os.path.basename(f))
                    count += 1
            self.update_status(f"Added {count} files.")

    def remove_files(self):
        selection = self.file_listbox.curselection()
        if not selection: return
        for index in reversed(selection):
            self.file_listbox.delete(index)
            del self.files[index]
        self.update_status("Removed selected files.")

    def clear_files(self):
        self.files = []
        self.file_listbox.delete(0, tk.END)
        self.update_status("Cleared all files.")

    def move_up(self):
        selection = self.file_listbox.curselection()
        if not selection: return
        for i in selection:
            if i == 0: continue
            text = self.file_listbox.get(i)
            self.file_listbox.delete(i)
            self.file_listbox.insert(i-1, text)
            self.files[i], self.files[i-1] = self.files[i-1], self.files[i]
            self.file_listbox.selection_set(i-1)

    def move_down(self):
        selection = self.file_listbox.curselection()
        if not selection: return
        for i in reversed(selection):
            if i == self.file_listbox.size() - 1: continue
            text = self.file_listbox.get(i)
            self.file_listbox.delete(i)
            self.file_listbox.insert(i+1, text)
            self.files[i], self.files[i+1] = self.files[i+1], self.files[i]
            self.file_listbox.selection_set(i+1)

    def merge_files(self):
        if not self.files:
            messagebox.showwarning("Warning", "No files to merge!", parent=self.root)
            return
        
        output = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF Files", "*.pdf")])
        if output:
            self.update_status("Merging...")
            success, msg = self.manager.merge_pdfs(self.files, output)
            if success:
                messagebox.showinfo("Success", msg, parent=self.root)
                self.update_status(f"Merged {len(self.files)} files.")
            else:
                messagebox.showerror("Error", msg, parent=self.root)
                self.update_status("Merge failed.")

    def split_file(self):
        selection = self.file_listbox.curselection()
        if not selection:
            messagebox.showwarning("Warning", "Please select a file to split.", parent=self.root)
            return
        
        if len(selection) > 1:
            messagebox.showwarning("Warning", "Please select only one file to split.", parent=self.root)
            return

        file_to_split = self.files[selection[0]]
        output_dir = filedialog.askdirectory(title="Select Output Directory for Split Pages")
        
        if output_dir:
            self.update_status("Splitting...")
            success, msg = self.manager.split_pdf(file_to_split, output_dir)
            if success:
                messagebox.showinfo("Success", msg, parent=self.root)
                self.update_status("Split complete.")
            else:
                messagebox.showerror("Error", msg, parent=self.root)
                self.update_status("Split failed.")

    def rotate_file(self):
        selection = self.file_listbox.curselection()
        if not selection:
            messagebox.showwarning("Warning", "Please select a file to rotate.", parent=self.root)
            return
            
        file_to_rotate = self.files[selection[0]]
        rotation = int(self.rotate_var.get())
        
        output = filedialog.asksaveasfilename(
            defaultextension=".pdf",
            filetypes=[("PDF Files", "*.pdf")],
            initialfile=f"rotated_{os.path.basename(file_to_rotate)}"
        )
        
        if output:
            self.update_status("Rotating...")
            success, msg = self.manager.rotate_pdf(file_to_rotate, output, rotation)
            if success:
                messagebox.showinfo("Success", msg, parent=self.root)
                self.update_status("Rotation complete.")
            else:
                messagebox.showerror("Error", msg, parent=self.root)
                self.update_status("Rotation failed.")

def run_gui():
    # Use ttkbootstrap Window instead of standard Tk
    # themename can be set to different themes: superhero, darkly, flatly, cosmo, etc.
    root = ttk.Window(themename="superhero")
    app = PDFApp(root)
    root.mainloop()

if __name__ == "__main__":
    run_gui()
