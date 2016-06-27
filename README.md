# MagicMirror-Toggle
GPIO control for Magic Mirror TV

This was created to control my Raspberry Pi Magic Mirror by switching the display on or off based on whether my phone is connected to the WiFi so that the mirror is only on when I am home.
There isn't a config file, but there are variables inside the main program such as the IP address of your phone (you would need to add a DHCP reservation for a static internal IP in your router for the phone) and the On/Off times for each day.

It's not perfect or ideal, the logic is quite simple as there is no way to check the on/off status, it operates on the assumption that the script is first run when the screen is off (such as when the power has been turned on to the Pi & Mirror).
