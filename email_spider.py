# import logging
# import os
# import pandas as pd
# import re
# import scrapy
# from scrapy.crawler import CrawlerProcess
# from scrapy.linkextractors.lxmlhtml import LxmlLinkExtractor
# # from googlesearch import search
#
# logging.getLogger('scrapy').propagate = False
#
# path='C:/Users/abdi/PycharmProjects/EmailScraping/email_scrape/email_scrape/emails.csv'
# # def get_urls(tag, n, language):
# #     urls = [url for url in search(tag, stop=n, lang=language)][:n]
# #     return urls
#
#
#
#
# # get_urls('movie rating', 5, 'en')
# # mail_list = re.findall(‘\w +
# #
# #
# # @
# #
# # \w +\.{1}\w +’, html_text)
#
# class MailSpider(scrapy.Spider):
#     name = 'email'
#     google_urls = ['http://www.autaugaacademy.com/information/staff.cfm',
#                    'https://www.autaugavilleschool.com/schoolstaff',
#                    'https://www.bsk12.net/schoolfaculty',
#                    'https://4pca.org/staff/',
#                    'https://www.gophslions.com/staff',
#                    'https://www.marburyhighschool.org/facultyandstaff']
#     print("ok1..")
#     def parse(self, response):
#
#         links = LxmlLinkExtractor(allow=()).extract_links(response)
#         links = [str(link.url) for link in links]
#         links.append(str(response.url))
#
#         for link in links:
#             yield scrapy.Request(url=link, callback=self.parse_link)
#
#     def parse_link(self, response):
#
#         for word in self.reject:
#             if word in str(response.url):
#                 return
#         print("ok2...")
#         html_text = str(response.text)
#         mail_list = re.findall('\w+@\w+\.{1}\w+', html_text)
#
#         dic = {'email': mail_list, 'link': str(response.url)}
#         df = pd.DataFrame(dic)
#
#         df.to_csv(self.path, mode='a', header=False)
#         df.to_csv(self.path, mode='a', header=False)
#
#
# # yield scrapy.Request(url=link, callback=self.parse_link)
#
#
#
# def ask_user(question):
#     response = input(question + ' y/n' + '\n')
#     if response == 'y':
#         return True
#     else:
#         return False
#
#
# def create_file(path):
#     response = False
#     if os.path.exists(path):
#         response = ask_user('File already exists, replace?')
#         if response == False: return
#
#     with open(path, 'wb') as file:
#         file.close()
#
# print("here is ok..")
# def get_info(tag, n, language, path, reject=[]):
#     create_file(path)
#     df = pd.DataFrame(columns=['email', 'link'], index=[0])
#     df.to_csv(path, mode='w', header=True)
#     print('Searching for emails...')
#     process = CrawlerProcess({'USER_AGENT': 'Mozilla/5.0'})
#     process.crawl(MailSpider, start_urls=google_urls, path=path, reject=reject)
#     process.start()
#
#     print('Cleaning emails...')
#     df = pd.read_csv(path, index_col=0)
#     df.columns = ['email', 'link']
#     df = df.drop_duplicates(subset='email')
#     df = df.reset_index(drop=True)
#     df.to_csv(path, mode='w', header=True)
#
#     return df
import scrapy
from scrapy import Request
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy.crawler import CrawlerProcess
import  re
import pandas as pd
from scrapy.spidermiddlewares.httperror import HttpError
from twisted.internet.error import DNSLookupError
from twisted.internet.error import TimeoutError, TCPTimedOutError
from urllib.parse import urlparse
from scrapy.exceptions import CloseSpider
class H1SpiderSpider(scrapy.Spider):
    name = 'email_scrape'
    # allowed_domains = ['www.almasd.net']
    temp_domain = []
    # with open('domain1.txt', 'r') as f:
    #     for i in range(1,2):
    #         k = f.readline().rstrip(',\n')
    #         start_urls.append(k)
    #         allowed_domains.append(urlparse(k).netloc)
    #     # self.allowed_domains =
    #     print(start_urls,"this will be scraped",'\n',len(start_urls),'\n',allowed_domains,'\n',len(allowed_domains))
    # # start_urls = ['https://www.huntsvillecityschools.org/schools/jemison-high-school/quasonya-johnson']
    # start_urls = [
    #     # 'https://westbloctonhighschool.com/contact-us/',
    #     # 'http://www.appalachianeagles.com/staff_directory',
    #     # 'http://www.clevelandhighschool.net/staff_directory'
    #     # 'https://www.butlerco.k12.al.us/domain/2089'
    #     # 'http://www.haydenhigh.net/staff_directory',
    #     # 'https://www.eufaulacityschools.org/domain/158'
    # ]
    # def start_requests(self):
    #     for u in self.start_urlss:
    #         # self.allowed_domains = []
    #         # dem = self.temp_domain[self.start_urls.index(u)]
    #         # self.allowed_domains.append(dem)
    #         yield scrapy.Request(u, callback=self.parse_item,
    #                                 errback=self.errback_httpbin)
    # start_urls = ['https://books.toscrape.com/']
    #it will crawl this whole subdomain
    # allowed_domains = ['clevelandhighschool.net']
        # ,'haydenhigh.net',
        #                'eufaulacityschools.org']
    startt_urls=[]

    def __init__(self,start):
        self.startt_urls=start
    # data = read_csv("Links - Sheet1.csv")
    # urls = data['Faculty link'].tolist()


    # rules = [
    #     Rule(LinkExtractor(
    #         allow=['.*']),
    #          callback='parse_item',
    #          follow=True)
    #     ]
    def start_requests(self):
        for url in self.startt_urls:
            yield scrapy.Request(url,callback=self.parse_item, errback=self.errback_httpbin)
        # start_urls = ['http://books.toscrape.com/']
   
    print("test 0 passed...")
    listrepeatedpages = []
    countrepeated = 0
    countall = 0
    listpages = []
    listrepeatedpages = []
    scraped_emails = []
    count_duplicate_emails =0
    countstart = 0
    def parse_item(self, response):
        emails_in_start_url = 0
        string = ''

        if response.url in self.startt_urls:
            emails_in_start_url = 0
            self.countstart+=1
            string = response.url
        if response.url in self.listpages:
            print("the page is repeated.")
            self.listrepeatedpages.append(response.url)
            self.countrepeated+=1
        else:
            self.listpages.append(response.url)
            self.countall+=1
            print(" a new page..")
            print("the number of all pages: ", self.countall)
            htmltext = str(response.text)
            print("html contentreceived\n")
            item = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', htmltext)
            for i in item:
                emaillist =[]
                links=[]
                if i in self.scraped_emails:
                    print("duplicate.. total",self.count_duplicate_emails)
                    self.count_duplicate_emails+=1
                else:

                    print("new email..")
                    print(i,"scraped from ", response.url)
                    self.scraped_emails.append(i)
                    emails_in_start_url+=1
                    print("the final emaillist:", self.scraped_emails)
                    print("legit emails:",len(self.scraped_emails))
                    emaillist.append(i)
                    links.append(response.url)
                    print(emaillist)
                    dic1 = {
                        'emails' : emaillist,
                        'links' : links
                    }
                    df = pd.DataFrame(dic1)
                    #print(df)
                    #f = open("emails.csv", "w")
                    with open('crawler_string_emails.csv','a') as f:
                        df.to_csv(f, mode='a', header=False)
                print(len(self.startt_urls))
                continue
                print("function is continuing...")
            # continue
                file1 = open("myfile.txt", "a")  # append mode
                final = string +" has " + str(emails_in_start_url)
                file1.writelines(final)
    print('number of start urls scanned',countstart )
    def errback_httpbin(self, failure):
        # log all failures
        self.logger.error(repr(failure))
        file1 = open("errorlogs.txt", "a")  # append mode

        # in case you want to do something special for some errors,
        # you may need the failure's type:

        if failure.check(HttpError):
            # these exceptions come from HttpError spider middleware
            # you can get the non-200 response
            response = failure.value.response
            self.logger.error('HttpError on %s', response.url)
            print(response.url,"does not content non 200 get is not working")
            str = response.url +'has ' + 'non 200 response' +'HTTP error\n'
            file1.writelines(str)
        elif failure.check(DNSLookupError):
            # this is the original request
            request = failure.request
            self.logger.error('DNSLookupError on %s', request.url)
            print(request.url,"no content and the DNS has error")
            str = request.url + 'has ' + 'non 200 response '+'DNS lookup error\n'
            file1.writelines(str)
        elif failure.check(TimeoutError, TCPTimedOutError):
            request = failure.request
            self.logger.error('TimeoutError on %s', request.url)
            print(request.url,"has timeout error")
            str = request.url + 'has ' + 'timeout errror\n'
            file1.writelines(str)
        else:
            print("has timeout error")
    # emaillist = []
        # html_text = str(response.text)

        # item = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', html_text)
        # # item = response.xpath('//h1/text()').getall()
        # for i in item:
        #     emaillist.append(i)
        #     links.append(response.url)
        # print(emaillist)
        # dic1 = {
        #     'emails' : emaillist,
        #     'links' : links
        # }
        # df = pd.DataFrame(dic1)
        # #print(df)
        # #f = open("emails.csv", "w")
        # df.to_csv("emails.csv", mode='a', header=False)
        #f.close()
        # df.columns()
        #item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        #item['name'] = response.xpath('//div[@id="name"]').get()
        #item['description'] = response.xpath('//div[@id="description"]').get()
    # def parse_url(self,response):
    #     yield scrapy.Request(response.url, callback=self.parse_item())
    #
    #     print(response.url)
class operations:
    # starturls = []
    start=[]
    def startProcess(starturls):
        process = CrawlerProcess({'USER_AGENT': 'Mozilla/5.0'})
        process.crawl(H1SpiderSpider,starturls)
        process.start()
urls=['http://tigers.wsc.k12.ar.us/highschooldirectory.htm', 'http://tigers.wsc.k12.ar.us/highschooldirectory.htm', 'http://tigers.wsc.k12.ar.us/highschooldirectory.htm', 'http://tigers.wsc.k12.ar.us/highschooldirectory.htm', 'http://tigers.wsc.k12.ar.us/highschooldirectory.htm', 'http://tigers.wsc.k12.ar.us/highschooldirectory.htm', 'http://tigers.wsc.k12.ar.us/highschooldirectory.htm', 'http://tigers.wsc.k12.ar.us/highschooldirectory.htm', 'http://tigers.wsc.k12.ar.us/highschooldirectory.htm', 'http://tigers.wsc.k12.ar.us/highschooldirectory.htm', 'http://tigers.wsc.k12.ar.us/highschooldirectory.htm', 'http://tigers.wsc.k12.ar.us/highschooldirectory.htm', 'http://tigers.wsc.k12.ar.us/highschooldirectory.htm', 'http://tigers.wsc.k12.ar.us/highschooldirectory.htm', 'http://tigers.wsc.k12.ar.us/highschooldirectory.htm', 'http://tigers.wsc.k12.ar.us/highschooldirectory.htm', 'http://tigers.wsc.k12.ar.us/highschooldirectory.htm', 'http://tigers.wsc.k12.ar.us/highschooldirectory.htm', 'http://tigers.wsc.k12.ar.us/highschooldirectory.htm', 'http://tigers.wsc.k12.ar.us/highschooldirectory.htm', 'http://tigers.wsc.k12.ar.us/highschooldirectory.htm', 'http://tigers.wsc.k12.ar.us/highschooldirectory.htm', 'http://tigers.wsc.k12.ar.us/highschooldirectory.htm', 'http://tigers.wsc.k12.ar.us/highschooldirectory.htm', 'http://tigers.wsc.k12.ar.us/highschooldirectory.htm', 'http://tigers.wsc.k12.ar.us/highschooldirectory.htm', 'http://tigers.wsc.k12.ar.us/highschooldirectory.htm', 'http://tigers.wsc.k12.ar.us/highschooldirectory.htm', 'http://tigers.wsc.k12.ar.us/highschooldirectory.htm', 'http://tigers.wsc.k12.ar.us/highschooldirectory.htm', 'http://tigers.wsc.k12.ar.us/highschooldirectory.htm', 'http://tigers.wsc.k12.ar.us/highschooldirectory.htm', 'http://tigers.wsc.k12.ar.us/highschooldirectory.htm', 'http://tigers.wsc.k12.ar.us/highschooldirectory.htm', 'http://tigers.wsc.k12.ar.us/highschooldirectory.htm', 'http://tigers.wsc.k12.ar.us/highschooldirectory.htm', 'http://tigers.wsc.k12.ar.us/highschooldirectory.htm', 'http://tigers.wsc.k12.ar.us/highschooldirectory.htm', 'http://tigers.wsc.k12.ar.us/highschooldirectory.htm', 'http://tigers.wsc.k12.ar.us/highschooldirectory.htm', 'http://tigers.wsc.k12.ar.us/highschooldirectory.htm', 'http://tigers.wsc.k12.ar.us/highschooldirectory.htm', 'http://tigers.wsc.k12.ar.us/highschooldirectory.htm', 'http://tigers.wsc.k12.ar.us/highschooldirectory.htm', 'http://tigers.wsc.k12.ar.us/highschooldirectory.htm', 'http://tigers.wsc.k12.ar.us/highschooldirectory.htm', 'http://tigers.wsc.k12.ar.us/highschooldirectory.htm', 'http://tigers.wsc.k12.ar.us/highschooldirectory.htm', 'http://tigers.wsc.k12.ar.us/highschooldirectory.htm', 'http://tigers.wsc.k12.ar.us/highschooldirectory.htm', 'http://tigers.wsc.k12.ar.us/highschooldirectory.htm', 'http://tigers.wsc.k12.ar.us/highschooldirectory.htm', 'http://tigers.wsc.k12.ar.us/highschooldirectory.htm', 'http://tigers.wsc.k12.ar.us/highschooldirectory.htm', 'http://tigers.wsc.k12.ar.us/highschooldirectory.htm', 'http://tigers.wsc.k12.ar.us/highschooldirectory.htm', 'http://tigers.wsc.k12.ar.us/highschooldirectory.htm', 'http://tigers.wsc.k12.ar.us/highschooldirectory.htm', 'http://tigers.wsc.k12.ar.us/highschooldirectory.htm', 'http://tigers.wsc.k12.ar.us/highschooldirectory.htm', 'http://tigers.wsc.k12.ar.us/highschooldirectory.htm', 'http://tigers.wsc.k12.ar.us/highschooldirectory.htm', 'http://tigers.wsc.k12.ar.us/highschooldirectory.htm', 'http://tigers.wsc.k12.ar.us/highschooldirectory.htm', 'http://tigers.wsc.k12.ar.us/highschooldirectory.htm', 'http://tigers.wsc.k12.ar.us/highschooldirectory.htm', 'http://tigers.wsc.k12.ar.us/highschooldirectory.htm', 'http://tigers.wsc.k12.ar.us/highschooldirectory.htm', 'http://tigers.wsc.k12.ar.us/highschooldirectory.htm', 'http://tigers.wsc.k12.ar.us/highschooldirectory.htm', 'http://tigers.wsc.k12.ar.us/highschooldirectory.htm', 'http://tigers.wsc.k12.ar.us/highschooldirectory.htm', 'http://tigers.wsc.k12.ar.us/highschooldirectory.htm', 'http://tigers.wsc.k12.ar.us/highschooldirectory.htm', 'http://tigers.wsc.k12.ar.us/highschooldirectory.htm', 'http://tigers.wsc.k12.ar.us/highschooldirectory.htm', 'http://tigers.wsc.k12.ar.us/highschooldirectory.htm', 'http://tigers.wsc.k12.ar.us/highschooldirectory.htm', 'http://tigers.wsc.k12.ar.us/highschooldirectory.htm', 'http://tigers.wsc.k12.ar.us/highschooldirectory.htm', 'http://tigers.wsc.k12.ar.us/highschooldirectory.htm', 'http://tigers.wsc.k12.ar.us/highschooldirectory.htm', 'http://tigers.wsc.k12.ar.us/highschooldirectory.htm', 'http://tigers.wsc.k12.ar.us/highschooldirectory.htm', 'http://tigers.wsc.k12.ar.us/highschooldirectory.htm', 'http://tigers.wsc.k12.ar.us/highschooldirectory.htm', 'http://tigers.wsc.k12.ar.us/highschooldirectory.htm', 'http://tigers.wsc.k12.ar.us/highschooldirectory.htm', 'http://tigers.wsc.k12.ar.us/highschooldirectory.htm', 'http://tigers.wsc.k12.ar.us/highschooldirectory.htm', 'http://tigers.wsc.k12.ar.us/highschooldirectory.htm', 'http://tigers.wsc.k12.ar.us/highschooldirectory.htm', 'http://tigers.wsc.k12.ar.us/highschooldirectory.htm', 'http://tigers.wsc.k12.ar.us/highschooldirectory.htm', 'http://tigers.wsc.k12.ar.us/highschooldirectory.htm', 'http://tigers.wsc.k12.ar.us/highschooldirectory.htm', 'http://tigers.wsc.k12.ar.us/highschooldirectory.htm', 'http://tigers.wsc.k12.ar.us/highschooldirectory.htm', 'http://tigers.wsc.k12.ar.us/highschooldirectory.htm', 'http://tigers.wsc.k12.ar.us/highschooldirectory.htm', 'http://tigers.wsc.k12.ar.us/highschooldirectory.htm', 'http://tigers.wsc.k12.ar.us/highschooldirectory.htm', 'http://tigers.wsc.k12.ar.us/highschooldirectory.htm', 'http://tigers.wsc.k12.ar.us/highschooldirectory.htm', 'http://tigers.wsc.k12.ar.us/highschooldirectory.htm', 'http://tigers.wsc.k12.ar.us/highschooldirectory.htm', 'http://tigers.wsc.k12.ar.us/highschooldirectory.htm', 'http://tigers.wsc.k12.ar.us/highschooldirectory.htm', 'http://tigers.wsc.k12.ar.us/highschooldirectory.htm', 'http://tigers.wsc.k12.ar.us/highschooldirectory.htm', 'http://tigers.wsc.k12.ar.us/highschooldirectory.htm', 'http://tigers.wsc.k12.ar.us/highschooldirectory.htm', 'http://tigers.wsc.k12.ar.us/highschooldirectory.htm', 'http://tigers.wsc.k12.ar.us/highschooldirectory.htm', 'http://tigers.wsc.k12.ar.us/highschooldirectory.htm', 'http://tigers.wsc.k12.ar.us/highschooldirectory.htm', 'http://tigers.wsc.k12.ar.us/highschooldirectory.htm', 'http://tigers.wsc.k12.ar.us/highschooldirectory.htm', 'http://tigers.wsc.k12.ar.us/highschooldirectory.htm', 'http://tigers.wsc.k12.ar.us/highschooldirectory.htm', 'http://tigers.wsc.k12.ar.us/highschooldirectory.htm', 'http://tigers.wsc.k12.ar.us/highschooldirectory.htm', 'http://tigers.wsc.k12.ar.us/highschooldirectory.htm', 'http://tigers.wsc.k12.ar.us/highschooldirectory.htm', 'http://tigers.wsc.k12.ar.us/highschooldirectory.htm', 'http://tigers.wsc.k12.ar.us/highschooldirectory.htm', 'http://tigers.wsc.k12.ar.us/highschooldirectory.htm', 'http://tigers.wsc.k12.ar.us/highschooldirectory.htm', 'http://tigers.wsc.k12.ar.us/highschooldirectory.htm', 'http://tigers.wsc.k12.ar.us/highschooldirectory.htm', 'http://tigers.wsc.k12.ar.us/highschooldirectory.htm', 'http://tigers.wsc.k12.ar.us/highschooldirectory.htm', 'http://tigers.wsc.k12.ar.us/highschooldirectory.htm', 'http://tigers.wsc.k12.ar.us/highschooldirectory.htm', 'http://tigers.wsc.k12.ar.us/highschooldirectory.htm', 'http://tigers.wsc.k12.ar.us/highschooldirectory.htm', 'http://tigers.wsc.k12.ar.us/highschooldirectory.htm', 'http://tigers.wsc.k12.ar.us/highschooldirectory.htm', 'http://tigers.wsc.k12.ar.us/highschooldirectory.htm', 'http://tigers.wsc.k12.ar.us/highschooldirectory.htm', 'http://tigers.wsc.k12.ar.us/highschooldirectory.htm', 'http://tigers.wsc.k12.ar.us/highschooldirectory.htm', 'http://tigers.wsc.k12.ar.us/highschooldirectory.htm', 'http://tigers.wsc.k12.ar.us/highschooldirectory.htm', 'http://tigers.wsc.k12.ar.us/highschooldirectory.htm', 'http://tigers.wsc.k12.ar.us/highschooldirectory.htm', 'http://tigers.wsc.k12.ar.us/highschooldirectory.htm', 'http://tigers.wsc.k12.ar.us/highschooldirectory.htm', 'http://tigers.wsc.k12.ar.us/highschooldirectory.htm', 'http://tigers.wsc.k12.ar.us/highschooldirectory.htm', 'http://tigers.wsc.k12.ar.us/highschooldirectory.htm', 'http://tigers.wsc.k12.ar.us/highschooldirectory.htm', 'http://tigers.wsc.k12.ar.us/highschooldirectory.htm', 'http://tigers.wsc.k12.ar.us/highschooldirectory.htm', 'http://tigers.wsc.k12.ar.us/highschooldirectory.htm', 'http://tigers.wsc.k12.ar.us/highschooldirectory.htm', 'http://tigers.wsc.k12.ar.us/highschooldirectory.htm', 'http://tigers.wsc.k12.ar.us/highschooldirectory.htm', 'http://tigers.wsc.k12.ar.us/highschooldirectory.htm', 'http://tigers.wsc.k12.ar.us/highschooldirectory.htm', 'http://tigers.wsc.k12.ar.us/highschooldirectory.htm', 'http://tigers.wsc.k12.ar.us/highschooldirectory.htm', 'http://tigers.wsc.k12.ar.us/highschooldirectory.htm', 'http://tigers.wsc.k12.ar.us/highschooldirectory.htm', 'http://tigers.wsc.k12.ar.us/highschooldirectory.htm', 'http://tigers.wsc.k12.ar.us/highschooldirectory.htm', 'http://tigers.wsc.k12.ar.us/highschooldirectory.htm', 'http://tigers.wsc.k12.ar.us/highschooldirectory.htm', 'http://tigers.wsc.k12.ar.us/highschooldirectory.htm', 'http://tigers.wsc.k12.ar.us/highschooldirectory.htm', 'http://tigers.wsc.k12.ar.us/highschooldirectory.htm', 'http://tigers.wsc.k12.ar.us/highschooldirectory.htm', 'http://tigers.wsc.k12.ar.us/highschooldirectory.htm', 'http://tigers.wsc.k12.ar.us/highschooldirectory.htm', 'http://tigers.wsc.k12.ar.us/highschooldirectory.htm', 'http://tigers.wsc.k12.ar.us/highschooldirectory.htm', 'http://tigers.wsc.k12.ar.us/highschooldirectory.htm', 'http://tigers.wsc.k12.ar.us/highschooldirectory.htm', 'http://tigers.wsc.k12.ar.us/highschooldirectory.htm', 'http://tigers.wsc.k12.ar.us/highschooldirectory.htm', 'http://tigers.wsc.k12.ar.us/highschooldirectory.htm', 'http://tigers.wsc.k12.ar.us/highschooldirectory.htm', 'http://tigers.wsc.k12.ar.us/highschooldirectory.htm', 'http://tigers.wsc.k12.ar.us/highschooldirectory.htm', 'http://tigers.wsc.k12.ar.us/highschooldirectory.htm', 'http://tigers.wsc.k12.ar.us/highschooldirectory.htm', 'http://tigers.wsc.k12.ar.us/highschooldirectory.htm', 'http://tigers.wsc.k12.ar.us/highschooldirectory.htm', 'http://tigers.wsc.k12.ar.us/highschooldirectory.htm', 'http://tigers.wsc.k12.ar.us/highschooldirectory.htm', 'http://tigers.wsc.k12.ar.us/highschooldirectory.htm', 'http://tigers.wsc.k12.ar.us/highschooldirectory.htm', 'http://tigers.wsc.k12.ar.us/highschooldirectory.htm', 'http://tigers.wsc.k12.ar.us/highschooldirectory.htm', 'http://tigers.wsc.k12.ar.us/highschooldirectory.htm', 'http://tigers.wsc.k12.ar.us/highschooldirectory.htm', 'http://tigers.wsc.k12.ar.us/highschooldirectory.htm', 'http://tigers.wsc.k12.ar.us/highschooldirectory.htm', 'http://tigers.wsc.k12.ar.us/highschooldirectory.htm', 'http://tigers.wsc.k12.ar.us/highschooldirectory.htm', 'http://tigers.wsc.k12.ar.us/highschooldirectory.htm', 'http://tigers.wsc.k12.ar.us/highschooldirectory.htm', 'http://tigers.wsc.k12.ar.us/highschooldirectory.htm', 'http://tigers.wsc.k12.ar.us/highschooldirectory.htm', 'http://tigers.wsc.k12.ar.us/highschooldirectory.htm', 'http://tigers.wsc.k12.ar.us/highschooldirectory.htm', 'http://tigers.wsc.k12.ar.us/highschooldirectory.htm', 'http://tigers.wsc.k12.ar.us/highschooldirectory.htm', 'http://tigers.wsc.k12.ar.us/highschooldirectory.htm', 'http://tigers.wsc.k12.ar.us/highschooldirectory.htm', 'http://tigers.wsc.k12.ar.us/highschooldirectory.htm', 'http://tigers.wsc.k12.ar.us/highschooldirectory.htm', 'http://tigers.wsc.k12.ar.us/highschooldirectory.htm', 'http://tigers.wsc.k12.ar.us/highschooldirectory.htm', 'http://tigers.wsc.k12.ar.us/highschooldirectory.htm', 'http://tigers.wsc.k12.ar.us/highschooldirectory.htm', 'http://tigers.wsc.k12.ar.us/highschooldirectory.htm', 'http://tigers.wsc.k12.ar.us/highschooldirectory.htm', 'http://tigers.wsc.k12.ar.us/highschooldirectory.htm', 'http://tigers.wsc.k12.ar.us/highschooldirectory.htm', 'http://tigers.wsc.k12.ar.us/highschooldirectory.htm', 'http://tigers.wsc.k12.ar.us/highschooldirectory.htm', 'http://tigers.wsc.k12.ar.us/highschooldirectory.htm', 'http://tigers.wsc.k12.ar.us/highschooldirectory.htm', 'http://tigers.wsc.k12.ar.us/highschooldirectory.htm', 'http://tigers.wsc.k12.ar.us/highschooldirectory.htm', 'http://tigers.wsc.k12.ar.us/highschooldirectory.htm', 'http://tigers.wsc.k12.ar.us/highschooldirectory.htm', 'http://tigers.wsc.k12.ar.us/highschooldirectory.htm', 'http://tigers.wsc.k12.ar.us/highschooldirectory.htm', 'http://tigers.wsc.k12.ar.us/highschooldirectory.htm', 'http://tigers.wsc.k12.ar.us/highschooldirectory.htm', 'http://tigers.wsc.k12.ar.us/highschooldirectory.htm', 'http://tigers.wsc.k12.ar.us/highschooldirectory.htm', 'http://tigers.wsc.k12.ar.us/highschooldirectory.htm', 'http://tigers.wsc.k12.ar.us/highschooldirectory.htm', 'http://tigers.wsc.k12.ar.us/highschooldirectory.htm', 'http://tigers.wsc.k12.ar.us/highschooldirectory.htm', 'http://tigers.wsc.k12.ar.us/highschooldirectory.htm', 'http://tigers.wsc.k12.ar.us/highschooldirectory.htm', 'http://tigers.wsc.k12.ar.us/highschooldirectory.htm', 'http://tigers.wsc.k12.ar.us/highschooldirectory.htm', 'http://tigers.wsc.k12.ar.us/highschooldirectory.htm', 'http://tigers.wsc.k12.ar.us/highschooldirectory.htm', 'http://tigers.wsc.k12.ar.us/highschooldirectory.htm', 'http://tigers.wsc.k12.ar.us/highschooldirectory.htm', 'http://tigers.wsc.k12.ar.us/highschooldirectory.htm', 'http://tigers.wsc.k12.ar.us/highschooldirectory.htm', 'http://tigers.wsc.k12.ar.us/highschooldirectory.htm', 'http://tigers.wsc.k12.ar.us/highschooldirectory.htm', 'http://tigers.wsc.k12.ar.us/highschooldirectory.htm', 'http://tigers.wsc.k12.ar.us/highschooldirectory.htm', 'http://tigers.wsc.k12.ar.us/highschooldirectory.htm', 'http://tigers.wsc.k12.ar.us/highschooldirectory.htm', 'http://tigers.wsc.k12.ar.us/highschooldirectory.htm', 'http://tigers.wsc.k12.ar.us/highschooldirectory.htm', 'http://tigers.wsc.k12.ar.us/highschooldirectory.htm', 'http://tigers.wsc.k12.ar.us/highschooldirectory.htm', 'http://tigers.wsc.k12.ar.us/highschooldirectory.htm', 'http://tigers.wsc.k12.ar.us/highschooldirectory.htm', 'http://tigers.wsc.k12.ar.us/highschooldirectory.htm', 'http://tigers.wsc.k12.ar.us/highschooldirectory.htm', 'http://tigers.wsc.k12.ar.us/highschooldirectory.htm', 'http://tigers.wsc.k12.ar.us/highschooldirectory.htm', 'http://tigers.wsc.k12.ar.us/highschooldirectory.htm', 'http://tigers.wsc.k12.ar.us/highschooldirectory.htm', 'http://tigers.wsc.k12.ar.us/highschooldirectory.htm', 'http://tigers.wsc.k12.ar.us/highschooldirectory.htm', 'http://tigers.wsc.k12.ar.us/highschooldirectory.htm', 'http://tigers.wsc.k12.ar.us/highschooldirectory.htm', 'http://tigers.wsc.k12.ar.us/highschooldirectory.htm', 'http://tigers.wsc.k12.ar.us/highschooldirectory.htm']

operations.startProcess(urls)