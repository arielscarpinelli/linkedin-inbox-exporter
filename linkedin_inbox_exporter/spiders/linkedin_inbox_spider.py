import scrapy
import re
import json
from linkedin_inbox_exporter import items

class LinkedinInboxSpider(scrapy.Spider):
    name = 'linkedin-inbox'
    start_urls = ['https://www.linkedin.com/uas/login']

    def __init__(self, email, password, folder="messages", sub_filter="none"):
        self.email = email
        self.password = password
        self.folder = folder
        self.sub_filter = sub_filter
        self.parse = self.login

    def login(self, response):
        return scrapy.FormRequest.from_response(
            response,
            formdata={'session_key': self.email, 'session_password': self.password},
            callback=self.after_login
        )

    def after_login(self, response):
        # check login succeed before going on
        if not "home" in response.url and not "/hp" in response.url:
            self.log("Login failed", level=scrapy.log.ERROR)
            return

        self.parse = self.parse_detail_json

        first_page_url = "https://www.linkedin.com/inbox/%s?subFilter=%s" % (self.folder, self.sub_filter)

        return self.make_inbox_page_requests([first_page_url])

    def parse_inbox_page(self, response):
        message_detail_urls = self.full_urls(response.css("a.detail-link::attr(href)").extract())
        message_detail_requests = [self.make_requests_from_url(url) for url in message_detail_urls if not "mbox" in url]

        next_page_urls = self.full_urls(response.css("button.next-page::attr(data-url)").extract())
        next_page_requests = self.make_inbox_page_requests(next_page_urls)
        
        return message_detail_requests

    def parse_detail_json(self, response):
        response_json = json.loads(response.body)
        message = response_json['content']['message']

        item = items.InboxItem(id = message['itemId'], body = message['bodyParts'][0]['text'], folder = message['folder'], date = message['createDate'],
            sender_name = message['sender']['name'], sender_profile_url = message['sender'].get('link_profile'), 
            to_name = message['recipients'][0]['name'], to_profile_url = message['recipients'][0].get('link_profile'), 
            is_replied = message['isReplied'])
        return item

    def make_inbox_page_requests(self, urls):
        return [scrapy.Request(url, self.parse_inbox_page) for url in urls]

    def full_urls(self, hashtag_urls):
        return ["https://www.linkedin.com" + hashtag_url.replace("#", "") for hashtag_url in hashtag_urls]

