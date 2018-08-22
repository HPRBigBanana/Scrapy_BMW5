# # -*- coding: utf-8 -*-
#
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
# from scrapy.pipelines.images import ImagesPipeline
# from scrapy import Request
# import re
# from copy import deepcopy
#
# class The03ScrapyBmwPipeline(ImagesPipeline):
#     def process_item(self, item, spider):
#         """"""
#         """1. 从mwcrawlspiderSpider中传入过来的item取出数据"""
#         # 循环每一张图片地址下载，若传过来的不是集合则无需循环直接yield
#         for image_url in item['img_url']:
#             # meta里面的数据是从spider获取，然后通过meta传递给下面方法：file_path
#             yield Request(image_url,callback=self.file_path,meta={'title': deepcopy(item['title'])})
#             print(image_url)
#
#     """重命名，若不重写这函数，图片名为哈希，就是一串乱七八糟的名字"""
#     def file_path(self, request, response=None, info=None):
#
#         # 提取url前面名称作为图片名。
#         image_name = request.url.split('/')[-1]
#         # 接收上面meta传递过来的图片名称
#         name = request.meta['title']
#         # 过滤windows字符串，不经过这么一个步骤，你会发现有乱码或无法下载
#         name = re.sub(r'[？\\*|“<>:/]', '', name)
#         # 分文件夹存储的关键：{0}对应着name；{1}对应着image_guid
#         filename = u'{0}/{1}'.format(name, image_name)
#
#         # return filename
#



import re
from scrapy.pipelines.images import ImagesPipeline
from scrapy import Request
from copy import deepcopy

class ImagesrenamePipeline(ImagesPipeline):
    """"""
    """
    注意：容易出错的地方：
         我们不能在process_item获取item数据，
         应该覆盖get_media_requests方法，并在get_media_requests
         获取item数据！！！
         
    以下为错误：
    def process_item(self, item, spider):
#         # 循环每一张图片地址下载，若传过来的不是集合则无需循环直接yield
#         for image_url in item['img_url']:
#             # meta里面的数据是从spider获取，然后通过meta传递给下面方法：file_path
#             yield Request(image_url,callback=self.file_path,meta={'title': deepcopy(item['title'])})
#             print(image_url)
    """

    def get_media_requests(self, item, info):
        # 循环每一张图片地址下载，若传过来的不是集合则无需循环直接yield
        for image_url in item['img_url']:
            # meta里面的数据是从spider获取，然后通过meta传递给下面方法：file_path
            yield Request(image_url,callback=self.file_path, meta={'name': deepcopy(item['title'])})

    """
    重命名，若不重写这函数，图片名为哈希，就是一串乱七八糟的名字
    （还可能出现无法下载的问题！）
    """
    def file_path(self, request, response=None, info=None):
        # 提取url前面名称作为图片名。
        image_guid = request.url.split('/')[-1]
        # 接收上面meta传递过来的图片名称
        name = request.meta['name']
        # 过滤windows字符串，不经过这么一个步骤，你会发现有乱码或无法下载
        name = re.sub(r'[？\\*|“<>:/]', '', name)
        # 分文件夹存储的关键：{0}对应着name；{1}对应着image_guid
        filename = u'{0}/{1}'.format(name, image_guid)
        return filename






















