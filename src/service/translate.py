from textblob import TextBlob

from src.service.constants import Messages, Map
from src.service.mapper import mapping


def txt_print(translate, text, check_input):
    msg = TextBlob(text)

    if len(translate) > 0:
        msg_translate = msg.translate(from_lang='en', to=translate)
        if check_input:
            return msg_translate
        else:
            print(msg_translate)
    else:
        if check_input:
            return msg
        else:
            print(msg)


def select_language():
    opt = int(input(Messages.SELECT_LANGUAGE))
    selected_lang = mapping(Map.MAP_LANGUAGE, opt)
    return selected_lang
