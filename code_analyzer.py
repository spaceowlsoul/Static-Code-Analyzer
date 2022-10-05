import sys
import os
import re
import ast


def s001(line_, i, file):
    max_length = 79
    message = f'{file}: Line {i}: S001 Too long line'
    try:
        assert len(line_) <= max_length, message
    except AssertionError as err:
        print(err)


def s002(line_, i, file):
    message = f'{file}: Line {i}: S002 Indentation is not a multiple of four'
    if line_.startswith(' '):
        first_letter = re.search(r'[a-zA-z@]', line_)
        if first_letter is not None:
            idx = first_letter.start()
            empty_spaces = line_[0:idx]
            try:
                assert len(empty_spaces) % 4 == 0, message
            except AssertionError as err:
                print(err)


def s003(line_, i, file):
    message = f'{file}: Line {i}: S003 Unnecessary semicolon after a statement'
    if ';' in line_:
        if '#' in line_:
            try:
                assert line_.index('#') < line_.index(';'), message
            except AssertionError as err:
                print(err)
        elif line_.endswith(';'):
            print(message)


def s004(line_, i, file):
    message = f'{file}: Line {i}: S004 Less than two spaces before ' \
              f'inline comments'
    if '#' in line_ and not line_.startswith('#'):
        i_1, i_2 = line_.index('#') - 1, line_.index('#') - 3
        try:
            assert line_[i_1:i_2:-1] == ' ' * 2, message
        except AssertionError as err:
            print(err)


def s005(line_, i, file):
    phrase = 'todo'
    message = f'{file}: Line {i}: S005 TODO found'
    line_ = line_.lower()
    if phrase in line_:
        if '#' in line_:
            try:
                assert line_.index('#') > line_.index(phrase), message
            except AssertionError as err:
                print(err)


def s006(i, lines, file):
    message = f'{file}: Line {i}: S006 More than two blank ' \
              f'lines used before this line'
    if i not in lines.keys() and (i - 1) in lines.keys() \
            and (i - 2) in lines.keys():
        if (i - 3) in lines.keys():
            try:
                assert lines[i - 3] != '', message
            except AssertionError as err:
                print(err)


def s007(line_, i, file):
    template = re.match(r' *(class|def)\s', line_)
    if template:
        construction_name = template.group().replace(' ', '')
        message = f"{file}: Line {i}: S007 Too many spaces after " \
                  f"'{construction_name}'"
        try:
            assert re.match(r' *(class|def)\s\S', line_), message
        except AssertionError as err:
            print(err)


def s008(line_, i, file):
    if re.match(' *class .+', line_):
        line_ = line_.replace(' ', '')
        class_name = line_[line_.index('class') + 5:line_.index(':')]
        message = f"{file}: Line {i}: S008 Class name '{class_name}' " \
                  f"should use CamelCase"
        try:
            assert re.match('^(:?[A-Z][()a-z0-9]*)+$', class_name), message
        except AssertionError as err:
            print(err)


def s009(line_, i, file):
    if re.match(' *def .+', line_):
        line_ = line_.replace(' ', '')
        function_name = line_[line_.index('def') + 3:line_.index('(')]
        message = f"{file}: Line {i}: S009 Function name '{function_name}' " \
                  f"should be written in snake_case"
        try:
            assert re.match('^(:?[_a-z][_a-z0-9]*)+$', function_name), message
        except AssertionError as err:
            print(err)


def ast_check_s010_s012(path):
    script = open(path).read()
    tree = ast.parse(script)
    # print(ast.dump(tree))
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            arguments = [a.arg for a in node.args.args]
            for arg in arguments:
                if re.match('^(:?[_a-z][_a-z0-9]*)+$', arg) is None:
                    print(f"{path}: Line {node.lineno}: S010 Argument name '{arg}' should be snake_case")
            for value in node.args.defaults:
                if isinstance(value, ast.List):
                    print(f"{path}: Line {node.lineno}: S012 Default argument value '{arg}' is mutable")
            for v in node.body:
                if isinstance(v, ast.Assign):
                    for g in v.targets:
                        if isinstance(g, ast.Name):
                            if re.match('^(:?[_a-z][_a-z0-9]*)+$', g.id) is None:
                                print(f"{path}: Line {g.lineno}: S011 Variable '{g.id}' in function should be snake_case")


def check(path):
    empty_lines = {}
    with open(path) as file:
        for index, line in enumerate(file.readlines(), start=1):
            line = line.rstrip('\n')
            s001(line, index, path)
            s002(line, index, path)
            s003(line, index, path)
            s004(line, index, path)
            s005(line, index, path)
            if line == '':
                empty_lines[index] = line
            s006(index, empty_lines, path)
            s007(line, index, path)
            s008(line, index, path)
            s009(line, index, path)
    try:
        ast_check_s010_s012(path)
    except IndentationError:
        pass


def main():
    path = str(sys.argv[1])

    if os.path.isfile(path) and path.endswith('.py'):
        check(path)
    elif os.path.isdir(path):
        dir_list = sorted(os.listdir(path))
        for file in dir_list:
            if file.endswith('.py'):
                check(os.path.join(path, file))


if __name__ == "__main__":
    main()
