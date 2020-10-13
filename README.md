# Smoltext

```
$ smoltext -h
usage: smoltext [-h] [-c] [-f FONT] [--list-fonts] [text [text ...]]

positional arguments:
  text                  text to process

optional arguments:
  -h, --help            show this help message and exit
  -c, --copy            copies processed text to clipboard
  -f FONT, --font FONT  which font to use
  --list-fonts          list all supported fonts
$ smoltext -f italic hello
𝘩𝘦𝘭𝘭𝘰
$ smoltext -f sub hello
ʰᵉˡˡᵒ
$ _
```

A font converter utility with the extra fonts included in utf8.

## Installation

### With pip:
```bash
pip install smoltext --user
```

### Manually:

```bash
git clone https://gitlab.com/imsofi/smoltext/
cd smoltext
pip install --upgrade setuptools wheel
python setup.py bdist_wheel
pip install dist/smoltext-*.whl
```

## Current Features

* Processes text input and gives an output of the desired font.
* List out all available fonts with previews.
* Clipboard functionality for fast usage.
* Easy to use CLI commands.

## Common issues

* Certain browsers and terminals fail to render certain font styles regardless of font.
* Kerning can be off in the terminal due to monospaced font.
* Certain fonts don't include all font styles used in this package.

## Issues?

If you are having issues. Feel free to [open an issue](https://gitlab.com/imsofi/smoltext/-/issues).
