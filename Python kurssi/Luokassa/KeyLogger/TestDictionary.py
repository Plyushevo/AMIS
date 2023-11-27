# Define the expanded dictionary with Unicode sequences as keys and key combinations as values
unicodeDictionary = {
    "\x08": "Backspace",       # Backspace character
    "\x09": "Tab",             # Tab character
    "\x0A": "Line Feed",       # Line Feed character (newline)
    "\x0D": "Carriage Return", # Carriage Return character
    "\x1B": "Escape",          # Escape character
    "\x20": "Space",           # Space character
    "\x21": "!",               # Exclamation Mark character
    "\x22": '"',               # Double Quote character
    "\x23": "#",               # Hash character
    "\x24": "$",               # Dollar character
    "\x25": "%",               # Percent character
    "\x26": "&",               # Ampersand character
    "\x27": "'",               # Single Quote character
    "\x28": "(",               # Left Parenthesis character
    "\x29": ")",               # Right Parenthesis character
    "\x2A": "*",               # Asterisk character
    "\x2B": "+",               # Plus character
    "\x2C": ",",               # Comma character
    "\x2D": "-",               # Minus character
    "\x2E": ".",               # Period character
    "\x2F": "/",               # Slash character
    "\x3A": ":",               # Colon character
    "\x3B": ";",               # Semicolon character
    "\x3C": "<",               # Less Than character
    "\x3D": "=",               # Equal character
    "\x3E": ">",               # Greater Than character
    "\x3F": "?",               # Question Mark character
    "\x40": "@",               # At character
    "\x5B": "[",               # Left Square Bracket character
    "\x5C": "\\",              # Backslash character
    "\x5D": "]",               # Right Square Bracket character
    "\x5E": "^",               # Caret character
    "\x5F": "_",               # Underscore character
    "\x60": "`",               # Grave Accent character
    "\x7B": "{",               # Left Curly Brace character
    "\x7C": "|",               # Vertical Bar character
    "\x7D": "}",               # Right Curly Brace character
    "\x7E": "~",               # Tilde character
    "\x7F": "Delete",          # Delete character
    "\x1A": "Ctrl + Z",        # Ctrl + Z key combination
    "\x03": "Ctrl + C",        # Ctrl + C key combination
    "\x04": "Ctrl + D"         # Ctrl + D key combination
}

# Function to get key combination for a given Unicode sequence
def getKeyCombination(unicodeSequence):

    if unicodeSequence in unicodeDictionary:
        return unicodeDictionary[unicodeSequence]
    else:
        return "Key combination not found"

        """
    Function to retrieve the key combination for a given Unicode sequence.
    
    Args:
        unicodeSequence (str): Unicode sequence to be looked up in the dictionary.
    
    Returns:
        str: Key combination corresponding to the given Unicode sequence.
            Returns "Key combination not found" if the sequence is not in the dictionary.
    """
# Example usage with input
unicodeInput = input("Enter Unicode sequence: ")    # Input "\x08" for Backspace
unicodeSequence = bytes(unicodeInput, "utf-8").decode("unicode_escape")     # Convert the input string into bytes and decode it to interpret escape sequences properly
keyCombination = getKeyCombination(unicodeSequence)                         # Get the key combination for the input Unicode sequence using the getKeyCombination function
print(f"Key combination for Unicode sequence {unicodeSequence} is: {keyCombination}")