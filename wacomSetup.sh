#!/bin/bash

#Set Keys:
xsetwacom set "Wacom Intuos5 touch M Pad pad" Button 1 key "m"					#Krita Mirror
xsetwacom set "Wacom Intuos5 touch M Pad pad" Button 2 key "key Shift_L"
xsetwacom set "Wacom Intuos5 touch M Pad pad" Button 3 key "key Control_L"
xsetwacom set "Wacom Intuos5 touch M Pad pad" Button 8 key "+ctrl z -ctrl"			#Krita undo
xsetwacom set "Wacom Intuos5 touch M Pad pad" Button 9 key "+ctrl +shift z -shift -ctrl"	#Krita redo
xsetwacom set "Wacom Intuos5 touch M Pad pad" Button 10 key "+"					#Krita zoom in
xsetwacom set "Wacom Intuos5 touch M Pad pad" Button 11 key "-"					#Krita zoom out
xsetwacom set "Wacom Intuos5 touch M Pad pad" Button 12 key "ctrl"				#Krita sample dropper
xsetwacom set "Wacom Intuos5 touch M Pad pad" Button 13 key "+ctrl z -ctrl"			

#Set wheel (reversing up and down was more intuitive for me)
xsetwacom set "Wacom Intuos5 touch M Pad pad" AbsWheelUp key "["				#Krita brush size down
xsetwacom set "Wacom Intuos5 touch M Pad pad" AbsWheelDown key "]"				#Krita brush size up

# Settings for tablet on the right side of the main monitor.
# Tablet dimensions are 1920x1080, main monitor is 1366xsomething
xsetwacom set "Wacom Intuos5 touch M Pen stylus" MapToOutput "1920x1080+1366+0"
xsetwacom set "Wacom Intuos5 touch M Pen eraser" MapToOutput "1920x1080+1366+0"
xsetwacom set "Wacom Intuos5 touch M Pad pad" MapToOutput "1920x1080+1366+0"

#Disable touch
xsetwacom set 12 touch off
xsetwacom set 13 touch off
xsetwacom set 14 touch off
xsetwacom set 19 touch off


# REFERENCE:
#Output of list devices:
#Wacom Intuos5 touch M Pad pad   	id: 12	type: PAD       
#Wacom Intuos5 touch M Pen stylus	id: 13	type: STYLUS    
#Wacom Intuos5 touch M Finger touch	id: 14	type: TOUCH     
#Wacom Intuos5 touch M Pen eraser	id: 19	type: ERASER    
#Wacom Intuos5 touch M Pen cursor	id: 20	type: CURSOR  

# Settings for buttons
# Note that the buttons numbers 4-7 are reserved by XInput
# (source: http://linuxwacom.sourceforge.net/wiki/index.php/Tablet_Configuration Tip in "Pad" section)
# so the buttons just up to 13.
# This is the mapping for the Wacom Intuos5 touch
#
#     +----+
#     |  2 |
#     +----+
#     |  3 |
#     +----+
#     |  8 |
#     +----+
#     |  9 |
#+----+----+-----+
#|AbsWheelUp/Down|
#|    +----+     |
#|    |  1 |     |
#|    +----+     |
#|               |
#+----+----+-----+
#     | 10 |
#     +----+
#     | 11 |
#     +----+
#     | 12 |
#     +----+
#     | 13 |
#     +----+
