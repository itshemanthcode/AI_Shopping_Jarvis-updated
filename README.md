# 🛍️ AI Shopping Jarvis

> This personal AI-powered product deals assistant — finds top-rated, lowest-price products across Amazon, Flipkart, and official brand stores. Voice-enabled search included! 🎤✨

---

## 💡 Features

- 🔎 **Search Products** by name (e.g., “iPhone 15”)
- 🤖 **AI Summary**: Get intelligent insights about available products
- ⭐ **Rating & Price Comparison** from:
  - ✅ Amazon
  - ✅ Flipkart
  - ✅ Official Brand Store
- 🛒 **Direct "Buy Now" links** to product payment pages
- 🗣️ **Speech-to-Text** (like “Jarvis, get me laptop deals”) *(Coming soon)*

---

## 📸 UI Preview

![AI Shopping Jarvis UI](screenshot.png)

---

## 🚀 Run Locally

### 1. Clone this Repo

```bash
git clone https://github.com/itshemanthcode/AI_Shopping_Jarvis.git
cd AI_Shopping_Jarvis
**2. Install Requirements**
bash
Copy
Edit
pip install -r requirements.txt
**3. Set OpenAI API Key**
Create a .env file in the root:

env
Copy
Edit
OPENAI_API_KEY=your_openai_api_key
**4. Start Flask App**
bash
Copy
Edit
python app.py
Go to 👉 http://127.0.0.1:5000/

📦 Folder Structure
bash
Copy
Edit
AI_Shopping_Jarvis/
│
├── app.py                  # Flask app
├── scraper.py              # Amazon + Flipkart scraping logic
├── ai_summary.py           # AI summary using OpenAI
├── templates/
│   └── index.html          # Frontend UI
├── static/
│   └── style.css           # Flashy UI styling
├── requirements.txt
└── .env                    # Your OpenAI API Key (not pushed to GitHub)
🔮 Coming Soon
🎤 Voice search ("Jarvis" style)

📱 Mobile-responsive UI

📊 Smart filters (price, rating, brand)

📦 Add more platforms (Snapdeal, Croma, etc.)

🧠 Built With
💬 Flask

🧠 Hugging Face

🌐 Selenium Web Scraping

🎨 HTML + CSS

🙌 Contribute
Pull requests are welcome! Feel free to fork, improve, and send PRs.

🧑‍💻 Author
Made with 💙 by @itshemanthcode
