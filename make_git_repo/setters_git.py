from constants import USER_GIT, ERR_USER_NOT_STR, ERR_OPTION, GIT_OPTION, \
    GIT_SWITCH, PROJECT_NAME, GIT_PUSH, ERR_SPACE
import os


def set_name_project():
    try:
        name_repo = str(input(PROJECT_NAME))
        while not " " in name_repo:
            return name_repo
        else:
            os.system("cls")
            print(ERR_SPACE)
            set_name_project()
    except OSError as error:
        print(error)
        set_name_project()


def set_user_git():
    try:
        user_git = input(USER_GIT)
        if str(user_git):
            return user_git
        else:
            os.system("cls")
            print(ERR_USER_NOT_STR)
            set_user_git()
    except OSError as error:
        print(error)
        set_user_git()


def set_git_type():
    opt = int(input(GIT_OPTION))
    try:
        if GIT_SWITCH.get(opt, ) is not None:
            return GIT_SWITCH.get(opt, )
        else:
            print(ERR_OPTION)
            set_git_type()
    except OSError as error:
        print(error)
        set_git_type()


def set_confirm_push():
    try:
        confirm = str(input(GIT_PUSH))
        if confirm == "y" or confirm == "Y":
            return True
        else:
            return False
    except OSError as error:
        print(error)
        set_confirm_push()
