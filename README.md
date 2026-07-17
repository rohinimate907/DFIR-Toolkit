# 🛡️ DFIR Toolkit

### Digital Forensics & Incident Response Toolkit


A modular Digital Forensics & Incident Response (DFIR) Toolkit developed in Python.

The toolkit assists investigators in analyzing digital evidence through file integrity verification, metadata extraction, and file signature validation.

Designed using modular software architecture, the project aims to simulate real-world forensic workflows while following professional software engineering practices.

## ✨ Features

- File Integrity Verification (Hash Calculator)
- Metadata Analysis
- File Signature Verification
- Extension Spoof Detection
- Modular Architecture
- Cross Platform


## 📂 Project Structure
DFIR-Toolkit/
│
├── core/
│   ├── hashing.py
│   ├── metadata.py
│   └── signature.py
│
├── samples/
├── reports/
├── docs/
├── tests/
│
├── main.py
├── README.md
├── requirements.txt
└── LICENSE

## 🛠 Technologies

- Python 3.13+
- Pathlib
- hashlib
- datetime

## 🚀 Installation

```bash
git clone https://github.com/rohinimate907/DFIR-Toolkit.git

cd DFIR-Toolkit

pip install -r requirements.txt


## ▶ Run

```bash
python main.py
```

## 🚧 Roadmap

- [x] Hash Calculator
- [x] Metadata Analyzer
- [x] File Signature Verification
- [x] CLI Integration
- [ ] IOC Scanner
- [ ] Timeline Generator
- [ ] Report Generator
- [ ] GUI


## 📄 License

This project is licensed under the MIT License.