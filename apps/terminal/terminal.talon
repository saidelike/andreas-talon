# this file is only active when the Talon-defined "terminal" tag is enabled
tag: terminal
-
# in a terminal, we want to be able to navigate folders, create files/folders, use git, npm, pip.
# and we also disable the optimized insert by pasting
tag(): user.file_manager
tag(): user.git
tag(): user.npm
tag(): user.pip
tag(): user.insert_paste_disabled

# TODO: some of the below is probably just bash, not terminal

vscode install:             "vsce package -o bundle.vsix && code --install-extension bundle.vsix --force\n"

vscode package:             "vsce package\n"

run talon deck:             "talon-deck\n"

python version:             "python --version\n"
java version:               "java --version\n"

# terminal
terminate:                  key(ctrl-c)
