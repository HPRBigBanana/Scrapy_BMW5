# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
import urllib

from the03_Scrapy_BMW.items import The03ScrapyBmwItem


class BmwcrawlspiderSpider(CrawlSpider):
    name = 'bmwCrawlSpider'
    allowed_domains = ['car.autohome.com.cn']
    start_urls = ['https://car.autohome.com.cn/pic/series/65.html#pvareaid=104387']


    """1. 进行crawlSpider参数设置"""
    rules = (
        Rule(
             # allow 表示通过正则表达式提取的url地址
             LinkExtractor(allow=r'https://car.autohome.com.cn/pic/series/65-.+\.html'),
             # callback 表示 获取到url地址时，callback函数的值作为回调函数
             callback='parse_item',
             # follow 表示是否跟进页面 根据规则 进行再次提取链接
             follow=False),
    )

    """2. 进行数据爬取"""
    def parse_item(self, response):
        """"""
        """3 实例化items文件中The03ScrapyBmwItem对象"""
        item = The03ScrapyBmwItem()

        """4. 从response 中获取多个单独的div块"""
        div_list = response.xpath("//div[@class='column grid-16']/div[@class='uibox']")
        # print(len(div_list))

        """5. 通过循环得到每个单独的div块"""
        for div in div_list:
            # 创建一个item
            # item = {}

            # 得到类别名称
            item["title"] = div.xpath("./div[@class='uibox-title']"
                                     "/text()").extract_first()

            # 获取图片url地址
            item["img_url"] = div.xpath(".//div[@class='uibox-con carpic-list03 border-b-solid']"
                                        "/ul/li/a/img/@src").extract()
            # 补全url
            item["img_url"] = [urllib.parse.urljoin(response.url, i) for i in item["img_url"]]
            # 将缩略图变成高清大图，从网址中修改特定字符
            item["img_url"] = [i.replace("/t_","/1024x0_1_q87_") for i in item["img_url"]]


            """6. 将item传入pipline中"""
            yield item

            # print(item)
            """注意： 该例子中，还必须有多页下载，稍后再弄"""



















