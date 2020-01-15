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


### Facts about rescurion
Recursion may be simpler, more intuitive

Recursion may be efficient from the programmers point of view

Recursion may not be efficient from computer point  of view. One of the downsides of recursion is memory consumption since a stack is maintained with each level of depth. An iterative approach is preferred to save on memory since the variables of each previous iteration are replaced or reused.

### Recursion with two base cases - Fibonacci numbers
#### Problem

Leonardo of Pisa (aka Fibonacci) modeled the following challenge 

◦Newborn pair of rabbits (one female, one male) are put in a pen 

◦Rabbits mate at age of one month ◦Rabbits have a one month gestaSon period 

◦Assume rabbits never die, that female always produces one new pair (one male, one female) every month from its second month on.

◦How many female rabbits are there at the end of one year?

#### Pseudocode

After one month (call it 0) there will be only 1 female

After second month – still 1 female (now pregnant) 

After third month – two females, one pregnant, one not. In general, females(n) = females(n-1) + females(n-2) 

◦Every female alive at month n-2 will produce one female in month n; ◦These can be added those alive in month n-1 to
get total alive in month n

More information about recursion can be found here: https://www.youtube.com/watch?v=WPSeyjX1-4s&list=PLUl4u3cNGP63WbdFxL8giv4yhgdMGaZNA&index=22



