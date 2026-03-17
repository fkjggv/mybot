import random
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

TOKEN = "8629733218:AAHrLdHlSE5pOG505XucG8OsrfgRyAppkbg"
OWNER_ID = 8203532937

print("BOT WORKING")

app = ApplicationBuilder().token(TOKEN).build()

games = {}

# ===== نكت =====
jokes = [f"😂 نكتة رقم {i}" for i in range(1,26)]

# ===== كت =====
questions_game = [f"🤔 سؤال كت رقم {i}" for i in range(1,26)]

# ===== لو خيروك =====
would_you = [f"😏 لو خيروك رقم {i}" for i in range(1,26)]

# ===== اسئلة =====
questions = [f"❓ سؤال عام رقم {i}" for i in range(1,26)]

# ===== البوت =====
async def reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    m = update.message
    if not m or not m.text:
        return

    user = m.from_user
    chat_id = m.chat_id
    text = m.text.lower()

    # ===== ردود =====
    if "هلا" in text:
        return await m.reply_text("هلا بيك 👋")

    if "بوت" in text:
        return await m.reply_text("اسمي خالد مو بوت 😒")

    if "ايدي" in text:
        return await m.reply_text(f"🆔 {user.id}")

    # ===== عرض الالعاب =====
    if text == "الالعاب":
        return await m.reply_text("🎮 نكته / كت / لو خيروك / اسئله / احكام")

    # ===== نكته =====
    if "نكته" in text:
        return await m.reply_text(random.choice(jokes))

    # ===== كت =====
    if "كت" in text:
        return await m.reply_text(random.choice(questions_game))

    # ===== لو خيروك =====
    if "لو خيروك" in text:
        return await m.reply_text(random.choice(would_you))

    # ===== اسئلة =====
    if "اسئله" in text:
        return await m.reply_text(random.choice(questions))

    # ===== بدء احكام =====
    if text == "احكام":
        games[chat_id] = {
            "owner": user.id,
            "players": [user.id]
        }

        return await m.reply_text(
            "🎯 تم بدء اللعبة وتم تسجيلك\n\n"
            "• اللي بيلعب يرسل (انا)"
        )

    # ===== تسجيل لاعب =====
    if text == "انا":
        if chat_id in games:
            if user.id not in games[chat_id]["players"]:
                games[chat_id]["players"].append(user.id)
                return await m.reply_text("✅ تم اضافتك")
            else:
                return await m.reply_text("❌ انت مسجل")

    # ===== اختيار =====
    if text == "نعم":
        if chat_id in games:
            if user.id != games[chat_id]["owner"]:
                return await m.reply_text("❌ بس صاحب اللعبة")

            players = games[chat_id]["players"]

            if len(players) < 2:
                return await m.reply_text("❌ لازم لاعبين على الاقل")

            p1, p2 = random.sample(players, 2)

            await m.reply_text(
                f"👑 الحاكم: {p1}\n😈 المحكوم: {p2}"
            )

            games.pop(chat_id)

# ===== تشغيل =====
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, reply))

app.run_polling()
