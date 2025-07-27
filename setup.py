#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
import os
import subprocess


changelog = "debian/changelog"
if os.path.exists(changelog):
    head = open(changelog).readline()
    try:
        version = head.split("(")[1].split(")")[0]
    except:
        print("debian/changelog format is wrong for get version")
        version = "0.0.0"
    f = open("data/version", "w")
    f.write(version)
    f.close()


data_files = [
    # Main executable and desktop file
    ("/usr/bin", ["kde-welcome"]),
    ("/usr/share/applications", ["kde-welcome.desktop"]),
    # Icons
    (
        "/usr/share/icons/hicolor/scalable/apps/",
        ["data/icons/kde-welcome.svg"],
    ),
    # Main application files
    ("/usr/share/kde-welcome/", ["main.py"]),
    # Source code - static
    ("/usr/share/kde-welcome/src/static", ["src/static/config.py"]),
    # Source code - theme
    ("/usr/share/kde-welcome/src/theme", ["src/theme/theme_manager.py"]),
    ("/usr/share/kde-welcome/src/theme/icons", [
        "src/theme/icons/branch-closed.png",
        "src/theme/icons/branch-open.png",
        "src/theme/icons/check-white.png"
    ]),
    # Source code - UI
    ("/usr/share/kde-welcome/src/ui", [
        "src/ui/categories.py",
        "src/ui/main_window.py"
    ]),
    # Source code - UI components
    ("/usr/share/kde-welcome/src/ui/components", [
        "src/ui/components/browser_comp.py",
        "src/ui/components/communication_comp.py",
        "src/ui/components/layout_sellector_comp.py",
        "src/ui/components/main_comp_widget.py",
        "src/ui/components/package_manager_comp.py",
        "src/ui/components/panel_comp.py",
        "src/ui/components/quick_menu_comp.py",
        "src/ui/components/screenshot_comp.py",
        "src/ui/components/shortcut_comp.py",
        "src/ui/components/sound_comp.py",
        "src/ui/components/system_improve_comp.py",
        "src/ui/components/terminal_comp.py",
        "src/ui/components/theme_comp.py",
        "src/ui/components/welcome_comp.py"
    ]),
    # Source code - UI widgets
    ("/usr/share/kde-welcome/src/ui/widgets", [
        "src/ui/widgets/BLabel.py",
        "src/ui/widgets/gif_viewer.py"
    ]),
    # Data files - theme
    ("/usr/share/kde-welcome/data", ["data/theme.qss"]),
    # Data files - icons
    ("/usr/share/kde-welcome/data/icons", [
        "data/icons/browser-svgrepo-com.svg",
        "data/icons/circle-menu-svgrepo-com.svg",
        "data/icons/dialog-svgrepo-com.svg",
        "data/icons/gui-gesture-pinch-close-svgrepo-com.svg",
        "data/icons/home-1-svgrepo-com.svg",
        "data/icons/layout-16-svgrepo-com.svg",
        "data/icons/LICENSE",
        "data/icons/package-svgrepo-com.svg",
        "data/icons/paint-roller-svgrepo-com.svg",
        "data/icons/panel-top-svgrepo-com.svg",
        "data/icons/quick_shortcut_panel.png",
        "data/icons/quick_shortcut_panel.svg",
        "data/icons/screenshot-mode-svgrepo-com.svg",
        "data/icons/sound-volume-2-svgrepo-com.svg",
        "data/icons/system-settings-svgrepo-com.svg",
        "data/icons/terminal-svgrepo-com.svg"
    ]),
    # Data files - images
    ("/usr/share/kde-welcome/data/images", [
        "data/images/kde_icon_dark.png",
        "data/images/kde_icon_dark.svg",
        "data/images/kde_icon_light.png",
        "data/images/kde_icon_light.svg",
        "data/images/zen_browser.png"
    ]),
    ("/usr/share/kde-welcome/data/images/gestures", [
        "data/images/gestures/2gesture_d.png",
        "data/images/gestures/2gesture_l.png",
        "data/images/gestures/3gesture_d.png",
        "data/images/gestures/3gesture_l.png",
        "data/images/gestures/4gesture_d.png",
        "data/images/gestures/4gesture_l.png"
    ]),
    # Data files - gifs
    ("/usr/share/kde-welcome/data/gifs", [
        "data/gifs/ekran.gif",
        "data/gifs/ekran_yazi.gif",
        "data/gifs/kesfet.gif",
        "data/gifs/krunner.gif",
        "data/gifs/menu.gif",
        "data/gifs/nala.gif",
        "data/gifs/ozel_panel.gif",
        "data/gifs/panel.gif",
        "data/gifs/panel_ust.gif",
        "data/gifs/pardus_magasa.gif",
        "data/gifs/ses_alt.gif",
        "data/gifs/tema.gif",
        "data/gifs/terminal.gif"
    ]),
    # Test gif
    ("/usr/share/kde-welcome/data", ["data/test.gif"]),
]


setup(
    name="kde-welcome",
    version=version,
    packages=find_packages(),
    scripts=["kde-welcome"],
    install_requires=["PyQt6", "pyautogui", "coloredlogs", "pyyaml", "pyxdg"],
    data_files=data_files,
    author="Muhammet Halak",
    author_email="halakmuhammet145@gmail.com",
    description="kde Welcome Application",
    license="GPLv3",
    keywords="kde-welcome, welcome, hoşgeldin, karşılama",
    url="https://github.com/kde-org/kde-welcome",
)