from constants import Constants
from infi.systray import SysTrayIcon

application_icon_path = f"{Constants.PROJECT_DIRECTORY}{Constants.SEPARATOR_CHAR}icons{Constants.SEPARATOR_CHAR}python_icon.ico"


def hello(sys_tray_icon):
    print("Hello World.")

def example_setting_1(sys_tray_icon):
    print("Example setting 1 clicked")


def example_setting_2(sys_tray_icon):
    print("Example setting 2 clicked")


def exit_application(sys_tray_icon):
    # Whatever we need to take care of before application exits
    exit()


def do_nothing(sys_tray_icon):
    pass


menu_options = (('Say Hello', application_icon_path, hello),
                ("Settings", application_icon_path, (("Example setting 1", application_icon_path, example_setting_1),
                                                     ("Example setting 2", application_icon_path, example_setting_2),
                                                     ))
                )

sysTrayIcon = SysTrayIcon(application_icon_path, Constants.PROJECT_NAME,
                          menu_options, on_quit=exit_application, default_menu_index=1)
sysTrayIcon.start()
