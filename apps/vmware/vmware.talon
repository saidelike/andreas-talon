app: vmware
-
tag(): user.insert_paste_disabled

^force application {user.vmware_application}$:
    user.vmware_set_application(vmware_application)

^clear applications$:
    user.vmware_clear_applications()
