# Election_Analysis

## Project Overview
A Colorado Board of Elections employee has given you the following tasks to complete the election audit of a recent local congressional election.

1. Calculate the total number of votes cast.
2. Get a complete list of candidates who received votes.
3. Calculate the total number of votes each candidate received.
4. Calculate the percentage of votes each candidate won.
5. Determine the winner of the election based on popular vote

## Resources
- Data Source: election_results.csv
- Software: Python 3.6.1, Visual Studio Code, 1.38.1

## Summary
The analysis of the election show that:
- There were **369,711** votes cast in the election.
- The candidates were:
    - Charles Casper Stockham
    - Diana DeGette
    - Raymon Anthony Doane
- The candidate results were:
    - Charles Casper Stockham received "23.0%" of the vote and "85,213" number of votes.
    - Diana DeGette received "73.8%" of the vote and "272,892" number of votes.
    - Raymon Anthony Doane received "3.1%" of the vote and "11,606" number of votes.
- The winner of the election was:
    - Diana DeGette who received "73.8%" of the vote and "272,892" number of votes.
   
# Election Analysis Challenge
## Overview
The overview of this challenge is to write algorithms using Python that will assist the confirmation and analysis of election results.

### Purpose
The purpose of this challenge is to audit the election results and accomplish the additional data requested by the election commission.
    -The voter turnout for each county
    -The percentage of votes from each county out of the total count
    -The county with the highest turnout
The starter code to perform this audit is 

    # Add our dependencies.
    import csv
    import os

    # Add a variable to load a file from a path.
    file_to_load = os.path.join("Resources", "election_results.csv")
    # Add a variable to save the file to a path.
    file_to_save = os.path.join("analysis", "election_analysis.txt")

    # Initialize a total vote counter.
    total_votes = 0

    # Candidate Options and candidate votes.
    candidate_options = []
    candidate_votes = {}

    # 1: Create a county list and county votes dictionary.



    # Track the winning candidate, vote count and percentage
    winning_candidate = ""
    winning_count = 0
    winning_percentage = 0

    # 2: Track the largest county and county voter turnout.



    # Read the csv and convert it into a list of dictionaries
    with open(file_to_load) as election_data:
        reader = csv.reader(election_data)

        # Read the header
        header = next(reader)

        # For each row in the CSV file.
        for row in reader:

            # Add to the total vote count
            total_votes = total_votes + 1

            # Get the candidate name from each row.
            candidate_name = row[2]

            # 3: Extract the county name from each row.


            # If the candidate does not match any existing candidate add it to
            # the candidate list
            if candidate_name not in candidate_options:

                # Add the candidate name to the candidate list.
                candidate_options.append(candidate_name)

                # And begin tracking that candidate's voter count.
                candidate_votes[candidate_name] = 0

            # Add a vote to that candidate's count
            candidate_votes[candidate_name] += 1

            # 4a: Write an if statement that checks that the
            # county does not match any existing county in the county list.


                # 4b: Add the existing county to the list of counties.


                # 4c: Begin tracking the county's vote count.


            # 5: Add a vote to that county's vote count.



    # Save the results to our text file.
    with open(file_to_save, "w") as txt_file:

        # Print the final vote count (to terminal)
        election_results = (
            f"\nElection Results\n"
            f"-------------------------\n"
            f"Total Votes: {total_votes:,}\n"
            f"-------------------------\n\n"
            f"County Votes:\n")
        print(election_results, end="")

        txt_file.write(election_results)

        # 6a: Write a for loop to get the county from the county dictionary.

            # 6b: Retrieve the county vote count.

            # 6c: Calculate the percentage of votes for the county.


             # 6d: Print the county results to the terminal.

             # 6e: Save the county votes to a text file.

             # 6f: Write an if statement to determine the winning county and get its vote count.


        # 7: Print the county with the largest turnout to the terminal.


        # 8: Save the county with the largest turnout to a text file.


        # Save the final candidate vote count to the text file.
        for candidate_name in candidate_votes:

            # Retrieve vote count and percentage
            votes = candidate_votes.get(candidate_name)
            vote_percentage = float(votes) / float(total_votes) * 100
            candidate_results = (
                f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

            # Print each candidate's voter count and percentage to the
            # terminal.
            print(candidate_results)
            #  Save the candidate results to our text file.
            txt_file.write(candidate_results)

            # Determine winning vote count, winning percentage, and candidate.
            if (votes > winning_count) and (vote_percentage > winning_percentage):
                winning_count = votes
                winning_candidate = candidate_name
                winning_percentage = vote_percentage

        # Print the winning candidate (to terminal)
        winning_candidate_summary = (
            f"-------------------------\n"
            f"Winner: {winning_candidate}\n"
            f"Winning Vote Count: {winning_count:,}\n"
            f"Winning Percentage: {winning_percentage:.1f}%\n"
            f"-------------------------\n")
        print(winning_candidate_summary)

        # Save the winning candidate's name to the text file
        txt_file.write(winning_candidate_summary)

The command line output of the given starter code is

![st_out](https://user-images.githubusercontent.com/95719819/150657479-b319b52b-a77f-46d8-97fd-3b3af6b3bfc4.png)



## Election-Audit
With the given starter code
    - We have created a list **county_list** to hold the name of the counties.
    - we have also created a dictionary **county_votes** to hold the county as the key and the votes cast for each county as the values.
    - We have initialized an empty string **largest_county** to hold the county name for the county with the largest turnout.
    - We also initialized two variables **largest_county_votes** and **largest_county_percentage** to zero, that will hold the number of votes of the county that had the largest turnout.
    - Using **for** loop the election results are read to get the county name in **county_name**.
    - Using **if** statement with the logical operator **not in** the **county_name** is verified with the **county_list** and it is appended to the list if its not in the list. 
    - The **county_votes** is initialized to zero to begin the vote counts for the county.
    - The **county_votes** adds a vote to the county's vote count as we loop through all the rows.
    - Again using for loop with **county_name** from the dictionary **county_votes**, we calculate **county_total_votes**, **county_percentage**.
    - The **county_results** is printed in the command line and with the **txt_file.write()** method the results are save to the text file.
    - Using the **if** statement and the logical operator **and** **county_total_votes** and **county_percentage** are compared with the **largest_county_votes** and **largest_county_percentage** respectively to get the largest county turnout.
    - The **largest_county_results** are printed and with the **txt_file.write()** method the results are save to the text file.


    # -*- coding: UTF-8 -*-
    """PyPoll Homework Challenge Solution."""

    # Add our dependencies.
    import csv
    import os

    # Add a variable to load a file from a path.
    file_to_load = os.path.join("Resources", "election_results.csv")
    # Add a variable to save the file to a path.
    file_to_save = os.path.join("analysis", "election_analysis.txt")

    # Initialize a total vote counter.
    total_votes = 0

    # Candidate Options and candidate votes.
    candidate_options = []
    candidate_votes = {}

    # 1: Create a county list and county votes dictionary.
    county_list = []
    county_votes={}


    # Track the winning candidate, vote count and percentage
    winning_candidate = ""
    winning_count = 0
    winning_percentage = 0

    # 2: Track the largest county and county voter turnout.
    largest_county = ""
    largest_county_votes = 0
    largest_county_percentage = 0


    # Read the csv and convert it into a list of dictionaries
    with open(file_to_load) as election_data:
        reader = csv.reader(election_data)

        # Read the header
        header = next(reader)

        # For each row in the CSV file.
        for row in reader:

            # Add to the total vote count
            total_votes = total_votes + 1

            # Get the candidate name from each row.
            candidate_name = row[2]

            # 3: Extract the county name from each row.
            county_name = row[1]

            # If the candidate does not match any existing candidate add it to
            # the candidate list
            if candidate_name not in candidate_options:

                # Add the candidate name to the candidate list.
                candidate_options.append(candidate_name)

                # And begin tracking that candidate's voter count.
                candidate_votes[candidate_name] = 0

            # Add a vote to that candidate's count
            candidate_votes[candidate_name] += 1

            # 4a: Write an if statement that checks that the
            # county does not match any existing county in the county list.
            if county_name not in county_list:

                # 4b: Add the existing county to the list of counties.
                county_list.append(county_name)

                # 4c: Begin tracking the county's vote count.
                county_votes[county_name] = 0

            # 5: Add a vote to that county's vote count.
            county_votes[county_name] +=1


    # Save the results to our text file.
    with open(file_to_save, "w") as txt_file:

        # Print the final vote count (to terminal)
        election_results = (
            f"\nElection Results\n"
            f"-------------------------\n"
            f"Total Votes: {total_votes:,}\n"
            f"-------------------------\n\n"
            f"County Votes:\n")
        print(election_results, end="")

        txt_file.write(election_results)

        # 6a: Write a for loop to get the county from the county dictionary.
        for county_name in county_votes:

            # 6b: Retrieve the county vote count.
            county_total_votes = county_votes.get(county_name)
            # 6c: Calculate the percentage of votes for the county.
            county_percentage = float(county_total_votes)/float(total_votes) * 100
            county_results = f"{county_name}:{county_percentage: .1f}% ({county_total_votes:,})\n"

            # 6d: Print the county results to the terminal.
            print(county_results, end="")

            # 6e: Save the county votes to a text file.
            txt_file.write(county_results)
            # 6f: Write an if statement to determine the winning county and get its vote count.
            if (county_total_votes > largest_county_votes) and (county_percentage > largest_county_percentage):
                largest_county_votes = county_total_votes
                largest_county = county_name
                largest_county_percentage = county_percentage

        # 7: Print the county with the largest turnout to the terminal.
        largest_county_results =(f"\n-------------------------\n"
        f"Largest County Turnout : {largest_county}\n"
        f"-------------------------\n")
        print(largest_county_results, end="")

        # 8: Save the county with the largest turnout to a text file.
        txt_file.write(largest_county_results)

        # Save the final candidate vote count to the text file.
        for candidate_name in candidate_votes:

            # Retrieve vote count and percentage
            votes = candidate_votes.get(candidate_name)
            vote_percentage = float(votes) / float(total_votes) * 100
            candidate_results = (
                f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})")

            # Print each candidate's voter count and percentage to the
            # terminal.
            print(candidate_results)
            #  Save the candidate results to our text file.
            txt_file.write(candidate_results)

            # Determine winning vote count, winning percentage, and candidate.
            if (votes > winning_count) and (vote_percentage > winning_percentage):
                winning_count = votes
                winning_candidate = candidate_name
                winning_percentage = vote_percentage

        # Print the winning candidate (to terminal)
        winning_candidate_summary = (
            f"-------------------------\n"
            f"Winner: {winning_candidate}\n"
            f"Winning Vote Count: {winning_count:,}\n"
            f"Winning Percentage: {winning_percentage:.1f}%\n"
            f"-------------------------\n")
        print(winning_candidate_summary)

        # Save the winning candidate's name to the text file
        txt_file.write(winning_candidate_summary)


The command line output of the above code is

![ch_out](https://user-images.githubusercontent.com/95719819/150657429-4544b683-b545-475e-82c3-b902a59165f1.png)

# Election-Audit Results
The analysis of the election show that:
- There were **369,711** votes cast in the election.
- The counties were:
    - Jefferson
    - Denver
    - arapahoe
- The county results were:
    - Jefferson county received "10.5%" of the vote and "38,855" number of votes.
    - Denver county received "82.8%" of the vote and "306,055" number of votes.
    - Arapahoe county received "6.7%" of the vote and "24,801" number of votes.
- The largest county turn out was
    - Denver county received "82.8%" of the vote and "306,055" number of votes.
- The candidates were:
    - Charles Casper Stockham
    - Diana DeGette
    - Raymon Anthony Doane
- The candidate results were:
    - Charles Casper Stockham received "23.0%" of the vote and "85,213" number of votes.
    - Diana DeGette received "73.8%" of the vote and "272,892" number of votes.
    - Raymon Anthony Doane received "3.1%" of the vote and "11,606" number of votes.
- The winner of the election was:
    - Diana DeGette who received "73.8%" of the vote and "272,892" number of votes.
# Election Audit Summary
We summarize this challenge with the business proposal to the election comission
    - To get the vote count of the candidates from each county.
    - To get the county name of the winning candidate.
