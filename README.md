# Sudoku

Welcome to my sudoku exercise.

Sudoku is a popular game that needs no introduction. Its earlier form was a popular item in French newspapers since late 19th century. The modern form was brought to us by Howard Garns (a 74-year-old retired architect) in 1979. In 1997, Wayne Gould (a Hong Kong judge) wrote a computer program to generate Soduku puzzles and The Times (in Britain) published their first one (then called Su Doku) on November 12, 2004. As they say, the rest is history.

If you haven't played one before, here's how it goes in a nutshell: in a 9-by-9 square puzzle, some numbers are shown and you're invited to fill the rest. The rule is simple: no number repeats in any row, in any column, or in any of the 9 3-by-3 smaller squares; they all contain 1 to 9.

## Solving Sudoku

Thanks to modern computing power, solving sudoku is easy without intelligent techniques. A recursive function going through all possibilities on all squares does the job faster than we mortals can react. My interest is in what makes some puzzles hard and some easy.

Contrary to a popular guess, <b>difficulty is not correlated with the amount of numbers missing</b>. While that may seem intuitive and true to some extent, two puzzles with identical available numbers (hence appearing similar from a distance) can vary in difficulty dramatically. The real factor is the complexity of the techniques employed. As a result, designing a puzzle with difficulty in mind certainly isn't simply removing a particular amount of numbers by random.

So the process should go like this: figure out the different techniques used to find a missing number. Give the less obvious or more time-consuming ones a higher "cost". Then start with a random full puzzle with all 81 numbers, and randomly remove some to begin; then constantly remove a pair of numbers at a time, and solve it. Each time this is done, see which technique was used, and keep a tally of the total difficulty cost. Once you reach the desired amount, that's a good puzzle. Obviously if the puzzle becomes too hard or impossible, take a step back and select something else to remove. If we're looking for a level 4 difficulty, you start with level 1 and keep going until 2, and on, until 4.

My idea was a little different. Instead, one simply removes the numbers with a pattern in mind. Seven out of the twelve common techniques had some kind of a pattern that felt programmable, and I reverse-engineered those. Still starting with a full board, just use those particular patterns to remove numbers depending on which difficulty is selected. 

## The Techniques

A write up with examples for al the techniques used here:

https://github.com/tianxiaozhang1/sudoku/blob/master/TECHNIQUES.md

Now let's take a look at the interface:

There are four difficulty levels:

![](https://github.com/tianxiaozhang1/sudoku/blob/main/sudoku01.gif)

(And the buttons will be less distracting when the game begins)

One can enter numbers with both the keyboard and the mouse:

![](https://github.com/tianxiaozhang1/sudoku/blob/main/sudoku02.gif)

No cheating when game is paused:

![](https://github.com/tianxiaozhang1/sudoku/blob/main/sudoku03.gif)

There's no need to have the clock over there adding pressure if you prefer otherwise:

![](https://github.com/tianxiaozhang1/sudoku/blob/main/sudoku04.gif)

Erasing a mistake is easy - can be done via the keyboard or the mouse:

![](https://github.com/tianxiaozhang1/sudoku/blob/main/sudoku05.gif)

And everything else should feel intuitive:

![](https://github.com/tianxiaozhang1/sudoku/blob/main/sudoku06.gif)

