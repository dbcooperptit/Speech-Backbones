""" from https://github.com/keithito/tacotron """

import re

valid_symbols = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
    't', 'u', 'v', 'w', 'x', 'y', 'z', 'à', 'á', 'â', 'ã', 'è', 'é', 'ê', 'ì', 'í', 'ð', 'ò', 'ó',
    'ô', 'õ', 'ö', 'ù', 'ú', 'ü', 'ý', 'ā', 'ă', 'đ', 'ĩ', 'ō', 'ũ', 'ū', 'ơ', 'ư', 'ạ', 'ả', 'ấ',
    'ầ', 'ẩ', 'ẫ', 'ậ', 'ắ', 'ằ', 'ẳ', 'ẵ', 'ặ', 'ẹ', 'ẻ', 'ẽ', 'ế', 'ề', 'ể', 'ễ', 'ệ', 'ỉ', 'ị',
    'ọ', 'ỏ', 'ố', 'ồ', 'ổ', 'ỗ', 'ộ', 'ớ', 'ờ', 'ở', 'ỡ', 'ợ', 'ụ', 'ủ', 'ứ', 'ừ', 'ử', 'ữ', 'ự',
    'ỳ', 'ỵ', 'ỷ', 'ỹ'
]

_valid_symbol_set = set(valid_symbols)


class CMUDict:
    def __init__(self, file_or_path, keep_ambiguous=True):

        entries = read_lexicon(file_or_path)
        self._entries = entries

    def __len__(self):
        return len(self._entries)

    def lookup(self, word):
        return [self._entries.get(word.upper()), self._entries.get(word.upper())] if self._entries.get(
            word.upper()) else None


def read_lexicon(lex_path):
    lexicon = {}
    with open(lex_path) as f:
        for line in f:
            temp = re.split(r"\s+", line.strip("\n"))
            word = temp[0]
            phones = temp[1:]
            if word.lower() not in lexicon:
                lexicon[word.lower()] = phones
    return lexicon
