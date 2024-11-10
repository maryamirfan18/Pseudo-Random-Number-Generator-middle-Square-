# Pseudo-Random-Number-Generator [middle-Square]
INTRODUCTION
A number is squared and the middle digits are returned as the next random number and same method is repeated to generate pseud random numbers. <br>
To generate a sequence of n-digit pseudorandom numbers, an n-digit 
starting value is created and squared, producing a 2n-digit number. If 
the result has fewer than 2n digits, leading zeroes are added to 
compensate. The middle n digits of the result would be the next 
number in the sequence and returned as the result. This process is then 
repeated to generate more numbers. 
The value of n must be even in order of the method to work – if the 
value of n is odd, then there will not necessarily be a uniquely defined 
"middle n-digits" to select from. Consider the following: If a 3-digit 
number is squared, it can yield a 6-digit number (e.g 5402 = 291600). 
If there were to be middle 3 digits, that would leave 6 − 3 = 3 digits to 
be distributed to the left and right of the middle. It is impossible to 
evenly distribute these digits equally on both sides of the middle 
number, and therefore there are no "middle digits". It is acceptable to 
pad the seeds with zeros to the left in order to create an even valued n
digit number (e.g. 540 → 0540).  
