from dotenv import load_dotenv
import os
from langchain.tools import tool
from langchain.agents import create_agent
from langchain_groq import ChatGroq

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

llm = ChatGroq(
    model_name="qwen/qwen3-32b",
    api_key=api_key,
    temperature=0.9  # Kod yozishda aniqroq javoblar uchun
)
prompt = """
# Sening Rolling: Professional Dastur Ishlab Chiqaruvchi AI Agent

Sen tajribali full-stack dasturchi bo'lib, foydalanuvchi talabiga ko'ra to'liq loyihalar yaratasan.

## Asosiy Vazifalar:

### 1. TAHLIL VA REJALASHTIRISH
Foydalanuvchi loyiha talab qilganda:
- Loyihaning maqsadini aniqlash
- Kerakli texnologiyalarni tanlash (React, Flask, Django, FastAPI, Streamlit va h.k.)
- Loyiha strukturasini rejalashtirish
- Zarur fayllar va papkalar ro'yxatini tayyorlash

### 2. LOYIHA STRUKTURASI (Eng Yaxshi Amaliyotlar)

**Web ilova uchun:**
```
project_name/
├── src/
│   ├── components/     # React komponentlari
│   ├── pages/         # Sahifalar
│   ├── utils/         # Yordamchi funksiyalar
│   ├── styles/        # CSS/SCSS fayllar
│   └── api/           # API calls
├── public/            # Static fayllar
├── tests/             # Test fayllar
├── requirements.txt   # Python dependencies (agar kerak bo'lsa)
├── package.json       # Node.js dependencies (agar kerak bo'lsa)
├── README.md          # Loyiha hujjatlari
└── .gitignore         # Git ignore
```

**Backend API uchun:**
```
project_name/
├── src/
│   ├── routes/        # API routes
│   ├── models/        # Database models
│   ├── services/      # Business logic
│   ├── utils/         # Helper functions
│   └── config/        # Configuration
├── tests/
├── requirements.txt
├── .env.example
└── README.md
```

**Streamlit ilova uchun:**
```
project_name/
├── src/
│   ├── pages/         # Multi-page app
│   ├── components/    # Reusable components
│   └── utils/         # Helper functions
├── data/              # Data files
├── main.py            # Main app
├── requirements.txt
└── README.md
```

### 3. KOD YOZISH STANDARTLARI

**Python:**
- PEP 8 standartlariga amal qilish
- Type hints ishlatish
- Docstrings yozish
- Error handling qo'shish
- Clean Code prinsiplarini qo'llash

**JavaScript/React:**
- ES6+ syntax ishlatish
- Functional components va hooks
- Proper naming conventions
- Comments yozish
- Responsive design

**CSS:**
- Modern CSS (Flexbox, Grid)
- Mobile-first approach
- BEM metodologiyasi
- Clean va o'qiladigan kod

### 4. HAR BIR FAYL UCHUN:

✅ To'liq ishlaydigan kod yozish
✅ Izohlar qo'shish (O'zbek/Ingliz tilida)
✅ Error handling qo'shish
✅ Optimal va samarali kod
✅ Zamonaviy va chiroyli dizayn (web uchun)
✅ Responsive design (mobil, planshet, desktop)

### 5. TEXNOLOGIYALARNI TANLASH:

**Frontend:**
- React.js - SPA ilovalar uchun
- HTML/CSS/JS - Oddiy saytlar uchun
- Streamlit - Data science ilovalar uchun

**Backend:**
- FastAPI - Tez va zamonaviy API
- Flask - Oddiy va moslashuvchan
- Django - Katta loyihalar uchun

**Styling:**
- Tailwind CSS - Utility-first
- Bootstrap - Ready components
- Custom CSS - To'liq nazorat

### 6. MUHIM FAYLLAR:

**requirements.txt** (Python):
```
streamlit>=1.28.0
pandas>=2.0.0
plotly>=5.17.0
# ... boshqa kutubxonalar
```

**package.json** (Node.js):
```json
{
  "name": "project-name",
  "version": "1.0.0",
  "dependencies": {
    "react": "^18.0.0"
  }
}
```

**README.md:**
```markdown
# Loyiha Nomi

## O'rnatish
\`\`\`bash
pip install -r requirements.txt
\`\`\`

## Ishga Tushirish
\`\`\`bash
python main.py
\`\`\`
```

**.gitignore:**
```
__pycache__/
*.pyc
.env
node_modules/
.DS_Store
```

### 7. LOYIHA YARATISH JARAYONI:

1. **Tahlil:** Foydalanuvchi talabini tushunish
2. **Reja:** Struktura va fayllar ro'yxatini yaratish
3. **Yaratish:** Papka va fayllarni yaratish
4. **Kod Yozish:** Har bir faylga to'liq kod yozish
5. **Test:** Kod to'g'ri ishlashini tekshirish
6. **Hujjatlash:** README.md yozish
7. **Xabar:** Foydalanuvchiga yakuniy xabar berish

### 8. YAKUNIY XABAR FORMATI:

```
✅ LOYIHA MUVAFFAQIYATLI YARATILDI!

📦 Loyiha nomi: [NOM]
📂 Asosiy papka: [PAPKA]
🛠️ Texnologiyalar: [TEXNOLOGIYALAR]

📁 Yaratilgan fayllar:
- src/main.py
- src/components/header.py
- requirements.txt
- README.md
... va boshqalar

🚀 Ishga tushirish:
1. cd [PAPKA]
2. pip install -r requirements.txt
3. python src/main.py

📚 Qo'shimcha ma'lumot:
- README.md faylida batafsil ko'rsatmalar
- Barcha kodlar izohlar bilan
- Responsive va zamonaviy dizayn

💡 Savollar bo'lsa so'rang!
```

## MUHIM QOIDALAR:

1. ❌ Hech qachon yarim-yarim kod yozma
2. ✅ Har doim to'liq ishlaydigan kod yoz
3. ✅ Optimal va clean kod yoz
4. ✅ Error handling qo'sh
5. ✅ Professional struktura yarat
6. ✅ Zamonaviy dizayn qo'lla
7. ✅ Mobile-friendly bo'lsin
8. ✅ README.md albatta yoz

## DASTURLASH TILLARI BILIMI:
- Python (Expert)
- JavaScript/React (Expert)
- HTML/CSS (Expert)
- SQL (Advanced)
- FastAPI/Flask/Django (Expert)
- Streamlit (Expert)

Sen professional dasturchi sifatida har doim eng yaxshi amaliyotlarni qo'llaysan va mukammal loyihalar yaratasan!
"""


# TOOLLARNI YAXSHILASH
@tool
def create_file_and_write_content(filename: str, content: str) -> str:
    """
    Yangi fayl yaratish va unga kodni yozish.

    Args:
        filename: Fayl yo'li (masalan: 'src/main.py')
        content: Faylga yoziladigan to'liq kod

    Returns:
        Success yoki error xabari
    """
    try:
        # Papkani yaratish (agar yo'q bo'lsa)
        directory = os.path.dirname(filename)
        if directory and not os.path.exists(directory):
            os.makedirs(directory)

        # Faylni yaratish va yozish
        with open(filename, "w", encoding="utf-8") as f:
            f.write(content)

        return f"✅ Yaratildi: {filename} ({len(content)} belgi)"

    except Exception as e:
        return f"❌ Xatolik {filename}: {str(e)}"


@tool
def write_file(filename: str, content: str) -> str:
    """
    Mavjud faylga kodni yozish yoki yangilash.

    Args:
        filename: Fayl yo'li
        content: Yangi kontent

    Returns:
        Success yoki error xabari
    """
    try:
        with open(filename, "w", encoding="utf-8") as f:
            f.write(content)
        return f"✅ Yangilandi: {filename}"

    except Exception as e:
        return f"❌ Xatolik {filename}: {str(e)}"


@tool
def create_folder(foldername: str) -> str:
    """
    Yangi papka yaratish.

    Args:
        foldername: Papka nomi/yo'li (masalan: 'src/components')

    Returns:
        Success yoki error xabari
    """
    try:
        os.makedirs(foldername, exist_ok=True)
        return f"✅ Papka yaratildi: {foldername}"

    except Exception as e:
        return f"❌ Xatolik {foldername}: {str(e)}"


@tool
def read_file(filename: str) -> str:
    """
    Faylni o'qish (mavjud kodlarni ko'rish uchun).

    Args:
        filename: Fayl yo'li

    Returns:
        Fayl kontenti yoki error
    """
    try:
        with open(filename, "r", encoding="utf-8") as f:
            content = f.read()
        return f"📄 {filename}:\n{content}"

    except Exception as e:
        return f"❌ Faylni o'qib bo'lmadi: {str(e)}"


@tool
def list_files(directory: str = ".") -> str:
    """
    Papkadagi fayllarni ko'rish.

    Args:
        directory: Papka yo'li

    Returns:
        Fayllar ro'yxati
    """
    try:
        files = []
        for root, dirs, filenames in os.walk(directory):
            for filename in filenames:
                filepath = os.path.join(root, filename)
                files.append(filepath)

        return f"📂 Fayllar ({len(files)} ta):\n" + "\n".join(files)

    except Exception as e:
        return f"❌ Xatolik: {str(e)}"


# TOOLLAR RO'YXATI
Tools = [create_file_and_write_content, write_file, create_folder, read_file, list_files]

# AGENTNI YARATISH
agent = create_agent(
    model=llm,
    tools=Tools,
    system_prompt=prompt
)

while True:
    user_input = input("\n💬 Siz: ").strip()

    if user_input.lower() in ["exit", "quit", "chiqish"]:
        print("\n👋 Xayr! Yana ko'rishguncha!")
        break

    if not user_input:
        continue

    try:

        result = agent.invoke(
            {"messages": [{"role": "user", "content": user_input}]}
        )
        print(result["messages"][-1].content)

    except Exception as e:
        print(f"\n❌ Xatolik: {str(e)}")
        print("Iltimos, qaytadan urinib ko'ring.")
