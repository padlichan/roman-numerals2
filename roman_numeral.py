def romanise(num):
    ones_roman = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
    tens_roman = ["", "X", "XX", "XXX", "XL", "L", " LX", "LXX", "LXXX", "XC"]
    hundreds_roman = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
    thousands_roman = ["", "M", "MM", "MMM"]
    
    if num > 3999:
        raise ValueError("number is greater than maximum of 3999")
    elif num <= -1:
        raise ValueError("number is lower than minimum of 0")

    output = ""
    
    thousands = num // 1000
    output += thousands_roman[thousands]
    num -= thousands * 1000
    
    hundreds = num // 100
    output += hundreds_roman[hundreds]
    num -= hundreds * 100
    
    tens = num // 10
    output += tens_roman[tens]
    num -= tens * 10 

    output += ones_roman[num]

    return output