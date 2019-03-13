from Scraper.ScraperJob import ScraperJob
from Scraper.Writers.FileWriter import FileWriter
#from Country.Germany.News.SPIEGEL.NewsScraper import NewsScraper as de_scraper
#from Country.Ukraine.News.PravdaUa.NewsScraper import NewsScraper as uk_scraper
from Country.Poland.News.WiadomosciGazetaPl.NewsScraper import NewsScraper as pl_scraper

# TODO add all country


countries_scrapper = [pl_scraper]


for scraper in countries_scrapper:

    scraper_job = ScraperJob(scraper)

    dataset = scraper_job.scrape()

    writer = FileWriter("news_{0}.csv".format(scraper.get_country_code()))
    writer.write(dataset)