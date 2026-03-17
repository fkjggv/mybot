from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
import os
import random

TOKEN = os.getenv("TOKEN")

players = []

ahkam = [
    "سوي مقلب بصديقك 😂",
    "احچي سر بسيط عنك 🤫",
    "غنّي مقطع أغنية 🎤",
    "دز ستيكر مضحك 🤣",
    "اكتب اسم كراش مالك 😏",
    "اختار واحد بالمجموعة وامدحه 💙"
]

# /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user.first_name
    await update.message.reply_text(f"هلا {user} 👋\nنورت البوت 🤖")

# /help
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📌 الأوامر:\n"
        "/start - تشغيل البوت\n"
        "/help - المساعدة\n"
        "/join - دخول لعبة الأحكام\n"
        "/game - بدء اللعبة\n"
        "/reset - تصفير اللاعبين\n"
    )

# ترحيب
async def welcome(update: Update, context: ContextTypes.DEFAULT_TYPE):
    for member in update.message.new_chat_members:
        await update.message.reply_text(f"🎉 هلا {member.first_name} نورت الكروب!")

# دخول لاعب
async def join(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user.first_name
    if user not in players:
        players.append(user)
        await update.message.reply_text(f"{user} دخل اللعبة ✅")
    else:
        await update.message.reply_text("أنت داخل مسبقًا 👍")

# بدء اللعبة
async def game(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if len(players) < 2:
        await update.message.reply_text("لازم لاعبين على الأقل 😅")
        return

    await update.message.reply_text("🎮 لعبة الأحكام بدأت!")

    chosen = random.choice(players)
    rule = random.choice(ahkam)

    await update.message.reply_text(f"👤 اللاعب: {chosen}\n📜 الحكم: {rule}")

# تصفير
async def reset(update: Update, context: ContextTypes.DEFAULT_TYPE):
    players.clear()
    await update.message.reply_text("تم تصفير اللاعبين 🔄")

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("help", help_command))
app.add_handler(CommandHandler("join", join))
app.add_handler(CommandHandler("game", game))
app.add_handler(CommandHandler("reset", reset))
app.add_handler(MessageHandler(filters.StatusUpdate.NEW_CHAT_MEMBERS, welcome))

print("Bot is running...")

app.run_polling()
