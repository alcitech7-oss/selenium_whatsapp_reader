selenium_whatsapp_reader

Bot that reads WhatsApp Web messages, classifies them by category (Order, Complaint, Delivery, etc.), and saves them to an Excel spreadsheet with separate tabs.

---

## 🚀 Features

- ✅ Automatic login via QR Code
- ✅ Real-time message reading (continuous loop)
- ✅ Intelligent classification with spaCy (lemmas and context)
- ✅ Excel spreadsheet with separate tabs per category
- ✅ Duplicate message filter (only adds new ones)
- ✅ Automatic pop-up closing
- ✅ **Bilingual support: automatically detects and classifies messages in Portuguese or English**

---

## 🛠️ Technologies

- Python 3.10+
- Selenium
- OpenPyXL
- spaCy (NLP for classification)
- WebDriver Manager
- langdetect (language detection)

---

## 📦 Installation

```bash
git clone https://github.com/alcitech7-oss/selenium_whatsapp_reader.git
cd selenium_whatsapp_reader
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python -m spacy download pt_core_news_sm
python -m spacy download en_core_web_sm
▶️ How to run
bash
python main.py
📂 Project Structure
text
selenium_whatsapp_reader/
├── main.py
├── requirements.txt
├── README.md
├── .gitignore
├── core/
│   ├── __init__.py
│   ├── login.py          # Handles WhatsApp login
│   ├── extractor.py      # Extracts and classifies messages
│   └── selectors.py      # XPath selectors
✅ Project Validated
Tested in a clean environment (fresh clone):

✔️ Dependencies installed successfully

✔️ Login via QR Code working

✔️ Message reading and classification ok

✔️ Spreadsheet generated with separate tabs

✔️ Continuous loop and pop-up handling ok

✔️ Bilingual support validated (PT / EN)

✔️ Ready for use and demonstration

📌 Development History
Complete refactoring: class-based selectors and continuous loop

Organization: Modular structure with core/ folder

Classification: Implemented with spaCy (lemmas and NLP)

Bilingual support: Added Portuguese and English detection with langdetect

Spreadsheet: Separate tabs per category

Final validation: Project tested and validated from scratch

🤝 Contribution
Feel free to contribute with improvements, new categories, or bug fixes.

