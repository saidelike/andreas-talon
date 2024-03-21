app: windbg
-
tag(): user.debugger

reload:                     ".reload\n"
break on exec:              "ba e 1 "
break list:                 "bl\n"
go:                         "g\n"

# ret-sync
load sink:                  ".load sync\n"
bang sink:                  "!sync\n"
