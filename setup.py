from distutils.core import setup
from codecs import open

setup(
    name = 'uoftscrapers',
    packages = [
        'uoftscrapers',
        'uoftscrapers.utils.scraper',
        'uoftscrapers.utils.layers',
        'uoftscrapers.courses',
        'uoftscrapers.buildings',
        'uoftscrapers.textbooks',
        'uoftscrapers.food',
        'uoftscrapers.calendar',
        'uoftscrapers.calendar.utsg',
        'uoftscrapers.calendar.utm',
        'uoftscrapers.calendar.utsc',
        'uoftscrapers.timetable',
        'uoftscrapers.timetable.utsg',
        'uoftscrapers.timetable.utm',
        'uoftscrapers.timetable.utsc',
        'uoftscrapers.exams',
        'uoftscrapers.exams.utsg',
        'uoftscrapers.exams.utm',
        'uoftscrapers.exams.utsc',
        'uoftscrapers.athletics',
        'uoftscrapers.athletics.utsg',
        'uoftscrapers.athletics.utm',
        'uoftscrapers.athletics.utsc'
    ],
    version = '0.4.0',
    description = 'University of Toronto public web scraping scripts.',
    author = 'Qasim Iqbal',
    author_email = 'me@qas.im',
    url = 'https://github.com/cobalt-io/uoft-scrapers',
    download_url = 'https://github.com/cobalt-io/uoft-scrapers/tarball/0.4.0',
    package_data = {'': ['LICENSE.md']},
    package_dir = {'uoftscrapers': 'uoftscrapers'},
    include_package_data = True,
    keywords = ['uoft', 'scraper', 'toronto', 'university of toronto', 'cobalt'],
    install_requires = ['requests>=2.6.2', 'beautifulsoup4>=4.3.2', 'pytidylib>=0.2.4', 'lxml>=3.6.0', 'pytz>=2016.3'],
    classifiers = [],
)
