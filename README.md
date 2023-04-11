# IndovinaEspressioni

This python library allows to find solutions in those expressions where you have to fill up with the correct operations.<b>

  As exmaple, given that expression:
    5 [] 4 [] 3 [] 2 [] 1 = 8

  the program finds the correct operation in order to fill all the gaps:
    5 [ + ] 4 [ - ] 3 [ + ] 2 [ / ] 1 = 8

However, the time of the solution may diverge pretty quickly for too long expressions. 
That's because the algorithm only searches the right answers between all the possible answers:

Each hole has to be to filled up with 1 out of 4 possibilities (+,-,*,/), these four possibilities must be repeated for all the n holes.
So, in the worst case the check ends after 4 to the power of n checks O(4^n) = O(2^2n) = O(2^n)

In other words, the time grows exponentially to the number of the operations to guess.
(code and prints in italian)
