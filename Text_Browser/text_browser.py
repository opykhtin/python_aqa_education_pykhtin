"""Text Browser"""

import sys
from collections import deque

import requests
from bs4 import BeautifulSoup
from colorama import Fore


class TextBrowser:
    page = "History is Empty"
    directory = None

    def __init__(self):
        self.history = deque()

    @staticmethod
    def save_content(name, content):
        """Save content"""
        with open(name, "w", encoding="utf-8") as f:
            f.write(content)

    def show_content(self):
        """Show last content (URL)"""
        name = self.previous_page()
        print(name)

    @staticmethod
    def user_input():
        """User input"""
        while True:
            entered_value = input('> ')
            if entered_value:
                return entered_value

    @staticmethod
    def url_validation(entered_value):
        """URL validation"""
        return "." in entered_value

    def add_history(self, content):
        """Add history"""
        self.history.append(content)

    def previous_page(self):
        """Return the previous url"""
        return self.history.pop()

    @staticmethod
    def get_content(url):
        """Enter URL"""
        response = requests.get(url if "https://" in url else "https://" + url,
                                headers={"user-agent": "Mozilla/5.0"}, timeout=5)
        return response

    def url_handle(self, url):
        """Data processing"""
        try:
            content = self.get_content(url)

        except NameError:
            print("Invalid URL")

        else:
            try:
                self.add_history(self.page)
                self.page = url
                self.save_content(url.split('.')[0], content.text)
                self.display_content(self.get_content(url))
            except NameError:
                print("Invalid data")

    def back(self):
        """Go back in browser"""
        page = self.previous_page()
        print(page)

    @staticmethod
    def display_content(response):
        """Remove tags"""
        soup = BeautifulSoup(response.content, "html.parser")
        tags = ["p", "h1", "h2", "h3", "h4", "h5", "h6", "a", "ul", "ol", "li"]
        page = soup.find_all(tags)
        for tag in page:
            text = tag.get_text()
            if tag.name == "a" and "href" in tag.attrs:
                print(Fore.GREEN + text)
            else:
                print(Fore.YELLOW + text)
            print(Fore.RESET)


browser = TextBrowser()


def main():
    while True:
        print('''Enter value from 1 to 3:
URL - 1        
Back - 2
Exit - 3''')
        entered_value = browser.user_input()
        if entered_value == "1":
            while True:
                print("Enter URL")
                url = browser.user_input()
                if browser.url_validation(url):
                    browser.url_handle(url)
                    break
                else:
                    print("Invalid URL")
                    continue
        elif entered_value == "2":
            browser.show_content()
        elif entered_value == "3":
            sys.exit()
        else:
            print("Incorrect input")


if __name__ == "__main__":
    main()
