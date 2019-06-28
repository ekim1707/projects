# Hotel Management App

## Instructions

Let's imagine that you're running a hotel, and you want to keep track of guests by floor and room number:

```
hotel = {
 '1': {
   '101': ['George Jefferson', 'Wheezy Jefferson'],
 },
 '2': {
   '237': ['Jack Torrance', 'Wendy Torrance'],
 },
 '3': {
   '333': ['Neo', 'Trinity', 'Morpheus']
 }
}
```

Write a program that works with this hotel data:

* Display a menu asking whether to check in or check out.
* Prompt the user for a floor number, then a room number.
* If checking in, ask for the number of occupants and what their names are.
* If checking out, remove the occupants from that room.
* Do not allow anyone to check into a room that is already occupied.
* Do not allow checking out of a room that isn't occupied.
