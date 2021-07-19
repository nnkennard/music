# Setup

1. Clone the gh-pages branch locally

2. Run `bash setup.sh`. Ensure that you have Python3 installed.


# Changing the songs

- The songs that appear on the website are generated directly from the files in the `_songs` directory (i.e. if you delete a song there, it will be deleted from the website)
- There are two steps to changing the songs:
  1. Change the files in `_songs`
  2. Run `bash process_songs.sh`


# Song format

Each song in the `_songs` directory should be a markdown (`*.md`) file, with the following format:

```
---
title: Hickory Dickory Dock
artist: Mother Goose
category: nursery-rhyme
---

Hickory, dickory, dock.
The mouse ran up the clock.
The clock struck one,
The mouse ran down,
Hickory, dickory, dock.
```

Notes:
* The filename can be anything, as long as it ends in `.md`. You should probably name it something identifiable, though.
* Please ensure that the category is a single word with no spaces. For now, the tool can only handle a single category for each song.


# Printing the QR codes

To print the QR codes, run the following:

```
source ve/bin/activate
python print_qrcodes.py
```

This creates a file called `printme.html`. You can open this file in a browser and print.
