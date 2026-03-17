from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import os
import random

# جلب التوكن من Variables
TOKEN = os.getenv("TOKEN")

players = []

ahkam = [
    "احكم على لاعب يغير صورته 😂",
    "احكم على لاعب يكتب رسالة غريبة 😈",
    "احكم على لاعب يطلع من القروب ويرجع 😅",
    "احكم على لاعب يمدح شخص عشوائي 💀",
    "احكم على لاعب يسوي نفسه بنت 😂",
]

# امر /start (ترحيب)
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🔥 هلا بيك ببوت الألعاب!\n\n"
        "الاوامر:\n"
        "/join - دخول اللعبة\n"
        "/players - عرض اللاعبين\n"
        "/ahkam - بدء لعبة احكام 😈"
    )

# دخول اللعبة
async def join(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user.first_name

    if user not in players:
        players.append(user)
        await update.message.reply_text(f"✅ {user} دخل اللعبة!")
    else:
        await update.message.reply_text("❌ انت داخل اصلاً")

# عرض اللاعبين
async def show_players(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not players:
        await update.message.reply_text("❌ ماكو لاعبين بعد")
    else:
        text = "👥 اللاعبين:\n"
        for p in players:
            text += f"- {p}\n"
        await update.message.reply_text(text)

# لعبة احكام
async def play_ahkam(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if len(players) < 2:
        await update.message.reply_text("❌ لازم لاعبين على الاقل")
        return

    chosen = random.choice(players)
    hokm = random.choice(ahkam)

    await update.message.reply_text(
        f"🎯 اللاعب: {chosen}\n"
        f"📜 الحكم: {hokm}"
    )

# تشغيل البوت
app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("join", join))
app.add_handler(CommandHandler("players", show_players))
app.add_handler(CommandHandler("ahkam", play_ahkam))

app.run_polling()
