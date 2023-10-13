from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext

token = '6480837188:AAGuOMa7Xq8r2Y_Ibk5aOoXqf7dIpmoL-kY'
nombre_usuario = 'jefemaestrobot'

def iniciar(update: Update, context: CallbackContext):
    update.message.reply_text('Hola, soy un bot. ¿En qué puedo ayudarte?')

def ayuda(update: Update, context: CallbackContext):
    update.message.reply_text('Ayuda: Puedes decir "Hola" o "Adiós".')

def personalizado(update: Update, context: CallbackContext):
    update.message.reply_text(update.message.text)

def manejar_respuesta(texto: str):
    texto_procesado = texto.lower()

    if 'hola' in texto_procesado:
        return 'Hola, ¿cómo estás?'
    elif 'adios' in texto_procesado:
        return 'Adiós'
    else:
        return 'No te entiendo'

def manejar_mensaje(update: Update, context: CallbackContext):
    tipo_mensaje = update.message.chat.type
    texto = update.message.text

    if tipo_mensaje == 'group':
        if texto.startswith(nombre_usuario):
            nuevo_texto = texto.replace(nombre_usuario, "")
            respuesta = manejar_respuesta(nuevo_texto)
        else:
            return
    else:
        respuesta = manejar_respuesta(texto)

    update.message.reply_text(respuesta)

def error(update: Update, context: CallbackContext):
    print(context.error)
    update.message.reply_text('Ha ocurrido un error')

if __name__ == '__main__':
    print('Iniciando bot')
    updater = Update(token=token, use_context=True)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', iniciar))
    dispatcher.add_handler(CommandHandler('help', ayuda))
    dispatcher.add_handler(CommandHandler('custom', personalizado))
    dispatcher.add_handler(MessageHandler(filters.text & ~filters.command, manejar_mensaje))
    dispatcher.add_error_handler(error)

    print('Bot iniciado')
    updater.start_polling()
    updater.idle()



# async def error(update: Update, contexto: CallbackContext):
#     print(contexto.error)
#     await update.message.reply_text('Ha ocurrido un error')


# if __name__ == '__main__':
#     print('Iniciando bot')
#     app = Application.builder().token(token).build()

#     app.agregar_manejador(CommandHandler('start', iniciar))
#     app.agregar_manejador(CommandHandler('help', ayuda))
#     app.agregar_manejador(CommandHandler('custom', personalizado))

#     app.agregar_manejador(CommandHandler(filtros.texto & ~FileExistsErroriltros.comando, manejar_mensaje))
#     app.agregar_manejador_error(error)

#     print('Bot iniciado')
#     app.ejecutar_encuesta(intervalo_encuesta=1, tiempo_limite=10)
