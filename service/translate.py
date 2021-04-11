from textblob import TextBlob

from constants.constants_globals import MAP_LANGUAGE, SELECT_LANGUAGE


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


def map_get_db(opt):
    return MAP_LANGUAGE.get(opt, "nothing")


def select_lenguage():
    opt = int(input(SELECT_LANGUAGE))
    selected_lang = map_get_db(opt)
    return selected_lang
