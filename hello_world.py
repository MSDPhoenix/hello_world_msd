# 1. TASK: print "Hello World"
print("Hello World")

# 2. print "Hello Noelle!" with the name in a variable
name = "Noelle"
print("Hello",name,"!")	# with a comma
print("Hello "+name+"!")	# with a +

# 3. print "Hello 42!" with the number in a variable
name = 42
print ("Hello",name,"!")	# with a comma
print("Hello "+str(name)+"!")	# with a +	-- this one should give us an error!

# 4. print "I love to eat sushi and pizza." with the foods in variables
fave_food1 = "sushi"
fave_food2 = "pizza"
print("I love to eat {} and {}.".format(fave_food1,fave_food2)) # with .format()
print(f"I love to eat {fave_food1} and {fave_food2}.") # with an f string

# 5.  other string methods

print("ear nose throat".partition("nose"))

print("0123456789".partition("45"))

print("ASDFGHKLL".lower())

print("asdfasdgljglsgjalsf".upper())

print("bananas make me laugh".removeprefix("bananas "))

print("asdfdswsasdfgfsdsasdfgdds".count("s"))

print("asdfasf".isalpha())

print("asdfasf".isdigit())

print("123123".isalpha())

print("123123".isdigit())

print("asdflkas".islower())

print("ADSLFHSAD".isupper())

print("ADSLFHSAD".islower())

print("1234567890".endswith("90"))

print("have you ever seen the rain?".title())

print("www.example.com".lstrip("wxcoz"))

print("        spacious       x")
print("        spacious       x".lstrip())