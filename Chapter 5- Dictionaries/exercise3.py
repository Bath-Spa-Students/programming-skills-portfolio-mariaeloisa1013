print("\n\tGlossary")
glossary = {"integer": "a whole number ",
    "float": "numbers with a decimal",
    "string": "text data",
    "variables": "a value",
    "statement": "a line of code",
    "concatenaton": "joining 2 strings with arithmetic operators",
    "rstrip": "right strip",
    "lstrip": "left strip",
    "index": "numbered position",
    "mutable": "changeable"}
for word, defintion in glossary.items() :
    print("\n" + word.title() + ":\n\t" + glossary[word])