###Coding Theory

This program is a computational approach to the main coding theory problem. We examine binary codes, or codes over the alphabet {0, 1}.

A hamming code has three parameters: 
* n: length - length of each code word.
* d: distance - the minimum hamming distance between any two given code words in the code. This parameter is an indication of error correcting capability.
* M: size - the number of code words in the code. This is a measure of the efficiency of the code.

In this program, we calculate the best possible code we can create given two fixed numbers for any two of the three parameters. For example, given that the size of the code is 8, and length of codes words is 6, we can find that the largest minimum hamming distance for the code would be 3.
