def on_button_pressed_a():
    basic.show_icon(IconNames.YES)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_gesture_screen_up():
    basic.show_string("Please Saying your Question")
    basic.pause(1000)
    basic.clear_screen()
    basic.show_icon(IconNames.EIGHTH_NOTE)
input.on_gesture(Gesture.SCREEN_UP, on_gesture_screen_up)

def on_button_pressed_ab():
    basic.show_leds("""
        . # # # .
        . . . # .
        . . # . .
        . . . . .
        . . # . .
        """)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    basic.show_icon(IconNames.NO)
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_logo_touched():
    basic.clear_screen()
input.on_logo_event(TouchButtonEvent.TOUCHED, on_logo_touched)
