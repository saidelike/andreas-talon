from talon import Module

mod = Module()

# we define what it is to be a "keepass" app, but it's already the case by default
mod.apps.keepass = """
os: windows
and app.exe: KeePass.exe
"""
