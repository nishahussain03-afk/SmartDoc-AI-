# 📄 SmartDoc AI

### Intelligent Document Understanding and Action Assistant using OCR and LLM

SmartDoc AI is an AI-powered document understanding application that extracts text from documents using Optical Character Recognition (OCR) and uses a Large Language Model (LLM) to understand and organize the extracted information.

Instead of simply displaying OCR text, SmartDoc AI converts unstructured document content into useful information such as document type, summary, important details, amounts, payment status, dates, and required actions.

---

## 🚀 Features

- 📤 Upload document images
- 🔍 OCR-based text extraction
- 🖼️ Image preprocessing using OpenCV
- 🧠 Multiple Tesseract OCR page segmentation modes
- 📊 OCR confidence measurement
- 🤖 LLM-powered document understanding
- 📄 Automatic document type identification
- 📝 Automatic document summarization
- 🔑 Important information extraction
- 💰 Amount and currency identification
- ✅ Payment status detection
- 💳 Payment method detection
- 📅 Important date identification
- 📌 Required action detection
- 🌐 Web-based Streamlit interface
- 🔐 Environment-variable based API key management

---

## 🎯 Problem Statement

Many documents contain important information in an unstructured format.

Examples include:

- Electricity bills
- Receipts
- Scholarship notifications
- Bank documents
- Government notices
- College documents
- Application forms
- Invoices

Users often have to manually read the entire document to find important information.

Traditional OCR systems only extract text and do not explain what the document means.

SmartDoc AI solves this problem by combining:

**OCR + Large Language Model + Document Understanding**

---

## 💡 Proposed Solution

SmartDoc AI follows a simple intelligent document processing pipeline:

```text
                 📄 Document
                      │
                      ▼
              📤 Document Upload
                      │
                      ▼
             🖼️ Image Processing
                      │
                      ▼
                🔍 Tesseract OCR
                      │
                      ▼
             📝 Extracted Text
                      │
                      ▼
              🤖 Large Language Model
                      │
                      ▼
          🧠 Document Understanding
                      │
                      ▼
       ┌───────────────────────────────┐
       │ Document Type                 │
       │ Summary                       │
       │ Key Information               │
       │ Amount                        │
       │ Payment Status                │
       │ Payment Method                │
       │ Important Dates               │
       │ Required Actions              │
       └───────────────────────────────┘
