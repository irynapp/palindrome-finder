
from optparse import OptionParser

class PalindromeFinder(object):
	"""
	Determine and display palindromes based on
	the default or given list of words.
	"""
	def __init__(self, words):
		"""Get list of words to process."""
		if not words:
			words = ['Gimli', 'Fili', 'Ilif', 'Ilmig', 'Mark']

		self.words = [w.lower() for w in words]
		self.palindromes = []

	def get_palindrome(self):
		"""
		Identify if any given word within the list
		can form a palindrome with.
		"""
		for word in self.words:
			reversed_word = word[::-1]
			if reversed_word in self.words:
				self.palindromes.append([word, reversed_word])

	def display_palindromes(self):
		"""Print palindromes."""
		for word, reversed_word in self.palindromes:
			print word + reversed_word

	def run(self):
		"""Helper method to find and print palindromes."""
		self.get_palindrome()
		self.display_palindromes()


if __name__ == '__main__':
	helper_string = 'Usage: %prog [options]'
	parser = OptionParser(usage=helper_string)
	parser.add_option(
		'-w', '--words', action='store', dest='words',
		type='string', help='Comma separated words without spaces'
	)

	(options, args) = parser.parse_args()

	words = []
	if options.words:
		words = options.words.split(',')

	obj = PalindromeFinder(words)
	obj.run()
