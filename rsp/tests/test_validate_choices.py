"""Tests to validate DEFAULT_CHOICES tuple."""

from collections import defaultdict

from rsp.rsp import choices_config


def test_is_tuple():
    """DEFAULT_CHOICES should be a tuple."""
    assert isinstance(choices_config(), tuple)


def test_choice_strings():
    """Each item in DEFAULT_CHOICES must be a string value."""
    for choice in choices_config():
        assert isinstance(choice, str)


def test_length():
    """Number of choices must be greater than 1."""
    assert len(choices_config()) > 1


def test_odd_number():
    """Number of choices must be odd."""
    assert len(choices_config()) % 2 == 1


def test_not_start_with_q():
    """No choice can begin with 'Q' (reserved for 'Quit')."""
    for choice in choices_config():
        assert not choice[0].lower() == 'q', f"Bad option: {choice}"


def test_not_start_with_space():
    """No choice can begin with a space."""
    for choice in choices_config():
        assert not choice[0].lower() == ' ', f"Bad option: {choice}"


def test_no_empty_names():
    """No choice can be an empty string."""
    for choice in choices_config():
        assert choice != '', "Bad option: Empty string"


def test_unique_first_letter():
    """Each choice must have a unique first letter (case-insensitive)."""
    first_letters = defaultdict(list)
    for choice in choices_config():
        first_letters[choice[0].lower()].append(choice)
    duplicates = {k: v for k, v in first_letters.items() if len(v) > 1}
    assert len(duplicates) == 0, f"Duplicate first letters found: {duplicates}"
