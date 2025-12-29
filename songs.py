import sys
import time
import os
from itertools import cycle

# colors = cycle([
#     "\033[91m", "\033[92m", "\033[93m",
#     "\033[94m", "\033[95m", "\033[96m"
# ])
# reset = "\033[0m"

brightness_levels = [
    "\033[2m",   # dim
    "\033[22m",  # normal
    "\033[1m",   # bright
    "\033[22m",  # normal
]

reset = "\033[0m"

poem = [
    "Essa Koi Shehar Nahi Jade Jat Ka Kehar Nahi...",
    "Mhare Barga Pyar Mile Na Mhare Barga Bair Nahi",
    "Audi Ne Bhi Fail Kare Look Neele 60 Ki",
    "Se Choudhar Poori Jat Ki"
    
]

# def typewriter(lines, delay=0.10):
#     try:
#         for line in lines:
#             for ch in line:
#                 sys.stdout.write(ch)
#                 sys.stdout.flush()
#                 time.sleep(delay)
#             sys.stdout.write("\n")
#             time.sleep(delay*12)
#     except KeyboardInterrupt:
#         print("\n\n--- Interrupted. Showing rest plainly ---\n")
#         for l in lines:
#             print(l)

# typewriter(poem)

############## moving subtitle
# def scroll(lines, delay=0.5):
#     for line in lines:
#         print(line)
#         time.sleep(delay)
#         os.system("cls" if os.name=="nt" else "clear")

# print("\nMETHOD 3: Scrolling Poetry\n")
# scroll(poem)

# def fade_in(lines, delay=0.03):
#     for line in lines:
#         temp = ""
#         for char in line:
#             temp += char
#             print("\r" + temp, end="")
#             time.sleep(delay)
#         print()
#         time.sleep(0.3)

# print("\nMETHOD 4: Fade-In Effect\n")
# fade_in(poem)

# def color_slow(lines, delay=0.2):
#     for line in lines:
#         c = next(colors)
#         print(c + line + reset)
#         time.sleep(delay)

# print("\nMETHOD 5: Rainbow Slow Motion\n")
# color_slow(poem)

def glowing_poetry(lines, delay=0.15, repeat=3):
    for line in lines:
        for _ in range(repeat):
            for b in brightness_levels:
                sys.stdout.write("\r" + b + line + reset)
                sys.stdout.flush()
                time.sleep(delay)
        print() 

print("\n Start\n")
glowing_poetry(poem)