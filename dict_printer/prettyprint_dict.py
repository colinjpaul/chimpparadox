#program to pretify output of large json which has been converted to dictionary


import pprint


pretify_me = input('Paste in string > ')

pretified = pprint.pformat(pretify_me)

print (pretified)

