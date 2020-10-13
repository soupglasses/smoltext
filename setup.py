import setuptools

with open('README.md', 'r') as f:
    long_description = f.read()

setuptools.setup(
    name='smoltext',
    version='1.0.0',
    scripts=['smoltext'],
    author='Sofi',
    description='A font converter utility with the extra fonts included in utf8.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://gitlab.com/imsofi/smoltext/',
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
