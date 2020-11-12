# Chomp
[Chomp] is a two-player strategy game played on a rectangular grid made up of smaller square cells, which can be thought of as the blocks of a chocolate bar. The players take it in turns to choose one block and "eat it" (remove from the board), together with those that are below it and to its right. The top left block is "poisoned" and the player who eats this loses.

This is a command line based implementation of Chomp with reinforced learning. The agent must first be trained which is done vs. another agent:

`python application.py train rows cols --iterations n`

where rows/cols are ints with the grid size

The policy is saved and will be reused for next training session.
The game randomizes who picks the first cell.

`python application.py play rows cols`

[Chomp]: https://en.wikipedia.org/wiki/Chomp
