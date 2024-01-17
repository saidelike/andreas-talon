# tag(): user.key_debug

settings():
    # Voice activity timeout (seconds) - default is 0.3
    speech.timeout = 0.25
    # Record speech
    speech.record_all = true

    # Set log level
    # Show parrot sounds being said and regular talon debug logs
    user.log_level = "debug"
    # disable it so we can actually see other things in the talon log window
    # user.log_level = "info"

    # Print timings for spoken phrases
    user.print_phrase_timings = false

    # Pretty print spoken phrases
    #user.pretty_print_phrase = true
    # temporarily disable it so we can actually see things in the talon log window
    user.pretty_print_phrase = false

    # Location to store cursorless settings
    #user.cursorless_settings_directory = "andreas-talon/settings/cursorless-settings"

    # Mouse scroll speed
    user.scroll_speed = 0.7

    # General gui
    # imgui.scale = 1.25
    user.gui_max_rows = 5
    # user.gui_max_cols = 80
    # increase the width for "command history" so we can print full paths
    user.gui_max_cols = 168

    # Help gui
    user.help_max_command_lines_per_page = 20
    user.help_max_contexts_per_page = 25
    # this is the max width of the help scope window
    user.help_scope_max_length = 100

    # Command history
    user.command_history_size = 50
    user.command_history_display = 10
    # user.command_history_ttl = 15
