# this file is always active, eg useful in vscode or notepad++
^force {user.code_language}$:
    user.code_set_language(code_language)

^clear language$:
    user.code_automatic_language()
