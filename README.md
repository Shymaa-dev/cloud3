# ☁️ Cloud Document Analyzer

A cloud-based document analytics system for uploading, sorting, searching, and classifying large collections of PDF and Word documents.  
Developed as part of the **Cloud and Distributed Systems (SICT 4313)** course at the **Islamic University of Gaza**.

> 🔬 Designed with a modular architecture and deployed on PythonAnywhere using Flask and Python 3.

---

## 🔗 Live Demo

Access the live application:  
🌍 [https://shaima1.pythonanywhere.com/](https://shaima1.pythonanywhere.com/)

---

## 📌 Key Features

- 📂 **Upload Documents**  
  Upload `.pdf`, `.docx`, or `.doc` files through an intuitive web interface. Files are securely stored in a cloud directory.

- 🧠 **Automatic Title Extraction & Sorting**  
  Extracts the first meaningful line of each document and displays them in alphabetical order.

- 🔍 **Full-Text Keyword Search**  
  Search across all uploaded documents using custom keywords. Results show matched text with **highlighting**.

- 🧭 **Smart Document Classification**  
  Automatically classifies documents based on a keyword-matching tree into categories like `Finance`, `Legal`, `Education`, `Technology`, and `Health`.

- 📊 **Statistics Dashboard**  
  Real-time system stats, including:
  - Total number of files
  - Combined file size
  - Time taken for sorting, searching, and classification

---

## 🛠️ Tech Stack

| Layer            | Technology                                |
|------------------|--------------------------------------------|
| Language         | Python 3.13                                |
| Web Framework    | Flask 3.1.1                                |
| Frontend         | HTML + Flask Templates                     |
| PDF Parser       | PyMuPDF (`fitz`)                           |
| Word Parser      | `docx2txt`, `python-docx`                  |
| Storage Model    | File-based storage (NoSQL-style JSON)      |
| Hosting Platform | [PythonAnywhere](https://www.pythonanywhere.com/) |

---

## 📁 Project Structure
project/
│
├── main.py # Flask app entry point
├── /templates/ # HTML pages for GUI
├── /services/ # Functional modules
│ ├── file_handler.py # Upload & text extraction
│ ├── search_engine.py # Keyword search
│ ├── classify.py # Document classification
│ └── stats.py # System statistics
├── /storage/
│ ├── documents/ # Uploaded files
│ └── classifications.json # Classification metadata
---  
You can find visuals of the following:
- Upload form
- Keyword search results with highlights
- Category classification view
- System statistics dashboard

--
## 📸 Screenshots
1.Home Page: Overview and entry point to functionalities.
https://github.com/Shymaa-dev/cloud3/blob/6fe4f168d472cfa96ee41f1fe339cb63df57689b/Screenshot_%D9%A2%D9%A0%D9%A2%D9%A5%D9%A0%D9%A6%D9%A2%D9%A6-%D9%A1%D9%A1%D9%A3%D9%A0%D9%A1%D9%A1_Chrome.jpg
2.Upload Page: Form to upload documents, with client-side file validation.
3.Documents Page: Lists documents sorted by title.
4.Search Page: Input field and search results with matched lines.
5.Classify Page: Button to trigger classification and display categorized documents.
6.Categories Page: Predefined category definitions and their respective files.
7.Statistics Page: Displays number of files, total size, and processing durations.
## 🚀 Deployment

This application is deployed on **PythonAnywhere**, a cloud PaaS for Python-based applications.

### Deployment Highlights:
- Persistent cloud storage
- Public web access via Flask + WSGI
- All file operations sandboxed to secure directories
- Fully functional via browser—no local installation required

---

## 🧪 Testing Summary

| Test Item                 | Result                      |
|---------------------------|------------------------------|
| Number of Documents       | 20                           |
| File Types Tested         | PDF, DOCX                    |
| Upload & Storage          | ✅ Successful                |
| Title Extraction & Sort   | ✅ Accurate                  |
| Keyword Search            | ✅ Highlighted Matches       |
| Classification Accuracy   | ✅ Correct Category Mapping  |
| Stats Generation          | ✅ Real-time Display         |

---

## 💡 Future Enhancements

- 🔐 Add user authentication and access control
- 🌍 Integrate a web scraper for dynamic document collection
- 💾 Use a scalable NoSQL database like Firebase or MongoDB
- 📈 Build a full analytics dashboard with visual charts and trends

---

## 👩‍💻 Developer Info

**👤 Shaima Maher Ismail Al Khozondar**  
Computer Science Department  
Islamic University of Gaza  

---

## 📜 License

This project is developed for academic purposes as part of university coursework.  
All rights reserved © 2025.

---
