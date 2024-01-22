# this file is only active when on Windows and the "user"-defined "user.file_manager" tag is enabled
# i.e. in Windows explorer or the terminal
os: windows
and tag: user.file_manager
-

go {user.letter} colon:     user.file_manager_go("{letter}:")
