
# Import utilities for the tool...

import sys
import argparse
from terminaltables import SingleTable
import urllib.parse

# Importing modules of decoding/encoding

from modules import old_phone
from modules import caesar
from modules import netbios
from modules import xor
from modules import basics_encode
from modules import analyse
from modules import DNA
from modules import walross
from modules import rc4
from modules import cloudflare
from modules import vigenere
from modules import rail_fence
from modules import bacon
from modules import braille
from modules import base_converter
from modules import deadfish
from modules import brainfuck
from modules import polybe
from modules import url

# Import additional functions...

from lib.exceptions import *
from lib.components import *
from lib.fileHandler import FileHandler


def parseArgs():

	parser = argparse.ArgumentParser(add_help=True, description='This tool allows you to decode/encode data, using different types of methods.')

	parser.add_argument("--format", dest="format", required=False, help="Specify the method you want to use to encode/decode.")
	
	parser.add_argument("--analyse", dest="analyse", action="store_true", required=False, help="Analyse the data, and return, which kind of format does it comes.")

	parser.add_argument("--attack", dest="attack", action="store_true", required=False, help="Use it to attack the encoded data, with all the methods, that the tool knows")

	parser.add_argument("-e", "--encode", dest="encode", action="store_true", required=False, help="Describe to the tool what to encode.")
	
	parser.add_argument("-d", "--decode", dest="decode", action="store_true", required=False, help="Describe to the tool what to decode.")

	parser.add_argument("-bf", "--force", dest="force", action="store_true", required=False, help="Claim to the tool to brute force a specific encoded format.")

	parser.add_argument(
		"-o","--offset", dest="offset", 
		required="caesar_ascii" in sys.argv and "--encode" in sys.argv or "netbios" in sys.argv and "--encode" in sys.argv,  
		type=int, help="Offset to encode the data."
		)

	parser.add_argument(
		"-k", "--key", dest="key",
		required=("--encode" in sys.argv or "--decode" in sys.argv or "-d" in sys.argv or "-e" in sys.argv) 
		and "rc4" in sys.argv or "vigenere" in sys.argv or "rail-fence" in sys.argv or "cloudflare" in sys.argv, 
		help="This is the key to cipher/decipher the data, required with certain algorithm."
		)
	
	parser.add_argument(
		"-f", "--filename", dest="filename", 
		required="--encode" in sys.argv or "-e" in sys.argv or "--decode" in sys.argv or "-d" in sys.argv, 
		help="Filename of the data."
		)
	
	parser.add_argument("--show", action="store_true", dest="show", required=False, help="Print out all the available formats.")

	parser.add_argument("-t", "--tell", dest="tell", action="store_true", required=False, help="Print out the help menu for each different types of format")
	
	args = parser.parse_args()
	
	return args

def handleGuren(filename, form=None, toEncode=False, toDecode=False, toTell=False, toAttack=None,toBruteForce=False, toAnalyse=False,offset=0, key=""):

	if toAnalyse:
		print(f"{WARNING} [*] We are analysing the data, you provide us...\n ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~{RESET}")
		analyzer = analyse.Analyzer(filename)
		print(analyzer)
		return


	if form != None:
		if form not in BASE_LIST:
			index = FORMAT_LIST.index(form)
		else:
			index = -1 # Case the user choose a base format, bcs all the bases formats are joined into the same class [ BaseConverter ].
	
	# If someone wanna see some help menu for each format...
	
	if toTell and index: # Case user enter wrong input parameters.
		helpFunction = HELP_FUNCTIONS_LIST[index]
		print(helpFunction())
		return

	OBJECT_LIST = [
		caesar.Caesar(filename, offset),old_phone.OldPhone(filename), basics_encode.Dec(filename), 
		basics_encode.Hex(filename), basics_encode.Bin(filename), DNA.DNA(filename),
		netbios.Netbios(filename, offset), walross.Walross(filename), brainfuck.BrainFuckInterpreter(filename),
		cloudflare.Cloudflare(filename, key=key), xor.XOR(filename), rc4.RC4(filename, key), polybe.Polybe(filename, key), 
		vigenere.Vigenere(filename, key), bacon.Bacon(filename), bacon.BaconBin(filename), 
		rail_fence.RailFence(filename, key), deadfish.DeadFishInterpreter(filename), 
		braille.Braille(filename), url.URL(filename), base_converter.BaseConverter(filename, ''.join([form if form == base else "" for base in BASE_LIST]))
	]
	if not toAttack:
		objEncoder = OBJECT_LIST[index]

	if toAttack:
		print(f"{WARNING} [*] We are attacking this encoded data, this might take some time...{RESET}")
		
		with open(DECODED_FILE, "a") as file_out:
			for idx, obj in enumerate(OBJECT_LIST):
				try:
					file_out.write("\nUsing : %s\n\n%s\n\n" % (FORMAT_LIST[idx], obj.decode()))
				except:
					file_out.write("\nUsing : %s => Not FOUND...\n" % (FORMAT_LIST[idx]))
					pass
			for base in BASE_LIST:
				try:
					file_out.write("\nUsing : %s\n\n%s\n\n" % (base, OBJECT_LIST[-1].decode()))
				except:
					file_out.write("\nUsing : %s => Not FOUND...\n" % (base))
					pass
		print(f"{OKMAGENTA} [+++] Result of the attack {DECODED_FILE}{RESET}")
		return

	elif toBruteForce:

		print(f"{WARNING} [*] We are trying to brute force, the {form} format{RESET}\n ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
		
		with open(DECODED_FILE, "w") as file_out:
			objEncoder.bruteForce(file_out)
		print(f"{OKGREEN} [++] Result of brute forcing are there {DECODED_FILE}{RESET}")
		return

	elif toEncode:
		
		message = MESSAGE_LIST_ENCODING[index]
		print(message)
		
		with open(ENCODED_FILE, "w") as file:
			file.write(objEncoder.encode())
		print(f"{OKGREEN} [+] Check result in {ENCODED_FILE}{RESET}")
		return

	elif toDecode:

		message = MESSAGE_LIST_DECODING[index]
		print(message)
		
		with open(DECODED_FILE, "w") as file:
			file.write(objEncoder.decode())
		print(f"{OKGREEN} [+] Check result in {DECODED_FILE}{RESET}")
		return

def main():

	print(home())

	args = parseArgs()

	if args.show:
		print(show())
		return 

	if (not checkEncodingInList(args.format) and not args.attack and not args.analyse):
		print(f"{FAIL} [!] The specified encoding format {args.format} is not in our list, please provide a valid format...{RESET}")
		return 
	
	if (args.filename is not None and not FileHandler(args.filename).fileExist()):
		print(f"{FAIL} [!] The specified file {args.filename}, doesn't exist !{RESET}")
		return
	
	else:
		try:
			handleGuren(
				args.filename, form=args.format, toEncode=args.encode, 
				toDecode=args.decode, toTell=args.tell, toAttack=args.attack, 
				toBruteForce=args.force, toAnalyse=args.analyse,
				offset=args.offset,key=args.key
				)
			return

		except (EncodingError, DecodingError) as err:
			details = err.args[0]
			print(f"{WARNING}{details['message']} {RESET}")
			if "keyboard" in details:
				print(f"{OKGREEN}{details['keyboard']} {RESET}")
			return


if __name__ == "__main__":
	main()