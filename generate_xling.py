#!/usr/bin/env python3

import sys
import json
import gzip
import random

from random import choice
from argparse import ArgumentParser


# Default user and assistant token strings
DEFAULT_USER_START = '<|im_start|>user\n'
DEFAULT_ASST_START = '<|im_start|>assistant\n'
DEFAULT_END  = '<|im_end|>\n'

# Templates by language
TEMPLATES = {
    'dan': [
        '{user}Oversæt til {trg_lang}: {src}{end}{asst}{trg}{end}'
    ],
    'eng': [
        '{user}Translate into {trg_lang}: {src}{end}{asst}{trg}{end}'
    ],
    'fin': [
        '{user}Käännä {trg_lang}: {src}{end}{asst}{trg}{end}'
    ],
    'isl': [
        '{user}Þýða á {trg_lang}: {src}{end}{asst}{trg}{end}'
    ],
    'nor': [
        '{user}Oversett til {trg_lang}: {src}{end}{asst}{trg}{end}'
    ],
    'swe': [
        '{user}Översätt till {trg_lang}: {src}{end}{asst}{trg}{end}'
    ],
}


# Language names by source language in form required for target
TRG_LANGUAGE = {
    'dan': {
        'dan': 'dansk',
        'eng': 'engelsk',
        'fin': 'finsk',
        'isl': 'islandsk',
        'nor': 'norsk',
        'swe': 'svensk',
    },
    'fin': {
        'dan': 'tanskaksi',
        'eng': 'englanniksi',
        'fin': 'suomeksi',
        'isl': 'islanniksi',
        'nor': 'norjaksi',
        'swe': 'ruotsiksi',
    },
    'eng': {
        'dan': 'Danish',
        'eng': 'English',
        'fin': 'Finnish',
        'isl': 'Icelandic',
        'nor': 'Norwegian',
        'swe': 'Swedish',
    },
    'isl': {
        'dan': 'dönsku',
        'eng': 'ensku',
        'fin': 'finnsku',
        'isl': 'íslensku',
        'nor': 'norsku',
        'swe': 'sænsku',
    },
    'nor': {
        'dan': 'dansk',
        'eng': 'engelsk',
        'fin': 'finsk',
        'isl': 'islandsk',
        'nor': 'norsk',
        'swe': 'svensk',
    },
    'swe': {
        'dan': 'danska',
        'eng': 'engelska',
        'fin': 'finska',
        'isl': 'isländska',
        'nor': 'norska',
        'swe': 'svenska',
    },
}


def argparser():
    ap = ArgumentParser()
    ap.add_argument('src_lang', help='Source language (three-character code)')
    ap.add_argument('trg_lang', help='Target language (three-character code)')
    ap.add_argument('src_file', help='Source language data (text lines)')
    ap.add_argument('trg_file', help='Target language data (text lines)')
    ap.add_argument('--invert', action='store_true', help='Generate TRG->SRC')
    ap.add_argument('--random', action='store_true', help='Invert at random')
    ap.add_argument('--user-str', default=DEFAULT_USER_START)
    ap.add_argument('--asst-str', default=DEFAULT_ASST_START)
    ap.add_argument('--end-str', default=DEFAULT_END)
    ap.add_argument('--seed', default=None, type=int, help='Random seed')
    return ap


def xopen(fn):
    if fn.endswith('.gz'):
        return gzip.open(fn, 'rt')
    else:
        return open(fn)


def main(argv):
    args = argparser().parse_args(argv[1:])

    random.seed(args.seed)

    assert args.src_lang in TEMPLATES, f'no templates for {args.src_lang}'

    with xopen(args.src_file) as sf:
        with xopen(args.trg_file) as tf:
            for src, trg in zip(sf, tf):
                src, trg = src.rstrip(), trg.rstrip()

                if args.random:
                    invert = random.choice((True, False))
                else:
                    invert = args.invert

                if invert:
                    trg_lang = TRG_LANGUAGE[args.src_lang][args.trg_lang]
                    template = choice(TEMPLATES[args.src_lang])
                else:
                    src, trg = trg, src
                    trg_lang = TRG_LANGUAGE[args.trg_lang][args.src_lang]
                    template = choice(TEMPLATES[args.trg_lang])

                text = template.format(
                    src=src,
                    trg=trg,
                    trg_lang=trg_lang,
                    user=args.user_str,
                    asst=args.asst_str,
                    end=args.end_str,
                )
                data = {
                    'text': text,
                }
                print(json.dumps(data, ensure_ascii=False))


if __name__ == '__main__':
    sys.exit(main(sys.argv))
