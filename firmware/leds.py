from kmk.extensions.rgb import RGB, AnimationModes
import board

def create_rgb():
    return RGB(
        pixel_pin=board.GP24,  # Update to your LED data pin
        num_pixels=38,
        animation_mode=AnimationModes.ALL,
        brightness=0.2
    )
