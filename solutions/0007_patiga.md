# Patiga

## Hint

This map contains a praise towards Patiga and his twmap and twgpu tool. It also has a clue for the next puzzle:
"DDNet is such an old game. -When was it released again? -But I will never give it up and enjoy every second it has left"

## Solution

This part of the puzzle contains multiple steps:

1. "DDNet is such an old game. -When was it released again?" is asking for the first release of ddnet. [According to the website](https://ddnet.org/staff/) it's just summer 2013.
2. "But I will never give it up" (or let it down) is a reference to the song "Never gonna give you up", which was linked in the QR code in the previous map in [0006_teini94.md](0006_teini94.md).
3. "and enjoy every second it has left" is a reference to time in seconds.

This shows, that you need to render the teini94 at a specific time in seconds. In this case it's 2013 which results in the following maprender command:

/maprender name:teini94 time:2013000

## Extra note

The community took really long for this step, because it knew a way more precise release date than me i.e. "01-02-2013" (not this one, but in principle) making it really hard to just guess the year and I should maybe have just asked for the year.
Also the bot expects milliseconds which was ingored a lot, so a lot of people tried to render with time:2013 making this step **very** hard

## Feedback

Add handling of timesteps to the ruleset and generalize it
