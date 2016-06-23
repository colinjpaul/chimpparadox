text = "X-DSPAM-Confidence:    0.8475";

findzero = text.find('0')
number = float(text[findzero:])
print number