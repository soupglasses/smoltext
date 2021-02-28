#!/usr/bin/env python3
import argparse
import smoltext.fonts as fonts

fonts = {
    'subscript': fonts.subscript,
    'emoji': fonts.emoji,
    'smallcaps': fonts.smallcaps,
    'bold': fonts.bold,
    'handwriting': fonts.handwriting,
    'italic': fonts.italic,
    'demonic': fonts.demonic,
    'fancy': fonts.fancy,
    'monospace': fonts.monospace,
}

def main():
    parser = argparse.ArgumentParser(
        description="A font utility to use the extra fonts included in utf8."
    )
    parser.add_argument(
        'text', nargs='*',
        help="text to process"
    )
    parser.add_argument(
        '-c', '--copy', action="store_true",
        help="copies processed text to clipboard"
    )
    parser.add_argument(
        '-f', '--font', default='subscript', choices=fonts, metavar='FONT',
        help="which font to use"
    )
    parser.add_argument(
        '--list-fonts', action="store_true",
        help="list all supported fonts"
    )
    args = parser.parse_args()

    if args.list_fonts:
        print(
            "Fonts:",
            *(f"{font.translate(fonts[font])} ({font})" for font in fonts),
            sep='\n • ',
        )
        quit()

    if args.text:
        text = " ".join(args.text)
    else:
        text = input('> ')

    print(text.translate(fonts[args.font]))
