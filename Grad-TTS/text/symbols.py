# Phonemes
""" from https://github.com/keithito/tacotron """

'''
Defines the set of symbols used in text input to the model.
'''
_pad = '_'
_punctuation = ';:,.!?¡¿—…"«»“”() '
_special = '-'
_letters = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
# Phonemes
_vowels = 'iyɨʉɯuɪʏʊeøɘəɵɤoɛœɜɞʌɔæɐaɶɑɒᵻ'
_non_pulmonic_consonants = 'ʘɓǀɗǃʄǂɠǁʛ'
_pulmonic_consonants = 'pbtdʈɖcɟkɡqɢʔɴŋɲɳnɱmʙrʀⱱɾɽɸβfvθðszʃʒʂʐçʝxɣχʁħʕhɦɬɮʋɹɻjɰlɭʎʟ'
_suprasegmentals = 'ˈˌːˑ'
_other_symbols = 'ʍwɥʜʢʡɕʑɺɧ'
_diacrilics = 'ɚ˞ɫ'
_extra_phons = ['g', 'ɝ', '̃', '̍', '̥', '̩', '̯','̪',
                '͡']  # some extra symbols that I found in from wiktionary ipa annotations

# Export all symbols:
symbols = list(
    _pad + _letters + _punctuation + _special + _vowels + _non_pulmonic_consonants
    + _pulmonic_consonants + _suprasegmentals + _other_symbols + _diacrilics) + _extra_phons

# Special symbol ids
SPACE_ID = symbols.index(" ")

symbols_set = set(symbols)
