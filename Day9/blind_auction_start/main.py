from replit import clear
#HINT: You can call clear() to clear the output in the console.

import art
print(art.logo)

auction_bids = {}


name1 = str(input("What is your name? "))
bid1 = float(input("What do you bid? $"))
auction_bids[name1] = bid1
largest_bid = bid1
largest_bidder = name1

print(auction_bids)

keep_asking = str(input("Are there any other bidders? Type 'yes' or 'no': "))

while keep_asking == 'yes':
  clear()
  name = str(input("What is your name? "))
  bid = float(input("What do you bid? $"))
  auction_bids[name] = bid
  keep_asking = str(input("Are there any other bidders? Type 'yes' or 'no': "))


for list_name in auction_bids:
  if auction_bids[list_name] > largest_bid:
    largest_bid = auction_bids[list_name]
    largest_bidder = list_name

print(f"The winner is {largest_bidder} with a bid of ${largest_bid}.")