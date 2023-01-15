from crawler import LinkCrawler, DataCrawler
import sys

if __name__ == '__main__':
    switch = sys.argv[1]
    if switch == 'find_links':
        crawler = LinkCrawler()
        crawler.start()
    elif switch == 'extract_pages':
        crawler = DataCrawler()
        crawler.start()
