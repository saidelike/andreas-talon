volume up:                  user.volume_up()
volume down:                user.volume_down()
volume mute:                key(mute)

media next:                 key(next)
media last:                 key(prev)
media (play | pause):       key(play_pause)
media stop:                 key(stop)

^playback {user.playback_device}:
    user.notify("Playback: {playback_device}")
    user.change_sound_device(playback_device)

^microphone {user.microphone_device}:
    user.notify("Microphone: {microphone_device}")
    user.change_sound_device(microphone_device)

^use {user.playback_microphone_pair}:
    user.change_sound_device_pair(playback_microphone_pair)
