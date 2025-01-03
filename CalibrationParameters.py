color_ratio = 2.5 # ratio of w/b pixeld in a tile
threshold = 50 # threshold for tile binarization

# get a screenshot of the portion of the screen in the box (x, y, width, height)
x = 583
y = 220
heigth = 672
width  = 672
tile_size = 85  # size of the second and third dimensions
number_of_tiles = 8  # number of tiles in the second and third dimensions

# GENERATE fen string
FEN = {
    "white": {
        "pawn": "P",
        "knight": "N",
        "bishop": "B",
        "rook": "R",
        "queen": "Q",
        "king": "K"
    },
    "black": {
        "pawn": "p",
        "knight": "n",
        "bishop": "b",
        "rook": "r",
        "queen": "q",
        "king": "k"
    }
}

pieces = ["pawn", "knight", "bishop", "rook", "queen", "king"]

depth = 10 # max depth