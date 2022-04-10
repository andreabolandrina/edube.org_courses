#!/usr/bin/env python3

# 3.4.1.12 The Timer class
# We need a class able to count seconds. Easy? Not as much as you may think as we're going to have some specific expectations.
# 
# Read them carefully as the class you're about write will be used to launch rockets carrying international missions to Mars.
# It's a great responsibility. We're counting on you!
# 
# Your class will be called Timer. 
# Its constructor accepts three arguments representing hours (a value from range [0..23] - we will be using the military time), 
# minutes (from range [0..59]) and seconds (from range [0..59]).
# 
# Zero is the default value for all of the above parameters. There is no need to perform any validation checks.
# 
# The class itself should provide the following facilities:
#   objects of the class should be "printable", i.e. they should be able to implicitly convert themselves into strings of the following form: "hh:mm:ss", 
#     with leading zeros added when any of the values is less than 10;
#   the class should be equipped with parameterless methods called next_second() and previous_second(), 
#     incrementing the time stored inside objects by +1/-1 second respectively.
# 
# Use the following hints:
#   all object's properties should be private;
#   consider writing a separate function (not method!) to format the time string.
# 
# Complete the template we've provided in the editor. Run your code and check whether the output looks the same as ours.
# Expected output
# 23:59:59
# 00:00:00
# 23:59:59


class Timer:
    def __init__(self, hours=0, minutes=0, seconds=0):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def __str__(self):
        hours   = str(self.hours)   if (self.hours > 9)   else ('0' + str(self.hours))
        minutes = str(self.minutes) if (self.minutes > 9) else ('0' + str(self.minutes))
        seconds = str(self.seconds) if (self.seconds > 9) else ('0' + str(self.seconds))
        return hours + ':' + minutes + ':' + seconds

    def next_second(self):
        self.seconds += 1
        if self.seconds == 60:
            self.seconds = 0
            self.minutes += 1
            if self.minutes == 60:
                self.minutes = 0
                self.hours += 1
                if self.hours == 24:
                    self.hours = 0

    def prev_second(self):
        self.seconds -= 1
        if self.seconds == -1:
            self.seconds = 59
            self.minutes -= 1
            if self.minutes == -1:
                self.minutes = 59
                self.hours -= 1
                if self.hours == -1:
                    self.hours = 23


timer = Timer(23, 59, 59)
print(timer)
timer.next_second()
print(timer)
timer.prev_second()
print(timer)
