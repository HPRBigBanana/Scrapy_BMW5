# -*- coding: utf-8 -*-
import scrapy
import urllib

class BmwspiderSpider(scrapy.Spider):
    name = 'bmwSpider'
    allowed_domains = ['car.autohome.com.cn']
    start_urls = ['https://car.autohome.com.cn/pic/series/65.html']

    """开始爬取"""
    def parse(self, response):
        """"""
        # """1. 获取整个需要的div块"""
        # div_all = response.xpath("//div[@class='column grid-16']")
        # print(len(div_all))

        """2. 从response 中获取多个单独的div块"""
        div_list = response.xpath("//div[@class='column grid-16']/div[@class='uibox']")
        print(len(div_list))

        """3. 使用循环得到div_list中的单独div块"""
        for div in div_list:
            # 新建一个字典
            item = {}
            # 获取标题
            item["title"] = div.xpath("./div[@class='uibox-title']"
                                      "/a[not(@class='more')]/text()").extract_first()

            # 获取对应div块下的所有图片名称
            item["img_name"] = div.xpath("./div[@class='uibox-con carpic-list03']"
                                         "/ul/li/div/a/text()").extract()

            # 获取对应div块下的所有图片地址
            item["img_url"] = div.xpath("./div[@class='uibox-con carpic-list03']"
                                    "/ul/li/a//img/@src").extract()
            item["img_url"] = [urllib.parse.urljoin(response.url,i) for i in item["img_url"]]
            # urllib.parse.urljoin(response.url, i)

            yield item

            print(item)


































