import os
import csv


file="election_data_2.csv"
count=1
candidate_total={}
total_cand=0


with open(file) as csvfile:
  reader = csv.DictReader(csvfile)
  for row in reader:
    voter_id = row["Voter ID"]
    county = row["County"]
    candidate = row["Candidate"]

    if (candidate in candidate_total.keys()):
      candidate_total[candidate]=candidate_total[candidate]+1
      total_cand=total_cand+1
    else:
      candidate_total[candidate]=1
      total_cand=total_cand+1

print("Election Results")
print("-----------------------------")
print("Total Votes: " + str(total_cand))
print("-----------------------------")
for person in candidate_total:
  print(person + ": " + str(round(candidate_total[person]/total_cand*100,3)) + "% (" + str(candidate_total[person]) +")")
print("-----------------------------")
print("Winner: " + max(candidate_total))
print("-----------------------------")

f= open("election_results.txt","w")
f.write("Election Results\n")
f.write("-----------------------------\n")
f.write("Total Votes: " + str(total_cand) + "\n")
f.write("-----------------------------\n")
for person in candidate_total:
  f.write(person + ": " + str(round(candidate_total[person]/total_cand*100,3)) + "% (" + str(candidate_total[person]) +")\n")
f.write("-----------------------------\n")
f.write("Winner: " + max(candidate_total) + "\n")
f.write("-----------------------------")
