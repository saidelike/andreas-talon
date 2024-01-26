# this file is only active when the "user"-defined "repl" app is enabled
app: repl
-

events tail win browser:    "events.tail('/^((?!win|browser).)*$/')\n"
events tail:                "events.tail()\n"
parrot events:              "events.tail('parrot predict')\n"

actions list [<user.text>]:
    'actions.list("{text or ""}")'
    key(left:2)
