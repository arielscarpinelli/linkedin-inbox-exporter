# -*- coding: utf-8 -*-

# Scrapy settings for linkedin_inbox_exporter project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'linkedin_inbox_exporter'

SPIDER_MODULES = ['linkedin_inbox_exporter.spiders']
NEWSPIDER_MODULE = 'linkedin_inbox_exporter.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'linkedin_inbox_exporter (+http://www.yourdomain.com)'
