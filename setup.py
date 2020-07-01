from setuptools import setup, find_packages


setup(
    name = 'fmp_python',
    version = '0.1.0',
    description = 'Python wrapper for Financial Modeling Prep API',
    keywords = ' python finance trading stocks prices worldtradingdata wtd alphavantage iex',
    url = 'https://github.com/ikbale/fmp_python',
    author = 'Ikbale Maghraoui',
    author_email = 'ikbale94@gmail.com',
    license = 'MIT',
    packages = find_packages(),
    install_requires = [
        'pandas',
		'requests',
        'requests_mock'
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    include_package_data = False,
    zip_safe = False
)