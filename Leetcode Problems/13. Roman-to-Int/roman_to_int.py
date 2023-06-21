numerals = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
numeralValues = {'I': 1, 'V': 5, 'X': 10,
                 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
prefixes = {'I': ['V', 'X'], 'V': '', 'X': ['L', 'C'],
            'L': '', 'C': ['D', 'M'], 'D': '', 'M': ''}


def roman_to_int(roman):
    check_roman(roman)
    check_length(roman)
    valueList = get_valueList(roman)
    value = valueList_to_totalValue(valueList)
    check_value(value)
    print(f"'{roman}' is equal to {value}!")
    return value


def check_roman(roman):
    wrongDigitsList = []
    for digit in roman:
        if digit not in numerals:
            wrongDigitsList.append(digit)
    if wrongDigitsList != []:
        raise Exception(
            f"Error: Digit(s) {wrongDigitsList} not Roman Numeral(s)!")
    return


def check_length(roman):
    if len(roman) > 15:
        raise Exception("Error: Too many digits! Must be 15 or less.")
    return


def get_valueList(roman):
    valueList = []
    index = 0
    while index < len(roman):
        digit = roman[index]
        length = check_prefixes(roman, digit, index)
        value = roman[index:(int(index)+int(length))]
        valueList.append(value)
        index += length
    return valueList


def check_prefixes(roman, digit, index):
    index = int(index)
    if prefixes[digit] == '':
        return len(digit)
    elif index + 1 == len(roman) or roman[index + 1] in prefixes[str(digit)]:
        return len(digit) + 1
    elif index + 2 == len(roman) or roman[index + 1] == digit and roman[index + 2] in prefixes[digit]:
        return len(digit) + 2
    else:
        return len(digit)


def valueList_to_totalValue(valueList):
    totalValue = 0
    for item in valueList:
        itemValue = 0
        if item[-1] in prefixes[item[0]]:
            for digit in item:
                if digit == item[-1]:
                    itemValue += numeralValues[digit]
                else:
                    itemValue -= numeralValues[digit]
        else:
            for digit in item:
                itemValue += numeralValues[digit]
        totalValue += itemValue
    return totalValue


def check_value(value):
    if value > 3999:
        raise Exception(
            "Error: Value of digits exceeds limit! Must be 3,999 or below.")
    return


print(roman_to_int('MCDXCVI'))
