""" from https://github.com/keithito/tacotron """

from text import cmudict

_pad        = '_'
_punctuation = '!\'(),.:;?"() '
_special = '-'
_letters = '0123546789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'

# Prepend "@" to ARPAbet symbols to ensure uniqueness:
_arpabet = ['@' + s for s in cmudict.valid_symbols]

# Export all symbols:
symbols = [_pad] + list(_special) + list(_punctuation) + list(_letters) + _arpabet