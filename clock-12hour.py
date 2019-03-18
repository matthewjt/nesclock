#!/usr/bin/env python

import time

import scrollphathd
import font3x7
import datetime

print("""
Scroll pHAT HD: Clock

Displays hours and minutes in text,
plus a seconds progress bar.

Press Ctrl+C to exit!

""")

BRIGHTNESS_HIGH = 0.5
BRIGHTNESS_LOW = 0.4

def time_in_range(start, end, x):
    """Return true if x is in the range [start, end]"""
    if start <= end:
        return start <= x <= end
    else:
        return start <= x or x <= end


# Uncomment the below if your display is upside down
#   (e.g. if you're using it in a Pimoroni Scroll Bot)
# scrollphathd.rotate(degrees=180)

while True:
    scrollphathd.clear()

    startamdig = datetime.time(1, 0, 0)
    endamdig = datetime.time(9, 59, 59)
    startpmdig = datetime.time(13, 0, 0)
    endpmdig = datetime.time(21, 59, 59)

    startam = datetime.time(0, 0, 0)
    endam = datetime.time(12, 0, 0)

    startdim = datetime.time(17, 0, 0)
    enddim = datetime.time(7, 0, 0)

    timenow = datetime.datetime.now().time()

#    timenow = datetime.time(17,0,0)

    timestring = time.strftime("%-I:%M")

    if time_in_range(startamdig, endamdig, timenow) or time_in_range(startpmdig, endpmdig, timenow):
      timestring = "  " + timestring

    if time_in_range(startdim, enddim, timenow):
      BRIGHTNESS = BRIGHTNESS_LOW
    else:
      BRIGHTNESS = BRIGHTNESS_HIGH

    # Display the time (HH:MM) in a 5x5 pixel font
    scrollphathd.write_string(
        time.strftime(timestring),
        x=0, # Align to the left of the buffer
        y=0, # Align to the top of the buffer
        font=font3x7, # Use the font font we imported above
        brightness=BRIGHTNESS # Use our global brightness value
    )

    # The dots (:) to blink in between seconds
    scrollphathd.set_pixel(8, 2, BRIGHTNESS)
    scrollphathd.set_pixel(8, 4, BRIGHTNESS)

    if not time_in_range(startam, endam, timenow):
      scrollphathd.set_pixel(8, 6, BRIGHTNESS)
    else:
      scrollphathd.set_pixel(8, 6, 0.0)

    # int(time.time()) % 2 will tick between 0 and 1 every second.
    # We can use this fact to clear the ":" and cause it to blink on/off
    # every other second, like a digital clock.
    # To do this we clear a rectangle 8 pixels along, 0 down,
    # that's 1 pixel wide and 5 pixels tall.
    if int(time.time()) % 2 == 0:
        scrollphathd.clear_rect(8, 0, 1, 5)

    # Display our time and sleep a bit. Using 1 second in time.sleep
    # is not recommended, since you might get quite far out of phase
    # with the passing of real wayl-time seconds and it'll look weird!
    #
    # 1/10th of a second is accurate enough for a simple clock though :D
    scrollphathd.show()
    time.sleep(0.1)
