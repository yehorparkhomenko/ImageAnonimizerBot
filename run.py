import os

from aiogram import executor, Bot, Dispatcher
from aiogram.types import Message, ContentType, InputFile
from PIL import Image

import utils

TOKEN = ''
bot = Bot(token=TOKEN)
dispatcher = Dispatcher(bot)


@dispatcher.message_handler(commands=['start'])
async def start(message: Message):
    help_text = (
        'Just send me a document that you want to anonymize.'
    )

    await message.answer(help_text)


@dispatcher.message_handler(content_types=[ContentType.DOCUMENT])
async def document_handler(message: Message):
    file_ext = message.document.file_name.split('.')[-1]
    file_path = utils.gen_filepath('static/', file_ext)
    await message.document.download(file_path)

    image_file = open(file_path)
    image = Image.open(image_file)

    # next 3 lines strip exif
    image_data = list(image.getdata())
    image_without_exif = Image.new(image.mode, image.size)
    image_without_exif.putdata(image_data)

    os.remove(file_path)

    image_without_exif.save(file_path)

    await message.answer_document(InputFile(file_path))

    os.remove(file_path)

