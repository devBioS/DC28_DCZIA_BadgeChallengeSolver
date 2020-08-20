# DC28 DCZIA Build-your-own-badge challenge writeup

In this Challenge we are provided with an image that's called Challenge.jpg and an encrypted 7z file called L00t.7z\
There is also a Readme that states:
>
> so you want the L00T huh!?!?
> Well you have to ask yourself one question. can you solve the puzzle? I bet you can scan it! so the rules are simple. find the keyword to the .ZIP for some SWEEEET L007.
> all of what you will need will be on the DCZIA Build-A-Badge with us badge, Remember there is more than one way to solve any puzzle! 
>
> with Love, 
>  Apl3xicon, Luna, and syntax
>


The image contains a barcode that is not scannable with a mobile or with other tools one can download (I used bcTester v5.0)


Trying different steganographic tools, e.g. stegsolve, steghide, on it didn't provide any clues.


However running exiftool on it shows some base64 data in a comment field that can be decoded to:
> "These bars contain the key to unzip Sweet Loot"


So clearly something is in the jpg and we began a journey that will least 5 days and bring us even dreams of barcodes...


Analyzing the picture show that there are uncommon sharp edges on the bars and the first idea we came of was to measure the pixelwidth of the black and white spaces.
This will give us the following numbers, in the header if it is a **black(b)** or white(w) section:
```
b  w       b  w  b  w  b  w  b  w  b  w  b  w  b  w  b  w   b  w   b  w  b  w  b  w  b  w  b  w  b      w
57 200     20 21 20 41 80 61 61 61 20 20 41 41 40 81 20 101 61 101 81 42 80 81 20 81 81 41 41 20 20     184
```


The first thing we tried was so convert the numbers to hex and see if they contain text but all attempts to do so wasn't successful.\
So we needed another approach.


For barcodes it is not uncommon to have defined spaces and barwidths, we studied the following resources to learn more about the widths and types of barcodes:
   * <a href="https://www.tec-it.com/download/PDF/Barcode_Reference_EN.pdf" target="_blank">https://www.tec-it.com/download/PDF/Barcode_Reference_EN.pdf</a>
   * <a href="https://www.barcodefaq.com/barcode-match/" target="_blank">https://www.barcodefaq.com/barcode-match/</a>
   * <a href="https://www.keyence.com/ss/products/auto_id/barcode_lecture/basic/mechanism/" target="_blank">https://www.keyence.com/ss/products/auto_id/barcode_lecture/basic/mechanism/</a>


Reading through it it became clear that we can count the "units" of the barcode.
Basically the width of 20 became 1 unit and then you can divide the other to make up the "bar units" in number form, this was our result:
>1 1 2 4 3 3 3 1 1 2 2 2 4 1 5 3 5 4 2 4 4 1 4 4 2 2 1 1


After that we tried again to convert these numbers to something useful but all attempts didn't yield anything but binary bogus.


Some voice emerged: "Pain begins. NOW!" (<a href="https://www.youtube.com/watch?v=WJWmzbWas_Q&feature=youtu.be&t=150" target="_blank">https://www.youtube.com/watch?v=WJWmzbWas_Q&feature=youtu.be&t=150</a>)


We thought of a kind of cipher but due to lack of knowledge about a specific cipher we went stuck and reviewed the image again.\
Additional to the black and white bars there was the word "DC ZIA", the number "28" and a square with a 5 in it.


Analysing the scope of numbers and googling hours long showed at least some sunrays: There are "Poly"- Ciphers that uses "squares or boxes": Four-Square, Box-Caesar, Two-Square, Vigenere and Polybius.


We tried all of the ciphers with different "keywords", mutiple options and different chaining **days** long but every attempt to decrypt the numbers failed.


One thing emerged: Polybius was the only cipher that take numbers and convert that with a matrix to text.


At this time @syntax released a public hint:
> "You would be a square if you didn't play Polybius with DCZia"


Ok, that was something we already know about but now we're sure Polybius was the last step, so it seems we have a problem at the beginning: The numbers or the order was not correct.


This time, we played only with polybius and systematicalls used all options it has:
   * the order in which it uses the matrix to decode like row/column or column/row 
   * the missing letter you must remove
   * the order of the ciphertext


I created a solver but that also used wrong options and therefor leaded to no results.


However, after playing around with it, a suprisingly english text came with one of the options:\
**"DPLZBEINSPIRED"**


The options we used:
   * Keyword "DCZIA", 
   * removing W from the matrix (uncommon)
   * using column/row decoding mode (uncommon)


trying around with different cases, the 7z let decrypt itself with the password **"plzbeinspired"**


Puh. Got It. Hate It. And loved it :)


After all if we had removed the first 2 one's in the ciphertext and used other character removals within the matrix key we would have done this much more faster.\
In this github repository I also created (afterwards) a "solver" that will try to bruteforce the Polybius options with a given ciphertext with a known key and validates it against english words.


Have Phun\
--BioS
