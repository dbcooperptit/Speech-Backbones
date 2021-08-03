""" from https://github.com/keithito/tacotron """

import re
from unidecode import unidecode
from phonemizer import phonemize
from .symbols import symbols_set
from .numbers import normalize_numbers

_whitespace_re = re.compile(r'\s+')

_abbreviations = [(re.compile('\\b%s\\.' % x[0], re.IGNORECASE), x[1]) for x in [
    ('mrs', 'misess'),
    ('mr', 'mister'),
    ('dr', 'doctor'),
    ('st', 'saint'),
    ('co', 'company'),
    ('jr', 'junior'),
    ('maj', 'major'),
    ('gen', 'general'),
    ('drs', 'doctors'),
    ('rev', 'reverend'),
    ('lt', 'lieutenant'),
    ('hon', 'honorable'),
    ('sgt', 'sergeant'),
    ('capt', 'captain'),
    ('esq', 'esquire'),
    ('ltd', 'limited'),
    ('col', 'colonel'),
    ('ft', 'fort'),
]]


def expand_abbreviations(text):
    for regex, replacement in _abbreviations:
        text = re.sub(regex, replacement, text)
    return text


def expand_numbers(text):
    return normalize_numbers(text)


def lowercase(text):
    return text.lower()


def collapse_whitespace(text):
    return re.sub(_whitespace_re, ' ', text)


def to_phonemes(text: str, lang: str) -> str:
    phonemes = phonemize(text,
                         language=lang,
                         backend='espeak',
                         strip=True,
                         preserve_punctuation=True,
                         with_stress=False,
                         njobs=1,
                         punctuation_marks=';:,.!?¡¿—…"«»“”()',
                         language_switch='remove-flags')
    phonemes = ''.join([p for p in phonemes if p in symbols_set])
    return phonemes


def convert_to_ascii(text):
    return unidecode(text)


def basic_cleaners(text):
    text = lowercase(text)
    text = collapse_whitespace(text)
    phonemes = to_phonemes(text, "vi")
    return phonemes


def transliteration_cleaners(text):
    text = convert_to_ascii(text)
    text = lowercase(text)
    text = collapse_whitespace(text)
    return text


def english_cleaners(text):
    text = convert_to_ascii(text)
    text = lowercase(text)
    text = expand_numbers(text)
    text = expand_abbreviations(text)
    text = collapse_whitespace(text)
    return text
