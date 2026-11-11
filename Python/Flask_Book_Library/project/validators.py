import re

# Biała lista: litery (także polskie), cyfry, spacja i . , ' -
TEXT_PATTERN = re.compile(r"^[\w .,'-]{1,64}$")


def validate_text(field, value):
    value = str(value).strip()
    if not TEXT_PATTERN.fullmatch(value):
        raise ValueError(f'{field}: niedozwolone znaki lub długość')
    return value


def validate_int(field, value, low, high):
    try:
        value = int(value)
    except (TypeError, ValueError):
        raise ValueError(f'{field}: wymagana liczba')
    if not low <= value <= high:
        raise ValueError(f'{field}: zakres {low}-{high}')
    return value
