import setuptools

with open('README.md', 'r', encoding='utf-8') as fh:
    long_description = fh.read()

setuptools.setup(
    name='steelseries-sonar-py',
    author='Mark7888',
    author_email='l.mark7888@gmail.com',
    description='Simple Python wrapper for the SteelSeries Sonar API',
    keywords='steelseries, sonar, volume, control, sonar-api',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/Mark7888/steelseries-sonar-py',
    project_urls={
        'Documentation': 'https://github.com/Mark7888/steelseries-sonar-py/blob/master/README.md',
        'Bug Reports': 'https://github.com/Mark7888/steelseries-sonar-py/issues',
        'Source Code': 'https://github.com/Mark7888/steelseries-sonar-py',
    },
    package_dir={'': 'src'},
    packages=setuptools.find_packages(where='src'),
    install_requires=[
        'requests >= 2.31.0',
    ],
    classifiers=[
        # see https://pypi.org/classifiers/
        'Development Status :: 5 - Production/Stable',

        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',

        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.1',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Programming Language :: Python :: 3 :: Only',
        'License :: OSI Approved :: MIT License',
        'Operating System :: Microsoft :: Windows',
    ],
    python_requires='>=3',
)
