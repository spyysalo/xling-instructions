#!/usr/bin/env python3

import sys
import gzip

from random import choice
from argparse import ArgumentParser


# Default user and assistant token strings
DEFAULT_USER_START = '<|im_start|>user\n'
DEFAULT_ASST_START = '<|im_start|>assistant\n'
DEFAULT_END  = '<|im_end|>\n'

# Templates by language
TEMPLATES = {
    'eng': [
        '{user}Translate into {trg_lang}: {src}{end}{asst}{trg}{end}'
    ],
    'fin': [
        '{user}Käännä {trg_tra}: {src}{end}{asst}{trg}{end}'
    ],
    'swe': [
        '{user}Översätt till {trg_lang}: {src}{end}{asst}{trg}{end}'
    ],
}

# Inverted templates by language
INV_TEMPLATES = {
    'eng': [
        '{user}Translate into {src_lang}: {trg}{end}{asst}{src}{end}'
    ],
    'fin': [
        '{user}Käännä {src_tra}: {trg}{end}{asst}{src}{end}'
    ],
    'swe': [
        '{user}Översätt till {src_lang}: {trg}{end}{asst}{src}{end}'
    ],
}

# Language names by source language
LANGUAGE = {
    'fin': {
        'eng': 'englanti',
        'fin': 'suomi',
        'swe': 'ruotsi',
    },
    'eng': {
        'eng': 'English',
        'fin': 'Finnish',
        'swe': 'Swedish',
    },
    'swe': {
        'eng': 'engelska',
        'fin': 'finska',
        'swe': 'svenska',
    },
}

# Translative forms of language by source language
TRANSLATIVE = {
    'fin': {
        'eng': 'englanniksi',
        'fin': 'suomeksi',
        'swe': 'ruotsiksi',
    }
}

def argparser():
    ap = ArgumentParser()
    ap.add_argument('src_lang', help='Source language (three-character code)')
    ap.add_argument('trg_lang', help='Target language (three-character code)')
    ap.add_argument('src_file', help='Source language data (text lines)')
    ap.add_argument('trg_file', help='Target language data (text lines)')
    ap.add_argument('--invert', action='store_true', help='Generate TRG->SRC')
    ap.add_argument('--user-str', default=DEFAULT_USER_START)
    ap.add_argument('--asst-str', default=DEFAULT_ASST_START)
    ap.add_argument('--end-str', default=DEFAULT_END)
    return ap


def xopen(fn):
    if fn.endswith('.gz'):
        return gzip.open(fn, 'rt')
    else:
        return open(fn)


def main(argv):
    args = argparser().parse_args(argv[1:])

    assert args.src_lang in TEMPLATES, f'no templates for {args.src_lang}'
    
    with xopen(args.src_file) as sf:
        with xopen(args.trg_file) as tf:
            for src, trg in zip(sf, tf):
                src, trg = src.rstrip(), trg.rstrip()

                src_lang = LANGUAGE[args.src_lang][args.src_lang]
                trg_lang = LANGUAGE[args.src_lang][args.trg_lang]
                src_tra = TRANSLATIVE.get(args.src_lang, {}).get(args.src_lang)
                trg_tra = TRANSLATIVE.get(args.src_lang, {}).get(args.trg_lang)

                if not args.invert:
                    template = choice(TEMPLATES[args.src_lang])
                else:
                    template = choice(INV_TEMPLATES[args.src_lang])

                print(template.format(
                    src=src,
                    trg=trg,
                    src_lang=src_lang,
                    trg_lang=trg_lang,
                    src_tra=src_tra,
                    trg_tra=trg_tra,
                    user=args.user_str,
                    asst=args.asst_str,
                    end=args.end_str,
                ))


if __name__ == '__main__':
    sys.exit(main(sys.argv))
