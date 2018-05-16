from typing import Tuple

class TrieNode(object):

	# the Trie implementation. Initializing the nodes

	def __init__(self, char: str):
		self.char = char
		self.children = []
		self.word_finished = False
		self.counter = 1

def add(root, word: str):

	# adding a word in Trie

	node = root
	for char in word:
		found_in_child = False

		#search for the character in the children of the present node

		for child in node.children:
			# We found it, increase the counter by 1 to keep track the another word as well
			if child.char == char:
				child.counter += 1

		
			# Point the node to the child that contains this char
				node = child

				found_in_child = True
				break

		# We didn't find it, so add the new child
		if not found_in_child:
			new_node = TrieNode(char)
			node.children.append(new_node)

			# And then point node to the new child
			node = new_node

	#Everything finished, mark it as the end of a word.
	node.word_finished = True


def find_prefix(root, prefix: str) -> Tuple[bool, int]:

	# Check and return
	# 1. If the prefix exists in any of the words we have added
	# 2. If Yes, then how many words actually have the prefix

	node = root
	# If the root node has no children, then return False.
	# this means we are searching an empty tree.

	if not root.children:
		return False, 0


	for char in prefix:
		char_not_found = True

	# Search through all the children of the present node

		for child in node.children:
			if child.char == char:

				# We found the char existing in the child.
				char_not_found = False

				# Assign node as the child containing the char and break

				node = child

				break

		# Return False when we didn't find a char
		if char_not_found:
			return False, 0

	return True, node.counter


if __name__ == "__main__":
	root = TrieNode('*')
	add(root, "hackathon")
	add(root, "hack")

	print(find_prefix(root, 'hac'))
	print(find_prefix(root, 'hack'))
	print(find_prefix(root, 'hackathon'))
	print(find_prefix(root, 'ha'))
	print(find_prefix(root, 'hammer'))


