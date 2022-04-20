#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from tabulate import tabulate
import os

OKGREEN = '\033[92m'
OKCYAN='\033[0;36m' 
OKMAGENTA = '\u001b[35;1m'
OKWHITE = '\u001b[37;1m'
WARNING = '\u001b[33;1m'
FAIL = '\u001b[31;1m'
RESET = '\033[0m'


BASE_LIST = [
	"base45", "base62", "base32", 
	"base64", "base16", "base85", 
	"base58"
]

FORMAT_LIST = [
	"caesar_ascii", "old-phone", "dec", "hex", 
	"bin", "DNA", "netbios", "walross", 
	"brainfuck", "cloudflare", "xor", "rc4", 
	"polybe", "vigenere", "bacon", "bacon-bin", 
	"rail-fence", "deadfish", "braille", "url",
] + BASE_LIST


DESCRIPTIONS = [
	"Decode/encode Caesar, on the ascii table",
	"Use T9-SMS code, to decode/encode", 
	"Will just convert your ascii char, into their decimal value in ascii table", 
	"Will just convert your ascii char, into their hexadecimal value in ascii table",
	"Convert your data into binary",
	"Decode/encode string into a DNA sequence",
	"Decode/encode with netbios algorithm",
	"Decode/encode your data with the morse code",
	"Brainfuck esoteric programming language invented by Urban Müller, encode your data with this one",
	"Obfuscate data with cloudflare algorithm",
	"Use this format to xor two strings, xor is an eXclusive OR",
	"Rivest Cipher 4, is a stream cipher, you can use it to cipher the data but it requires a key",
	"Polybe cipher is a substitution cipher using a matrix of letter to substitute as a key",
	"The Vigenere cipher is a polyalphabetic cipher, requires a key",
	"Baconian encoding",
	"Baconian encoding with binary",
	"The Rail Fence Cipher, also known as zigzag cipher, is a transposition cipher that jumbles up the letters",
	"Deadfish is an interpreted programming langauge invented by Jonathan Todd Skinner",
	"The braille language used by blind people",
	"Url encoding/decoding", 
	"Base45 encoding, use upper chars + digits '$%*+\\-./:'",
	"Base62 encoding, use upper/lower chars + digits",
	"Base32 encoding, use upper chars + digits [2-7] and padding",
	"Base64 encoding use all the chars upper/lower + digits + '+/'",
	"Base16 encoding same as hex format",
	"Base85 encoding us digits + chars upper/lower + '!#$%&()*+\\-;<=>?@^_`{|}~'",
	"Base58 encoding, is done two possible list of characters BITCOIN or RIPPLE, default is set to BITCOIN but you can see RIPPLE with brute force method",
]


SHOW_MENU_DATA = {
	"Available Encoding" : FORMAT_LIST,
	"Description" : DESCRIPTIONS
	}

# Define const output files.

ENCODED_FILE = "encoded.txt" # Describe where the encoded data will be store, you can change the name as you want ;)
DECODED_FILE = "decoded.txt" # Describe where the decoded data will be store, you can change the name as you want ;)

TAB_SIZE = 7 # Describe the size you want for the table code error output like (walross, braille, bacon, ...)!

# Define Message to print when encoding/decoding

MESSAGE_LIST_ENCODING = [
	f"{OKCYAN} [+] We are encoding using caesar on ascii table\n ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~{RESET}",
	f"{OKCYAN} [+] We are encoding with the T9 SMS code\n ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~{RESET}",
	f"{OKCYAN} [+] We are converting, into decimal\n ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~{RESET}",
	f"{OKCYAN} [+] We are converting, into hexadecimal\n ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~{RESET}",
	f"{OKCYAN} [+] We are converting, into binary\n ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~{RESET}",
	f"{OKCYAN} [+] We are encoding this text as a DNA sequence\n ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~{RESET}",
	f"{OKCYAN} [+] We are encoding with netbios\n ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~{RESET}",
	f"{OKCYAN} [+] We are encoding in morse code\n ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~{RESET}",
	f"{OKCYAN} [+] We are encoding with brainfuck \n ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~{RESET}",
	f"{OKCYAN} [+] We are obfuscating with cloudflare\n ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~{RESET}",
	f"{OKCYAN} [+] We are xoring the string in your file\n ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~{RESET}",
	f"{OKCYAN} [+] We are ciphering with RC4\n ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~{RESET}\n{WARNING} [*] The data will be written as hexadecimal output...{RESET}",
	f"{OKCYAN} [+] We are encoding with Polybe substitution\n ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~{RESET}",
	f"{OKCYAN} [+] We are encoding with Vigenere\n ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~{RESET}\n{WARNING} [*] Encoding is done only with the letter of alphabet {RESET}",
	f"{OKCYAN} [+] We are encoding with Baconian cipher\n ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~{RESET}",
	f"{OKCYAN} [+] We are encoding with Binary Baconian cipher\n ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~{RESET}",
	f"{OKCYAN} [+] We are encoding with Rail Fence cipher\n ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~{RESET}",
	f"{OKCYAN} [+] We are encoding with deadfish \n ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~{RESET}",
	f"{OKCYAN} [+] We are encoding with braille cipher\n ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~{RESET}",
	f"{OKCYAN} [+] We are converting data to url encoding\n ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~{RESET}",
	f"{OKCYAN} [+] We are encoding with that base\n ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~{RESET}",
]

MESSAGE_LIST_DECODING = [
	f"{OKCYAN} [+] We are decoding using caesar on ascii table\n ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~{RESET}",
	f"{OKCYAN} [+] We are decoding with the T9 SMS code\n ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~{RESET}",
	f"{OKCYAN} [+] We are converting, decimal into text\n ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~{RESET}",
	f"{OKCYAN} [+] We are converting, hexadecimal into text\n ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~{RESET}",
	f"{OKCYAN} [+] We are converting, binary into text\n ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~{RESET}",
	f"{OKCYAN} [+] We are decoding this DNA sequence into text\n ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~{RESET}",
	f"{OKCYAN} [+] We are decoding with netbios\n ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~{RESET}",
	f"{OKCYAN} [+] We are decoding morse code\n ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~{RESET}",
	f"{OKCYAN} [+] We are decoding with brainfuck \n ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~{RESET}",
	f"{OKCYAN} [+] We are desobfuscating with cloudflare\n ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~{RESET}",
	f"{OKCYAN} [+] We are xoring the string into your file\n ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~{RESET}",
	f"{OKCYAN} [+] We are deciphering RC4\n ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~{RESET}\n{WARNING} [*] The data will be written as hexadecimal output...{RESET}",
	f"{OKCYAN} [+] We are decoding with Polybe substitution\n ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~{RESET}",
	f"{OKCYAN} [+] We are decoding with Vigenere\n ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~{RESET}\n{WARNING} [*] Decoding is done only with the alphabet {RESET}",
	f"{OKCYAN} [+] We are decoding with Baconian cipher\n ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~{RESET}",
	f"{OKCYAN} [+] We are decoding with Binary Baconian cipher\n ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~{RESET}",
	f"{OKCYAN} [+] We are decoding with Rail Fence cipher\n ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~{RESET}",
	f"{OKCYAN} [+] We are decoding with deadfish \n ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~{RESET}",
	f"{OKCYAN} [+] We are decoding with braille cipher\n ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~{RESET}",
	f"{OKCYAN} [+] We are decoding url data\n ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~{RESET}",
	f"{OKCYAN} [+] We are decoding that base\n ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~{RESET}",
]

# Defining usage way, to avoid repetition for each help menu !

USAGE_WITH_OFFSET = "[+] Usage: python3 main.py [FORMAT] [DECODE/ENCODE] OFFSET [ENCODED_FILE/TO_ENCODE_FILE]"
USAGE_WITH_KEY = "[+] Usage: python3 main.py [FORMAT] [DECODE/ENCODE] KEY [ENCODED_FILE/TO_ENCODE_FILE]"
USAGE = "[+] Usage: python3 main.py [FORMAT] [DECODE/ENCODE] [ENCODED_FILE/TO_ENCODE_FILE]" 

# This is the home menu.

def home():
	os.system("clear")
	home = """      
   ████████                                 
  ██░░░░░░██                                
 ██      ░░  ██   ██ ██████  █████  ███████ 
░██         ░██  ░██░░██░░█ ██░░░██░░██░░░██
░██    █████░██  ░██ ░██ ░ ░███████ ░██  ░██
░░██  ░░░░██░██  ░██ ░██   ░██░░░░  ░██  ░██
 ░░████████ ░░██████░███   ░░██████ ███  ░██
  ░░░░░░░░   ░░░░░░ ░░░     ░░░░░░ ░░░   ░░

  {{ Author }} : [ {auth} ]
  {{ Description }} : [ {desc} ]
  {{ Version }} : [ {version} ]
  {{ Doc }} : [ {doc} ]
	"""
	return home.format(
		auth=f"{OKMAGENTA}D0pp3lgang3r{RESET}",
		desc=f"{FAIL}Tool to encode/decode data{RESET}",
		version=f"{OKWHITE}1.0{RESET}",
		doc=f"{WARNING}python3 guren.py --help{RESET}"
	)

# Print all the availables encoding formats of the tool.

def show():
	return tabulate(SHOW_MENU_DATA, headers="keys", tablefmt="fancy_grid")

# Help menu for all formats

def helpCaesar(alg='caesar_ascii', desc='Encode data on the ascii table, with caesar'):
	txt = f"""
 {USAGE_WITH_OFFSET}

 [?] Information : {desc}

 [++] Exemples :\n 
 python3 main.py --format {alg} --encode --offset 62 -f input.txt
 python3 main.py --format {alg} --decode --offset 62 -f encoded.txt
 python3 main.py --format {alg} --decode --force -f encoded.txt # Will brute force

{FAIL} [!] --offset : Must absolutely be specified for encoding, choose it between [1-255] !{RESET}

{FAIL} [!] --decode : Can specify offset or not for decoding, if not then use brute force. {RESET}
	"""
	return txt

def helpOldPhone(alg="old-phone", desc=DESCRIPTIONS[1]):
	txt = f"""
 [+] Usage: python3 main.py [FORMAT] [DECODE/ENCODE] [ENCODED_FILE/TO_ENCODE_FILE]

 [?] Information : {desc}

 [++] Exemples :\n
 python3 main.py --format {alg} --encode -f input.txt
 python3 main.py --format {alg} --decode -f encoded.txt
	"""
	return txt

def helpNetbios():
	return helpCaesar(alg="netbios", desc=DESCRIPTIONS[7])

def helpDecimal():
	return helpOldPhone(alg="dec", desc=DESCRIPTIONS[2])

def helpHex():
	return helpOldPhone(alg="hex", desc=DESCRIPTIONS[3])

def helpBin():
	return helpOldPhone(alg="bin", desc=DESCRIPTIONS[4])

def helpBraille():
	return helpOldPhone(alg="braille", desc=DESCRIPTIONS[18])

def helpWalross():
	return helpOldPhone(alg="walross", desc=DESCRIPTIONS[7])

def helpCloudflare():
	txt = f"""
 {USAGE_WITH_KEY}

 [?] Information : {DESCRIPTIONS[9]}

 [++] Exemples :\n
 python3 main.py --format cloudflare --encode --key ff -f input.txt
 python3 main.py --format cloudflare --decode --key ff -f encoded.txt
 python3 main.py --format cloudlfare --decode --force -f encoded.txt # Will brute force.

 {FAIl}[!] Use a pair of chars belonging to [0123456789abcdef] as the key, ex : a9{RESET}
	"""
	return txt

def helpXor():
	txt = f"""
 {USAGE}

 [?] Information : {DESCRIPTIONS[10]}

 [++] Exemples :\n
 python3 main.py --format xor --encode -f input.txt
 python3 main.py --format xor --decode -f encoded.txt

 {FAIL}[!] Please provide us your 2 strings encoded in hexadecimal and each one on one line.{RESET}
	"""
	return txt

def helpDNA():
	return helpOldPhone(alg="DNA", desc=DESCRIPTIONS[5])

def helpBrainfuck():
	return helpOldPhone(alg='brainfuck', desc=DESCRIPTIONS[8])

def helpUrl():
	return helpOldPhone(alg='url', desc=DESCRIPTIONS[19])

def helpDeadfish():
	return helpOldPhone(alg='deadfish', desc=DESCRIPTIONS[17])

def helpPolybe():
	txt = f"""
 {USAGE_WITH_KEY}
 
 [?] Information : {DESCRIPTIONS[12]}

 [++] Exemples :\n
 python3 main.py --format polybe --encode --key ABCDEFGHIJKLMNOPQRSTUVWXY -f input.txt
 python3 main.py --format polybe --decode --key ABCDEFGHIJKLMNOPQRSTUVWXY -f encoded.txt

 {WARNING}[!] As you can see in the exemple, the key is represented by the 25 chars of your choice, that will be doing the polybe square\n
 What's the tool gonna do is placing each chars sequentially inside of the matrix, which looks like this : 
 	[
 		['A', 'B', 'C', 'D', 'E']
		['F', 'G', 'H', 'I', 'J']
		['K', 'L', 'M', 'N', 'O']
		['P', 'Q', 'R', 'S', 'T']
		['U', 'V', 'W', 'X', 'Y']
	]{RESET}
	"""
	return txt

def helpBacon():
	return helpOldPhone(alg='bacon', desc=DESCRIPTIONS[14])

def helpBaconBin():
	return helpOldPhone(alg='deadfish', desc=DESCRIPTIONS[15])

def helpRC4():
	txt = f"""
 {USAGE_WITH_KEY}
	
 [?] Information : {DESCRIPTIONS[11]}

 [++] Exemples :\n
 python3 main.py --format rc4 --encode --key secret_key;) -f input.txt
 python3 main.py --format rc4 --decode --key secret_key;) -f encoded.txt
 python3 main.py --format rc4 --decode --force --wordlist rockyou.txt -f encoded.txt # Will brute force the key

 {WARNING}[!] The data will always be output in hex format, and we expect you to put hex data, when you want to decode.{RESET}
	"""
	return txt

def helpVigenere():
	txt = f"""
 {USAGE_WITH_KEY}

 [?] Information : {DESCRIPTIONS[13]}

 [++] Exemples:\n
 python3 main.py --format vigenere --encode --key 0xK3y_ -f input.txt
 python3 main.py --format vigenere --decode --key 0xK3y_ -f encoded.txt
 python3 main.py --foramt vigenere --decode --force --wordlist rockyou.txt -f encoded.txt # Will brute force the key

 {WARNING}[!] As you can see above the key is 0xK3y_, but vigenere only use uppercase letter of the alphabet so 0xK3y_ will become XKY{RESET}
	"""
	return txt

def helpRailFence():
	txt = f"""
 {USAGE_WITH_KEY}

 [?] Information : {DESCRIPTIONS[16]}

 [++] Exemples:\n
 python3 main.py --format rail-fence --encode --key secret -f input.txt
 python3 main.py --format vigenere --decode --key secret -f encoded.txt
 python3 main.py --foramt vigenere --decode --force -f encoded.txt # Will brute force the with the keylen

 {WARNING}[!] For rail-fence we use the length of the key. So use terces as the key will give you the same output than secret{RESET}
	"""
	return txt

def helpBase():
	txt = f"""
 {USAGE}

 [??] Information :\n
 	[?] base45 : {DESCRIPTIONS[20]}\n
 	[?] base62 : {DESCRIPTIONS[21]}\n
 	[?] base32 : {DESCRIPTIONS[22]}\n
 	[?] base64 : {DESCRIPTIONS[23]}\n
 	[?] base16 : {DESCRIPTIONS[24]}\n
 	[?] base85 : {DESCRIPTIONS[25]}\n
 	[?] base58 : {DESCRIPTIONS[26]}\n
 
 [++] Exemples :
 	python3 main.py --format base64 --encode -f input.txt
 	python3 main.py --format base64 --decode -f encoded.txt
 	python3 main.py --format anybase --force -f encoded.txt 
	"""
	return txt

# List of all help functions that we use in the main.

HELP_FUNCTIONS_LIST = [
	helpCaesar, helpOldPhone, helpDecimal, helpHex, 
	helpBin, helpDNA, helpNetbios, helpWalross, 
	helpBrainfuck, helpCloudflare, helpXor,
	helpRC4,helpPolybe, helpVigenere, helpBacon, 
	helpBaconBin,helpRailFence, helpDeadfish, helpBraille,
	helpUrl, helpBase
]

# Constant needed for base converter.

BASE64 = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz./="
BASE32 = "234567ABCDEFGHIJKLMNOPQRSTUVWXYZ="
BASE62 = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
BASE45 = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ $%*+-./:"
BASE58_BITCOIN = "123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz"
BASE58_RIPPLE = "rpshnaf39wBUDNEGHJKLM4PQRST7VWXYZ2bcdeCg65jkm8oFqi1tuvAxyz"
BASE85 = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz!#$%&()*+\-;<=>?@^_`{|}~"
BASE91 = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!#$%&()*+,./:;=>?@[]^_`{|}~\""

BASE45_DICT = dict((elt, idx) for idx, elt in enumerate(BASE45))
BASE58_BITCOIN_DICT = dict((elt, idx) for idx, elt in enumerate(BASE58_BITCOIN))
BASE58_RIPPLE_DICT = dict((elt, idx) for idx, elt in enumerate(BASE58_RIPPLE))
BASE62_DICT = dict((elt, idx) for idx, elt in enumerate(BASE62))

# BASE91_DICT = dict((elt, idx) for idx, elt in enumerate(BASE91)) 





# Use in some classes

def getKeyFromValue(dico, value):
	return ''.join([k for k, v in dico.items() if v == value])

def checkEncodingInList(encoding):
	return encoding in FORMAT_LIST

# Print table error code output

def tableCode(group_keys, group_values):

	TABLE = []
	row = []
	keys = []
	values = []
		
	last = 0

	for i in range(0, len(group_keys)+TAB_SIZE, TAB_SIZE):
			
		keys.append(group_keys[last:i])
			
		values.append(group_values[last:i])
			
		last = i
		
	del keys[0], values[0]
		
	for i in range(len(keys)):
		for j in range(TAB_SIZE):
			try:
				row.append(keys[i][j])
				row.append(values[i][j])
			except:
				pass
		TABLE.append(row)
		row = []

	return tabulate(TABLE, tablefmt="fancy_grid")

