# Tower-of-Hanoi
Solution to Tower of Hanoi problem using a recursive algorithm. #DSA

for more information about the puzzle check here: https://www.tutorialspoint.com/data_structures_algorithms/tower_of_hanoi.htm

The algorithm goes as follows

Step 1 − Move n-1 disks from source to aux

Step 2 − Move nth disk from source to dest

Step 3 − Move n-1 disks from aux to dest

### Interesting things to note about recursion


Each recursive call to a  function creates its own scope

Binding variables in a scope are not changed by recursive call

flow control passes back to previous scope once the function call returns a value


### facts about rescurion
Recursion may be simpler, more intuitive

Recursion may be efficient from the programmers point of view

Recursion may not be efficient from computer point  of view. One of the downsides of recursion is memory consumption since a stack is maintained with each level of depth. An iterative approach is preferred to save on memory since the variables of each previous iteration are replaced or reused.

More information about recursion can be found here: https://www.youtube.com/watch?v=WPSeyjX1-4s&list=PLUl4u3cNGP63WbdFxL8giv4yhgdMGaZNA&index=22



