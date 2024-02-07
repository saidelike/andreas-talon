from talon import Module

mod = Module()

# we define what it is to be a "winmerge" app, but it's already the case by default
mod.apps.winmerge = """
os: windows
and app.exe: WinMergeU.exe
"""
