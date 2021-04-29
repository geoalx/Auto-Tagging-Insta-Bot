# Auto-Tagging-Insta-Bot
An Instagram bot that tags automatically your friends in posts

[![built with Python3](https://img.shields.io/badge/built%20with-Python3-red.svg)](https://www.python.org/) [ ![built with Selenium](https://img.shields.io/badge/built%20with-Selenium-yellow.svg)](https://github.com/SeleniumHQ/selenium)

In order to use this file you need to have the Selenium Library installed. In order to do this you need to write the following in the terminal:
```bash
pip install selenium
```

Also you need to unzip and copy the [Chrome webdriver](https://chromedriver.chromium.org/downloads) into the PATH folder of your system ([basic instructions](https://www.computerhope.com/issues/ch000549.htm))


###Using the bot
In the same folder you used to save the bot you need to make a txt file named "credentials.txt" with the following format:
```bash
INSTA_USERNAME
INSTA_PASSWORD
LINK_TO_POST
LIST_OF_FRIENDS
```

The LIST_OF_FRIENDS attribute is all your friends that you need to tag sepparated with a comma (,), also the "@" symbol before the username is necessary.
