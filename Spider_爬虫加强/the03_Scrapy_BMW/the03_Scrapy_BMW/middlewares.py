# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
import random
from the03_Scrapy_BMW.settings import USER_AGENTS
from the03_Scrapy_BMW.settings import PROXIES

class The03Random(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    def process_request(self, request, spider):

        # setting文件中取出useragent（随机抽取）
        ua = random.choice(spider.settings.get("USER_AGENTS"))
        # 将useragent传入request中
        request.headers["User-Agent"] = ua

        # setting文件中取出ip（随机抽取）
        ip = random.choice(spider.settings.get("PROXIES"))
        request.proxies = ip




    # def process_response(self, request, response, spider):
    #
    #     # 将随机的user-agent和ip输出在界面上，便于观看
    #
    #     print("*"*50)
    #     print(request.headers["User-Agent"])
    #     print(request.proxies)
    #     print("*" * 50)
    #
    #     return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)