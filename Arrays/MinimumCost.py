'''A shop is selling candies at a discount. For every two candies sold, the shop gives a third candy for free.

The customer can choose any candy to take away for free as long as the cost of the chosen candy is less than or equal
to the minimum cost of the two candies bought.

For example, if there are 4 candies with costs 1, 2, 3, and 4, and the customer buys candies with costs 2 and 3, 
they can take the candy with cost 1 for free, but not the candy with cost 4.
Given a 0-indexed integer array cost, where cost[i] denotes the cost of the ith candy, return the minimum cost of buying all the candies.'''

cost = [6,5,7,9,2,2]
cost.sort()
ans=0
took=0
for i in range(len(cost)-1,-1,-1):
    if took==2:
        took=0
    else:
        ans+=cost[i]
        took+=1
print(ans)