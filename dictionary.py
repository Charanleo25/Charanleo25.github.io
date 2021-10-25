class vowels:


	dictionary = {
		"vowels": "aeiouAEIOU"
		}

def countVowels():
	count = 0
	countCons = 0
	string = input("Enter the string:")
	for i in string:
		if (not(i.isdigit())):
			if (i in dictionary["vowels"]):
				count += 1
			else:
				countCons += 1
	return count,countCons

def main():
	vowels, consonants = countVowels()
	print("Number of vowels:",vowels)
	print("Number of consonants:",consonants)

main()
