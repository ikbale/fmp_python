import io
from os import path

from setuptools import setup, find_packages

current_dir = path.abspath(path.dirname(__file__))

# Get the README content
with io.open(path.join(current_dir, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='fmp_python',
    version='0.1.7',
    description='Python wrapper for Financial Modeling Prep API',
    long_description=long_description,
    long_description_content_type='text/markdown',
    keywords=' python finance trading stocks prices financialmodelingprep api fmp alphavantage wtd iex',
    url='https://github.com/qlikstar/fmp_python',
    author='Ikbale Maghraoui / Sanket Mishra',
    author_email='ikbale94@gmail.com/isanketmishra@gmail.com',
    license='MIT',
    packages=find_packages(),
    install_requires=[
        'pandas',
        'requests',
    ],
    test_requires=[
        'requests_mock'
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    include_package_data=False,
    zip_safe=False
)
