
# 📘 GitHub README.md Description

```md
# 🚀 Advanced PDF Manager Pro

A powerful **Python-based PDF management tool** that supports both **Graphical User Interface (GUI)** and **Command Line Interface (CLI)** for flexible usage.

This project allows users to efficiently perform common PDF operations like merging, splitting, and rotating files with a clean and modern interface.

---

## ✨ Features

- 📄 Merge multiple PDF files into a single document  
- ✂️ Split PDF files into individual pages  
- 🔄 Rotate PDF pages (90°, 180°, 270°)  
- 🖥️ Dual Mode Support:
  - GUI Mode (Tkinter + ttkbootstrap)
  - CLI Mode (argparse-based automation)
- ⚡ Lightweight and fast processing using `pypdf`
- 🧩 Modular architecture (separated logic & UI)
- 🧪 Includes test scripts for validation

---

## 🛠️ Tech Stack

- Python 3.x  
- Tkinter (GUI)  
- ttkbootstrap (Modern UI styling)  
- pypdf (PDF manipulation)  
- argparse (CLI support)  
- reportlab (test PDF generation)

---

## 📂 Project Structure

```

main.py           # CLI entry point
gui.py            # GUI application
merger.py         # PDF processing logic
test.py           # Unit testing script

````

---

## 🚀 How to Run

### ▶️ GUI Mode
```bash
python main.py
````

### 💻 CLI Mode

Merge PDFs:

```bash
python main.py file1.pdf file2.pdf -o output.pdf
```

Split PDF:

```bash
python main.py --split file.pdf -o output_folder
```

Rotate PDF:

```bash
python main.py --rotate 90 file.pdf -o rotated.pdf
```

---

## 🧠 What I Learned

* Building desktop applications in Python
* Working with PDF manipulation libraries
* Designing CLI + GUI hybrid systems
* Writing modular and reusable code
* Handling file operations efficiently

---

## 📌 Future Improvements

* Add drag & drop support
* Add PDF compression feature
* Add OCR-based text extraction
* Cloud integration for file storage

---

## 👨‍💻 Author

**Zain ul Abideen** – Computer Science Student & Python Developer

---

## 📜 License

This project is open-source and free to use for learning purposes.

```

---

If you want, I can also:
✅ :contentReference[oaicite:0]{index=0}  
✅ Or :contentReference[oaicite:1]{index=1}  
✅ Or :contentReference[oaicite:2]{index=2}
```
