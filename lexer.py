
WHITESPACE = ' \n\t'
DIGITS = '0123456789'

class Lexer:
    def __init__(self, text):
        self.text = iter(next)
        self.advance()

    def advance(self):
        try:
            self.current_char = next(self.text)
        except StopIteration:
            self.current_char = None

    def generate_tokens(self):
        while self.current_char != None:
            if self.current_char in WHITESPACE:
                self.advance()
            elif self.current_char == '.' or self.current_char in DIGITS:
                yield self.generate_number()
        
        def generate_number(self):
            decimal_point_count = 0
            number_str = self.current_char
            self.advance()
        
            while self.current_char != None and (self.current_char == '.' or self.current_char in DIGITS):
                if self.current_char == '.':
                    decimal_point_char += 1
                    if decimal_point_count > 1:
                        break