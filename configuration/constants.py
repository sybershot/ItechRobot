BROWSER_TYPE = "Firefox"
TIMEOUT = 5

DOWNLOADS_PATH = 'project/downloads'
STEAM_URL = 'https://store.steampowered.com/'
LOGIN_URL = 'https://store.steampowered.com/login/'

LOGIN_LINK_LOCATOR = '//a[@class="global_action_link"]'
LOGIN_BUTTON_LOCATOR = '//button[@class="btn_blue_steamui btn_medium login_btn"]'
USERNAME_FIELD_LOCATOR = '//input[@id="input_username"]'
PASSWORD_FIELD_LOCATOR = '//input[@id="input_password"]'
ERROR_MESSAGE_BOX_LOCATOR = '//*[@id="error_display"]'
ERROR_MESSAGE_VISIBLE_LOCATOR = '//*[@id="error_display" and @style=""]'

DOWNLOAD_BUTTON_LOCATOR = '//a[@class="about_install_steam_link"]'
DOWNLOAD_LINK_LOCATOR = '//a[@class="header_installsteam_btn_content"]'

STEAM_GENRE_MENU_LOCATOR = '//div[@id="genre_tab"]'
STEAM_GENRES_LOCATOR = '//div[@class="popup_genre_expand_content responsive_hidden" and @data-genre-group and not(@data-genre-group="themes") and not(@data-genre-group="social_and_players")]'
STEAM_SUBGENRES_LOCATOR = './child::a[@class="popup_menu_item"]'
STEAM_STORE_GAMES_CAROUSEL_LOCATOR = '//div[@class="tab_content_section_ctn"]'
STEAM_STORE_ITEM_LOCATOR = '//div[contains(@id, "NewReleasesRows")]/a[contains(@class, "tab_item")]'
STEAM_SEARCH_BAR_LOCATOR = '//input[@id="store_nav_search_term"]'
STEAM_SEARCH_SUGGEST_LOCATOR = '//div[contains(@class, "search_suggest")]'
