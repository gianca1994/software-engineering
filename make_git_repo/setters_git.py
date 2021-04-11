from constants.constants_globals import USER_GIT, ERR_USER_NOT_STR, ERR_OPTION, GIT_OPTION, \
    GIT_SWITCH, PROJECT_NAME, GIT_PUSH, ERR_SPACE, CHECK_YES_NO
import os

from service.translate import txt_print


def set_name_project(language):
    try:
        name_repo = str(input(txt_print(language, PROJECT_NAME, True)))

        while not " " in name_repo:
            return name_repo
        else:
            os.system("cls")
            txt_print(language, ERR_SPACE, False)
            set_name_project(language)
    except OSError as error:
        txt_print(language, error, False)
        set_name_project(language)


def set_user_git(language):
    try:
        user_git = input(txt_print(language, USER_GIT, True))
        if str(user_git):
            return user_git
        else:
            os.system("cls")
            txt_print(language, ERR_USER_NOT_STR, True)
            set_user_git(language)
    except OSError as error:
        txt_print(language, error, False)
        set_user_git(language)


def set_git_type(language):
    opt = int(input(txt_print(language, GIT_OPTION, True)))
    try:
        if GIT_SWITCH.get(opt, ) is not None:
            return GIT_SWITCH.get(opt, )
        else:
            txt_print(language, ERR_OPTION, False)
            set_git_type(language)
    except OSError as error:
        txt_print(language, error, False)
        set_git_type(language)


def set_confirm_push(language):
    try:
        confirm = str(input(txt_print(language, GIT_PUSH, True) + CHECK_YES_NO))
        if confirm == "y" or confirm == "Y":
            return True
        else:
            return False
    except OSError as error:
        txt_print(language, error, False)
        set_confirm_push(language)
