from talon import Module

mod = Module()

# we define what it is to be a "talon_repl" app
mod.apps.talon_repl = """
os: windows
and app.exe: cmd.exe

os: windows
and app.exe: conhost.exe

os: windows
and app.exe: windowsterminal.exe

title: Talon - REPL
"""
