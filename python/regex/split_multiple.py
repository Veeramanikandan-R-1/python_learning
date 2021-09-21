import re
data = 00,000,000.000
print(re.split(r"[.,]",str(data)))
