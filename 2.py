quantityOfVoters = int(input("how many people will vote?"))

options = ["A", "B", "C"]
votes = {"A": 0, "B": 0, "C": 0}

for i in range(quantityOfVoters):
    option = ""
    while option not in options:
        option = input("what option will you vote for?").upper()
    
    votes[option] += 1

print(f"final result: {votes}")
theMostVoted = next(iter(dict(sorted(votes.items(), key=lambda vote: vote[1], reverse=True))))
print(f"the most voted option: {theMostVoted}")