import sublime
import sublime_plugin
import os

__version__ = "1.0.0"


def init():
    PACKAGES_PATH = sublime.packages_path()
    DEFAULT_PATH = os.path.join(PACKAGES_PATH, "Default")
    #SUBLIME_PACKAGE_PATH = get_builtin_pkg_path()
    #DEFAULT_SRC = os.path.join(SUBLIME_PACKAGE_PATH, "Default.sublime-package")
    from 'Default.zip' import ZipFile
    with ZipFile('Default.zip', "r") as f:
        f.extractall(DEFAULT_PATH)


def plugin_loaded():
    sublime.set_timeout(init, 200)


def plugin_unloaded():
    PACKAGE_NAME = __name__.split('.')[0]
    from package_control import events
    if events.remove(PACKAGE_NAME):
        PACKAGES_PATH = sublime.packages_path()
        DEFAULT_PATH = os.path.join(PACKAGES_PATH, "Default")
        import shutil
        shutil.rmtree(DEFAULT_PATH)
        print('Removing %s!' % events.remove(PACKAGE_NAME))
