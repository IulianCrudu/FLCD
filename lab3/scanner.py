from typing import List, Tuple
from symbol_table import SymbolTable
import re


class Scanner:
    def __init__(self):
        self.tokens: List[str] = self.read_tokens()
        self.composed_tokens = {
            ":": ["="],
            "=": ["="],
            "<": ["=", ">"],
            ">": ["="],
            "&": ["&"],
            "|": ["|"],
            "\\": ["t", "n"]
        }
        self.symbol_table = SymbolTable(41)
        self.pif: List[Tuple[str, int]] = []

    def read_tokens(self) -> List[str]:
        tokens: List[str] = []
        file = open("tokens.in", "r")

        for line in file:
            tokens.append(line.strip())

        return tokens

    def is_constant_or_identifier(self, character: str):
        return bool(self.is_constant(character)) or bool(self.is_identifier(character))

    def is_identifier(self, token):
        return re.search("^[a-zA-Z]+[a-zA-Z0-9]*$", token)

    def is_character(self, token):
        return re.search("^'[a-zA-Z0-9]'$", token)

    def is_string(self, token):
        return re.search("^\"[a-zA-Z0-9 :]*\"$", token)

    def is_integer(self, token):
        return re.search("^([+-]?[1-9][0-9]*)|0$", token)

    def is_boolean(self, token):
        return re.search("[01]", token)

    def is_constant(self, token):
        return self.is_character(token) or self.is_string(token) or self.is_integer(token) or self.is_boolean(token)

    def scan_and_save(self, in_file_name: str, out_file_name: str):
        self.scan(in_file_name)
        self.save_to_files(out_file_name)

    def scan(self, file_name: str):
        file = open(file_name, "r")
        line_count = 0

        for line in file:
            line_count += 1
            tokens = self.tokenize_line(line)
            print("line", self.tokenize_line(line))

            for token in tokens:
                if token in self.tokens:
                    self.pif.append((token, -1))
                elif self.is_constant_or_identifier(token):
                    position = self.symbol_table.add_element(token)
                    self.pif.append((token, position))
                else:
                    raise RuntimeError(f"Lexical error on line {line_count}. Token not defined: {token}")

    def handle_string_tokens(self, tokens: List[str], separator) -> List[str]:
        new_tokens = []
        current_string_token = ""

        for token in tokens:
            if token == separator:
                if not current_string_token:
                    current_string_token = token
                else:
                    current_string_token += token
                    new_tokens.append(current_string_token)
                    current_string_token = ""
            else:
                if not current_string_token:
                    new_tokens.append(token)
                else:
                    current_string_token += token

        return new_tokens

    def tokenize_line(self, line: str) -> List[str]:
        i = 0
        tokens = []

        while i < len(line):
            character = line[i]

            if self.is_constant_or_identifier(character):
                if character in ["-", "+"]:
                    if i < len(line) - 1 and line[i+1] != " ":
                        tokens.append(character)
                    else:
                        tokens.append(" ")
                        tokens.append(character)
                        tokens.append(" ")
                else:
                    tokens.append(character)
            elif character in self.composed_tokens:
                if i < len(line) - 1 and line[i + 1] in self.composed_tokens[character]:
                    tokens.append(" ")
                    tokens.append(character)
                    tokens.append(line[i + 1])
                    tokens.append(" ")
                    i += 1
                else:
                    tokens.append(" ")
                    tokens.append(character)
                    tokens.append(" ")
            else:
                tokens.append(" ")
                tokens.append(character)
                tokens.append(" ")

            i += 1

        tokens = "".join(tokens).split()
        tokens = self.handle_string_tokens(tokens, "\"")
        tokens = self.handle_string_tokens(tokens, "\'")
        return tokens

    def save_to_files(self, file_name: str):
        pif_file = open(f"PIF_{file_name}", "w")
        pif_file.write("TOKEN | POSITION \n")

        for token, code in self.pif:
            pif_file.write(f"{token} | {code}\n")
        pif_file.close()

        st_file = open(f"ST_{file_name}", "w")
        st_file.write(str(self.symbol_table))
