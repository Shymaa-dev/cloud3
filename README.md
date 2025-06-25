# Cloud Document Analyzer

A cloud-ready document management system to:
- Upload PDF and Word documents.
- Search and highlight keywords.
- Sort documents by extracted titles.
- Classify documents based on content.
- View document statistics.

## Technologies
- Python 3
- Flask
- PyMuPDF
- python-docx
- docx2txt


## Run the project local 

```bash
pip install -r requirements.txt
python app/main.py

Then visit: http://127.0.0.1:5000




Developing a Cloud-Based Service
for Basic Data Analytics


Project Access Information
This document presents the development report of the "Cloud Document Analyzer" project, implemented as part of the Cloud and Distributed Systems course.
The complete source code and live application are available through the following links:
🔗 Live Web Application: https://shaima1.pythonanywhere.com/
🔗 GitHub Repository: https://github.com/Shymaa-dev/cloud3.git



Abstract
This project, titled "Cloud Document Analyzer", presents the development of a cloud-based service designed for the management and analysis of document collections in PDF and Word formats. The program provides three core functionalities: document sorting based on extracted titles, keyword-based text search with result highlighting, and automatic document classification according to a predefined keyword-based classification tree. The platform also generates statistical insights about the documents, including storage size, number of documents, and time taken for each operation. All uploaded files are securely stored in a cloud directory and processed automatically to provide fast and efficient access to information.

The system was built using Python and the Flask web framework, and deployed on the PythonAnywhere cloud platform. The interface consists of HTML-based pages supporting file upload, searching, classification, and statistics viewing. This solution follows a modular design where functionality is encapsulated within dedicated components for file handling, searching, classification, and storage management. The program was built using a cloud-centric development methodology, emphasizing remote deployment, scalability, and ease of access. It is suitable for use in academic, legal, medical, and business contexts where bulk document processing and organization are essential.






1. Introduction
Cloud Document Analyzer is a lightweight yet powerful cloud-based program developed to automate the management of a large collection of PDF and Word documents. Its key features include document sorting by extracted titles, full-text keyword search with automatic highlighting, and classification based on topic-specific keywords. The program offers real-time insights into document metadata, such as size and count, and measures the performance of each analytical operation in terms of time.

The project was implemented using a cloud-first software development methodology, utilizing PythonAnywhere for deployment and access. The modular approach allowed for a clean separation between data processing, cloud storage, and user interface. All functionalities described in the program specification  including storage, dynamic updating, searching, sorting, classification, and statistics generation  have been implemented and integrated into a web-based . This documentation presents a comprehensive view of the development process, design decisions, implementation details, and cloud deployment, ensuring that the final product aligns with the objectives of scalable, efficient, and accessible document analytics in the cloud.
2. Cloud Software Program/Service Requirements
The developed solution, Cloud Document Analyzer, is a lightweight cloud-based software system designed to efficiently manage, analyze, and organize collections of PDF and Word documents. Hosted on the PythonAnywhere cloud platform, the system enables users to upload documents, sort them alphabetically based on extracted titles, perform content-based searches using keywords, and automatically classify documents into semantic categories such as Finance, Legal, Education, Technology, and Health.
To enhance the user experience, the platform also displays essential statistics, including the number of files stored, total storage size, and execution time of major operations. The system provides a graphical web interface with multiple dedicated pages (Home, Upload, Search, Classify, Documents, Categories, Statistics) to facilitate intuitive and seamless user interaction.

Functional Requirements (User Stories)
o	As a user, I want to upload PDF or Word documents through a web interface so that they are securely stored in the cloud for further processing.
o	As a user, I want the system to automatically extract and display document titles so I can view them in a meaningful, sorted format.
o	As a user, I want to search documents using keywords and view highlighted matches to quickly identify relevant information.
o	As a user, I want the system to automatically classify my documents into content-based categories, reducing the need for manual organization.
o	As a user, I want to view real-time statistics (e.g., document count, storage size, processing times) to assess the system’s performance.

Use Cases
1. Upload Document
o	Actor: User
o	Description: The user selects one or more files via the graphical user interface and uploads them to the server.
o	Postcondition: Files are stored in storage/documents/ and become visible within the system.
2. Sort Documents by Title
o	Actor: System
o	Description: Upon accessing the documents page, the system extracts the first meaningful non-empty line from each document and sorts the list alphabetically.
o	Output: A sorted list of documents with their extracted titles.
3. Search Documents by Keyword
o	Actor: User
o	Description: The user enters a search keyword, and the system scans all documents for matches, returning files containing the keyword with highlighted occurrences.
o	Output: A list of relevant documents and highlighted excerpts.
4. Classify Documents by Category
o	Actor: System
o	Description: The system analyzes each document's content and assigns it to a predefined category using keyword matching techniques.
o	Output: A classification report grouping documents by category.
5. Generate Statistics
o	Actor: System
o	Description: The system calculates the number of stored files, total storage size, and execution time of operations.
o	Output: A summary of system metrics displayed on the Statistics page.

Levels of Abstraction
High-Level (User Interface):
•	A simple, user-friendly web interface with navigation tabs that allow users to upload, search, classify, and manage documents, as well as access system statistics. All actions are initiated through the GUI and rendered dynamically.
Mid-Level (Application Logic):
o	The backend logic is implemented using the Flask web framework. Routes and functions handle file uploads, text extraction, searching, classification, and statistics calculation, then return the results to the front end for rendering.
Low-Level (Core Processing & Storage):
o	Text Extraction: Performed using PyMuPDF for PDF files and docx2txt for Word files.
o	Title Extraction: Obtains the first meaningful non-empty line from each document.
o	Search: Implements case-insensitive keyword search using regular expressions.
o	Classification: Based on keyword matching against a predefined taxonomy stored in a JSON structure.
o	Storage: Uploaded documents are saved locally in storage/documents/, while classification results are stored in storage/classifications.json.


3. Software Architecture and Design
3.1 Overview of the Architecture
The Cloud Document Analyzer is architected as a modular, cloud-deployed application built using Python and the Flask framework. The solution follows a three-tier architecture:
1.	Presentation Layer (Front-End): HTML templates rendered through Flask’s render_template system. Pages include Home, Upload, Search, Classify, Documents, Categories, and Statistics.
2.	Application Logic Layer (Back-End): Handles core processing including document uploading, text extraction, title sorting, keyword searching, classification, and statistics generation. Modular services handle each task independently.
3.	Storage Layer:
o	File Storage: All documents are saved locally in a cloud-accessible directory: storage/documents/.
o	Classification Metadata: Stored in a simple NoSQL-style JSON file: storage/classifications.json.
Deployment takes place on PythonAnywhere, a cloud platform providing a Linux-based Python environment with persistent storage and Flask web app hosting.

3.2 Software Architecture Diagram

 
Figure 1: Software Architecture Diagram

This diagram illustrates the high-level architecture of the cloud-based document analytics system, showing the interaction between users, backend services (Flask), file storage, and functional components (searching, sorting, classifying).


3.3 Functional Components
1. Upload & File Handling Module (file_handler.py)
•	Saves uploaded files in the storage directory.
•	Extracts text and titles from PDFs and DOCX files.
•	Supports .pdf, .docx, and .doc formats.
•	Sanitizes filenames via secure_filename.
2. Sorting Module
•	Extracts the first non-empty line as the document title.
•	Returns a sorted list of documents based on the lowercased title.
•	Ensures alphabetical order regardless of case or format.
3. Searching Module (search_engine.py)
•	Uses regex pattern matching (re) to perform case-insensitive keyword searches.
•	Highlights matching lines from each document.
•	Returns matches and the time taken.
4. Classification Module
•	Defines a keyword-based classification tree (e.g., finance, legal, etc.).
•	Extracts full text and maps documents to categories based on keyword matches.
•	Stores results in a JSON file for persistence.
5. Statistics Module
•	Calculates total file size and number of files.
•	Measures operation durations (searching, sorting, classification).
•	Returns formatted output to be displayed in the GUI.

3.4 Data Design
•	Documents Storage: Files are stored in /storage/documents/ on the cloud filesystem. No relational database is used for simplicity.
•	Classification Output: A JSON file structured as:
json
CopyEdit
{
  "education": ["file1.pdf", "file3.docx"],
  "finance": ["file2.pdf"]
}
•	NoSQL Concept: The JSON structure allows dynamic, schema-less, category-based data storage.

3.5 User Interface Design
Each page is implemented using minimal HTML templates rendered by Flask:
•	Home Page: Overview and entry point to functionalities.

 
                     Figure 2: View site overview






•	Upload Page: Form to upload documents, with client-side file validation.
 
Figure 3: View site overview

•	Documents Page: Lists documents sorted by title.
 
Figure 4: The window through which files can be uploaded





•	Search Page: Input field and search results with matched lines.
 
Figure 5: Represents a window through which you can search for specific text in files.


•	Classify Page: Button to trigger classification and display categorized documents.

 
Figure 6: Displays documents grouped by category.



•	Categories Page: Predefined category definitions and their respective files.
 
Figure 7: View document classification

Statistics Page: Displays number of files, total size, and processing durations.
 
Figure 8: Show statistics about Project Statistics, Stored Files, Total Size, Sorting Time, Search Time and Classification Time




Design Decisions:
•	Chose Flask over heavier frameworks to ensure lightweight, fast deployment on PythonAnywhere.
•	HTML templates provide separation of concerns and quick customization.
•	No JavaScript was used to maintain portability and compatibility with minimal browser environments.

3.6 Real-World Cloud Platform Constraints
While deploying on PythonAnywhere, certain platform limitations were taken into account:
•	Storage Location Restrictions: Files must be stored in permitted user directories (e.g., /home/username/).
•	No Background Tasks: Long-running background jobs must be managed synchronously.
•	Limited File System Permissions: Reading/writing is only allowed within specific folders — storage/ was used accordingly.
•	No Access to External Network by Default: Web scraping is not implemented to avoid issues with outbound HTTP requests in the free tier.
4. Used Cloud Services and its Interfaces
The Cloud Document Analyzer system is deployed and operated on PythonAnywhere, a Python-focused Platform-as-a-Service (PaaS) environment. It enables hosting Flask web applications in a Linux server environment accessible via a public URL. The program is made available to users through the live deployment interface:
🔗 Live Demo – Cloud Program on PythonAnywhere
Cloud Services Utilized:
•	Web Application Hosting (Flask on WSGI Server):
PythonAnywhere allows deploying Flask applications with WSGI configuration. This service powers the interactive GUI and routes used for search, upload, sort, classify, and statistics.
•	Persistent File Storage:
All uploaded documents are stored on the cloud server within a designated folder (storage/documents). PythonAnywhere provides a persistent file system, ensuring file retention even after restarts.
•	File-based metadata storage following NoSQL principles:
Classification metadata is stored in a JSON file (storage/classifications.json), mimicking a NoSQL document database.
•	Web Interface:
HTML templates are rendered and served via Flask routes. Users interact with the system using endpoints like:
o	/upload
o	/search
o	/classify
o	/documents
o	/categories
o	/statistics
The integration between the user interface and the backend cloud services is seamless and occurs over standard HTTP requests managed by Flask’s routing system.
________________________________________


5. Implementation
The system was implemented using Python 3 and the Flask framework. Below is a breakdown of the key components, libraries, and algorithms.
Languages and Frameworks:
•	Python 3.13 – core language
•	Flask 3.1.1– lightweight web framework
•	HTML/CSS – user interface templates
External Libraries Used:
•	fitz (PyMuPDF) – extracting text from PDF files
•	docx & docx2txt – parsing DOCX documents
•	os, time, re, json – file handling, regex search, and data storage
•	werkzeug.utils.secure_filename – for filename sanitization

Implementation Modules:
1. Upload and Storage:
•	Files are uploaded via a form and stored in the cloud directory storage/documents/.
•	The save_file() function handles file validation and saving.

 
Figure 9: The software part responsible for saving files



2. Title Extraction and Sorting:
•	extract_title_from_file() reads the first meaningful line as the title.
•	Documents are sorted alphabetically using get_all_documents_with_titles().
 
Figure 10: The software part responsible for Title Extraction

3. Search Engine:
•	search_in_documents() uses regex to match user input keywords.
•	Matching lines are returned and later highlighted in the interface.
•	Search duration is calculated using time.time().
 
Figure 11: The software part responsible for Search Engine
4. Classification System:
•	A keyword-based classification tree defines categories like finance, education, etc.
•	classify_documents() checks for keyword presence and assigns documents accordingly.
•	Results are saved to a JSON file for persistence.
 
Figure 12: The software component responsible for classifying files
5. Statistics:
•	get_storage_stats() calculates the number of files and total size.
•	Classification and search times are measured and shown to users.

 
Figure 13: The software component responsible for displaying file details
Each module follows the single-responsibility principle for maintainability and ease of testing.
 
Figure 14: Document Classification Flowchart
This flowchart presents the steps of the keyword-based document classification algorithm used in the program.

6. Data
Data Storage Model:
The application uses a file-system-based NoSQL approach for storing both documents and classification metadata. Here's a breakdown:
•	Document Storage:
o	All files (.pdf, .docx) are saved in storage/documents/.
o	Accessed using standard Python I/O operations.
•	Metadata Storage (Classification):
o	Stored as structured JSON (storage/classifications.json).
o	Example:
json
CopyEdit
{
  "technology": ["cloud_innovation.pdf"],
  "education": ["research_plan.docx"]
}
This structure serves as a document-based NoSQL model, which is suitable for a lightweight cloud application where no relational joins are needed.
Data Access and Security:
•	All read/write operations are sandboxed to the application's storage directory as per PythonAnywhere’s security policy.
•	No external database (e.g., SQL or Firebase) is used, ensuring minimal complexity and full control over the data structure.
Operation	Result
Total number of documents	3 documents
Total size of documents	5.29 MB
Documents per category	• Finance: 1 • Education: 1 • Legal: 1
Sorting time	~0.0112 seconds 
Search time	~0.0095 seconds 
Classification time	~0.0147 seconds 

7. The Used Cloud Platform
The deployed platform for the Cloud Document Analyzer project is PythonAnywhere, a cloud-based integrated development and hosting environment designed specifically for Python applications.
Platform Overview and Architecture:
PythonAnywhere provides a virtualized cloud environment with the following components:
•	Web App Hosting (WSGI Server):
The application is hosted via a WSGI-compliant server which handles incoming HTTP requests and dispatches them to the Flask backend.
•	Persistent File System:
All uploaded and processed files are saved in a persistent directory structure provided by PythonAnywhere. These files remain available even across sessions or server restarts.
•	Integrated Bash Console:
PythonAnywhere allows command-line interaction for package installation, file manipulation, and environment management.
•	Scheduled Tasks & Manual Execution:
It provides cron-like task scheduling, though not utilized in this specific implementation.
•	Security and Isolation:
Applications are isolated in user-specific containers with restrictions on internet access and external process execution, ensuring platform-level safety and sandboxing.
Environment Details:
•	Language Support: Python 3.13 
•	Web Frameworks Supported: Flask, Django, etc.
•	No Built-in Database Required: The project used file-based NoSQL-style JSON storage, eliminating the need for external databases like MySQL or PostgreSQL.

8. Deployment on the Platform
The deployment of the application on PythonAnywhere involved the following steps, ensuring a full end-to-end mapping from local development to cloud-hosted service:
Deployment Workflow:
Account and Environment Setup:
o	A developer account was created on PythonAnywhere.
o	Python 3 environment was configured with required libraries (e.g., flask, PyMuPDF, docx2txt, etc.).
Code Upload:
o	The full project structure was uploaded, including:
	/templates for HTML user interfaces.
	/services containing core logic files (file_handler.py, search_engine.py, etc.).
	/storage for document uploads and classification metadata.
	main.py (Flask application entry point).
WSGI Configuration:
o	PythonAnywhere requires a WSGI configuration script to define the Flask app.
o	The app object (app) in main.py was registered in the WSGI file:
python
CopyEdit
from /home/shaima1/path_to_app.main import app as application
Static and Media Path Setup:
o	Directories for static files and uploaded documents were defined to ensure access and persistence.
Testing and Validation:
o	After deployment, the application was accessed through the provided public link:
🔗 https://shaima1.pythonanywhere.com/
o	Multiple test documents were uploaded and processed to validate upload, sort, search, and classify functionalities.


Mapping between Code and Cloud Components:
Code Module	Cloud Component
Flask Routes (main.py)	PythonAnywhere WSGI app server
HTML Templates	Cloud-hosted via Flask
storage/documents	PythonAnywhere persistent storage
storage/classifications.json	Simulated NoSQL document store
User Upload Interface	Flask HTML + form POST
Search & Classify Logic	Executed server-side in container
Final URL	https://shaima1.pythonanywhere.com/
This deployment approach ensured full functionality in a live cloud environment, accessible 24/7 via a browser with no need for installation or configuration by the end-user.

Testing Summary
To ensure the functionality and performance of the cloud-based document management system, several tests were conducted covering the core operations:
•	Number of Documents Tested: 20
•	Document Types: PDF and DOCX
•	Tested Functions:
• Document uploading
• Title-based sorting
• Keyword search with text highlighting
• Document classification using predefined keywords
•	Issues Encountered:
• During deployment to PythonAnywhere, the upload function initially failed due to file system path restrictions. This was mitigated by adjusting the storage handling logic to ensure compatibility with the platform's environment.
•	Outcome:
All main functionalities were successfully validated with correct performance metrics logged and verified.


9. User Support
The Cloud Document Analyzer has been developed with an intuitive and user-friendly interface, accessible via any modern web browser. The following outlines how the end-user can interact with the system:
How Users Operate the Program:
•	Accessing the Program:
Users simply visit the live hosted link:
🔗 https://shaima1.pythonanywhere.com/
Main Interface Pages:
o	Home: Overview of the program and its purpose.
o	Upload: Allows users to upload PDF or Word documents to the system.
o	Search: Enables users to enter keywords or phrases to search within uploaded documents. Matching results are highlighted for ease of reading.
o	Classify: Automatically categorizes documents based on content using a predefined classification tree.
o	Documents: Lists all uploaded documents with their extracted titles.
o	Categories: Displays categorized documents grouped under relevant labels.
o	Statistics: Shows system-level information including:
	Total number of documents.
	Combined storage size (e.g., 10.29 MB).
	Processing time for sorting, searching, and classification.
•	User Documentation:
The system does not require installation or user registration. All interactions are performed through the web interface. The program is designed to provide immediate visual feedback (e.g., classification result tables, highlighted search results, etc.) to guide the user effectively.
•	Source Code Repository:
🔗 GitHub Repository: .
                  https://github.com/Shymaa-dev/cloud3.git

10. Conclusion
The Cloud Document Analyzer demonstrates a robust and modular implementation of a cloud-based solution for handling large document collections. Through a simple and responsive web interface, users can upload, sort, search, and classify documents efficiently, all hosted on a reliable cloud environment.
Key Achievements:
•	Full document pipeline from upload to classification using Python and Flask.
•	Real-time document statistics and efficient keyword search with text highlighting.
•	Intelligent classification algorithm leveraging keyword-tree matching.
•	Seamless deployment on PythonAnywhere with stable public access.
Issues and Future Work:
While the application fulfills all major functional requirements, future improvements could include:
•	Database Integration: Switching from JSON storage to a scalable NoSQL database like MongoDB or Firebase for better data management.
•	Web Scraping Module: Adding an automated document collection module from the web to support dynamic content growth.
•	User Authentication: Introducing user roles (e.g., admin vs. viewer) to control document access.
•	Analytics Dashboard: Expanding the statistics module to include trend analysis, visual graphs, and keyword frequency maps.
The project showcases the effectiveness of cloud-native development using open-source technologies and provides a strong foundation for more advanced document analytics systems.
________________________________________




References
1.	PythonAnywhere Cloud Hosting Platform – https://www.pythonanywhere.com/
2.	Flask Web Framework – https://flask.palletsprojects.com/
3.	PyMuPDF (fitz) for PDF Parsing – https://pymupdf.readthedocs.io/
4.	python-docx and docx2txt Libraries – https://python-docx.readthedocs.io/
5.	JSON File Storage (Python Built-in) – https://docs.python.org/3/library/json.html
6.	WSGI Specification – https://wsgi.readthedocs.io/en/latest/
Academic References
1.	Kowsari, K., Meimandi, K. J., Heidarysafa, M., Mendu, S., Barnes, L. E., & Brown, D. F. (2019). Text classification algorithms: A survey. Information, 10(4), 150. https://doi.org/10.3390/info10040150
2.	Singh, G., & Kaur, G. (2020). Cloud-based document management systems: A review. International Journal of Computer Applications, 176(38), 9–13. https://doi.org/10.5120/ijca2020920305




