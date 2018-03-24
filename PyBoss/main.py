import os
import csv
from datetime import datetime

us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}
file="employee_data2.csv"


new_format=[]

with open(file) as csvfile:
  reader = csv.DictReader(csvfile)
  for row in reader:
    emp_id = row["Emp ID"]
    name_full = row["Name"]
    first_name = []
    last_name = []
    dob = row["DOB"]
    ssn = row["SSN"]
    state = row["State"]
    
    name_full = name_full.split()
    first_name.append(name_full[0])
    first_name = ''.join(first_name)
    last_name.append(name_full[1])
    last_name = ''.join(last_name)
    
    middate = datetime.strptime(dob, '%Y-%m-%d')
    dob = datetime.strftime(middate, '%m/%d/%Y')
    
    ssn = ssn.split('-')
    ssn = f'XXX-XX-{ssn[2]}'
    
    state_abbrev = us_state_abbrev[state]
               
    new_format.append(
      {
        "Emp ID": row["Emp ID"],
        "First Name": first_name,
        "Last Name": last_name,
        "DOB": dob,
        "SSN": ssn,
        "State": state_abbrev
      }
    )



with open("HR_Format.csv","w",newline="") as csvfile:
  field_names = ["Emp ID", "First Name", "Last Name", "DOB", "SSN", "State"]
  writer=csv.DictWriter(csvfile, fieldnames=field_names)
  writer.writeheader()
  writer.writerows(new_format)
