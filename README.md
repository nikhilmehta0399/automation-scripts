# 🛠️ Automation Scripts

A collection of Python automation scripts for everyday tasks.  
This repository is designed to simplify repetitive workflows like file handling, API calls, data parsing, and other daily-use utilities. New scripts will be added regularly to build a handy toolkit for developers and power users.

---

## 📂 Repository Structure
```
automation-scripts/
│── file_processor.py        # Pick files from a folder, call API, move processed files
│── input_files/             # Place files here to be processed
│── processed_files/         # Processed files are moved here
│── requirements.txt         # Python dependencies
│── README.md
│── LICENSE
```

---

## 🚀 Available Scripts

### 1️⃣ File Processor
- Picks files from `input_files/`
- Uploads them to an API (`multipart/form-data`)
- Moves them to `processed_files/` after successful processing  
- Leaves unprocessed files in `input_files/` for retry  

Run it with:
```bash
python file_processor.py
```

Configure API details in the script:
```python
INPUT_FOLDER = "input_files"
PROCESSED_FOLDER = "processed_files"
API_URL = "http://example.com/upload"   # Replace with your API endpoint
API_PARAM_NAME = "file"                 # API parameter name for file
```

---

## ⚙️ Setup & Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/<your-username>/automation-scripts.git
   cd automation-scripts
   ```

2. (Optional) Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Place your files in the `input_files/` folder and run the script.

---

## 📦 Dependencies
- [requests](https://pypi.org/project/requests/) – for making API calls  

Install with:
```bash
pip install requests
```

---

## 🔮 Future Enhancements
- Continuous folder monitoring (auto-run on new files)  
- Retry logic for failed uploads  
- Log file for API responses  
- Additional automation scripts (file renamer, folder organizer, log parser, etc.)

---

## 🤝 Contributing
Want to add a useful script? Contributions are welcome!  
1. Fork the repo  
2. Add your script in a new file  
3. Submit a pull request  

---

## 📝 License
This project is licensed under the MIT License.
