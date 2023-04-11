
"""
Design and write a program to calculate Net Run Rate scored by the two teams use controls to validate a condition such that the team with the higher run rate will top the points table and also think for the tie-breaker condition.
Steps to Follow: 
Understand how net run rate getting calculated (Cite the reference in submission comment)
Follow the computational thinking process.
Understand inputs required to calculate various parameters (Give Appropriate Comments to the code)
Design Controls -  Compound Statements and Suites
Provide Feedback to the User (Console level Feedback)
Test (Paper Calculation)
Validate (Paper Calculation = Code  Result)
"""
i=1
print("Input for team 1")
while i<=2:
    team_scored = int(input("Enter the total runs scored by Team 1: "))
    team_faced = int(input("Enter the total overs faced by Team : "))
    team_conceded = int(input("Enter the total runs conceded by Team : "))
    team_bowled= int(input("Enter the total overs bowled by Team : "))
    if i==1:
        team1_Nrr = (team_scored / team_faced) - (team_conceded / team_bowled)
        print("Input for team 2")
    else:
        team2_Nrr = (team_scored / team_faced) - (team_conceded / team_bowled)
    i+=1
if team1_Nrr > team2_Nrr:
    print("Team 1 has a higher Net Run Rate and tops the points table.")
elif team2_Nrr > team1_Nrr:
    print("Team 2 has a higher Net Run Rate and tops the points table.")
else:
    print(" Match Tie")