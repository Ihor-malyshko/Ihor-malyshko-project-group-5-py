# Translates Cyrillic input typed in QWERTY layout to the corresponding Latin characters.
KEYBOARD_LAYOUT = str.maketrans(
    "йцукенгшщзхъфывапролджэячсмитьбюіїєґё", "qwertyuiop[]asdfghjkl;'zxcvbnm,.iie`~"
)
