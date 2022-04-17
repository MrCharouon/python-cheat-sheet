# Program to convert Roman
# Numerals to Numbers
roman = {}
roman['I'] = 1
roman['V'] = 5
roman['X'] = 10
roman['L'] = 50
roman['C'] = 100
roman['D'] = 500
roman['M'] = 1000
	
# This function returns value
# of a Roman symbol
def romanToInt(s):
    sum = 0
    n = len(s)

    i = 0
    while i < n :

        # If present value is less than next value,
        # subtract present from next value and add the
        # resultant to the sum variable.
        # print(roman[s[i]],roman[s[i+1]])
        if (i != n - 1 and roman[s[i]] < roman[s[i + 1]]):
            sum += roman[s[i + 1]] - roman[s[i]]
            i += 2
            continue
        else:
            sum += roman[s[i]]
        i += 1
    return sum

# Driver Code
	
# Considering inputs given are valid
input = "MMMDCCXXIV"

print(f"Integer form of Roman Numeral is {romanToInt(input)}")

# This code is contributed by shinjanpatra
