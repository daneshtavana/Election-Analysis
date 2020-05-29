# ******** Lists  ********
#print("Hello World ")
#print(type(73.18))
#print(type("Hello World"))
#print("Hello World ")
#help("keywords")
#counties = ["Arapahoe","Denver","Jefferson"]
#print(counties)
#print(len(counties))
#print(counties[0:2], counties[:2], counties[1:3],counties[1:])
#print(counties)
#counties.remove("El Paso")
#print(counties)
#counties.pop(3)
#print(counties)
#counties.insert(1, "El Paso")
#counties.remove("Arapahoe")
#counties[2] = "Denver"
#counties[1] = "Jefferson"
#counties.insert(3,"Arapahoe")
#print(counties)
#
# ******** Tuples ********
#counties_tuple = ("Arapahoe","Denver","Jefferson")
#print(counties_tuple)
#print(len(counties_tuple))
#print(counties_tuple[:2])
#
# ******** Dictionary ********
#counties_dict = {}
#counties_dict["Arapahoe"] = 42282
#counties_dict["Denver"] = 463353
#counties_dict["Jefferson"] = 432438
#print(counties_dict)
#print(len(counties_dict))
#print(counties_dict.items())
#print(counties_dict.keys())
#print(counties_dict.values())
#print(counties_dict.get("Denver"))
#print(counties_dict['Denver'])
#
# ******** List of Dictionaries *******
#voting_data = []
#voting_data.append({"county":"Arapahoe", "registered_voters": 422829})
#voting_data.append({"county":"Denver", "registered_voters": 463353})
#voting_data.append({"county":"Jefferson", "registered_voters": 432438})
#print(voting_data)
#print(len(voting_data))
#voting_data.insert(1, {"county":"El Paso", "registered_voters": 461149})
#print(voting_data)
#
# ******** Decision Statement *******
#my_votes = int(input("How many votes did you get in the election? "))
#total_votes = int(input("What is the total votes in the election? "))
#percentage_votes = (my_votes / total_votes) * 100
#print("I received " + str(percentage_votes)+"% of the total votes.")
#counties = ["Arapahoe","Denver","Jefferson"]
#if counties[3] != 'Jefferson':
#    print(counties[2])
# What is the score?
#score = int(input("What is your test score? "))
# Determine the grade.
#if score >= 90:
#    print('Your grade is an A.')
#elif score >= 80:
#    print('Your grade is a B.')
#elif score >= 70:
#    print('Your grade is a C.')
#elif score >= 60:
#    print('Your grade is a D.')
#else:
#    print('Your grade is an F.')
#
#counties = ["Arapahoe","Denver","Jefferson"]
#if "El Paso" in counties:
#    print("El Paso is in the list of counties.")
#else:
#    print("El Paso is not the list of counties.")
#    
#if "Arapahoe" in counties and "El Paso" in counties:
#    print("Arapahoe and El Paso are in the list of counties.")
#else:
#    print("Arapahoe or El Paso is not in the list of counties.")
#
#if "Arapahoe" in counties and "El Paso" not in counties:
#   print("Only Arapahoe is in the list of counties.")
#else:
#    print("Arapahoe is in the list of counties and El Paso is not in the list of counties.")
#
#count = 7
#while count < 1:
#    print("Hello World")
#
#for county in counties:
#    print(county)
#
#for i in range(len(counties)):
#    print(counties[i])
#
counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
#for county in counties_dict:
#    print(county)
#
#for county in counties_dict.keys():
#    print(county) 
# 
#for county in counties_dict:
#    print(counties_dict[county])
#
#for voters in counties_dict.values():
#    print(voters)
#
#for county in counties_dict:
#    print(counties_dict.get(county))
#
#for county, voters in counties_dict.items():
#    print(str(county) + " County has", str(voters) + " registered voters.")
#
voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]
#for county_dict in voting_data:
#    print(county_dict)
#
#for i in range(len(voting_data)):
#    print(voting_data[i])
#
#for county_dict in voting_data:
#    for value in county_dict.values():
#        print(value)
#for county_dict in voting_data:
#    print(county_dict['registered_voters'])
#for county_dict in voting_data:
#    print(county_dict['county'])
#
# ******** Format *******
#my_votes = int(input("How many votes did you get in the election? "))
#total_votes = int(input("What is the total votes in the election? "))
#print(f"I received {my_votes / total_votes * 100}% of the total votes.")
#
#counties_dict = {"Arapahoe": 369237, "Denver":413229, "Jefferson": 390222}
#for county, voters in counties_dict.items():
#    print(county + " county has " + str(voters) + " registered voters.")
#
#for county, voters in counties_dict.items():
#    print(f"{county} county has {voters:,d} registered voters.")
#
# Create a filename variable to a direct or indirect path to the file.
import os
file_to_save = os.path.join("Analysis", "election_analysis.txt")
# Using the with statement open the file as a text file.
with open(file_to_save, "w") as txt_file:

    # Write some data to the file.
    txt_file.write("Hello World\n")
    # Write three counties to the file.
    txt_file.write("Arapahoe\nDenver\nJefferson")
