from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support.ui import WebDriverWait
import time

class YaroomScrap(object):
    def __init__(self) -> None:
        super().__init__()
        opts = ChromeOptions()
        # opts.add_argument("--headless")
        self.driver = webdriver.Chrome(options=opts)
        self.roomdic = {
            'AB':16959,
            'CC':16960,
            'IB':36669
        }
        self.wait = WebDriverWait(self.driver,10)
        # print(self.driver.page_source)

    def loginGuest(self):
        self.driver.get(r'https://dku.yarooms.com/account/login?return=https:%2F%2Fdku.yarooms.com%2Fschedule%2Fweekly%3Flocation%3D16959')
        self.wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR,r'#wrapper > div.content > div > div:nth-child(1) > div.login-right > form > a > span'))
        ).click()
        time.sleep(10)

    def ScrapeRoom(self, Room, numWeek):
        self.driver.get('https://dku.yarooms.com/schedule/weekly?location={}'.format(self.roomdic[Room]))
        avail_dic = dict()
        for i in range(2):

            table = self.wait.until(
                EC.visibility_of_element_located((By.CSS_SELECTOR,r'#content'))
            )

            time.sleep(30)
            relativeDiv = table.find_element_by_css_selector(r'div.tleft.weekly').find_element_by_css_selector(r'div.relative')
            rowRooms = relativeDiv.find_elements_by_css_selector(r'div.trow.room')
            # print(relativeDiv.get_attribute('innerHTML'))

            roomLst = [rowRoom.find_element_by_css_selector(r'div.name').get_attribute('title') for rowRoom in rowRooms ]
            roomNum = len(roomLst)
            lftTable = table.find_element_by_css_selector(r'div.tright.weekly.expanded')
            divRs = lftTable.find_elements_by_css_selector(r'div:not(.heading-row) div.trow')
            for i in range(roomNum + 1):
                print(i)
                if (i == 0):
                    continue
                divCell = divRs[i].find_elements_by_css_selector(r'div.cell')[numWeek - 1]
                print(divCell.find_elements_by_css_selector('span.no.faded'))
                # print(divCell.get_attribute('innerHTML'))
                if( divCell.find_elements_by_css_selector('span.no.faded') ):
                    avail_dic[roomLst[i-1]] = None
                else:
                    # time.sleep(5)
                    divSchedule = divCell.find_element_by_css_selector(r'div.schedule-meetings')
                    print(divSchedule.get_attribute('innerHTML'))
                    reservLst = divSchedule.find_element_by_css_selector(r'a').get_attribute('ya-tooltip').split("<br>")
                    avail_dic[roomLst[i-1]] = {
                        'reserver' : reservLst[0],
                        'time' : reservLst[1]
                    }

            print(avail_dic)

            if((Room == 'CC') or (i == 1)):
                return
            else:
                time.sleep(10)
                self.wait.until(
                    EC.visibility_of_element_located((By.CSS_SELECTOR,r'#pageView2 > a'))
                ).click()


def main():
    scraper = YaroomScrap()
    scraper.loginGuest()
    scraper.ScrapeRoom('AB',4)
    time.sleep(10)

if __name__ == '__main__' :
    main()