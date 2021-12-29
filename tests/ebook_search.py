from pages.initial_steps import InitialSteps
from bs4 import BeautifulSoup
from requests import get
import pytest


URL = 'https://www.salesmanago.pl/info/knowledgecenter.htm'
page = get(URL)

soup = BeautifulSoup(page.content, 'html.parser')
resoults = soup.find_all("div", class_="ebook__img--container")
records = []

for result in resoults:
    link = result.find('a', href=True)
    records.append(link['href'])


def find_url(filtered_url):
    filtered_urls = []
    for i, url in enumerate(records):
        for val in filtered_url.split():
            if val in url:
                filtered_urls.append(i)
    return records[max(set(filtered_urls), key=filtered_urls.count)]


@pytest.mark.usefixtures('setup')
class TestEbookSearch:

    @pytest.mark.parametrize('search_query', ["Kompletny przewodnik po Headless Commerce"])
    def test_initial(self, search_query):
        initial = InitialSteps(self.driver)

        # hovers over the menu and select EBOOK
        initial.firstSteps(self.driver)

        # chooses EBOOK
        self.driver.get(find_url(search_query))

        # completes the form fields
        initial.fill_in("Mateusz Kaleta",
                        "mateusz.kaleta.benhauer+testrekrutacja@salesmanago.com",
                        "mkpresetss", "799041521", "mkprestess.pl")

        # download button
        initial.click_download_button(self.driver)
