from talon import Module

mod = Module()

# we define what it is to be a "repl" app
mod.apps.repl = """
os: windows
and app.exe: cmd.exe

os: windows
and app.exe: conhost.exe

os: windows
and app.exe: windowsterminal.exe

title: Talon - REPL
"""
