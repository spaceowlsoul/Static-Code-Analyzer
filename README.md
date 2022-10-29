# 🔎 Static-Code-Analyzer for python files

What's good code? 

The one that works correctly under different, even unexpected circumstances? 
Of course!

The one that's easy to understand and easy to manage even for a non-familiar programmer?
Yes again!

The one that's complies with the general standards and requirements and falls under the common rules of code grammar?
Definitely!

The latter is easier to handle with the help of specialized code analyzers, whose prime function is to help you maintain a high code quality by pointing out any stylistic errors.

## How does this analyzer work?

1.To start download the 'code_analyzer.py' file and copy the path to it.

2.Run the command prompt, paste the copied path and start executing the python file as follows:

    python code_analyzer.py {path to the python file being analyzed}
    
    
3.If any mistakes have been detected, you'll see them in this format:

    {path to the analyzed python file} Line {number of line in your code}: {error code} {error description}

For example:

    test\test.py Line 1: S001 Too long line
    
    
List of analyzed stylistic errors supported by this analyzer:

- SOO1 Too long line;
- S002 Indentation is not a multiple of four;
- S003 Unnecessary semicolon after a statement;
- S004 Less than two spaces before inline comments;
- S005 TODO found;
- S006 More than two blank lines used before this line;
- S007 Too many spaces after '{construction_name}';
- S008 Class name '{class_name}' should use CamelCase;
- S009 Function name '{function_name}' should be written in snake_case;
- S010 Argument name '{argument}' should be snake_case;
- S011 Variable '{variable}' in function should be snake_case;
- S012 Default argument value '{argument}' is mutable.
