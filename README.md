# 🛍️ Amharic E-commerce Named Entity Recognition - EthioMart

**EthioMart** aims to become Ethiopia’s primary hub for Telegram-based e-commerce by centralizing product discovery, order placement, and communication across multiple Telegram channels.

This project focuses on collecting, preprocessing, and labeling e-commerce-related data from Telegram messages to support the development of an Amharic Named Entity Recognition (NER) system. The extracted structured information will power EthioMart’s unified shopping platform.

---

## 🎯 Objectives

- Ingest messages (text, images, metadata) from multiple Telegram-based vendor channels.
- Preprocess Amharic text to prepare clean and structured data.
- Manually label a subset of messages for key business entities in CoNLL format.
- Enable fine-tuning of NER models to extract entities like Product, Price, and Location.

---

## 🛠️ Methodology

### 1. Data Ingestion

- **Script:** `telegram_scraper.py`
- **Tool:** [`Telethon`](https://github.com/LonamiWebs/Telethon)
- **Data Collected:**
  - Message ID
  - Channel Title & Username
  - Message Date
  - Raw Text Message

Messages are scraped from selected Telegram channels and saved in CSV format.

---

### 2. Text Preprocessing

- **Notebook:** `preprocess.ipynb`
- **Processing Steps:**
  - Normalize Amharic text (character-level normalization, punctuation removal)
  - Tokenize sentences and words
  - Clean and structure the dataset
  - Separate message content from metadata

Structured fields include:
- `channel_title`
- `channel_username`
- `message_id`
- `date`
- `cleaned_text`
- `tokens`

---

### 3. NER Data Labeling

- **Goal:** Manually annotate 30–50 Amharic messages using the CoNLL format.
- **Labels Used:**
  - `B-Product`, `I-Product`
  - `B-PRICE`, `I-PRICE`
  - `B-LOC`, `I-LOC`
  - `O` (Outside any entity)
- **Format:**
  Each token is labeled and written line-by-line, with messages separated by blank lines.

- **Output File:** `amharic_ner_dataset.conll`

---

## 📦 Tools Used

- `Telethon`: Telegram scraping
- `pandas`: Data manipulation
- `re`: Text cleaning and normalization
- `Jupyter Notebooks`: Preprocessing and labeling
- `Python 3.10+`

---

## 📁 Outputs

- `telegram_data.csv`: Raw scraped Telegram messages
- `structured_data.json` or `.csv`: Cleaned and tokenized messages
- `amharic_ner_dataset.conll`: Manually labeled CoNLL-format file for training NER models

---

## 📈 Next Steps

- Fine-tune a transformer-based model (e.g., Amharic BERT) on the labeled dataset.
- Automate real-time ingestion and tagging for EthioMart platform.
- Expand labeled dataset for better model generalization.

---

> 💡 Built for **EthioMart** to unify and enrich Amharic e-commerce data through intelligent automation.
