# # from urllib.parse import urlparse
# #
# import re
#
# str = 'mailto:ismailmailto'
# item = re.findall('mailto:',str)
# for i in item:
#     print(i)
# # file = open("domain.txt", 'r')
# # file2 = open("fbgooglelinks.txt",'a')
file3 = open('links.txt','r')
times = 11
# # list2 = []
# # # list = file.readlines()
for i in range(1,times):
    print("test 1 passed ✔")
    file4 = open(str('domains\\'+'domains_for_spider'+str(i)+'.txt'),'a')
    start = i*100
    stop = start +100
    print("test 2 passed ✔")
    for i in range(start,stop):
        string = file3.readline()
        file4.write(string)
    print("test 3 passed ✔")



# #     l = file.readline()
# #     k = l.rstrip('\n')
# #     matches=["drive.google.com", "docs.google.com", "facebook.com" ]
# #     if k:
# #         if any(x in k for x in matches):
# #             print(k)
# #             str = k + '\n'
# #             # dom = urlparse(k).netloc
# #             # list.append(dom)
# #             file2.write(str)
# #             list2.append(k)
# #         else:
# #             str = k +'\n'
# #             file3.write(str)
# #
# # # print(len(list))
# # print(list2,'\n',len(list2))
# # # domain = urlparse(string).netloc
# # # file2.writelines(domain)
# # # print(domain)
# # class dom:
# #
# #     def __init__(self, filename=None):
# #         if filename:
# #             with open(filename, 'r') as f:
# #                 self.start_urls = f.readlines()
# #                 # self.allowed_domains =
# #                 print(self.start_urls, "this will be scraped")
# # list = [1,76,98,67]
# # list2 =['kk','hhh','ali','ismail']
# # if list[0]==1:
# #     print("one")
# # else:
# #     continue
# # print("hello continue")