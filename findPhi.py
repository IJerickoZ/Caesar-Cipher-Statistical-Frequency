message = "IDZXAAILDQXGSHLXIWDCTHIDCT"
print("message: ", message)
print("")

loweralphabet_dict = {}
unicode = 97
for i in range(26):
    loweralphabet_dict[chr(unicode)] = unicode
    unicode +=1


frequency_message = {}
loweralphabet_list = list(message)
for letter in loweralphabet_dict:
    if letter in loweralphabet_list:
        letter_count =loweralphabet_list.count(letter)
        letter_frequency = letter_count/len(loweralphabet_list)
        frequency_message[letter] = letter_frequency

    else:
        letter_frequency = 0
        frequency_message[letter] = letter_frequency


upperalphabet_dict = {}
unicode = 65
for i in range(26):
    upperalphabet_dict[chr(unicode)] = unicode
    unicode +=1

uppercaseletterslist = list(upperalphabet_dict)
cleaned_messagelist = []
for letter in message:
    if letter in uppercaseletterslist:
        cleaned_messagelist.append(letter)


frequency_uppercasemessage = {}
for letter in uppercaseletterslist:
    if letter in cleaned_messagelist:
        upcase_count = cleaned_messagelist.count(letter)
        upcase_frequency = upcase_count/len(cleaned_messagelist)
        frequency_uppercasemessage[letter] = upcase_frequency


print("This is the frequency of letters in message\n", frequency_uppercasemessage)
print("")
source_frequency = {"A":0.080, "B": 0.015, "C": 0.030, "D": 0.040, "E": 0.130, "F": 0.020, "G":0.015, "H":0.060, "I": 0.065, "J": 0.005, "K": 0.005, "L": 0.035, "M":0.030, "N": 0.070, "O":0.080, "P": 0.020, "Q": 0.002, "R":0.065, "S": 0.060, "T": 0.090, "U": 0.030, "V": 0.010, "W": 0.015, "X": 0.005, "Y": 0.020, "Z": 0.002}
print("This is the frequency of alphabets in the english language\n", source_frequency)
print("")

c_valuedict = {}
start = 0
for letter in uppercaseletterslist:
        c_valuedict[letter] = start
        start +=1

print("These are the positions", c_valuedict)

print("These are the i values linked to alphabets\n",c_valuedict)
i_correlations = {}

print("")
for i in range(0,26):
    sum_equation = 0
    for letter1, frequency in frequency_uppercasemessage.items():
        letter1pos = c_valuedict[letter1]
        if letter1pos >= i:
            x_pos = letter1pos - i 
        else:
            adjustedpos = i - letter1pos
            reverse_alphpos = 26 - adjustedpos
            x_pos = reverse_alphpos

        for l, c in c_valuedict.items():
            if c == x_pos:
                x_char = l

        freq_xchar = source_frequency[x_char]
        freq_letter = frequency
        equation = freq_xchar * freq_letter 
        sum_equation += equation

    i_correlations[i] = sum_equation

print("")
values_list = []
for values in i_correlations.values():
    values_list.append(values)

finallist = sorted(values_list)

sorteddict = {}
for value in reversed(finallist):
    for k,v in i_correlations.items():
        if value == v:
            sorteddict[k] = value

print("")
print("The Sorted i – Correlation with Cleaned Text\n")

for k,v in sorteddict.items():
    print("The position is %d and the correlation is %.4f"%(k,v))

print("")