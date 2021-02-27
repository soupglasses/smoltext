# Smoltext

```
$ smoltext -h
usage: smoltext [-h] [-c] [-f FONT] [--list-fonts] [text [text ...]]

A font converter utility with the extra fonts included in utf8.

positional arguments:
  text                  text to process

optional arguments:
  -h, --help            show this help message and exit
  -c, --copy            copies processed text to clipboard
  -f FONT, --font FONT  which font to use
  --list-fonts          list all supported fonts
$ smoltext -f italic hello
𝘩𝘦𝘭𝘭𝘰
$ smoltext -f subscript hello
ʰᵉˡˡᵒ
$ _
```

A font converter utility with the extra fonts included in utf8.

## Installation

### With pip:

```bash
pip install --upgrade --user smoltext
```

### With git:

```bash
git clone https://gitlab.com/imsofi/smoltext/
cd smoltext
pip install --upgrade setuptools
python setup.py install --user
```

## Current Features

* Processes text input and gives an output of the desired font.
* List out all available fonts with previews.
* Easy to use CLI commands.

## Common issues

* Certain browsers and terminals fail to render certain font styles regardless of font.
* Kerning can be off due to terminals using a monospaced font.
* Certain fonts don't include all font styles used in this package.

## Links

* [Gitlab](https://gitlab.com/imsofi/smoltext/)
* [PyPI](https://pypi.org/project/smoltext/)
