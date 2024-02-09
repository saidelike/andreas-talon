# this file is only active when the "user"-defined "cmd" tag is enabled
app: cmd
-
tag(): terminal

talon repl:                 insert('"C:\\Program Files\\Talon\\python.exe" "C:\\Program Files\\Talon\\repl.py"')

# TODO: merge the below commands with the other terminals
tree files:                 "tree /f\n"
tree folders:               "tree\n"

list:                       "dir\n"
