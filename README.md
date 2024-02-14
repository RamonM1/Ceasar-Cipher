# Ceasar-Cipher
According to legends, ciphers were even present in 50 BC when Julius Caesar was fighting the Gauls in the forests of modern-day France.

To communicate plans with his generals, Caesar sent a courier out into the wilderness with nothing but his sandals, sword, and blessings from Jupiter or whichever Pantheon was preferred during that day.

The risk of this courier being caught was high. Therefore, to ensure that any message in Latin was indecipherable to the Gauls, Caesar's armies encrypted their message using a method we know as Caesar Cipher.

The algorithm for this cipher is as follows:

Select some string value as your message. The program prompts you to choose e/d encrypt or decrypt. Label this string as ciphertext or plaintext.
Select some numeric key value to encode your message. Label this value as key.
For each letter in “message”
a. Shift each letter in your message k letters forward. b. If we go past the last letter in our alphabet (1-26), simply continue counting from the first letter (1-26).

So let's say for example, we take the message, "hello world". We want to then use the key value of 10 to move along the alphabet.

We would take each letter of the message and shift it 10 letters forward. So for the letter "h" in "hello world", that would now become the letter "r", the letter "e" would become "o", so on and so forth.

So the complete message for "hello world" with the key value of 10 would be "rovvy gybvn".

Exploration
For this project, we are trying to figure out how to have every letter advance forward by a selected numberof spaces 1-26 first. Then the next step is to make sure that when we reach closer to the end of the alphabet, the counter restarts to the beginning of the alphabet and continues with the key value from step 1.

To implement the shifting, the American Standard Code for Information Interchange (ASCII) is utilized. 