# coding: utf-8
import re
import os
from setuptools import setup, find_packages


def fpath(name):
    return os.path.join(os.path.dirname(__file__), name)


def read(fname):
    return open(fpath(fname)).read()


file_text = read(fpath('chiki_jinja.py'))


def grep(attrname):
    pattern = r"{0}\W*=\W*'([^']+)'".format(attrname)
    strval, = re.findall(pattern, file_text)
    return strval


def get_data_files(*dirs):
    results = []
    for src_dir in dirs:
        for root, dirs, files in os.walk(src_dir):
            results.append((root, map(lambda f: root + "/" + f, files)))
    return results


setup(
    name='chiki-jinja',
    version='0.0.1',
    url='https://github.com/endsh/chiki-jinja',
    author='Linshao',
    author_email='438985635@qq.com',
    description='chiki jinja libs.',
    py_modules=['chiki_jinja'],
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    platforms='any',
    install_requires=[
        'Flask==0.10.1',
    ],
)
