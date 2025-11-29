# Just Eat / pyszne.pl Restaurants Scraper

A clean and simple Python scraper for collecting restaurant data from food delivery platforms of the **Just Eat Takeaway** group (including **pyszne.pl** in Poland).

The script uses HTTP requests to access publicly available API endpoints (used by the website itself) and exports a clean CSV file with restaurant data for any selected location.

> ⚠️ **Disclaimer:**  
> This project is for educational and internal tooling purposes only.  
> Always respect the Terms of Service and robots.txt of any website before scraping.

---

## 🚀 Features

- Fetch restaurant lists for a given **city / coordinates**
- Save results into **CSV** for easy use in Google Sheets / Excel
- Basic **data cleaning** (duplicates, empty fields, formatting)
- Easy to extend with additional fields or logic

Collected fields include (depending on API structure):

- `restaurant_id`
- `name`
- `city`
- `address`
- `latitude` / `longitude`
- `cuisines`
- `rating`
- `minimum_order_amount`
- `delivery_fee`
- `url`

---

## 🛠 Tech Stack

- **Python 3.10+**
- `requests` — HTTP client
- `pandas` — data processing
- CLI via `argparse`

---

## 📦 Installation

```bash
git clone https://github.com/yanyanovskyi/justeat-pyszne-restaurants-scraper.git
cd justeat-pyszne-restaurants-scraper

python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate

pip install -r requirements.txt
