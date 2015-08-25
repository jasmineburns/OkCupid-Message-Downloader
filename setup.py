from distutils.core import setup
setup(
  name = 'okcmd',
  packages = ['okcmd'], # this must be the same as the name above
  entry_points = {'console_scripts': [
      'okcmd = okcmd.arrow_fetcher:main_func',
  ],},
  version = '0.7',
  description = 'A simple Python script for downloading your sent and received OkCupid messages.',
  author = 'Steven Lehrburger',
  author_email = 'lehrburger@gmail.com',
  url = 'https://github.com/lehrblogger/OkCupid-Message-Downloader',
  download_url = 'https://github.com/lehrblogger/OkCupid-Message-Downloader/tarball/0.1',
  keywords = ['okcupid', 'okc', 'okcmd', 'dating', 'archive', 'message', 'download', 'backup'],
  classifiers = [
      'Development Status :: 3 - Alpha',
      'License :: OSI Approved :: MIT License',
      'Programming Language :: Python :: 2.7',
  ],
)

