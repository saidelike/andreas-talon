# this file is only active when the "user"-defined "cmd" tag is enabled
app: cmd
-
tag(): terminal
# this is using groupy
tag(): user.tabs

talon repl:                 insert('"C:\\Program Files\\Talon\\python.exe" "C:\\Program Files\\Talon\\repl.py"')
git bash:                   insert('"C:\\Program Files\\Git\\bin\\bash.exe" -li')

# TODO: merge the below commands with the other terminals
tree files:                 "tree /f\n"
tree folders:               "tree\n"

i p conf:                   "ipconfig\n"
