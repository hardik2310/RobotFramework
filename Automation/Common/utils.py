import os
import shutil
from datetime import datetime


def sort_dates_in_list(list_of_dates):
    list_of_dates.sort(key=lambda date: datetime.strptime(date, "%d/%m/%Y"))


def create_profile(download_path, browser):
    if browser.lower() == 'ff' or browser.lower() == 'firefox':
        from selenium.webdriver.firefox.options import Options
        options = Options()
        options.set_preference("browser.download.dir", download_path)
        options.set_preference("browser.download.folderList", 2)
        options.set_preference("browser.download.manager.showWhenStarting", False)
        options.set_preference("browser.helperApps.neverAsk.openFile", True)
        options.set_preference("browser.helperApps.neverAsk.saveToDisk", "text/csv")
        return options
    elif browser.lower() == 'chrome' or browser.lower() == 'googlechrome':
        from selenium.webdriver.chrome.options import Options
        options = Options()
        options.add_experimental_option("prefs", {
            "download.default_directory": download_path,
            "download.prompt_for_download": False,
        })
        return options
