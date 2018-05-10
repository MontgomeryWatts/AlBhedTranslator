e_to_AB = {'a': 'y', 'b': 'p', 'c': 'l', 'd': 't', 'e': 'a', 'f': 'v', 'g': 'k', 'h': 'r', 'i': 'e', 'j': 'z',
		 'k': 'g', 'l': 'm', 'm': 's', 'n': 'h', 'o': 'u', 'p': 'b', 'q': 'x', 'r': 'n', 's': 'c', 't': 'd',
		 'u': 'i', 'v': 'j', 'w': 'f', 'x': 'q', 'y': 'o', 'z': 'w'}

AB_to_E = dict()

for key in e_to_AB:
	AB_to_E[e_to_AB[key]] = key

def translate(string: str, lang_map: dict) -> str:
	output = ""
	do_not_translate = False
	for char in string:
		if do_not_translate:
			if char == '*':
				do_not_translate = False
		elif char.lower() in lang_map.keys():
			if char.isupper():
				char = lang_map[char.lower()].upper()
			else:
				char = lang_map[char]
		else:
			if char == '*':
				do_not_translate = True
		output += char
	return output

def prompt() -> None:
	print("1. Translate a string from English to Al Bhed.")
	print("2. Translate a string from Al Bhed to English.")
	print("3. Quit.")

def main() -> None:
	user_input = ""
	while user_input != '3':
		prompt()
		user_input = input()
		if user_input == '1':
			print("Enter a string to translate. Enclose words to preserve with asterisks.")
			print(translate(input(), e_to_AB))
		elif user_input == '2':
			print("Enter a string to translate. Enclose words to preserve with asterisks.")
			print(translate(input(), AB_to_E))

if __name__ == '__main__':
	main()