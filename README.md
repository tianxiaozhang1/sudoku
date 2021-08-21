# sudoku

Sudoku is a popular logic game that needs no introduction. Its earlier form was a popular item in French newspapers since late 19th century. The modern form was brought to us by Howard Garns (a 74-year-old retired architect) in 1979. In 1997, Wayne Gould (a Hong Kong judge) wrote a computer program to generate new puzzles and The Times (in Britain) published their first Sudoku (then-called Su Doku) on November 12, 2004. And as they say, the rest is history.

If you haven't played one before, here's how it goes in a nutshell: in a 9 by 9 square puzzle, some numbers are shown and you're invited to fill the rest. The rule is simple: no number repeats in any row, in any column, or in any 3 by 3 smaller square.

Thanks for modern computing power, solving sudoku is fairly easy without the need for intelligent techniques. Just a recursive function using brute force (going through all possibilities on all squares) does the job faster than we mortals can react. My interest is in what makes some puzzles hard and some easy.

Contrary to a popular guess, the difficulty is not correlated with the amount of numbers missing. While that may seem intuitive and true to some extent, two puzzle with identical available numbers, hence appearing to be rather similar from a distance, can vary in difficulty dramatically. The real factor is the complexity of the techniques employed in solving one. As a result, designing a puzzle with difficulty in mind certainly isn't simply removing a particular amount of numbers by random.

So the process should go like this: first figure out the different techniques used to solve a missing number. Give the less obvious or more time-consuming ones a higher "rating" or "cost". Then start with a random full puzzle with all 81 numbers, and randomly remove some to begin; then constantly remove a pair of numbers at a time, and solve it. Each time this is done, see which technique was used, and keep a tally of the total difficulty cost. Once you reach the desired amount, that's a good puzzle. Obviously if the puzzle becomes too hard or impossible, take a step back (put the most recent removals back) and select something else to remove. So if we're looking for a level 4 difficulty, you start with level 1 and keep going until 2, and on, until 4.

My idea was a little different. Instead, one simply removes the numbers with a pattern in mind. Seven out of the twelve common techniques had some kind of a pattern that can be programmed for my skill level, and I reverse-engineered those. Still starting with a full board, just use those particular patterns to remove numbers depending on which difficulty is selected. 

The first technique is "Single Position". Consider where 1 can go in the highlighted row here:

![](https://github.com/tianxiaozhang1/sudoku/blob/main/single_position_01.png){:width="800px"}

Obviously given the positions of the red 1s, we're down to a swift definitive answer:

![](https://github.com/tianxiaozhang1/sudoku/blob/main/single_position_02.png)

Easy. Next is "Candidate Line". Where can 5 go in the highlighted 3x3 box?

![](https://github.com/tianxiaozhang1/sudoku/blob/main/candidate_line_01.png)

There are only two places it can go, and they form a line. This implies the 5 in that full column must be in the bottom right box and can't be anywhere else on that line. This knowledge even helps solving another box above (blue):

![](https://github.com/tianxiaozhang1/sudoku/blob/main/candidate_line_02.png)

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

