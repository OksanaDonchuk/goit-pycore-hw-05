from setuptools import setup, find_packages

setup(
    name='assistant_bot',
    version='0.1',
    description='Assistant bot',
    url='https://github.com/OksanaDonchuk/',
    author='Oksana Donchuk',
    author_email='ksunya.donchuk@gmail.com',
    packages=find_packages(),
    entry_points={'console_scripts': ['assistant-bot=assistant_bot.main:main']}
)