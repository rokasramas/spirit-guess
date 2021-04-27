
SUPPORTED_LANGUAGES = {'af': 'Afrikaans',
 'ar': 'Arabic',
 'az': 'Azeri',
 'bg': 'Bulgarian',
 'bn': 'Bengali',
 'bo': 'Tibetan',
 'ca': 'Catalan',
 'ceb': 'Cebuano',
 'cs': 'Czech',
 'cy': 'Welsh',
 'da': 'Danish',
 'de': 'German',
 'el': 'Greek',
 'en': 'English',
 'eo': 'Esperanto',
 'es': 'Spanish',
 'et': 'Estonian',
 'eu': 'Basque',
 'fa': 'Farsi',
 'fi': 'Finnish',
 'fr': 'French',
 'gu': 'Gujarati',
 'ha': 'Hausa',
 'haw': 'Hawaiian',
 'he': 'Hebrew',
 'hi': 'Hindi',
 'hr': 'Croatian',
 'hu': 'Hungarian',
 'hy': 'Armenian',
 'id': 'Indonesian',
 'is': 'Icelandic',
 'it': 'Italian',
 'ka': 'Georgian',
 'kk': 'Kazakh',
 'km': 'Cambodian',
 'ky': 'Kyrgyz',
 'la': 'Latin',
 'lt': 'Lithuanian',
 'lv': 'Latvian',
 'mk': 'Macedonian',
 'ml': 'Malayalam',
 'mn': 'Mongolian',
 'mr': 'Marathi',
 'nb': 'Norwegian Bokmal',
 'nr': 'South Ndebele',
 'ne': 'Nepali',
 'nl': 'Dutch',
 'nso': 'Sepedi',
 'pa': 'Punjabi',
 'pl': 'Polish',
 'ps': 'Pashto',
 'pt': 'Portuguese',
 'pt_PT': 'Portuguese (Portugal)',
 'pt_BR': 'Portuguese (Brazil)',
 'ro': 'Romanian',
 'ru': 'Russian',
 'sk': 'Slovak',
 'sl': 'Slovene',
 'so': 'Somali',
 'sq': 'Albanian',
 'sr': 'Serbian',
 'ss': 'Swati',
 'st': 'Sotho',
 'sv': 'Swedish',
 'sw': 'Swahili',
 'te': 'Telugu',
 'th': 'Thai',
 'tl': 'Tagalog',
 'tlh': 'Klingon',
 'tn': 'Setswana',
 'tr': 'Turkish',
 'ts': 'Tsonga',
 'uk': 'Ukrainian',
 'ur': 'Urdu',
 'uz': 'Uzbek',
 've': 'Venda',
 'vi': 'Vietnamese',
 'xh': 'Xhosa',
 'zu': 'Zulu'
}

LANGUAGE_GROUPS = {
    'basic_latin': {  # https://unicode-table.com/en/blocks/basic-latin/
        "ceb", "en", "eu", "ha", "haw", "id", "la", "nr", "nso", "so", "ss",
        "st", "sw", "tlh", "tn", "ts", "xh", "zu"},
    'extended_latin': {
        "af", "az", "ca", "cs", "cy", "da", "de", "eo", "es", "et", "fi", "fr",
        "hr", "hu", "is", "it", "lt", "lv", "nb", "nl", "pl", "pt", "ro", "sk",
        "sl", "sq", "sv", "tl", "tr", "ve", "vi"},
    'cyrillic': {"bg", "kk", "ky", "mk", "mn", "ru", "sr", "uk", "uz"},
    'arabic': {"ar", "fa", "ps", "ur"},
    'devanagari': {"hi", "mr", "ne"},
    'portuguese': {"pt_BR", "pt_PT"},
}

INDIVIDUAL_LANGS = {
    "hy", "he", "bn", "pa", "el", "gu", "or", "te", "kn", "ml", "si", "th", "lo",
    "bo", "my", "ka", "mn-Mong", "km"
}

_UNICODE_BLOCKS = {
    (0, 8):   (LANGUAGE_GROUPS['basic_latin'] | LANGUAGE_GROUPS['extended_latin'],  'Basic Latin'),
    (8, 16):  (LANGUAGE_GROUPS['extended_latin'], 'Extended Latin'),
    (16, 24): (LANGUAGE_GROUPS['extended_latin'], 'Extended Latin'),
    (24, 37): (LANGUAGE_GROUPS['extended_latin'], 'Latin Extended-B'),
    (37, 43): (LANGUAGE_GROUPS['extended_latin'], 'Extended Latin'),
    (43, 48): (None, 'Spacing Modifier Letters'),
    (55, 64): ({'el'}, 'Greek and Coptic'),
    (64, 80): (LANGUAGE_GROUPS['cyrillic'], 'Cyrillic'),
    (80, 83): (LANGUAGE_GROUPS['cyrillic'], 'Cyrillic Supplement'),
    (83, 89): ({'hy'}, 'Armenian'),
    (89, 96): ({'he'}, 'Hebrew'),
    (96, 112): (LANGUAGE_GROUPS['arabic'], 'Arabic'),
    (112, 117): (None, 'Syriac'),
    (117, 120): (LANGUAGE_GROUPS['arabic'], 'Arabic Supplement'),
    (120, 124): (None, 'Thaana'),
    (124, 128): (None, 'NKo'),
    (128, 132): (None, 'Samaritan'),
    (132, 134): (None, 'Mandaic'),
    (138, 144): (LANGUAGE_GROUPS['arabic'], 'Arabic Extended-A'),
    (144, 152): (LANGUAGE_GROUPS['devanagari'], 'Devanagari'),
    (152, 160): ({"bn"},  'Bengali'),
    (160, 168): ({"pa"},  'Gurmukhi'), # i.e. Punjabi
    (168, 176): ({"gu"},   'Gujarati'),
    (176, 184): ({"or"},   'Oriya'),
    (184, 192): ({"ta"},   'Tamil'),
    (192, 200): ({"te"},   'Telugu'),
    (200, 208): ({'kn'},   'Kannada'),
    (208, 216): ({'ml'},   'Malayalam'),
    (216, 224): ({'si'},   'Sinhala'),
    (224, 232): ({'th'},   'Thai'),
    (232, 240): ({'lo'},   'Lao'),
    (240, 256): ({'bo'},   'Tibetan'),
    (256, 266): ({'my'},   'Myanmar'),
    (266, 272): ({'ka'},   'Georgian'),
    (272, 288): ({'ko'},  'Hangul Jamo'),
    (288, 312): (None, 'Ethiopic'),
    (312, 314): (None, 'Ethiopic Supplement'),
    (314, 320): (None, 'Cherokee'),
    (320, 360): (None, 'Unified Canadian Aboriginal Syllabics'),
    (360, 362): (None, 'Ogham'),
    (362, 368): (None, 'Runic'),
    (368, 370): ({'tl'}, 'Tagalog'),
    (370, 372): (None, 'Hanunoo'),
    (372, 374): (None, 'Buhid'),
    (374, 376): (None, 'Tagbanwa'),
    (376, 384): ({'km'}, 'Khmer'),
    (384, 395): ({'mn'}, 'Mongolian'),
    (395, 400): (None, 'Unified Canadian Aboriginal Syllabics Extended'),
    (400, 405): (None, 'Limbu'),
    (405, 408): (None, 'Tai Le'),
    (408, 414): (None, 'New Tai Lue'),
    (416, 418): (None, 'Buginese'),
    (418, 427): (None, 'Tai Tham'),
    (432, 440): (None, 'Balinese'),
    (440, 444): (None, 'Sundanese'),
    (444, 448): (None, 'Batak'),
    (448, 453): (None, 'Lepcha'),
    (453, 456): (None, 'Ol Chiki'),
    (461, 464): (None, 'Vedic Extensions'),
    (464, 472): (None, 'Phonetic Extensions'),
    (472, 476): (None, 'Phonetic Extensions Supplement'),
    (480, 496): (LANGUAGE_GROUPS['extended_latin'], 'Latin Extended Additional'),
    (496, 512): ({'el'},  'Greek Extended'),
    (519, 522): (None, 'Superscripts and Subscripts'),
    (528, 533): (None, 'Letterlike Symbols'),
    (533, 537): (None, 'Number Forms'),
    (704, 710): (None, 'Glagolitic'),
    (710, 712): (LANGUAGE_GROUPS['extended_latin'], 'Latin Extended-C'),
    (712, 720): (None, 'Coptic'),
    (720, 723): (None, 'Georgian Supplement'),
    (723, 728): (None, 'Tifinagh'),
    (728, 734): (None, 'Ethiopic Extended'),
    (736, 744): (None, 'Supplemental Punctuation'),
    (768, 772): (None, 'CJK Symbols and Punctuation'),
    (772, 778): ({'ja'}, 'Hiragana'),
    (778, 784): ({'ja'},  'Katakana'),
    (784, 787): ({'zh'},  'Bopomofo'),
    (787, 793): ({'ko'},  'Hangul Compatibility Jamo'),
    (794, 796): ({'zh'},  'Bopomofo Extended'),
    (799, 800): ({'ja'}, 'Kana'),
    (832, 1244):  ({'zh'}, 'CJK Unified Ideographs Extension A'),
    (1248, 2560): ({'zh'}, 'CJK Unified Ideographs'),
    (2560, 2633): (None, 'Yi Syllables'),
    (2637, 2640): (None, 'Lisu'),
    (2640, 2660): (None, 'Vai'),
    (2660, 2666): (LANGUAGE_GROUPS['cyrillic'],  'Cyrillic Extended-B'),
    (2666, 2672): (None, 'Bamum'),
    (2672, 2674): (None, 'Modifier Tone Letters'),
    (2674, 2688): (LANGUAGE_GROUPS['extended_latin'], 'Latin Extended-D'),
    (2688, 2691): (None, 'Syloti Nagri'),
    (2692, 2696): (None, 'Phags-pa'),
    (2696, 2702): (None, 'Saurashtra'),
    (2702, 2704): (LANGUAGE_GROUPS['devanagari'],  'Devanagari Extended'),
    (2704, 2707): (None, 'Kayah Li'),
    (2707, 2710): (None, 'Rejang'),
    (2710, 2712): ({'ko'}, 'Hangul Jamo Extended-A'),
    (2712, 2718): (None, 'Javanese'),
    (2720, 2726): (None, 'Cham'),
    (2726, 2728): ({'my'}, 'Myanmar Extended-A'),
    (2728, 2734): (None, 'Tai Viet'),
    (2734, 2736): (None, 'Meetei Mayek Extensions'),
    (2736, 2739): (None, 'Ethiopic Extended-A'),
    (2748, 2752): (None, 'Meetei Mayek'),
    (2752, 3451): ({'ko'}, 'Hangul Syllables'),
    (3451, 3456): ({'ko'}, 'Hangul Jamo Extended-B'),
    (3984, 4016): (None, 'CJK Compatibility Ideographs'),
    (4016, 4021): (None, 'Alphabetic Presentation Forms'),
    (4021, 4064): (LANGUAGE_GROUPS['arabic'], 'Arabic Presentation Forms-A'),
    (4071, 4080): (LANGUAGE_GROUPS['arabic'], 'Arabic Presentation Forms-B'),
    (4080, 4095): (None, 'Halfwidth and Fullwidth Forms'),
    (4096, 4104): (None, 'Linear B Syllabary'),
    (4104, 4112): (None, 'Linear B Ideograms'),
    (4136, 4138): (None, 'Lycian'),
    (4138, 4142): (None, 'Carian'),
    (4144, 4147): (None, 'Old Italic'),
    (4147, 4149): (None, 'Gothic'),
    (4152, 4154): (None, 'Ugaritic'),
    (4154, 4158): (None, 'Old Persian'),
    (4160, 4165): (None, 'Deseret'),
    (4165, 4168): (None, 'Shavian'),
    (4168, 4171): (None, 'Osmanya'),
    (4224, 4228): (None, 'Cypriot Syllabary'),
    (4228, 4230): (None, 'Imperial Aramaic'),
    (4240, 4242): (None, 'Phoenician'),
    (4242, 4244): (None, 'Lydian'),
    (4248, 4250): (None, 'Meroitic Hieroglyphs'),
    (4250, 4256): (None, 'Meroitic Cursive'),
    (4256, 4262): (None, 'Kharoshthi'),
    (4262, 4264): (None, 'Old South Arabian'),
    (4272, 4276): (None, 'Avestan'),
    (4276, 4278): (None, 'Inscriptional Parthian'),
    (4278, 4280): (None, 'Inscriptional Pahlavi'),
    (4288, 4293): (None, 'Old Turkic'),
    (4352, 4360): (None, 'Brahmi'),
    (4360, 4365): (None, 'Kaithi'),
    (4365, 4368): (None, 'Sora Sompeng'),
    (4368, 4373): (None, 'Chakma'),
    (4376, 4382): (None, 'Sharada'),
    (4456, 4461): (None, 'Takri'),
    (4608, 4672): (None, 'Cuneiform'),
    (4864, 4931): (None, 'Egyptian Hieroglyphs'),
    (5760, 5796): (None, 'Bamum Supplement'),
    (5872, 5882): (None, 'Miao'),
    (6912, 6928): ({'ja'}, 'Kana Supplement'),
    (7488, 7552): (None, 'Mathematical Alphanumeric Symbols'),
    (7904, 7920): (None, 'Arabic Mathematical Alphabetic Symbols'),
    (8192, 10862):  ({'zh'}, 'CJK Unified Ideographs Extension B'),
    (10864, 11124): ({'zh'}, 'CJK Unified Ideographs Extension C'),
    (11124, 11138): ({'zh'}, 'CJK Unified Ideographs Extension D'),
    (12160, 12194): ({'zh'}, 'CJK Compatibility Ideographs Supplement')
}

def unicode_block(num, option='lang'):
    # From https://stackoverflow.com/a/67236220/610569
    for (start, end), (langs, scripts) in _UNICODE_BLOCKS.items():
        if start <= num < end:
            if option == 'script':
                return scripts
            elif option == 'lang':
                return langs
            else:
                return langs
    return None
