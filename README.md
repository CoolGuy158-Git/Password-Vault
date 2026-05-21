# Password vault

---

## What is it

A python program which does password things.
It saves, generates, rates your password, and takes your password.

---

## Why is it

Side project.

---

## How it checks password

```txt
Checks the user password by having three cats:
    Must be over 6 chars
    Must contain 1 capital letter
    Must contain 1 lowercase letters
    Must contain digits
    Must contain special characters
```

---

## What module used for save and gen

Keyring for saving

Secrets for generating (Attempted to make my own password generator, but I ended up making somthing that uhh, just go read rant if you want to know.)

---

## GUI or TUI

TUI

---

## Usage

Use it for personal stuff, no banking or high security stuff.

---

## Privacy

Creator is too broke to own a server...
I can't spy on you and add age verification, sorry.

---

## Rant

Ok so I tried making my own password gen from scratch no secrets module and heres what I made!!!

I lost the source code so lemme just say what it does.

First it makes the seed!!! Using os.urandom() so far so good, right?
Then I used random to sometimes turn some numbers into a letter and random chose it to be lowercase or uppercase also.
Then I got data from my mic listening to the noise from outside and got the last few parts of it then added it to that stuff.
Then I hashed the whole thing.
Then I turned every remaining letter into a number using ord.
Then I randomly mixed the hash and the chars of those things 1000 times.
Then I randomly turned some nums to letters and randomly picked whether they should be lowercase or uppercase
Then I took the last 8 digits as the final password.

---

