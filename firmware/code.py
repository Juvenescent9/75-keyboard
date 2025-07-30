import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners import DiodeOrientation
from kmk.keys import KC
from kmk.modules.encoder import EncoderHandler
from kmk.extensions.media_keys import MediaKeys

# Import your LED setup from leds.py
from leds import create_rgb

keyboard = KMKKeyboard()

# --- MATRIX SETUP ---
keyboard.row_pins = (board.GP0, board.GP1, board.GP2, board.GP3, board.GP4, board.GP5)
keyboard.col_pins = (
    board.GP7, board.GP8, board.GP9, board.GP10, board.GP11,
    board.GP12, board.GP13, board.GP14, board.GP15, board.GP16, board.GP17,
    board.GP18, board.GP19, board.GP20, board.GP21, board.GP6
)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

# --- ENCODER SETUP ---
keyboard.modules.append(MediaKeys())
encoder_handler = EncoderHandler()
keyboard.modules.append(encoder_handler)
encoder_handler.pins = ((board.GP22, board.GP23),)
encoder_handler.map = [((KC.VOLD, KC.VOLU),)]

# --- RGB SETUP ---
rgb = create_rgb()
keyboard.extensions.append(rgb)

# --- KEYMAP ---
keyboard.keymap = [
    [  # Layer 0 example
        KC.ESC, KC.N1, KC.N2, KC.N3, KC.N4, KC.N5, KC.N6, KC.N7, KC.N8, KC.N9,
        KC.N0, KC.MINS, KC.EQL, KC.BSPC, KC.DEL,

        KC.TAB, KC.Q, KC.W, KC.E, KC.R, KC.T, KC.Y, KC.U, KC.I, KC.O,
        KC.P, KC.LBRC, KC.RBRC, KC.BSLS, KC.PGUP,

        KC.CAPS, KC.A, KC.S, KC.D, KC.F, KC.G, KC.H, KC.J, KC.K, KC.L,
        KC.SCLN, KC.QUOT, KC.ENT, KC.PGDN,

        KC.LSFT, KC.Z, KC.X, KC.C, KC.V, KC.B, KC.N, KC.M, KC.COMM, KC.DOT,
        KC.SLSH, KC.RSFT, KC.UP,

        KC.LCTL, KC.LGUI, KC.LALT, KC.SPC, KC.RALT, KC.NO, KC.LEFT, KC.DOWN, KC.RIGHT
    ]
]

if __name__ == '__main__':
    keyboard.go()
