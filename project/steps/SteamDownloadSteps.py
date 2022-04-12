from robot.api.deco import keyword

from project.page_objects.steam_download_page import SteamDownloadPage
from project.page_objects.steam_main_page import SteamMainPage


class SteamDownloadSteps:

    @staticmethod
    @keyword(name="Go to download page")
    def go_to_download_page():
        page = SteamMainPage()
        page.click_install_steam()

    @staticmethod
    @keyword(name="Click download button")
    def click_download_button():
        page = SteamDownloadPage()
        page.download()
