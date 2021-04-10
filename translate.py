from textblob import TextBlob


def txt_print(translate, text):
    msg = TextBlob(text)

    if len(translate) > 0:
        msg_translate = msg.translate(from_lang='en', to=translate)
        return msg_translate
    else:
        return msg


map = {
    1: '',
    2: 'es',
    3: 'fr',
    4: 'ja',
}


def map_get_db(opt):
    return map.get(opt, "nothing")


def select_lenguage():
    opt = int(input("Select language [1- ingles | 2- español | 3- frances | 4- japones]: "))
    selected_lang = map_get_db(opt)
    return selected_lang
