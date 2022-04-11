
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

class H1SpiderSpider(CrawlSpider):
	name = 'xpath'
	emails_file = 'emails.csv'
	logs_file = 'logs.txt'
	urls_no_of_emails = 'urlsstats.txt'
	urls_with_mailto = 'mailto.txt'
	start_urls = []

	# start_urls = ['https://books.toscrape.com/']
	allowed_domains = []
	# start_urls = ['https://www.books.toscrape.com/']
	with open('domains.txt', 'r') as f:
		for i in range(1,2):
			k = f.readline().rstrip(',\n')
			start_urls.append(k)
			allowed_domains.append(urlparse(k).netloc)
		# self.allowed_domains =
		print(start_urls,"this will be scraped",'\n',len(start_urls),'\n',allowed_domains,'\n',len(allowed_domains))
	rules = (
		Rule(LinkExtractor(), callback='parse_item',errback='errback_httpbin', follow=True),)
	#
	print("test 0 passed...")
	listrepeatedpages = []
	countrepeated = 0
	countall = 0
	listpages = []
	listrepeatedpages = []
	scraped_emails = []
	emaillist =[]
	links =[]
	count_duplicate_emails =0
	def parse_item(self, response):
		emails_in_start_url = 0
		string = ''
		htmltext = str(response.text)


		if response.url in self.listpages:
			print("the page is repeated.")
			self.listrepeatedpages.append(response.url)
			self.countrepeated+=1
		else:
			if response.url in self.start_urls:
				self.emails_in_start_url = 0
				string = response.url
				self.listpages.append(response.url)

				self.countall += 1
				print(" a new page..")
				print("the number of all pages: ", self.countall)
				item = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', htmltext)
				if item:
					# if  find_mail_hidden:
					# 	filemailto = open(self.urls_with_mailto, 'a')
					# 	to_be_written = item + ',' +response.url + ' , ' + 'has mailtofield\n'
					# 	filemailto.write(to_be_written)
					# 	return
					for i in item:
						intm = 0
						temp_email = []
						temp_links = []
						if i in self.scraped_emails:
							print("duplicate.. total", self.count_duplicate_emails)
							self.count_duplicate_emails += 1
						else:

							print("new email..")
							print(i, "scraped from ", response.url)
							self.scraped_emails.append(i)
							self.emails_in_start_url += 1
							self.emaillist.append(i)
							self.links.append(response.url)
							temp_email.append(i)
							temp_links.append(response.url)
							print("the final emaillist:", self.emaillist)
							print("legit emails:", len(self.scraped_emails))

							print(temp_email)
							dic1 = {
								'emails': temp_email,
								'links': temp_links
							}
							df = pd.DataFrame(dic1)
							# print(df)
							# f = open("emails.csv", "w")
							df.to_csv(self.emails_file, mode='a', header=False)
			else:
				self.listpages.append(response.url)

				self.countall+=1
				print(" a new page..")
				print("the number of all pages: ", self.countall)
				item = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', htmltext)
				if item:
					# if  find_mail_hidden:
					# 	filemailto = open(self.urls_with_mailto, 'a')
					# 	to_be_written = item + ',' +response.url + ' , ' + 'has mailtofield\n'
					# 	filemailto.write(to_be_written)
					# 	return
					for i in item:
						intm=0
						temp_email =[]
						temp_links = []
						if i in self.scraped_emails:
							print("duplicate.. total",self.count_duplicate_emails)
							self.count_duplicate_emails+=1
						else:

							print("new email..")
							print(i,"scraped from ", response.url)
							self.scraped_emails.append(i)
							self.emails_in_start_url+=1
							self.emaillist.append(i)
							self.links.append(response.url)
							temp_email.append(i)
							temp_links.append(response.url)
							print("the final emaillist:",self.emaillist )
							print("legit emails:",len(self.scraped_emails))

							print(temp_email)
							dic1 = {
								'emails': temp_email,
								'links': temp_links
							}
							df = pd.DataFrame(dic1)
							# print(df)
							# f = open("emails.csv", "w")
							df.to_csv(self.emails_file, mode='a', header=False)
				else:
					print("no email field")
					return
		file1 = open(self.urls_no_of_emails, 'a')  # append mode
		final = string +"    ," + str(emails_in_start_url ) +'\n'
		file1.writelines(final)

	def errback_httpbin(self, failure):
		# log all failures
		self.logger.error(repr(failure))
		file1 = open(self.logs_file, "a")  # append mode

		# in case you want to do something special for some errors,
		# you may need the failure's type:

		if failure.check(HttpError):
			# these exceptions come from HttpError spider middleware
			# you can get the non-200 response
			response = failure.value.response
			self.logger.error('HttpError on %s', response.url)
			print(response.url, "does not content non 200 get is not working")
			str = response.url + 'page not found\n'
			file1.writelines(str)
		elif failure.check(DNSLookupError):
			# this is the original request
			request = failure.request
			self.logger.error('DNSLookupError on %s', request.url)
			print(request.url, "no content and the DNS has error")
			str = request.url + 'has ' + 'non 200 response ' + 'DNS lookup error\n'
			file1.writelines(str)
		elif failure.check(TimeoutError, TCPTimedOutError):
			request = failure.request
			self.logger.error('TimeoutError on %s', request.url)
			print(request.url, "has timeout error")
			str = request.url + 'has ' + 'timeout errror\n'
			file1.writelines(str)
		else:
			print("has timeout error")

class operations:
	# starturls = []
	process = CrawlerProcess({'USER_AGENT': 'Mozilla/5.0'})
	process.crawl(H1SpiderSpider)
	process.start()
