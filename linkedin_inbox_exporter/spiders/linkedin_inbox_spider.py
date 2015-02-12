import scrapy

class LinkedinInboxSpider(scrapy.Spider):
    name = 'Linkedin Inbox Spider'
    start_urls = ['https://www.linkedin.com/uas/login']

    def parse(self, response):
        return scrapy.FormRequest.from_response(
            response,
            formdata={'session_key': 'john', 'session_password': 'secret'},
            callback=self.after_login
        )

    def after_login(self, response):
        # check login succeed before going on
        if "errors" in response.body:
            self.log("Login failed", level=log.ERROR)
            return

        # continue scraping with authenticated session...