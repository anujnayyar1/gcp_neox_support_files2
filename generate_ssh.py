import random
 
# The limit for the extended ASCII Character set
MAX_LIMIT = 255
 
random_string = ''
 
for _ in range(48):
    random_integer = random.randint(0, MAX_LIMIT)
    # Keep appending random characters using chr(x)
    random_string += (chr(random_integer))
 
print(random_string, len(random_string))