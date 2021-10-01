from setuptools import find_packages, setup

# read the contents of README file
from os import path
from io import open  # for Python 2 and 3 compatibility

# get __version__ from _version.py
ver_file = path.join('torchattention', 'version.py')
with open(ver_file) as f:
    exec(f.read())

this_directory = path.abspath(path.dirname(__file__))


# read the contents of README.rst
def readme():
    with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
        return f.read()


# read the contents of requirements.txt
with open(path.join(this_directory, 'requirements.txt'),
          encoding='utf-8') as f:
    requirements = f.read().splitlines()

setup(
    name='torchattention',
    version=__version__,
    description='A Python library for Pytorch Attention Mechanism',
    long_description=readme(),
    long_description_content_type='text/x-rst',
    author_email='aadityaura@gmail.com',
    url='https://github.com/monk1337/TorchAttention.git',
    download_url='https://github.com/monk1337/TorchAttention/archive/refs/heads/main.zip',
    keywords=['Attention', 'Pytorch', 'Pytorch Attention', 'Transformers'],
    packages=find_packages(exclude=['test']),
    include_package_data=True,
    install_requires=requirements,
    setup_requires=['setuptools>=38.6.0'],
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Education',
        'Intended Audience :: Science/Research',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
)