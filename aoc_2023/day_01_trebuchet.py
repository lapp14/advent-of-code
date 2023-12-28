

"""
--- Day 1: Trebuchet?! ---
Something is wrong with global snow production, and you've been selected to take a look. The Elves have even given you a map; on it, they've used stars to mark the top fifty locations that are likely to be having problems.

You've been doing this long enough to know that to restore snow operations, you need to check all fifty stars by December 25th.

Collect stars by solving puzzles. Two puzzles will be made available on each day in the Advent calendar; the second puzzle is unlocked when you complete the first. Each puzzle grants one star. Good luck!

You try to ask why they can't just use a weather machine ("not powerful enough") and where they're even sending you ("the sky") and why your map looks mostly blank ("you sure ask a lot of questions") and hang on did you just say the sky ("of course, where do you think snow comes from") when you realize that the Elves are already loading you into a trebuchet ("please hold still, we need to strap you in").

As they're making the final adjustments, they discover that their calibration document (your puzzle input) has been amended by a very young Elf who was apparently just excited to show off her art skills. Consequently, the Elves are having trouble reading the values on the document.

The newly-improved calibration document consists of lines of text; each line originally contained a specific calibration value that the Elves now need to recover. On each line, the calibration value can be found by combining the first digit and the last digit (in that order) to form a single two-digit number.

For example:

1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet
In this example, the calibration values of these four lines are 12, 38, 15, and 77. Adding these together produces 142.

Consider your entire calibration document. What is the sum of all of the calibration values?
"""

"""
Part 2
Your calculation isn't quite right. It looks like some of the digits are actually spelled out with letters: one, two, three, four, five, six, seven, eight, and nine also count as valid "digits".

Equipped with this new information, you now need to find the real first and last digit on each line. For example:

two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen
In this example, the calibration values are 29, 83, 13, 24, 42, 14, and 76. Adding these together produces 281.

"""

import os

NUMBER_STRINGS = [
    'one',
    'two',
    'three',
    'four',
    'five',
    'six', 
    'seven',
    'eight',
    'nine'
]

test_input = [
    '1abc2',
    'pqr3stu8vwx',
    'a1b2c3d4e5f',
    'treb7uchet',
    '9sevenvlttm',
    '422268',
    '1fourrj',
    'bx7',
    '258'
]

test_input_pt2 = [
    'two1nine',
    'eightwothree',
    'abcone2threexyz',
    'xtwone3four',
    '4nineeightseven2',
    'zoneight234',
    '7pqrstsixteen',
]

def read_input():
    script_dir = os.path.dirname(__file__)
    filepath = os.path.join(script_dir, 'inputs/01_trebuchet.txt')

    with open(filepath, encoding='utf8') as file:
        lines = [line.rstrip() for line in file]

    return lines


def replace_last_occurrance(text, substring, replace_value):
    return replace_value.join(text.rsplit(substring, 1))

def prep_row(text):
    replace_left = False
    replace_right = False

    for char_index in range(len(text)):
        if replace_left:
            break

        substring = text[:char_index]
        # print(f"substring {substring}")

        for i, number_string in enumerate(NUMBER_STRINGS):
            if substring.find(number_string) >= 0:
                text = text.replace(number_string, str(i + 1), 1)
                replace_left = True
                break
            
    for char_index in range(len(text), 0, -1):
        if replace_right:
            break 

        substring = text[char_index:]    
        # print(f"substring {substring}")     

        for i, number_string in enumerate(NUMBER_STRINGS):
            if substring.find(number_string) >= 0:
                text = replace_last_occurrance(text, number_string, str(i + 1))
                replace_right = True
                break
            
    return text



def get_row_numbers(row, text_numbers):
    current_row = row

    if text_numbers:
        current_row = prep_row(row)

    left = 0
    right = len(current_row) - 1
    while not (current_row[left].isnumeric()) or not (current_row[right].isnumeric()):         
        current_left = current_row[left]
        current_right = current_row[right]

        # print(f"left {current_left}, right {current_right}")

        if not current_left.isnumeric():
            left += 1

        if not current_right.isnumeric():
            right -= 1

    return int(float(f"{current_row[left]}{current_row[right]}"))

# The text_numbers param checks text for spelled out numbers if True
def calibrate(calibration_input, text_numbers=False):
    sums = []
    for row in calibration_input:
        result = get_row_numbers(row, text_numbers)
        sums.append(result)

    return sum(sums)


if __name__ == '__main__':
    # solution = calibrate(test_input)
    puzzle_input = read_input()

    # part 1
    print('Part 1')
    print(calibrate(puzzle_input))

    # part 2
    print('Part 2')
    print(calibrate(puzzle_input, True))
