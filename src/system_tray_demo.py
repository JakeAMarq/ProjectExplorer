from infi.systray import SysTrayIcon
from path_utils import get_project_root_path

application_icon_path = get_project_root_path() + "\\icons\\" + "python_icon.ico"
hover_text = "SysTrayIcon Demo"


def hello(sys_tray_icon):
    print("Hello World.")


def simon(sys_tray_icon):
    print("Hello Simon.")


def bye(sys_tray_icon):
    print("Bye, then.")


def do_nothing(sys_tray_icon):
    pass


menu_options = (('Say Hello', application_icon_path, hello),
                ('Do nothing', None, do_nothing),
                ('A sub-menu', application_icon_path, (('Say Hello to Simon', application_icon_path, simon),
                                                       ('Do nothing', None, do_nothing),
                                                       ))
                )
sysTrayIcon = SysTrayIcon(application_icon_path, hover_text, menu_options, on_quit=bye, default_menu_index=1)
sysTrayIcon.start()
