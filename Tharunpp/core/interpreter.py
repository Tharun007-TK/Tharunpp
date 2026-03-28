"""Tharun++ Interpreter using Lark parser"""

from lark import Lark, Tree, Token
from pathlib import Path
import sys


# Custom Exceptions
class TharunppError(Exception):
    """Base exception for Tharun++"""
    pass


class TharunppSyntaxError(TharunppError):
    """Syntax error in Tharun++ code"""
    pass


class TharunppNameError(TharunppError):
    """Variable not defined"""
    pass


class TharunppTypeError(TharunppError):
    """Type mismatch error"""
    def __init__(self, expected, got):
        super().__init__(f"Expected {expected}, got {got}")


class TharunppZeroDivisionError(TharunppError):
    """Division by zero"""
    def __init__(self):
        super().__init__("Cannot divide by zero")


class TharunppReturnValue(Exception):
    """Used to return values from functions"""
    def __init__(self, value):
        self.value = value


# Environment for variable and function storage
class Environment:
    def __init__(self, parent=None):
        self.vars = {}
        self.parent = parent
    
    def set(self, name, value):
        self.vars[name] = value
    
    def get(self, name):
        if name in self.vars:
            return self.vars[name]
        elif self.parent:
            return self.parent.get(name)
        else:
            raise TharunppNameError(f"Variable '{name}' is not defined")
    
    def update(self, name, value):
        if name in self.vars:
            self.vars[name] = value
        elif self.parent:
            self.parent.update(name, value)
        else:
            raise TharunppNameError(f"Variable '{name}' is not defined")


class Interpreter:
    def __init__(self):
        self.global_env = Environment()
        self.parser = None
    
    def _get_parser(self):
        if self.parser is None:
            grammar_path = Path(__file__).parent / "tharunpp.lark"
            with open(grammar_path) as f:
                grammar = f.read()
            self.parser = Lark(grammar, parser='earley', ambiguity='resolve')
        return self.parser
    
    def run(self, source):
        from lark.exceptions import UnexpectedInput, UnexpectedCharacters, UnexpectedToken
        try:
            tree = self._get_parser().parse(source)
        except (UnexpectedInput, UnexpectedCharacters, UnexpectedToken) as e:
            raise TharunppSyntaxError(str(e))
        self._exec_program(tree, self.global_env)
    
    def _exec_program(self, tree, env):
        # Handle the start -> program wrapper
        if tree.data == "start":
            tree = tree.children[0]  # Get the actual program node
        
        # Now iterate through the program's statements
        for child in tree.children:
            if isinstance(child, Tree):
                self._exec_statement(child, env)
    
    def _exec_statement(self, tree, env):
        d = tree.data
        
        # Handle statement wrapper - unwrap and process the actual statement
        if d == "statement":
            if tree.children and isinstance(tree.children[0], Tree):
                return self._exec_statement(tree.children[0], env)
            return
        
        if d == "var_declare":
            self._exec_var_declare(tree, env)
        elif d == "assign_stmt":
            self._exec_assign(tree, env)
        elif d == "print_stmt":
            self._exec_print(tree, env)
        elif d == "debug_stmt":
            self._exec_debug(tree, env)
        elif d == "warn_stmt":
            self._exec_warn(tree, env)
        elif d == "if_stmt":
            self._exec_if(tree, env)
        elif d == "while_stmt":
            self._exec_while(tree, env)
        elif d == "for_stmt":
            self._exec_for(tree, env)
        elif d == "func_def":
            self._exec_func_def(tree, env)
        elif d == "return_stmt":
            self._exec_return(tree, env)
        elif d == "func_call_stmt":
            self._eval(tree.children[0], env)
        elif d == "try_stmt":
            self._exec_try(tree, env)
        elif d == "throw_stmt":
            self._exec_throw(tree, env)
        elif d == "assert_stmt":
            self._exec_assert(tree, env)
        elif d == "pass_stmt":
            pass
        elif d == "import_stmt":
            self._exec_import(tree, env)
        elif d == "list_declare":
            self._exec_list_declare(tree, env)
        elif d == "list_append":
            self._exec_list_append(tree, env)
        elif d == "list_get":
            self._exec_list_get(tree, env)
    
    def _exec_var_declare(self, tree, env):
        name = str(tree.children[1].value)  # Get the actual NAME token value
        value = self._eval(tree.children[3], env)  # Skip ASSIGN, get the expr
        env.set(name, value)
    
    def _exec_assign(self, tree, env):
        name = str(tree.children[0].value)  # Get the actual NAME token value
        value = self._eval(tree.children[2], env)  # Skip ASSIGN, get the expr
        env.update(name, value)
    
    def _exec_print(self, tree, env):
        values = []
        for child in tree.children:
            if isinstance(child, Token) and child.type == 'PRINT':
                continue  # Skip the PRINT keyword itself
            values.append(self._eval(child, env))
        print(*values)
    
    def _exec_debug(self, tree, env):
        values = []
        for child in tree.children:
            if isinstance(child, Token) and child.type == 'DEBUG':
                continue  # Skip the DEBUG keyword itself
            values.append(self._eval(child, env))
        print("[KALAAI]", *values)
    
    def _exec_warn(self, tree, env):
        values = []
        for child in tree.children:
            if isinstance(child, Token) and child.type == 'WARN':
                continue  # Skip the WARN keyword itself
            values.append(self._eval(child, env))
        print("[IRUNGH BHAII]", *values)
    
    def _exec_if(self, tree, env):
        ch = tree.children

        def _collect_block(start_idx):
            block = []
            i = start_idx
            while i < len(ch):
                c = ch[i]
                if isinstance(c, Token) and c.type in ("ELSE_IF", "ELSE_COND", "BLOCK_END"):
                    break
                if isinstance(c, Tree):
                    block.append(c)
                i += 1
            return block, i

        # IF_COND expr COLON statement*
        cond = self._eval(ch[1], env)
        i = 3  # skip IF_COND, expr, COLON
        block, i = _collect_block(i)
        if cond:
            for stmt in block:
                self._exec_statement(stmt, env)
            return

        # (ELSE_IF expr COLON statement*)* (ELSE_COND COLON statement*)?
        while i < len(ch):
            c = ch[i]
            if isinstance(c, Token) and c.type == "ELSE_IF":
                cond = self._eval(ch[i + 1], env)
                i = i + 3  # skip ELSE_IF, expr, COLON
                block, i = _collect_block(i)
                if cond:
                    for stmt in block:
                        self._exec_statement(stmt, env)
                    return
                continue

            if isinstance(c, Token) and c.type == "ELSE_COND":
                i = i + 2  # skip ELSE_COND, COLON
                block, i = _collect_block(i)
                for stmt in block:
                    self._exec_statement(stmt, env)
                return

            i += 1
    
    def _exec_while(self, tree, env):
        # Tree structure: [WHILE, condition, COLON, statements..., BLOCK_END]
        cond_expr = tree.children[1]  # Skip WHILE token, get condition
        
        # Find where COLON is and start body after it
        body_start = 3  # Skip WHILE, condition, COLON
        
        while self._eval(cond_expr, env):
            for i in range(body_start, len(tree.children)):
                child = tree.children[i]
                if isinstance(child, Token) and child.type == "BLOCK_END":
                    break
                if isinstance(child, Tree):
                    self._exec_statement(child, env)
    
    def _exec_for(self, tree, env):
        # Tree: [FOR_START, NAME, FOR_RANGE_START, start_expr, FOR_RANGE_END, end_expr, COLON, statements..., BLOCK_END]
        var_name = str(tree.children[1].value)
        start = int(self._eval(tree.children[3], env))
        end = int(self._eval(tree.children[5], env))
        
        for i in range(start, end + 1):
            env.set(var_name, i)
            for child in tree.children[7:]:
                if isinstance(child, Token) and child.type == "BLOCK_END":
                    break
                if isinstance(child, Tree):
                    self._exec_statement(child, env)
    
    def _exec_func_def(self, tree, env):
        # Tree structure: [FUNC_DECLARE, NAME, LPAREN, params?, RPAREN, COLON, statements..., FUNC_END]
        func_name = str(tree.children[1].value)  # Get NAME token
        
        # Find param_list if exists (between LPAREN and RPAREN)
        params = []
        body_start = None
        
        for i, child in enumerate(tree.children):
            if isinstance(child, Token) and child.type == "COLON":
                body_start = i + 1
                break
            elif isinstance(child, Tree) and child.data == "param_list":
                params = [str(p.value) for p in child.children if isinstance(p, Token) and p.type == "NAME"]
        
        # Get function body (statements between COLON and FUNC_END)
        body = []
        if body_start:
            for i in range(body_start, len(tree.children)):
                child = tree.children[i]
                if isinstance(child, Token) and child.type == "FUNC_END":
                    break
                if isinstance(child, Tree):
                    body.append(child)
        
        # Store function
        func = {
            'params': params,
            'body': body,
            'env': env
        }
        env.set(func_name, func)
    
    def _exec_return(self, tree, env):
        value = self._eval(tree.children[1], env)  # Skip RETURN keyword, get the actual value
        raise TharunppReturnValue(value)
    
    def _exec_try(self, tree, env):
        ch = tree.children
        i = 0
        
        # Find the catch clause
        catch_idx = None
        for idx, child in enumerate(ch):
            if isinstance(child, Token) and child.type == "CATCH":
                catch_idx = idx
                break
        
        if catch_idx is None:
            return
        
        try:
            # Execute try block
            for i in range(catch_idx):
                if isinstance(ch[i], Tree):
                    self._exec_statement(ch[i], env)
        except TharunppError as e:
            # Execute catch block
            err_var = str(ch[catch_idx + 1].value)
            catch_env = Environment(env)
            catch_env.set(err_var, str(e))
            
            for i in range(catch_idx + 2, len(ch)):
                if isinstance(ch[i], Token) and ch[i].type == "BLOCK_END":
                    break
                if isinstance(ch[i], Tree):
                    self._exec_statement(ch[i], catch_env)
    
    def _exec_throw(self, tree, env):
        msg = self._eval(tree.children[1], env)
        raise TharunppError(str(msg))
    
    def _exec_assert(self, tree, env):
        cond = self._eval(tree.children[1], env)
        if not cond:
            msg = "Assertion failed"
            if len(tree.children) > 3:
                msg = str(self._eval(tree.children[3], env))
            raise TharunppError(msg)
    
    def _exec_import(self, tree, env):
        # Simple import - just a placeholder
        module_name = str(tree.children[0]).strip('"\'')
        # For now, do nothing with imports
        pass
    
    def _exec_list_declare(self, tree, env):
        name = str(tree.children[1].value)
        items = []
        for child in tree.children:
            if isinstance(child, Tree) and child.data == "arg_list":
                items = [self._eval(a, env) for a in child.children]
        env.set(name, items)
    
    def _exec_list_append(self, tree, env):
        name = str(tree.children[1].value)
        value = self._eval(tree.children[2], env)
        lst = env.get(name)
        if not isinstance(lst, list):
            raise TharunppTypeError("list", type(lst).__name__)
        lst.append(value)
    
    def _exec_list_get(self, tree, env):
        target = str(tree.children[1].value)
        source = str(tree.children[4].value)
        index = int(self._eval(tree.children[6], env))
        lst = env.get(source)
        env.set(target, lst[index])
    
    def _eval(self, tree, env):
        if isinstance(tree, Token):
            t = tree.type
            v = str(tree.value)
            
            if t == "NUMBER":
                return int(v) if '.' not in v else float(v)
            elif t == "STRING":
                return v.strip('"\'')
            elif t == "BOOL_TRUE":
                return True
            elif t == "BOOL_FALSE":
                return False
            elif t == "NULL_VAL":
                return None
            elif t == "NAME":
                return env.get(v)
            else:
                return v
        
        if not isinstance(tree, Tree):
            return tree
        
        d = tree.data
        ch = tree.children
        
        if d == "or_expr":
            result = self._eval(ch[0], env)
            for i in range(1, len(ch), 2):
                if result:
                    return True
                result = self._eval(ch[i + 1], env)
            return bool(result)
        
        if d == "and_expr":
            result = self._eval(ch[0], env)
            for i in range(1, len(ch), 2):
                if not result:
                    return False
                result = self._eval(ch[i + 1], env)
            return bool(result)
        
        if d == "not_expr":
            return not self._eval(ch[1], env)
        
        if d == "comp_expr":
            if len(ch) == 1:
                return self._eval(ch[0], env)
            left = self._eval(ch[0], env)
            op = str(ch[1])
            right = self._eval(ch[2], env)
            
            if op == "==":
                return left == right
            elif op == "!=":
                return left != right
            elif op == "<":
                return left < right
            elif op == ">":
                return left > right
            elif op == "<=":
                return left <= right
            elif op == ">=":
                return left >= right
        
        if d == "arith_expr":
            result = self._eval(ch[0], env)
            i = 1
            while i < len(ch):
                op = str(ch[i])
                right = self._eval(ch[i + 1], env)
                if op == "+":
                    # PROMPT 5: String concatenation with type coercion
                    if isinstance(result, str) or isinstance(right, str):
                        result = str(result) + str(right)
                    else:
                        result = result + right
                elif op == "-":
                    result = result - right
                i += 2
            return result
        
        if d == "term":
            result = self._eval(ch[0], env)
            i = 1
            while i < len(ch):
                op = str(ch[i])
                right = self._eval(ch[i + 1], env)
                if op == "*":
                    result = result * right
                elif op == "/":
                    # PROMPT 5: Type-safe division
                    if right == 0:
                        raise TharunppZeroDivisionError()
                    result = result / right
                    return int(result) if result == int(result) else result
                elif op == "%":
                    result = result % right
                i += 2
            return result
        
        if d == "factor":
            if len(ch) == 2:
                op = str(ch[0])
                val = self._eval(ch[1], env)
                if op == "+":
                    return +val
                elif op == "-":
                    return -val
            return self._eval(ch[0], env)
        
        if d == "atom":
            return self._eval(ch[0], env)
        
        if d == "func_call":
            func_name = str(ch[1].value)
            func = env.get(func_name)
            
            if not isinstance(func, dict):
                raise TharunppTypeError("function", type(func).__name__)
            
            # Get arguments
            args = []
            for child in ch:
                if isinstance(child, Tree) and child.data == "arg_list":
                    args = [self._eval(a, env) for a in child.children]
                    break
            
            # Create function environment
            func_env = Environment(func['env'])
            
            # Bind parameters
            for i, param in enumerate(func['params']):
                if i < len(args):
                    func_env.set(param, args[i])
                else:
                    func_env.set(param, None)
            
            # Execute function body
            try:
                for stmt in func['body']:
                    if isinstance(stmt, Tree):
                        self._exec_statement(stmt, func_env)
                return None
            except TharunppReturnValue as ret:
                return ret.value
        
        if d == "list_len_expr":
            lst = env.get(str(ch[1].value))
            return len(lst)
        
        # Default: eval first child
        if ch:
            return self._eval(ch[0], env)
        return None


def main():
    """CLI entry point"""
    if len(sys.argv) < 2:
        print("Usage: python -m Tharunpp.core.interpreter <file.tpp>")
        sys.exit(1)
    
    filename = sys.argv[1]
    with open(filename) as f:
        code = f.read()
    
    interpreter = Interpreter()
    try:
        interpreter.run(code)
    except TharunppError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
