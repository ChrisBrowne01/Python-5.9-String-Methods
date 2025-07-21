# Placeholder sample variables 
value = string = "this is some SAMPLE TEXT WHICH i wrote"
txt = "My name is Ståle!"
expand_tab_text = "H\te\tl\tl\to"
format_string = "Get a {item} for only {price}!"
split_string = "John, Peter, Vicky"
strip_text = ",,, ,,Hello world! %  ,,"
split_lines_string = "Thank you for the music\nWelcome to the jungle"
digit = "30"
value_to_check = "TEXT WHICH"

character = "o"
string_length = len(string) + 8
dictionary = {"item" : "tablet", "price" : "half price"}
tuple_names = ("John", "Peter", "Vicky")

# Displaying the use of different String Methods 
print("Displaying examples demonstraing various string methods:\n")
print("capitalize(): ", string.capitalize())	                 # Converts the first character to upper case
print("casefold(): ", string.casefold())                       #	Converts string into lower case
print("center(): ", string.center(string_length, character))   # Returns a centered string
print("count(): ", string.count(value, 5, 7))	                 # Returns the number of times a specified value occurs in a string
print("encode(): ", txt.encode(encoding="ascii", errors="backslashreplace")) # Returns an encoded version of the string
print("endswith(): ", string.endswith(value_to_check, 20, 30)) # Returns true if the string ends with the specified value
print("expandtabs(): ", expand_tab_text.expandtabs(2))	       # Sets the tab size of the string
print("find(): ", string.find(character, 4, 23))	             # Searches the string for a specified value and returns the position of where it was found
print("format(): ", format_string.format(item = "tablet", price = "half price")) # Formats specified values in a string
print("format_map(): ", format_string.format_map(dictionary))  # Formats specified values in a string
print("index(): ", string.index(character, 7, 11))	           # Searches the string for a specified value and returns the position of where it was found
print("isalnum(): ", string.isalnum())	                       # Returns True if all characters in the string are alphanumeric
print("isalpha(): ", string.isalpha())	                       # Returns True if all characters in the string are in the alphabet
print("isascii(): ", string.isascii())	                       # Returns True if all characters in the string are ascii characters
print("isdecimal(): ", digit.isdecimal())	                     # Returns True if all characters in the string are decimals
print("isdigit(): ", digit.isdigit())	                         # Returns True if all characters in the string are digits
print("isidentifier(): ", string.isidentifier())	             # Returns True if the string is an identifier
print("islower(): ", string.islower())	                       # Returns True if all characters in the string are lower case
print("isnumeric(): ", digit.isnumeric())	                     # Returns True if all characters in the string are numeric
print("isprintable(): ", string.isprintable())	               # Returns True if all characters in the string are printable
print("isspace(): ", string.isspace())	                       # Returns True if all characters in the string are whitespaces
print("istitle(): ", expand_tab_text.istitle())	               # Returns True if the string follows the rules of a title
print("isupper(): ", value_to_check.isupper())	               # Returns True if all characters in the string are upper case
print("join(): ", ",".join(tuple_names))	                     # Joins the elements of an iterable to the end of the string
print("ljust(): ", string.ljust(string_length, character))	   # Returns a left justified version of the string
print("lower(): ", string.lower())	                           # Converts a string into lower case
print("lstrip(): ", strip_text.lstrip(" %,"))	                 # Returns a left trim version of the string
maketrans_table = txt.maketrans("ål", "ac")	                   # Returns a translation table to be used in translations
print("maketrans(): ", maketrans_table)
print("partition(): ", string.partition("SAMPLE"))	           # Returns a tuple where the string is parted into three parts
print("replace(): ", txt.replace("Ståle", " Me", 2))	         # Returns a string where a specified value is replaced with a specified value
print("rfind(): ", string.rfind(character, 20, 36))	           # Searches the string for a specified value and returns the last position of where it was found
print("rindex(): ", string.rindex(character, 20, 36))	         # Searches the string for a specified value and returns the last position of where it was found
print("rjust(): ", string.rjust(string_length, character))	   # Returns a right justified version of the string
print("rpartition(): ", string.rpartition("SAMPLE"))	         # Returns a tuple where the string is parted into three parts
print("rsplit(): ", split_string.rsplit(",", 1))	             # Splits the string at the specified separator, and returns a list
print("rstrip(): ", strip_text.rstrip(" %,"))	                 # Returns a right trim version of the string
print("split(): ", split_string.split(",", 1))	               # Splits the string at the specified separator, and returns a list
print("splitlines(): ", split_lines_string.splitlines())	     # Splits the string at line breaks and returns a list. Syntax: string.splitlines([Optional: True|False])
print("startswith(): ", string.startswith("is", 2, 30))	       # Returns true if the string starts with the specified value
print("strip(): ", strip_text.strip(" %,"))	                   # Returns a trimmed version of the string
print("swapcase(): ", string.swapcase())	                     # Swaps cases, lower case becomes upper case and vice versa
print("title(): ", string.title())	                           # Converts the first character of each word to upper case
print("translate(): ", string.translate(maketrans_table))	     # Returns a translated string
print("upper(): ", string.upper())	                           # Converts a string into upper case
print("zfill(): ", string.zfill(10))	                         # Fills the string with a specified number of 0 values at the beginning
