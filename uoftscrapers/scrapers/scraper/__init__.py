import logging
import os
import shutil
import sys

class Scraper:
    """Scraper class."""

    logger = logging.getLogger("uoftscrapers")

    @staticmethod
    def ensure_location(location):
        """Ensure that the location given exists."""

        if not os.path.exists(location):
            os.makedirs(location)

    @staticmethod
    def flush_percentage(decimal):
        """Update the last line in stdout to a percentage formatted value."""

        sys.stdout.write('%.2f%%\r' % (decimal * 100))
        sys.stdout.flush()

    @staticmethod
    def get_html(s, url, headers=None):
        """Fetches the HTML page source, automatically retrying if it times out."""

        html = None
        while html is None:
            try:
                r = s.get(url, headers=headers)
                if r.status_code == 200:
                    html = r.text
            except (requests.exceptions.Timeout,
                    requests.exceptions.ConnectionError):
                continue

        return html.encode('utf-8')

    @staticmethod
    def get_text_from_class(soup, name):
        obj = soup.find(class_=name)
        if obj != None:
            return obj.get_text().replace('\xa0', ' ').strip()
        else:
            return ''
