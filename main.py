from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler
import threading
import time

# ✅ CONFIGURAZIONE
TOKEN = '7927897914: AAE0d2ae_TsU_aePp6
my00NosZ3M3V8yigM'  # Inserisci il token del bot di @BotFather
CHANNEL_ID = '-1002171692138'  # Inserisci l'ID corretto del canale privato

# Timer per rimuovere l'utente dopo 30 giorni
def remove_user_after_30_days(user_id, application):
    time.sleep(30 * 24 * 60 * 60)  # 30 giorni in secondi
    try:
        # API Telegram per rimuovere un membro
        application.bot.ban_chat_member(chat_id=CHANNEL_ID, user_id=user_id)
        print(f"✅ Utente {user_id} rimosso dopo 30 giorni.")
    except Exception as e:
        print(f"❌ Errore nella rimozione di {user_id}: {e}")

# Funzione per registrare l'utente e avviare il timer di 30 giorni
async def start(update: Update, context):
    user_id = update.message.from_user.id
    threading.Thread(target=remove_user_after_30_days, args=(user_id, context.application)).start()
    await update.message.reply_text(f"✅ Registrato! Verrai rimosso dal canale dopo 30 giorni.")

# Comando per mostrare gli utenti registrati e il tempo rimanente (utile per debug)
async def list_users(update: Update, context):
    await update.message.reply_text(f"L'ID del canale è {CHANNEL_ID}.\nRimozione utenti attiva dopo 30 giorni.")

# Configura i comandi del bot
def main():
    application = ApplicationBuilder().token(TOKEN).build()

    # Comando per avviare il bot e registrare l'utente
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("list", list_users))

    print("✅ Bot avviato correttamente!")
    application.run_polling()

if __name__ == '__main__':
    main()
