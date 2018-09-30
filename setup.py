"""
Sets up the system to use the ChatServerMaster program.
"""

from setuptools import setup
from setuptools.command.install import install


class PostInstallation(install):
    def run(self):
        install.run(self)


setup(
    name="ChatServerMaster",
    version="1.2.2",
    description="This program is an open source implementation of a chat server, with a in browser client.",
    author="Charles Engen",
    platforms="Windows",
    author_email="owenengen@gmail.com",
    license="MIT",
    packages=['Client', 'ConfigManger', 'Server', 'tests'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Communications',
        'Topic :: Chat',
        'License :: MIT',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    python_requires='>=3',

    keywords='chat server',

    install_requires=['websockets', 'passlib', ],

    entry_points={
        'console_scripts': [
            'chat = server.server:main'
        ]
    },
    cmdclass={
        'install': PostInstallation,
    },
)
