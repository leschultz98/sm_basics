import math
import string
import pygame
import time


# Waypoint 1: Say Greeting
def hello(name):
    """Display a simple greeting."""
    return 'Hello {}!'.format(name.strip())


# Waypoint 2: Pythagorean Theorem
def calculate_hypotenuse(a, b):
    """Calculate the length of the hypotenuse of a right triangle."""
    return math.sqrt(a ** 2 + b ** 2)


# Waypoint 3: Test whether all Conditions are True
def are_all_conditions_true(conditions):
    """Test whether all conditions are True."""
    if conditions:
        return False not in conditions
    return None


# Waypoint 4: Test whether at least one Condition is True
def is_a_condition_true(conditions):
    """Test whether at least conditions are True."""
    if conditions:
        return True in conditions
    return None


# Waypoint 5: Filter List of Integers
def filter_integers_greater_than(l, n):
    """Create a list which every integer greater than n."""
    return [number for number in l if number > n]


# Waypoint 6: Find Cheapest Hotels
def find_cheapest_hotels(hotel_daily_rates, maximum_daily_rate):
    """Find cheapest hotels."""
    return [x for x, y in sorted(hotel_daily_rates, key=lambda rate: rate[1])
            if y <= maximum_daily_rate]


# Waypoint 7: Calculate Distance between two 2D Points
def calculate_euclidean_distance_between_2_points(p1, p2):
    """Calculate distance between two 2D points."""
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)


# Waypoint 8: Calculate Distance between several 2D Points
def calculate_euclidean_distance_between_points(points):
    """Calculate distance between several 2D points."""
    # Catch exception
    if len(points) < 2:
        raise ValueError('The list MUST contain at least 2 points')

    return sum([math.sqrt((points[x - 1][0] - points[x][0]) ** 2 +
                          (points[x - 1][1] - points[x][1]) ** 2)
                for x in range(1, len(points))])


# Waypoint 9: Capitalize the Words of a String
def capitalize_words(s):
    """Return a copy of the string with all the words capitalized.

    This function sets the first character in each word of the string `s`
    to uppercase and the rest to lowercase.

    The function removes any duplicate whitespace characters between
    words.

    If `None` is passed, the function returns `None`.

    @param s: a string that possibly contains words separated by whitespace
        characters.

    @return: a string where the first character in each word of the string
        `s`has been converted to uppercase and all remaining characters of
        this word have been converted to lowercase.

    @raise TypeError: if the argument `s` is not a string.
    """
    # Catch exception
    if not isinstance(s, str):
        raise TypeError('Not a string')

    if s:
        return ' '.join(s.split()).title()
    return None


# Waypoint 10: Uppercase and Lowercase Words
def uppercase_lowercase_words(s):
    """Change even word to uppercase and odd word to lowercase."""
    # Catch exception
    if not isinstance(s, str):
        raise TypeError('Not a string')

    if s:
        return ' '.join([s.split()[x].upper()
                         if x % 2 == 0 else s.split()[x].lower()
                         for x in range(len(s.split()))])
    return None


# Waypoint 11: Factorial
def factorial(n):
    """Calculate factorial of a number (n!)."""
    # Catch exception
    if not isinstance(n, int):
        raise TypeError('Not an integer')
    if n < 0:
        raise ValueError('Not a positive integer')
    return 1 if n == 0 else n * factorial(n - 1)


# Waypoint 12: Convert a Digit Character to an Integer
def char_to_int(c):
    """Convert a digit character to an integer."""
    # Catch exception
    if not isinstance(c, str):
        raise TypeError('Not a string')
    if len(c) > 1 or ord(c) < 48 or ord(c) > 57:
        raise ValueError('Not a single digit')
    return ord(c) - 48


# Waypoint 13: Convert a String of Digit Characters to an Integer
def string_to_int(s):
    """Convert a string of digit characters to an integer."""
    # Catch exception
    if not isinstance(s, str):
        raise TypeError('Not a string')
    integer = 0
    for x in range(len(s)):
        if 47 < ord(s[x]) < 58:
            integer += char_to_int(s[x]) * 10 ** (len(s) - x - 1)
        else:
            raise ValueError('Not a positive integer string expression')
    return integer


# Waypoint 14: Test Palindrome String
def is_palindrome(value):
    """Check whether a string is palindrome."""
    # Convert value to string
    # Remove punctuation
    changed_value = str(value).lower().translate(
        str(value).maketrans("", "", string.punctuation))
    # Remove whitespaces
    changed_value = changed_value.replace(' ', '')
    # Compare first character with last character
    return changed_value == changed_value[::-1]


# Waypoint 15: Convert Roman Numerals to Integer
def roman_numeral_to_int(roman_numeral):
    """Convert roman numerals to integer."""
    symbols = {"N": 0, "I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500,
               "M": 1000}
    subtraction = {"IV": -2, "IX": -2, "XL": -20, "XC": -20, "CD": -200,
                   "CM": -200}
    add = 0
    # Catch exception
    if not isinstance(roman_numeral, str):
        raise TypeError('Not a string')
    if roman_numeral:
        for character in roman_numeral:
            if character in symbols:
                add += symbols[character]
            else:
                raise ValueError('Not a Roman numeral')
        subtract = sum([roman_numeral.count(key) *
                        subtraction[key] for key in subtraction])
    else:
        raise ValueError('Not a Roman numeral')
    return add + subtract


# Waypoint 16: Play a Melody
def play_melody(melody, sound_basedir):
    """Play sound."""
    pygame.init()
    notes = {'C#': 'Db', 'D#': 'Eb', 'F#': 'Gb', 'G#': 'Ab', 'A#': 'Bb'}
    for note in melody:
        if '#' in note:
            note = note.replace(note[:2], notes[note[:2]])
        path = '{}{}.ogg'.format(sound_basedir, note.lower())
        print(path)
        pygame.mixer.Sound(path).play(maxtime=450, fade_ms=50)
        time.sleep(0.2)
