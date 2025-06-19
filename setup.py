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
    ("/usr/bin", ["quick-shortcut-panel"]),
    ("/usr/share/applications", ["bismih-welcome.desktop"]),
    # Icons
    (
        "/usr/share/icons/hicolor/scalable/apps/",
        ["data/icons/quick_shortcut_panel.png"],
    ),
    # Main application files
    ("/usr/share/bismih-welcome/", ["main.py"]),
    # Source code
    ("/usr/share/bismih-welcome/src/common", ["src/common/Logging.py"]),
    (
        "/usr/share/bismih-welcome/src/process",
        [
            "src/process/plugin_manager.py",
            "src/process/pro_types.py",
            "src/process/runner.py",
        ],
    ),
    (
        "/usr/share/bismih-welcome/src/static",
        ["src/static/config.py", "src/static/file_paths.py"],
    ),
    (
        "/usr/share/bismih-welcome/src/ui/menu_config",
        ["src/ui/menu_config/config_ui.py", "src/ui/menu_config/piece_node.py"],
    ),
    (
        "/usr/share/bismih-welcome/src/ui/menu_config/process_ui",
        [
            "src/ui/menu_config/process_ui/app_selecetor.py",
            "src/ui/menu_config/process_ui/command_runner_ui.py",
            "src/ui/menu_config/process_ui/short_cut_selector.py",
            "src/ui/menu_config/process_ui/spacial_plugin.py",
        ],
    ),
    ("/usr/share/bismih-welcome/src/ui/panel", ["src/ui/panel/main_panel.py"]),
    ("/usr/share/bismih-welcome/src/ui/theme", ["src/ui/theme/theme_manager.py"]),
    # Data files
    (
        "/usr/share/bismih-welcome/data",
        ["data/menu.json", "data/menu.yaml", "data/theme.qss", "data/version"],
    ),
    (
        "/usr/share/bismih-welcome/data/icons",
        ["data/icons/quick_shortcut_panel.png"],
    ),
    # Prepared plugins
    (
        "/usr/share/bismih-welcome/data/prepared_plugins",
        [
            "data/prepared_plugins/Çeviri.json",
            "data/prepared_plugins/Hoparlör_Eko.json",
            "data/prepared_plugins/Hoparlör_gürültü.json",
            "data/prepared_plugins/Hoparlör_Normal.json",
            "data/prepared_plugins/Mirofon_Gürültü.json",
            "data/prepared_plugins/yazilim_modu.json",
        ],
    ),
]


setup(
    name="quick-shortcut-panel",
    version=version,
    packages=find_packages(),
    scripts=["quick-shortcut-panel"],
    install_requires=["PyQt6", "pyautogui", "coloredlogs", "pyyaml", "pyxdg"],
    data_files=data_files,
    author="Muhammet Halak",
    author_email="halakmuhammet145@gmail.com",
    description="A quick shortcut panel for Linux",
    license="GPLv3",
    keywords="quick-shortcut-panel, quick, panel, hızlı, kısayol",
    url="https://github.com/bismih-org/bismih-welcome",
)
