import json
from math import radians, cos,sin,acos
import pandas as pd

with open("Customers.txt") as file_input:
    data = file_input.read()

def distance(slat, slon, elat, elon):
    dist = R * acos(sin(slat) * sin(elat) + cos(slat) * cos(elat) * cos(slon - elon))
    # other way to calcute distance but right now we not using this
    # a = sin(dlat / 2) ** 2 + cos(lat1) * cos(rad_lat) * sin(dlon / 2) ** 2
    # c = 2 * atan2(sqrt(a), sqrt(1 - a))
    # distance = R * c
    return dist

context = data.split('\n')
print(context[1])
data_invite = {str(i): json.loads(context[i]) for i in range(len(context))}
print(type(float(data_invite["0"]['latitude'])))

R = 6373.0 # radius of earth

print("Input location on Dublin")
# if you want dynamic input
# lat = input("latitude: ")
# longi = input("longitude: ")
lat = 53.339428  #Dublin
longi = -6.257664 #Dublin
rad_lat = radians(lat)
rad_longi = radians(longi)
invitation = []
for i in range(len(data_invite)):
    dist = distance(rad_lat, rad_longi, radians(float(data_invite["%s"%i]["latitude"])),
                    radians(float(data_invite["%s"%i]["longitude"])))
    if dist <= 100:
        invitation.append([data_invite["%s"%i]["user_id"], data_invite["%s"%i]["name"], dist])

n = len(invitation)
for i in range(n):
    min_val = i
    for j in range(i + 1, n):
        if invitation[min_val][0] > invitation[j][0]:
            min_val = j
    invitation[i], invitation[min_val] = invitation[min_val], invitation[i]

print(invitation)

file_json = json.dumps(data_invite)
with open("output.json","w") as read:
    read.write(file_json)

#just for preparing Excel sheet
user_id = []
name = []
place_dist = []
for k in range(len(invitation)):
    user_id.append(invitation[k][0])
    name.append(invitation[k][1])
    place_dist.append(invitation[k][2])

d = {'user_id': pd.Series(user_id),
     'name': pd.Series(name),
     'distance': pd.Series(place_dist)}

df = pd.DataFrame(d)
df.to_csv('file.csv')