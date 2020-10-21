from datetime import datetime
from selenium import webdriver


def sort_dates_in_list(list_of_dates):
    list_of_dates.sort(key=lambda date: datetime.strptime(date, "%d/%m/%Y"))


def create_profile(download_path, browser):
    browser_profile = None
    if browser.lower() == 'ff' or browser.lower() == 'firefox':
        browser_profile = webdriver.FirefoxProfile()
        browser_profile.set_preference("browser.download.dir", download_path)
        browser_profile.set_preference("browser.download.folderList", 2)
        browser_profile.set_preference("browser.helperApps.neverAsk.openFile", False)
        browser_profile.set_preference("browser.helperApps.neverAsk.openFile",
                                       "application/pdf,text/plain,application/octet-stream,application/x-pdf,application/vnd.pdf,application/vnd.openxmlformats-officedocument.spreadsheethtml,text/csv,text/html,application/x-msexcel,application/excel,application/x-excel,application/vnd.ms-excel")
        browser_profile.set_preference("browser.helperApps.neverAsk.saveToDisk",
                                       "application/pdf,text/plain,application/octet-stream,application/x-pdf,application/vnd.pdf,application/vnd.openxmlformats-officedocument.spreadsheethtml,text/csv,text/html,application/x-msexcel,application/excel,application/x-excel,application/vnd.ms-excel")
        browser_profile.set_preference("browser.helperApps.alwaysAsk.force", False)
        browser_profile.update_preferences()
    return browser_profile
