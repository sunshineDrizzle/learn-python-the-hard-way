try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'My Project',
    'author': 'cxy',
    'url': 'URL to get it at.',
    'download_url': 'Where to download it.',
    'author_email': '954830460@qq.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['myProject'],
    'scripts': [],
    'name': 'myProject'
}

setup(**config)  # **dict是一种参数传递方式，详见python学习手册
