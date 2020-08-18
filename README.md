# Zoom-Code-Scraper
Finds Zoom Codes for you.

## Information
This tool will scrape Twitter data for you. It specifically searches for Zoom Codes/URLs posted recently by other users.

I got the idea from verdict, he made a similar tool a few months ago but using TweetDeck. Mine uses Twitter's official API.<br/>
His Discord username: verdict#0200

## Preview
![](https://i.imgur.com/8mfXao4.png)<br/>
![](https://i.imgur.com/0jSibRF.png)

## Usage
- Python 3.6 or above is required.
- I develop for Windows machines only and do not intentionally support other operating systems.
- If you do not already have the **requests** library installed, run setup.py — make sure PIP is added to PATH.
1. Edit the "authorization" header's value with your Twitter account's bearer token at line [20](https://github.com/zoony1337/Zoom-Code-Scraper/blob/master/main.py#L20).
2. Edit the "cookie" header's value with your Twitter account's cookies at line [23](https://github.com/zoony1337/Zoom-Code-Scraper/blob/master/main.py#L23).
3. Run main.py
4. All set!

I am aware I could have made a simple loading script for all the dynamic values, but I just wanted to get the idea out.
