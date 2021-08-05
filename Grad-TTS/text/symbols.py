""" from https://github.com/keithito/tacotron """

'''
Defines the set of symbols used in text input to the model.
The default is a set of ASCII characters that works well for English or text that has been run through Unidecode. For other data, you can modify _characters. See TRAINING_DATA.md for details. '''

_pad = '_'
_punctuation = ';:,.!?¡¿—…"«»“” '
_special = '-'
_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
# Phonemes
_vowels = 'iyɨʉɯuɪʏʊeøɘəɵɤoɛœɜɞʌɔæɐaɶɑɒᵻ'
_non_pulmonic_consonants = 'ʘɓǀɗǃʄǂɠǁʛ'
_pulmonic_consonants = 'pbtdʈɖcɟkɡqɢʔɴŋɲɳnɱmʙrʀⱱɾɽɸβfvθðszʃʒʂʐçʝxɣχʁħʕhɦɬɮʋɹɻjɰlɭʎʟ'
_suprasegmentals = 'ˈˌːˑ'
_other_symbols = 'ʍwɥʜʢʡɕʑɺɧ'
_diacrilics = 'ɚ˞ɫ'
_extra_phons = ['g', 'ɝ', '̃', '̍', '̥', '̩', '̯',
                '͡']  # some extra symbols that I found in from wiktionary ipa annotations

symbols = list(
    _pad + _letters + _punctuation + _special + _vowels + _non_pulmonic_consonants
    + _pulmonic_consonants + _suprasegmentals + _other_symbols + _diacrilics) + _extra_phons

symbols_set = set(symbols)
