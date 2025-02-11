import re
from test_bpt import BuildParseTree
from algebricTokeniser import AlgebricTokeniser
from tokeniser import Tokeniser

class AlgebricEquation(BuildParseTree):
    def __init__(self):
        super().__init__() 
        # --- Helper methods to work with our polynomial representation ---

    def make_poly(self, token):
        """
        Given a token (either a number or a variable expression) return
        its polynomial representation [dict, constant].
        
        A numeric token (or one that can be parsed as a float) is treated as a constant.
        A token that represents a variable (for example: "2p", "p", or "3p^2")
        is parsed into its coefficient and exponent.
        """
        # If the token is already a number (float or int) then return constant-only poly.
        if isinstance(token, (int, float)):
            return [{}, float(token)]
        if isinstance(token, str):
            # Try to interpret token as a number first.
            try:
                value = float(token)
                return [{}, value]
            except ValueError:
                # Token is not a pure number; try to parse a variable term.
                # This regex will match an optional signed number, followed by a letter,
                # optionally followed by '^' and an exponent.
                pattern = r'^([+-]?(\d+(\.\d*)?|\.\d+)?)([a-zA-Z])(?:\^(\d+))?$'
                match = re.match(pattern, token)
                if match:
                    coef_str = match.group(1)
                    # If no coefficient is given or only a sign is provided,
                    # assume coefficient is 1 (or -1).
                    if coef_str in ("", "+", "-"):
                        coef = 1.0 if coef_str != "-" else -1.0
                    else:
                        coef = float(coef_str)
                    # If no exponent is provided, assume power 1.
                    power = int(match.group(5)) if match.group(5) else 1
                    # Return a representation where the variable term is in the dictionary
                    # and the constant part is zero.
                    return [{power: coef}, 0]
                else:
                    raise ValueError(f"Unable to parse token: {token}")
        raise ValueError("Unsupported token type in make_poly.")

    def poly_add(self, p1, p2):
        new_dict = {}
        # Add variable parts
        for power, coeff in p1[0].items():
            new_dict[power] = coeff
        for power, coeff in p2[0].items():
            new_dict[power] = new_dict.get(power, 0) + coeff
        # Add constant parts
        new_const = p1[1] + p2[1]
        return [new_dict, new_const]

    def poly_sub(self, p1, p2):
        new_dict = {}
        for power, coeff in p1[0].items():
            new_dict[power] = coeff
        for power, coeff in p2[0].items():
            new_dict[power] = new_dict.get(power, 0) - coeff
        new_const = p1[1] - p2[1]
        return [new_dict, new_const]

    def poly_mul(self, p1, p2):
        new_dict = {}
        # Multiply variable parts (dictionary * dictionary)
        for pwr1, coef1 in p1[0].items():
            for pwr2, coef2 in p2[0].items():
                new_power = pwr1 + pwr2
                new_dict[new_power] = new_dict.get(new_power, 0) + coef1 * coef2
        # Multiply variable part of p1 with constant part of p2
        for pwr, coef in p1[0].items():
            new_dict[pwr] = new_dict.get(pwr, 0) + coef * p2[1]
        # Multiply variable part of p2 with constant part of p1
        for pwr, coef in p2[0].items():
            new_dict[pwr] = new_dict.get(pwr, 0) + coef * p1[1]
        new_const = p1[1] * p2[1]
        return [new_dict, new_const]

    def poly_div(self, p1, p2):
        """
        Divide p1 by p2.
        Here we support division only when p2 is a constant (i.e. its dictionary is empty).
        """
        if p2[0]:
            raise ValueError("Division by a non-constant polynomial is not supported")
        if p2[1] == 0:
            raise ZeroDivisionError("Division by zero")
        new_dict = {p: coef / p2[1] for p, coef in p1[0].items()}
        new_const = p1[1] / p2[1]
        return [new_dict, new_const]
    
    def poly_inv(self, p):
        if not p[0]:
            if p[1] == 0:
                raise ZeroDivisionError("Zero polynomial not invertible")
            return [{}, 1 / p[1]]

        if len(p[0]) == 1 and p[1] == 0:
            for q, coef in p[0].items():
                if coef == 0:
                    raise ZeroDivisionError("Division by zero")
                return [{-q: 1 / coef}, 0]
        raise ValueError("Polynomial not invertible")

    def poly_pow(self, p, n):
        if n < 0:
            inv = self.poly_inv(p)
            return self.poly_pow(inv, -n)
        else:
            result = [{}, 1]
            for _ in range(n):
                result = self.poly_mul(result, p)
            return result
            

    # --- Modified evaluate method ---
    def evaluate(self, node=None):

        if node is None:
            node = self.tree

        leftTree = node.getLeftTree()
        rightTree = node.getRightTree()
        op = node.getKey()

        # If leaf node then convert the token into a polynomial
        if leftTree is None and rightTree is None:
            return self.make_poly(op)

        # Recursively evaluate left and right subtrees
        left_poly = self.evaluate(leftTree)
        right_poly = self.evaluate(rightTree)

        if op == '+':
            return self.poly_add(left_poly, right_poly)
        elif op == '-':
            return self.poly_sub(left_poly, right_poly)
        elif op == '*':
            return self.poly_mul(left_poly, right_poly)
        elif op == '/':
            return self.poly_div(left_poly, right_poly)
        elif op == '**':
            # For exponentiation, the exponent must be a constant.
            if right_poly[0]:
                raise ValueError("Exponent must be a constant")
            exponent = right_poly[1]
            if not float(exponent).is_integer():
                raise ValueError("Exponent must be an integer")
            return self.poly_pow(left_poly, int(exponent))
        else:
            raise ValueError(f"Invalid operator: {op}")
        
    def inputExpression(self):
        self.exp = input("Please enter the expression you want to evaluate:\n")
        self.tokens = AlgebricTokeniser(self.exp).tokenise()
    