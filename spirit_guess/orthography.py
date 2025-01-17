import string
from collections import Counter

from spirit_guess.languages import unicode_block


def count_chars_in_blocks(text: str, option='lang', normalize=True, remove_unknown=False) -> Counter:
    # Initialize counter.
    block_counts = Counter()
    for ch in text:  # Iterate through each character.
        if ch in string.punctuation or not ch.strip() or ch.isdigit():
            continue
        try:
            # For some reason, the original code shifts to right by 4 bits
            # See https://stackoverflow.com/a/8345671/610569
            this_block = unicode_block(ord(ch) >> 4, option=option)
            if option == 'lang':
                block_counts.update(this_block)
            elif option == 'script':
                block_counts[this_block] += 1
        except (TypeError, KeyError):
            block_counts['unknown'] += 1
    # Normalize ths score.
    if normalize:
        sum_scores = sum(block_counts.values())
        for lang, count in block_counts.items():
            block_counts[lang] = count / sum_scores
    # Remove unknown, if user specifies.
    if remove_unknown:
        del block_counts['unknown']
    # Return the counter object.
    return block_counts
