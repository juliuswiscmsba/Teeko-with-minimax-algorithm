### UW-Madison CS540 Fall 2022 HW9: Teeko with minimax algorithm

#### Teeko introduction:

<img width="334" alt="Screenshot 2022-12-11 at 12 51 15 AM" src="https://user-images.githubusercontent.com/90480106/206890357-a9c2d94b-515f-4b8f-bdc9-9e6a2875114f.png">

It is a game between two players on a 5x5 board. Each player has four markers of either red or black. Beginning with black, they take turns placing markers (the "drop phase") until all markers are on the board, with the goal of getting four in a row horizontally, vertically, or diagonally, or in a 2x2 box as shown above. If after the drop phase neither player has won, they continue taking turns moving one marker at a time -- to an adjacent space only! (this includes diagonals, not just left, right, up, and down one space)-- until one player wins. 

#### Win conditions:

1. Four same colored markers in a row horizontally, vertically, or diagonally.

2. Four same colored markers that form a 2x2 box.

