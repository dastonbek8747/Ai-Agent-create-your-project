# 🤖 AI Agent — Loyiha Yaratuvchi

Sun'iy intellekt yordamida dastur loyihalarini yaratish bo'yicha namunalar. **Claude** va **Groq (Qwen)** modellaridan foydalanadi.

---

## ✨ Imkoniyatlar

- 🧠 **AI agent:** foydalanuvchi talabiga ko'ra kod/loyiha yozadi
- 🔌 **Ko'p model:** Anthropic Claude va Groq
- 🛠 **LangChain** tool'lari
- 📝 **Prompt muhandisligi** namunasi

---

## 🛠 Texnologiyalar

| Texnologiya | Maqsad |
|---|---|
| **Python 3.10+** | Asosiy til |
| **anthropic** | Claude API |
| **langchain** | Agent framework |
| **langchain_groq** | Groq modellari |
| **python-dotenv** | Muhit o'zgaruvchilari |

---

## ⚙️ O'rnatish

```bash
git clone https://github.com/dastonbek8747/Ai-Agent-create-your-project.git
cd Ai-Agent-create-your-project
python -m venv venv
source venv/bin/activate
pip install anthropic langchain langchain-groq python-dotenv
```

`.env` fayl yarating:

```env
NEW_API=<anthropic_api_key>
GROQ_API_KEY=<groq_api_key>
```

> 🔒 `.env` git'ga qo'shilmaydi.

---

## ▶️ Ishga tushirish

```bash
python claud.py     # Claude namunasi
python daston.py    # Groq + LangChain agent namunasi
```

---

## 📁 Loyiha tuzilishi

```
Ai-Agent-create-your-project/
├── claud.py           # Claude API namunasi
├── daston.py          # LangChain agent
└── .gitignore
```

---

## 📄 Litsenziya

Litsenziya ko'rsatilmagan.
