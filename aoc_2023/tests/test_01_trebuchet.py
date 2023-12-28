from aoc_2023 import day_01_trebuchet

def test_calibrate_numbers_only():
    input_data = ['zoneight234']
    result = day_01_trebuchet.calibrate(input_data)
    assert result == 24

    input_data = ['8wo3']
    result = day_01_trebuchet.calibrate(input_data)
    assert result == 83  

def test_calibrate():
    input_data = ['eightwothree']
    result = day_01_trebuchet.calibrate(input_data, True)
    assert result == 83

def test_prep_row():
    input_data = 'eightwothree'
    result = day_01_trebuchet.prep_row(input_data)
    assert result == '8wo3'

    input_data = 'eighttwothree'
    result = day_01_trebuchet.prep_row(input_data)
    assert result == '8two3'

def test_replace_last_occurrance():
    input_data = 'mississipi'
    result = day_01_trebuchet.replace_last_occurrance(input_data, 'iss', 'asd')
    assert result == 'missasdipi'


