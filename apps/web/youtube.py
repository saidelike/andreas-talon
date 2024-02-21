from talon import Module

mod = Module()

# we define what it is to be a "youtube" app
# are the browser.host and browser.path populated automatically by Talon based on the browser.address() action?
mod.apps.youtube = r"""
tag: browser
browser.host: www.youtube.com
browser.path: /watch
"""
