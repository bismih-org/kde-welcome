from src.ui.components.package_manager_comp import PackageManagerComp
from src.ui.components.panel_comp import PanelComp
from src.ui.components.screenshot_comp import ScreenShotComp
from src.ui.components.terminal_comp import TerminalComp
from src.ui.components.shortcut_comp import ShortcutComp
from ui.components.browser_comp import BrowserComp
from src.ui.components.sound_comp import SoundComp
from src.ui.components.theme_comp import ThemeComp
from src.ui.components.welcome_comp import WelcomeComp
from src.ui.components.quick_menu_comp import QuickMenuComp
from src.ui.components.communication_comp import CommunicationComp


class Categories:
    def __init__(self):
        self.categories_list = [
            ["Hoş Geldiniz", "browser-svgrepo-com.svg", WelcomeComp()],
            ["Kısa Yollar", "gui-gesture-pinch-close-svgrepo-com.svg", ShortcutComp()],
            ["Paket Yönetimi", "package-svgrepo-com.svg", PackageManagerComp()],
            ["Panel Kullanımı", "panel-top-svgrepo-com.svg", PanelComp()],
            [
                "Hızlı Menü",
                "circle-menu-svgrepo-com.svg",
                QuickMenuComp(),
            ],  # TODO: Gerçek ikonu ekle
            ["Ekran Görüntüsü", "screenshot-mode-svgrepo-com.svg", ScreenShotComp()],
            ["Ses", "sound-volume-2-svgrepo-com.svg", SoundComp()],
            ["Terminal", "terminal-svgrepo-com.svg", TerminalComp()],
            ["Temalar", "paint-roller-svgrepo-com.svg", ThemeComp()],
            ["Tarayıcı", "browser-svgrepo-com.svg", BrowserComp()],
            ["İletişim", "dialog-svgrepo-com.svg", CommunicationComp()],
        ]

    def get_categories(self):
        return self.categories
