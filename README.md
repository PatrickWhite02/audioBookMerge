# audioBookMerge

A simple python script for merging audiobook mp3 files

When you rip an audiobook cd to digital so that you can play it on your phone, you'll bee met with folders full of short mp3 tracks. This doesn't lead to the relaxing experience you should have while listening to an audiobook

audioBookMerge makes it easy to merge the source files for multiple audiobooks, all in one click



<b>Instructions:</b>

Place mergeScript.py in the folder where you ripped your audiobooks, using the convention NAME OF BOOK / DISC # / TRACKS

The program is capable of setting ID3 tags (The data most music players look for so they can sort tracks into Artists and Ablums,) if you would like to use this feature you'll need to install <a href="https://eyed3.readthedocs.io/en/latest"> eyed3 </a>, a python module for tagging audio files. You can just run pip3 install eyed3 and it should install for you! 
If you don't want this, skip this step

run the python script and let the program work it's magic!
You should soon see an audio track for each disc, then an audio merging these discs into groups of 5 for ease of use. Please note, I DON'T delete your source files, on the off chance something goes wrong you're ripped audio files will remain completely intact!
