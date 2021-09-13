# SMS script

I've always wanted to be able to send an SMS from a computer.
It is possible by subscribing to an SMS service like Twilio, but I mean
if I have a SIM card, why shouldn't I be able to use it? And why should
I require an internet connection, if I already have a cellular connection?

When playing with my LTE router, I discovered that it has this feature!
From the web control panel, one can send and receive SMS messages, and
the router has its own phone number (from the SIM).

## Proof of concept

A little reverse engineering of the API lead to this script for sending
messages.
I don't use my LTE router with a SIM these days but one day I might put this
idea to use. At the moment, it's just a proof of concept.
Until then, someone else might be able to use it too.

Notes:

* I'm pretty sure there is an android binary somewhere in the router
  powering the cellular and LTE connection, no idea how (in)secure it is.
* This script uses Python3 and the third-party `requests` module.
* I'm sure there is dedicated software and hardware for this purpose, but
  this was just a small exploration.

---

Matt
