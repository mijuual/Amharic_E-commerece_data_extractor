# 🛍️ Amharic E-commerce Named Entity Recognition – EthioMart

**EthioMart** aims to become Ethiopia’s primary hub for Telegram-based e-commerce by centralizing product discovery, order placement, and communication across multiple Telegram channels.

This project focuses on collecting, preprocessing, labeling, and analyzing e-commerce-related data from Telegram messages to power an Amharic Named Entity Recognition (NER) system and extract vendor intelligence. The structured information enables features like vendor scoring for micro-lending and intelligent search.

---

## 🎯 Objectives

- Ingest messages (text + metadata) from multiple Telegram vendor channels.
- Preprocess and tokenize Amharic text.
- Manually annotate data in CoNLL format for NER training.
- Fine-tune transformer-based NER models for extracting `Product`, `Price`, `Location`, etc.
- Develop a **Vendor Analytics Engine** to generate FinTech lending scores from message-level data.

---

## 🛠️ Methodology

### 1. Data Ingestion

- **Script:** `telegram_scraper.py`
- **Tool:** [`Telethon`](https://github.com/LonamiWebs/Telethon)
- **Data Collected:**
  - `channel_title`
  - `channel_username`
  - `message_id`
  - `date`
  - `raw_text`

Scraped data is stored in CSV for preprocessing.

---

### 2. Text Preprocessing

- **Notebook:** `preprocess.ipynb`
- **Steps:**
  - Normalize Amharic text (remove non-standard characters & symbols)
  - Tokenize sentences and words
  - Clean and structure the dataset

**Structured Output Fields:**

- `channel_title`
- `channel_username`
- `message_id`
- `date`
- `cleaned_text`
- `tokens`

---

### 3. NER Annotation

- **Goal:** Manually annotate ~50 Amharic e-commerce messages using CoNLL format.
- **Entity Tags:**
  - `B-Product`, `I-Product`
  - `B-PRICE`, `I-PRICE`
  - `B-LOC`, `I-LOC`
  - `O` (Outside any entity)

- **Annotation File:** `amharic_ner_dataset.conll`

---

### 4. NER Model Training

- **Models Used:**
  - `xlm-roberta-base`
  - `distilbert-base-multilingual-cased`

- **Training Code:** `ner_training.ipynb` (Colab)
- **Tokenization & Alignment:** Sentence-level tokenization aligned with NER tags.
- **Metrics Evaluated:** Accuracy, Precision, Recall, F1 Score (per epoch)

- **Model Output Folder:** `amharic_ner_model/`

---

### 5. Named Entity Inference

- **NER Pipeline:**
  - Load trained model locally via `transformers`
  - Run predictions on cleaned Telegram text
  - Extract entities like product names, prices, and locations

---

## 📊 Vendor Analytics Engine – FinTech Lending Score

To support **micro-lending decisions**, EthioMart analyzes vendor activity and engagement levels:

### ✅ Metrics Computed Per Vendor

- `posts`: Total number of messages
- `post_freq_per_week`: Activity level (avg. posts/week)
- `avg_views`: Placeholder (can be filled with view data if available)
- `avg_price`: Average price extracted by NER
- `top_post_text`: Placeholder for most viewed post
- `top_post_views`: Placeholder for engagement
- `lending_score`: Weighted score using frequency & pricing

### 📁 Sample Output:

```
vendor,posts,post_freq_per_week,avg_views,top_post_text,top_post_views,avg_price,lending_score
@Shageronlinestore,4102,18.74,,,,12668.45,287.43
@ZemenExpress,4840,17.97,,,,17794.47,279.73
@nevacomputer,2851,8.26,,,,11170.71,182.57
@ethio_brand_collection,3245,7.9,,,,17418.91,179.04
@meneshayeofficial,877,6.34,,,,15820.36,163.42
```

> The score helps identify vendors with high engagement and revenue potential.

---

## 📦 Tools & Libraries

- `Telethon` – Telegram scraping
- `transformers` – NER model training
- `datasets` – Token classification dataset management
- `pandas`, `numpy` – Data processing
- `scikit-learn`, `seqeval` – Evaluation metrics
- `matplotlib`, `plotly` – (Optional) visualization

---

## 📁 Project Structure

- `telegram_data.csv` – Raw scraped messages
- `preprocess.ipynb` – Text normalization & tokenization
- `amharic_ner_dataset.conll` – Labeled data for NER
- `ner_training.ipynb` – Fine-tuning notebook
- `amharic_ner_model/` – Trained NER model
- `vendor_scorecard.csv` – Analytics output for lending

---

> 💡 Built to unlock insights from unstructured Amharic commerce data and empower small businesses with credit access.
