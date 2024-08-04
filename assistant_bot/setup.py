from setuptools import setup, find_packages

setup(
    name='assistant_bot',
    version='0.1',
    description='Assistant bot for managing contacts',
    url='https://github.com/OksanaDonchuk/goit-pycore-hw-05/blob/main/assistant_bot/assistant_bot/main.py',
    author='Oksana Donchuk',
    author_email='ksunya.donchuk@gmail.com',
    packages=find_packages(include=['assistant_bot', 'assistant_bot.*']),
    entry_points={'console_scripts': ['assistant-bot=assistant_bot.main:main']},
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)

