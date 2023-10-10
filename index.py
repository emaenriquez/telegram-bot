

from telegram import Update
from telegram.ext import Applicacion, ComandoManejador, ManejadorMensaje, Filtros, TiposContexto

token = '6480837188:AAGuOMa7Xq8r2Y_Ibk5aOoXqf7dIpmoL-kY'
nombre_usuario = 'jefemaestrobot'

async def iniciar(update: Update, contexto: TiposContexto):
    await update.message.reply_text('Hola, soy un bot. ¿En qué puedo ayudarte?')

async def ayuda(update: Update, contexto: TiposContexto):
    await update.message.reply_text('Ayuda: Puedes decir "Hola" o "Adiós".')


async def personalizado(update: Update, contexto: TiposContexto):
    await update.message.reply_text(update.message.text)


def manejar_respuesta(texto: str, contexto: TiposContexto, update: Update):
    texto_procesado = texto.lower()

    if 'hola' in texto_procesado:
        return 'Hola, ¿cómo estás?'
    elif 'adios' in texto_procesado:
        return 'Adiós'
    else:
        return 'No te entiendo'


async def manejar_mensaje(update: Update, contexto: TiposContexto):
    tipo_mensaje = update.message.chat.type
    texto = update.message.text

    if tipo_mensaje == 'group':
        if texto.startswith(nombre_usuario):
            nuevo_texto = texto.replace(nombre_usuario, "")
            respuesta = manejar_respuesta(nuevo_texto, contexto, update)
        else:
            return
    else:
        respuesta = manejar_respuesta(texto, contexto, update)

    await update.message.reply_text(respuesta)


async def error(update: Update, contexto: TiposContexto):
    print(contexto.error)
    await update.message.reply_text('Ha ocurrido un error')


if __name__ == '__main__':
    print('Iniciando bot')
    app = Applicacion.builder().token(token).build()

    app.agregar_manejador(ComandoManejador('start', iniciar))
    app.agregar_manejador(ComandoManejador('help', ayuda))
    app.agregar_manejador(ComandoManejador('custom', personalizado))

    app.agregar_manejador(ManejadorMensaje(Filtros.texto & ~Filtros.comando, manejar_mensaje))
    app.agregar_manejador_error(error)

    print('Bot iniciado')
    app.ejecutar_encuesta(intervalo_encuesta=1, tiempo_limite=10)
