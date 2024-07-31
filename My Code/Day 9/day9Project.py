# Day 9: The Auction

import blind_auction
print(blind_auction.logo)

all_the_bids = {}
any_more_bidders = True

while any_more_bidders:
    name = input("What is your name: ")
    new_bid = float(input("How much are you bidding: $ "))
    all_the_bids[name] = new_bid
    any_more_bidders_string = input("Are there any more bidders? yes or no: ").lower()
    if any_more_bidders_string == "no":
        any_more_bidders = not any_more_bidders
    elif any_more_bidders_string != "yes":
        any_more_bidders = not any_more_bidders
        print("\nYour invalid response made the Auction end.")
    print("")

highest_bid_name = ""
highest_bid_amount = 0
for name in all_the_bids:
    if all_the_bids[name] > highest_bid_amount:
        highest_bid_amount = int(all_the_bids[name])
        highest_bid_name = name
print(f"If you had cents, We do not accept those!")
print(f"{highest_bid_name} has the highest bid of $ {highest_bid_amount}!")
