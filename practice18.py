import re
text="hey there"
a=re.search("hey",text)
if a:
    print("word found")
else:
    print("word not found")
