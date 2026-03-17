if u.id in waiting_reply:
        if waiting_reply[u.id]["step"]==1:
            waiting_reply[u.id]["word"]=t
            waiting_reply[u.id]["step"]=2
            return await m.reply_text("💬 تمام شنو تريد يكون الرد؟")

        elif waiting_reply[u.id]["step"]==2:
            replies[waiting_reply[u.id]["word"]]=t
            save("replies.json",replies)
            del waiting_reply[u.id]
            return await m.reply_text("✅ تم حفظ الرد")

    # ===== اضافة امر =====
    if t=="اضف امر":
        if not is_admin(u.id):
            return await m.reply_text("❌ للادمن وفوك")
        waiting_command[u.id]={"step":1}
        return await m.reply_text("✍️ شنو الامر؟")

    if u.id in waiting_command:
        if waiting_command[u.id]["step"]==1:
            waiting_command[u.id]["cmd"]=t
            waiting_command[u.id]["step"]=2
            return await m.reply_text("💬 شنو الرد؟")

        elif waiting_command[u.id]["step"]==2:
            commands[waiting_command[u.id]["cmd"]]=t
            save("commands.json",commands)
            del waiting_command[u.id]
            return await m.reply_text("✅ تم حفظ الامر")

    # ===== عرض الاوامر =====
    if t=="الاوامر":
        if not commands:
            return await m.reply_text("ماكو اوامر")
        msg="📜 الاوامر:\n"
        for k in commands:
            msg+=f"- {k}\n"
        return await m.reply_text(msg)

    # ===== حذف امر =====
    if t.startswith("حذف امر"):
        if not is_admin(u.id):
            return
        cmd=t.replace("حذف امر","").strip()
        if cmd in commands:
            del commands[cmd]
            save("commands.json",commands)
            return await m.reply_text("❌ تم حذف الامر")
        else:
            return await m.reply_text("مو موجود")

    # ===== عرض الردود =====
    if t=="الردود":
        if not replies:
            return await m.reply_text("ماكو ردود")
        msg="📜 الردود:\n"
        for k in replies:
            msg+=f"- {k}\n"
        return await m.reply_text(msg)

    # ===== حذف رد =====
    if t.startswith("حذف رد"):
        if not is_admin(u.id):
            return
        word=t.replace("حذف رد","").strip()
        if word in replies:
            del replies[word]
            save("replies.json",replies)
            return await m.reply_text("❌ تم حذف الرد")
        else:
            return await m.reply_text("مو موجود")

    # ===== تنفيذ الردود =====
    if t in replies:
        return await m.reply_text(replies[t])

    # ===== تنفيذ الاوامر =====
    if t in commands:
        return await m.reply_text(commands[t])

    # ===== العاب =====
    if t=="العاب":
        return await m.reply_text("🎮 كلمات / نكته / لو خيروك / كت / احكام")

    if t=="نكته":
        return await m.reply_text(random.choice(jokes))

    if t=="كت":
        return await m.reply_text(random.choice(questions))

    if t=="لو خيروك":
        return await m.reply_text(random.choice(would_you))

# ===== تشغيل =====
app=ApplicationBuilder().token(TOKEN).build()
app.add_handler(MessageHandler(filters.ALL,h))

print("🔥 BOT FINAL DIRECT TOKEN")
app.run_polling()
