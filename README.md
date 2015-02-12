# Linkedin Inbox Exporter
Allows you to export / download your whole inbox from your LinkedIn account.

# Usage
Be sure you have scrappy installed. Check http://scrapy.org/

Then standing at the cloned repo path run:

$ scrapy crawl linkedin-inbox -a email=[YOUR EMAIL] -a password=[YOUR PASSWORD] -o inbox.csv

This will by default export your entire Messages folder from your inbox and save it in a filed called inbox.csv (you can save in other formats like JSON and XML, check http://doc.scrapy.org/en/latest/topics/feed-exports.html)

You can optionally specify the "-a folder=" parameter with the values:
	- messages: Your messages inbox
	- invitations: Invitations you recieved
	- sent: Your sent items
	- archive: Your archived items
	- trash: Your items in trash

There is also the "-a sub_filter=" paramter wich allows you to filter down the retrived values for messages, archive, and trash folders:
	- unread: only the unread messages
	- read: only the read messages
	- inmail: only inmail messages
	- blocked: only blocked messages

And in case you are retriving the sent folder you can use "-a sub_filter=" with the folowing values:
	- message: only messages
	- invitation: only invitations
	- userStarred: only messages you starred
	- inmail: only messages sent thru inmail

A filtered example:

$ scrapy crawl linkedin-inbox -a email=[YOUR EMAIL] -a password=[YOUR PASSWORD] -a folder=sent -a sub_filter=message -o sent-messages.csv

