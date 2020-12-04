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

### Enable tab completion:

Either use this for global argcomplete for all python scripts.

```bash
activate-global-python-argcomplete --user
```

Or you can add `eval "$(register-python-argcomplete smoltext)"` to your .bashrc to only allow smoltext to have argcomplete completion.

More detailed instructions for argcomplete installation can be found [here](https://kislyuk.github.io/argcomplete/#global-completion).

## Current Features

* Processes text input and gives an output of the desired font.
* List out all available fonts with previews.
* Clipboard functionality for fast usage.
* Easy to use CLI commands.
* Tab completion.

## Common issues

* Certain browsers and terminals fail to render certain font styles regardless of font.
* Kerning can be off in the terminal due to monospaced font.
* Certain fonts don't include all font styles used in this package.

## Links

* [Gitlab](https://gitlab.com/imsofi/smoltext/)
* [PyPI](https://pypi.org/project/smoltext/)
