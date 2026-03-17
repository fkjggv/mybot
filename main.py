import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import random

# جلب التوكن من Railway
TOKEN = "8629733218:AAHrLdHlSE5pOG505XucG8OsrfgRyAppkbg"

if not TOKEN:
    raise ValueError("TOKEN NOT FOUND ❌ تأكد من Variables")

# ---------------- ترحيب ----------------
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    await update.message.reply_text(
        f"هلا {user.first_name} 👋\n"
        "نورت البوت ❤️\n\n"
        "الأوامر:\n"
        "/game - لعبة عشوائية 🎮\n"
        "/ahkam - لعبة أحكام 😈"
    )

# ---------------- لعبة عشوائية ----------------
async def game(update: Update, context: ContextTypes.DEFAULT_TYPE):
    games = [
        "🎯 تحدي: اكتب اسمك مقلوب!",
        "😂 قول نكتة تضحك الكل",
        "🔥 قول سر ماحد يعرفه",
        "🎤 غني سطر من أغنية",
        "📸 صور شي قريب منك"
    ]
    await update.message.reply_text(random.choice(games))

# ---------------- لعبة أحكام ----------------
async def ahkam(update: Update, context: ContextTypes.DEFAULT_TYPE):
    rules = [
        "😈 الحكم: غير اسمك لمدة ساعة",
        "🔥 الحكم: دز فويس واغني",
        "😂 الحكم: اكتب منشور عشوائي",
        "🎭 الحكم: مثل شخصية مشهورة",
        "📞 الحكم: اتصل بصديقك وكله احبك 😂"
    ]
    await update.message.reply_text(random.choice(rules))

# ---------------- تشغيل البوت ----------------
app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("game", game))
app.add_handler(CommandHandler("ahkam", ahkam))

print("Bot is running... 🚀")

app.run_polling()
