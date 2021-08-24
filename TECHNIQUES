# The Techniques

## Easy - Single Position

Consider where 1 can go in the highlighted row here:

<img src="https://github.com/tianxiaozhang1/sudoku/blob/main/single_position_01.png" width="680">

Obviously given the positions of the red 1s, we're down to a swift definitive answer:

<img src="https://github.com/tianxiaozhang1/sudoku/blob/main/single_position_02.png" width="680">

Easy.

## Medium - Candidate Line

Where can 5 go in the highlighted 3x3 box?

<img src="https://github.com/tianxiaozhang1/sudoku/blob/main/candidate_line_01.png" width="680">

There are only two places it can go, and they form a line. This implies the 5 in that full column must be in the bottom right box and can't be anywhere else on that line. This knowledge helps solving another box above (blue):

<img src="https://github.com/tianxiaozhang1/sudoku/blob/main/candidate_line_02a.png" width="680">

## Medium - Double Pairs

We're looking for 3 in the highlighted area (columns 4-6):

<img src="https://github.com/tianxiaozhang1/sudoku/blob/main/double_pairs_01.png" width="680">

It's obvious that they can only be in those four spots in colums 4 and 6. They form two lines along those two columns. As a result, the 3 in the middle bottom can only be along the middle column, marked blue:

<img src="https://github.com/tianxiaozhang1/sudoku/blob/main/double_pairs_02a.png" width="680">

## Hard - Naked Pairs

For the highlighted row, candidates for all the empty squares are marked. Note the pair that are "2 6":

<img src="https://github.com/tianxiaozhang1/sudoku/blob/main/naked_pairs_01.png" width="680">

We haven't a clue which goes where, but we do know those two are 2 and 6 for sure. It's a significant find when we realize none of the other squares can contain 2 and 6:

<img src="https://github.com/tianxiaozhang1/sudoku/blob/main/naked_pairs_02.png" width="680">

## Expert - X-Wings

9 can only be in four places in the highlighted columns:

<img src="https://github.com/tianxiaozhang1/sudoku/blob/main/x_wings_01a.png" width="680">

Among those four squares, imagine deciding the top left to be 9. This would imply 9 won't be in the same row or column, hence the diagonal square (bottom right) will be 9 as well. Similarly, if the top right is 9, the diagonal (bottom left) will also be 9. The two scenarios are shown here:

<img src="https://github.com/tianxiaozhang1/sudoku/blob/main/x_wings_02d.png">

Hence the name of the technique:

<img src="https://github.com/tianxiaozhang1/sudoku/blob/main/x_wings_03.png" width="680">

## Expert - Swordfish

X-wings is a study of two rows. Now let's tackle three. Here's a puzzle that probably can't be solved further with simple techniques. Candidates for 5 are highlighted:

<img src="https://github.com/tianxiaozhang1/sudoku/blob/main/swordwish_01.png" width="680">

Among the candidates, we need a chain of six or more, the same way x-wings needs a chain of four:

<img src="https://github.com/tianxiaozhang1/sudoku/blob/main/swordwish_02.png" width="680">

And we have two scenarios for going either way on the top left square:

<img src="https://github.com/tianxiaozhang1/sudoku/blob/main/swordwish_03b.png">

Back on the whole board, 5 anywhere in the three highlighted columns but not in those highlighted rows can be disregarded:

<img src="https://github.com/tianxiaozhang1/sudoku/blob/main/swordwish_04.png" width="680">
