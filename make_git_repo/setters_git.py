from constants import USER_GIT, ERR_USER_NOT_STR, ERR_OPTION, GIT_OPTION, \
    GIT_SWITCH, PROJECT_NAME, GIT_PUSH, ERR_SPACE
import os

from translate import txt_print


def set_name_project(language):
    try:
        name_repo = str(input(txt_print(language, PROJECT_NAME)))

        while not " " in name_repo:
            return name_repo
        else:
            os.system("cls")
            print(txt_print(language, ERR_SPACE))
            set_name_project(language)
    except OSError as error:
        print(txt_print(language, error))
        set_name_project(language)


def set_user_git(language):
    try:
        user_git = input(txt_print(language, USER_GIT))
        if str(user_git):
            return user_git
        else:
            os.system("cls")
            print(txt_print(language, ERR_USER_NOT_STR))
            set_user_git(language)
    except OSError as error:
        print(txt_print(language, error))
        set_user_git(language)


def set_git_type(language):
    opt = int(input(txt_print(language, GIT_OPTION)))
    try:
        if GIT_SWITCH.get(opt, ) is not None:
            return GIT_SWITCH.get(opt, )
        else:
            print(txt_print(language, ERR_OPTION))
            set_git_type(language)
    except OSError as error:
        print(txt_print(language, error))
        set_git_type(language)


def set_confirm_push(language):
    try:
        confirm = str(input(txt_print(language, GIT_PUSH)))
        if confirm == "y" or confirm == "Y":
            return True
        else:
            return False
    except OSError as error:
        print(txt_print(language, error))
        set_confirm_push(language)
