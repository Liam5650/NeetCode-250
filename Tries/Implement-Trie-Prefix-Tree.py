# Helper class to store data for each character
class Node:
    def __init__(self, val):
        self.val = val  # The character
        self.children = {}  # The set of nodes containing characters that follow this one

class PrefixTree:

    # Create node to mark the head
    def __init__(self):
        self.head = Node(0)

    def insert(self, word: str) -> None:

        # Go through each char in the word, creating a new node for each character
        # that doesn't already exist (linked list)
        curr = self.head
        for ch in word:
            if ch in curr.children:
                curr = curr.children[ch]
            else:
                new = Node(ch)
                curr.children[ch] = new
                curr = new
        
        # Special marker to indicate this was the end of the word
        curr.children["end"] = True

    def search(self, word: str) -> bool:

        # Go through the nodes and make sure we find a valid path
        curr = self.head
        for ch in word:
            if not ch in curr.children: return False
            curr = curr.children[ch]

        # Check if the final node was marked as the end of a word
        return "end" in curr.children  
        
    
    def startsWith(self, prefix: str) -> bool:

        # Go through the nodes and make sure we find a valid path
        curr = self.head
        for ch in prefix:
            if not ch in curr.children: return False
            curr = curr.children[ch]

        # We don't care if end of word, so just return true if valid
        # until the end point
        return True   