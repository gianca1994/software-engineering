from textblob import TextBlob

from src.service.constants import Messages, Map
from src.service.mapper import mapping


def txt_print(translate, text, check_input):
    """
    This function receives by parameter, 'translate': the language to which it is
    going to translate. 'text': the content of the message, all these come from
    file 'constants.py' and finally 'check_input': it is a boolean which It tells
    us if this message is going to be shown as a print or if it is going to go to
    a function 'input', if true, the translated message is returned otherwise, it
    is printed.
    """
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
    """
    Method to select the language in which to display all the messages,
    we do the mapping with the option that the user chooses and we return
    the language you chose.
    """
    opt = int(input(Messages.SELECT_LANGUAGE))
    selected_lang = mapping(Map.LANGUAGE_MAP, opt)
    return selected_lang
