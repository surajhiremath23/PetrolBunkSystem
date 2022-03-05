import re
pswd="SSuu@1"
reg="^([A-Z][A-Z])([a-z][a-z])([@$!%*#?&])([0-9])(?=.{0,6})$"

match_re = re.compile(reg)

# searching regex
res = re.search(match_re, pswd)

# validating conditions
if res:
   print("Valid Password")
else:
   print("Invalid Password")