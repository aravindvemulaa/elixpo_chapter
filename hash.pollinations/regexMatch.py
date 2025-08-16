import re

TOKEN_REGEX = re.compile(r'Poll_[A-Z2-7]{27}')

text = """
Some random code:
api_key = "Poll_EC53MY42FN5NTX3JQNJJIY3LE7U frgrggrg kjg rv rn gbrjng hrb grf"
4grgrgrgrgrgrghrgvrg
"""

matches = TOKEN_REGEX.findall(text)
print(matches)  
