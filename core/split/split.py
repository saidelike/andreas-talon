from talon import Module, actions


mod = Module()
mod.tag("splits")


@mod.action_class
class Actions:
    # Arrangement
    def split_move_up():
        """Move the current window to above split group"""

    def split_move_down():
        """Move the current window to below split group"""

    def split_move_left():
        """Move the current window to left split group"""

    def split_move_right():
        """Move the current window to right split group"""

    # Navigation
    def split_focus_up():
        """Focus the split group above the current window"""

    def split_focus_down():
        """Focus the split group below the current window"""

    def split_focus_left():
        """Focus the split group to the left of the current window"""

    def split_focus_right():
        """Focus the split group to the right of the current window"""

    def split_focus_next():
        """Focus the next split group"""

    def split_focus_last():
        """Focus the previous split group"""

    def split_focus(number: int):
        """Focus the nth split group"""

    # Resizing
    def split_shrink_width():
        """Shrink the width of the current split group"""

    def split_shrink_height():
        """Shrink the height of the current split group"""

    def split_expand_width():
        """Expand the width of the current split group"""

    def split_expand_height():
        """Expand the height of the current split group"""

    # Layout
    def split_layout_toggle():
        """Mirror the split groups layout diagonally or toggle between horizontal/vertical layout"""

    def split_layout_join_two_groups():
        """Join two closest split groups into one split group"""

    def split_layout_clear():
        """Clear the layout of all the split groups and merge all windows into one"""

    def split_layout_toggle_maximize():
        """Toggle between maximize the current split group or show all split groups"""
