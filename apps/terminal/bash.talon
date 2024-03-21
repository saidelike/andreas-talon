# this file is only active when the "user"-defined "user.bash" tag is enabled
tag: user.bash
-
# when the "user.bash" tag is enabled, we want to be able to use terminal features
tag(): terminal

flag:                       " -"
flag <user.letters>:        " -{letters} "

# TODO: merge the below commands with the other terminals
list long pipe:             "ls -lah | "

tree files:                 "tree\n"
tree folders:               "tree -d\n"

history:                    "history "
history tail:               "history | tail\n"
history tail <number_small>: "history | tail -{number_small}\n"
history grep:               "history | grep "
run history <number>:       "!{number}\n"
run last:                   "!!\n"
run last <number>:          "!-{number}\n"

head <number_small>:        "head -{number_small}"
tail <number_small>:        "tail -{number_small}"

print dir:                  "pwd\n"
copy dir:                   "pwd | clipboard\n"

tar create:                 "tar -czvf "
tar extractf:               "tar -xzvf "

echo:                       "echo "
echo <user.text>$:          "echo {text}"

grep:                       "grep "
move:                       "mv "
# remove:                        "rm "
copy:                       "cp "
less:                       "less "
sudo:                       "sudo "
apt install:                "apt install "
apt update:                 "apt update\n"
# word count:                 "wc "
change mode:                "chmod "
change owner:               "chown "
exargs:                     "xargs "
exec:                       "exec "
cat:                        "cat "
diff:                       "diff "
unique:                     "uniq "
clipboard:                  "clipboard"
translate:                  "tr "
vim:                        "vim "
curl:                       "curl "
yarn:                       "yarn "
dev null:                   "/dev/null"
print exit code:            "echo $?\n"
pipe:                       " | "
op and:                     " && "
op or:                      " || "
clear:                      key(ctrl-l)
revert:                     key(alt-r)
ssh:                        "ssh "

# head:                          "head "
# tail:                          "tail "
# find:                          "find "
# sed:                           "sed "
# set:                           "set "
# ctrl-
# find -exec grep \;
# locate
# echo hello >> myfile.text
# pushd https://linuxhint.com/bash_pushd_command/
# cat /etc/os-release
#cat /proc/version
# fc last command in editor.

talon user update:
    "find {user.talon_user()} -type d -name .git -print -execdir git pull --ff-only \\;\n"
    "git -C {user.user_home()}/repositories/cursorless-talon pull\n"

watch talon log:            "tail -f {user.talon_home()}/talon.log\n"
