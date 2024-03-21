# this file is only active when the Talon-defined "terminal" tag is enabled
tag: terminal
-
# in a terminal, we want to be able to navigate folders, create files/folders, use git, npm, pip.
# and we also disable the optimized insert by pasting
tag(): user.file_manager
tag(): user.git
tag(): user.npm
tag(): user.pip

go:                         user.file_manager_go_step("")
go <user.text>$:            user.file_manager_go_step(text)
go (pace | paste)$:         user.file_manager_go_step(clip.text())
go <user.letters>$:         user.file_manager_go_step(letters)
go <user.text> tab$:        user.file_manager_go_step("{text}\t")
go <user.letters> tab$:     user.file_manager_go_step("{letters}\t")

list:                       user.list_directory("")
list (pace | paste):        user.list_directory(clip.text())
list <user.text>$:          user.list_directory(text)
list all:                   user.list_directory_all("")
list long:                  user.list_directory_long("")

make dir:                   user.make_directory("")
make dir <user.text>$:      user.make_directory(text)
make dir (pace | paste)$:   user.make_directory(clip.text())

# TODO: some of the below is probably just bash, not terminal

vscode install:             "vsce package -o bundle.vsix && code --install-extension bundle.vsix --force\n"

vscode package:             "vsce package\n"

run talon deck:             "talon-deck\n"

python version:             "python --version\n"
java version:               "java --version\n"

# terminal
terminate:                  key(ctrl-c)
