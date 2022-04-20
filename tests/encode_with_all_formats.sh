#!/bin/bash
# file: encode_with_all_formats.sh

myArray=(
	"base45" "base62" "base32" "base64" "base16" "base85" "base58" 
	"caesar_ascii" "old-phone" "dec" "hex" "bin" "DNA" "netbios" 
	"walross" "brainfuck" "cloudflare" "xor" "rc4" 
	"polybe" "vigenere" "bacon" "bacon-bin" 
	"rail-fence" "deadfish" "braille" "url"
	)

for form in ${myArray[@]}; do
	python3 ../guren.py --format $form --encode --offset 45 --key FalseKey -f ../input.txt
done
