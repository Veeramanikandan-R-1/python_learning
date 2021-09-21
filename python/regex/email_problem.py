import re
email='abc@gmail.com'
match=re.findall(r'^[a-z]+@[a-z]+.[a-z]+',email)
print(match)
pattern_email=r'([a-z]+)@([a-z]+).([a-z]+)'
match_1=re.match(pattern_email,email)
print(match_1.groupdict())
