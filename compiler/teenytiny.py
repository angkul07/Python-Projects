from lex import *
from parse import *
from emit import *
import sys

def main():
    print("Teeny Tiny Compiler")

    if len(sys.argv) != 2:
        sys.exit("Error: Compiler needs source file as argument.")
    with open(sys.argv[1], 'r') as inputFile:
        source = inputFile.read()

    #Initialize the lexer and parser and emitter.
    lexer = Lexer(source)
    emitter = Emitter("out.c")
    parser = Parser(lexer, emitter)

    parser.program() #start the parser
    emitter.writeFile() # Write the output to file.
    print("Compiling completed.")

main()