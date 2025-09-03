# 🛠️ Automation Scripts

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.8%2B-blue)](https://www.python.org/)
[![Contributions Welcome](https://img.shields.io/badge/contributions-welcome-brightgreen)](#-contributing)

A collection of Python automation scripts for everyday tasks:
- 📂 File handling (move, compress, backup)
- 🌐 API integrations (bulk caller, downloader)
- 📝 Data utilities (JSON formatter, text search)

---

## 🚀 Quick Start

```bash
git clone https://github.com/<your-username>/automation-scripts.git
cd automation-scripts
pip install -r requirements.txt
```

Run a script:

```bash
python main.py --script file_compressor --input my_folder --output archive.zip --mode zip
```

More examples in [USAGE.md](USAGE.md) 🔗

---

## 📂 Repository Structure

```
automation-scripts/
│── main.py                  # CLI entry point
│── requirements.txt         # Python dependencies
│── LICENSE                  # MIT License
│── README.md                # Project documentation
│
├── utils/                   # Shared utilities
│   ├── file_ops.py          # File handling functions
│   ├── api_ops.py           # API helper functions
│   └── log_ops.py           # Logging functions
│
└── scripts/                 # Individual automation scripts
    ├── file_processor.py    # Move/upload files
    ├── file_compressor.py   # Compress files/folders
    ├── json_formatter.py    # Validate & format JSON
    ├── text_search.py       # Keyword search in files
    ├── bulk_api_caller.py   # Call API in bulk from CSV
    ├── file_downloader.py   # Download files from URL list
    └── backup_utility.py    # Timestamped backups
```

---

## 📦 Dependencies

- [requests](https://pypi.org/project/requests/) – API calls, file downloads
- [pandas](https://pypi.org/project/pandas/) – CSV handling, API results
- [openpyxl](https://pypi.org/project/openpyxl/) – Excel logging

Install all dependencies:

```bash
pip install -r requirements.txt
```

---

## 🤝 Contributing

Contributions are welcome! 🎉  
See [CONTRIBUTING.md](CONTRIBUTING.md) for details.

---

## 📝 License

This project is licensed under the [MIT License](LICENSE).
