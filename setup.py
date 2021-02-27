import setuptools

with open('README.md', 'r') as f:
    long_description = f.read()

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setuptools.setup(
    name='smoltext',
    version='1.4.6',
    install_requires=requirements,
    scripts=['smoltext'],
    author='Sofi',
    description='A font converter utility with the extra fonts included in utf8.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=setuptools.find_packages(),
    project_urls={
        'Source': 'https://gitlab.com/imsofi/smoltext/',
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
