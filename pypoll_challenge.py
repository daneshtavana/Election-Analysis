# Psuedocode
# 1-Open the data file
# 2-A complete list of candidates who received votes
# 3-Total number of votes each candidate received
# 4-Total number of votes cast for election
# 5-Percentage of votes each candidate won
# 6-The winner of the election based on popular vote
#
# Add our dependencies.
import csv
import os

# Open the data file (pseudocode 1)
# Assign a variable to load a file from a path
file_to_load = os.path.join("Resources/election_results.csv")
# Assign a variable to save the file to a path
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize variables used in code
candidate_list = []     # List of candidates (pseudocode 2)
county_list = []        # List of candidates (challenge task)
candidate_votes = {}    # Key-value pair dictionary of candidates-votes (pseudocode 3)
county_votes = {}       # Key-value pair dictionary of counties-votes (challenge task)
total_votes = 0         # Total vote counter (pseudocode 4)
winning_candidate = ""  # Variable used in pseudocode 6
winning_county = ""     # vaiable used in challenge task
winning_count = 0       # Variable used in pseudocode 6
winning_percentage = 0     # Variable used in pseudocode 6    

# Open the election results, read the file object with the reader function
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Skip and rint the header row 
    headers = next(file_reader)
    #### print(headers)
    
    for row in file_reader:
        # Extract complete list of candidates who received votes (pseudocode 2)
        candidate_name = row[2] 
        county_name = row[1]
        # if candidate name is not in candidate list add it to list and initialize vote
        if candidate_name not in candidate_list:
            candidate_list.append(candidate_name)
            candidate_votes[candidate_name] = 0
        if county_name not in county_list:
            county_list.append(county_name)
            county_votes[county_name] = 0        
        candidate_votes[candidate_name] += 1    # accumulate votes each candidate received (challenge 3)
        county_votes[county_name] += 1          # accumulate votes each county received (challenge task)
        # Extract total number of votes cast for election (pseudocode 4)
        total_votes += 1

    #### print(total_votes)
    #### print(candidate_list)
    #### print (candidate_votes)

    # Save the results to  text file.
with open(file_to_save, "w") as txt_file:
    # Print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n\n"
        f"County Vote\n")
    print(election_results, end="")
    # Save the final vote count to the text file.
    txt_file.write(election_results)

    # Determine Percentage of votes each candidate won

    for county in county_votes:
        # Retrieve vote count of a county.
        votes = county_votes[county]
        # Calculate the percentage of votes.
        vote_percentage = int(votes) / int(total_votes) * 100
        # Print the county name and percentage of votes.
        results = (f"{county}: {vote_percentage:.1f}% ({votes:,})\n")
        print(results)
        # Save the final vote count to the text file.
        txt_file.write(results)

        if (votes > winning_count) and (vote_percentage > winning_percentage):
            # If true, then set winning_count = votes and winning_percent = vote_percentage.
            winning_count = votes
            winning_percentage = vote_percentage
            # If true, then set the winning_county equal to the county's name.
            #### print(f"test breakpint: {county}")
            winning_county = county

    winning_county_summary = (
            f"\n"
            f"-------------------------\n"
            f"Largest County Turnout: {winning_county}\n"
            f"-------------------------\n")
    print(winning_county_summary)
    # Save the wining county summary to the text file.
    txt_file.write(winning_county_summary)

    for candidate in candidate_votes:
        # Retrieve vote count of a candidate.
        votes = candidate_votes[candidate]
        # Calculate the percentage of votes.
        vote_percentage = int(votes) / int(total_votes) * 100
        # Print the candidate name and percentage of votes.
        results = (f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n")
        print(results)
        # Save the final vote count to the text file.
        txt_file.write(results)

        if (votes > winning_count) and (vote_percentage > winning_percentage):
            # If true then set winning_count = votes and winning_percent = vote_percentage.
            winning_count = votes
            winning_percentage = vote_percentage
            # And, set the winning_candidate equal to the candidate's name.
            winning_candidate = candidate

    winning_candidate_summary = (
        f"\n"
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)

    # Save the winning candidate's results to the text file.
    txt_file.write(winning_candidate_summary)



