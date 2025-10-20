from microbit import sleep, display, Image, button_a, button_b
import tinybit

# Custom letter images
LETTER_IMAGES = {
"L": Image("90000:90000:90000:90000:99999"),
"O": Image("09990:90009:90009:90009:09990"),
"D": Image("99000:90900:90090:90009:99999"),
"Z": Image("99999:00090:00900:09000:99999"),
}

# Movement sequences for each letter
LETTER_MOVEMENTS = {
"L": [("run", 80, 1000), ("spinleft", 180, 400), ("run", 80, 1000), ("stop", 0, 0)],
"O": [
("run", 80, 1000),
("spinleft", 180, 400),
("run", 80, 1000),
("spinleft", 180, 400),
("run", 80, 1000),
