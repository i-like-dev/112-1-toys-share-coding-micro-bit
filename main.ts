input.onButtonPressed(Button.A, function on_button_pressed_a() {
    basic.showIcon(IconNames.Yes)
})
input.onGesture(Gesture.ScreenUp, function on_gesture_screen_up() {
    basic.showString("Please Saying your Question")
    basic.pause(1000)
    basic.clearScreen()
    basic.showIcon(IconNames.EighthNote)
})
input.onButtonPressed(Button.AB, function on_button_pressed_ab() {
    basic.showLeds(`
        . # # # .
        . . . # .
        . . # . .
        . . . . .
        . . # . .
        `)
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    basic.showIcon(IconNames.No)
})
input.onLogoEvent(TouchButtonEvent.Touched, function on_logo_touched() {
    basic.clearScreen()
})
