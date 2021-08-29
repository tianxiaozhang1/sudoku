# Sudoku

Welcome to my sudoku exercise.

Sudoku is a popular game that needs no introduction. Its earlier form was a popular item in French newspapers since late 19th century. The modern form was brought to us by Howard Garns (a 74-year-old retired architect) in 1979. In 1997, Wayne Gould (a Hong Kong judge) wrote a computer program to generate Soduku puzzles and The Times (in Britain) published their first one (then called Su Doku) on November 12, 2004. As they say, the rest is history.

If you haven't played one before, here's how it goes in a nutshell: in a 9-by-9 square puzzle, some numbers are shown and you're invited to fill the rest. The rule is simple: no number repeats in any row, in any column, or in any of the 9 3-by-3 smaller squares; they all contain 1 to 9.

## Solving Techniques

Although one may rightfully guess sudoku's difficulty is directly correlated with the amount of numbers missing, that isn't quite true. This program reverse-engineers some of the techniques involved in solving sudoku and attempts to design puzzles with different difficulty levels:

<img src="https://github.com/tianxiaozhang1/sudoku/blob/main/techniques.png" width="680">

A detailed write of those techniques:

https://github.com/tianxiaozhang1/sudoku/blob/master/TECHNIQUES.md

## Requirements

### Python 3
https://www.python.org/downloads

### Pygame
https://www.pygame.org/news

## Gameplay

There are four difficulty levels:

![](https://github.com/tianxiaozhang1/sudoku/blob/main/sudoku01a.gif)

![](https://github.com/tianxiaozhang1/sudoku/blob/main/sudoku02a.gif)

![](https://github.com/tianxiaozhang1/sudoku/blob/main/sudoku03a.gif)

![](https://github.com/tianxiaozhang1/sudoku/blob/main/sudoku04a.gif)

![](https://github.com/tianxiaozhang1/sudoku/blob/main/sudoku05a.gif)

![](https://github.com/tianxiaozhang1/sudoku/blob/main/sudoku06a.gif)

## Further Reading

All techniques used in this program and many of the examples are from:

https://www.sudokuoftheday.com/

Thanks for visiting.
