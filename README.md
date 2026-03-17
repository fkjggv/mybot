import json
import random
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

TOKEN = "8629733218:AAHrLdHlSE5pOG505XucG8OsrfgRyAppkbg"
OWNER_ID = 8203532937

print("BOT WARKING")
# ===== تحميل =====
def load(file):
    try:
        return json.load(open(file))
    except:
        return {}

def save(file, data):
    json.dump(data, open(file, "w"))

replies = load("replies.json")
commands = load("commands.json")
ranks = load("ranks.json")

waiting_reply = {}
waiting_command = {}

# ===== الرتب =====
def get_rank(uid):
    if uid == OWNER_ID:
        return "مطور"
    return ranks.get(str(uid), "عضو")

def is_admin(uid):
    return get_rank(uid) in ["مطور", "مالك اساسي", "مالك", "مدير", "ادمن"]

# ===== محتوى =====
jokes = [f"😂 نكتة رقم {i}" for i in range(1, 26)]
questions = [f"🤔 سؤال رقم {i}" for i in range(1, 26)]
would_you = [f"😏 لو خيروك رقم {i}" for i in range(1, 26)]

# ===== البوت =====
async def handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    m = update.message
    if not m or not m.text:
        return

    u = update.effective_user
    t = m.text

    # ===== سلام =====
    if "السلام عليكم" in t:
        return await m.reply_text("وعليكم السلام ❤️")

    # ===== ايدي =====
    if t == "ايدي":
        return await m.reply_text(f"👤 {u.first_name}\n🆔 {u.id}")

    # ===== ردود ثابتة =====
    if "بوت" in t:
        return await m.reply_text("اسمي خالد مو بوت 😒")

    # ===== اضافة رد =====
    if t == "اضف رد":
        if not is_admin(u.id):
            return await m.reply_text("❌ بس للادمن وفوك")
        waiting_reply[u.id] = {"step": 1}
        return await m.reply_text("✍️ شتريد تضيف؟")

    if u.id in waiting_reply:
        if waiting_reply[u.id]["step"] == 1:
            waiting_reply[u.id]["word"] = t
            waiting_reply[u.id]["step"] = 2
            return await m.reply_text("💬 شنو الرد؟")

        elif waiting_reply[u.id]["step"] == 2:
            replies[waiting_reply[u.id]["word"]] = t
            save("replies.json", replies)
            del waiting_reply[u.id]
            return await m.reply_text("✅ تم حفظ الرد")

    # ===== حذف رد =====
    if t.startswith("حذف رد"):
        if not is_admin(u.id):
            return
        word = t.replace("حذف رد", "").strip()
        if word in replies:
            del replies[word]
            save("replies.json", replies)
            return await m.reply_text("❌ تم حذف الرد")

    if t == "الردود":
        return await m.reply_text("\n".join(replies.keys()) or "ماكو ردود")

    # ===== اوامر =====
    if t == "اضف امر":
        if not is_admin(u.id):
            return await m.reply_text("❌ بس للادمن")
        waiting_command[u.id] = {"step": 1}
        return await m.reply_text("✍️ شنو الامر؟")

    if u.id in waiting_command:
        if waiting_command[u.id]["step"] == 1:
            waiting_command[u.id]["cmd"] = t
            waiting_command[u.id]["step"] = 2
            return await m.reply_text("💬 شنو الرد؟")

        elif waiting_command[u.id]["step"] == 2:
            commands[waiting_command[u.id]["cmd"]] = t
            save("commands.json", commands)
            del waiting_command[u.id]
            return await m.reply_text("✅ تم حفظ الامر")

    if t.startswith("حذف امر"):
        if not is_admin(u.id):
            return
        cmd = t.replace("حذف امر", "").strip()
        if cmd in commands:
            del commands[cmd]
            save("commands.json", commands)
            return await m.reply_text("❌ تم حذف الامر")

    if t == "الاوامر":
        return await m.reply_text("\n".join(commands.keys()) or "ماكو اوامر")

    # ===== تنفيذ =====
    if t in replies:
        return await m.reply_text(replies[t])

    if t in commands:
        return await m.reply_text(commands[t])

    # ===== العاب =====
    if t == "العاب":
        return await m.reply_text("🎮 نكته / كت / لو خيروك / احكام")

    if t == "نكته":
        return await m.reply_text(random.choice(jokes))

    if t == "كت":
        return await m.reply_text(random.choice(questions))
