score = raw_input("Enter Score: ")
try:
	s = float(score)
	if s >= 0.9 and s <=1.0:
		print 'A'
	elif s >= 0.8:
		print 'B'
	elif s >= 0.7:
		print 'C'
	elif s >= 0.6:
		print 'D'
	elif s < 6:
		print 'F'
	else:
		"Value out of range"

except:
	print "Input must be numeric"
