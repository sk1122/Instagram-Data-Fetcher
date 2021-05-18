from instaloader import *
import pandas as pd
import json

L = Instaloader()

filename = 'api/data.json'

# df = pd.read_csv('../insta_profile.csv')

# ser = pd.Series(df['Instagram URL'])

# data = {}
# for i in ser:
# 	print(f'Started')
# 	jsonData = {}

# 	try:
# 		profile = Profile.from_username(L.context, i[26:-1])
# 		jsonData["followers"] = profile.followers
# 		jsonData["followees"] = profile.followees
# 		jsonData["full_name"] = profile.full_name
# 		jsonData["business_category"] = profile.business_category_name
# 		jsonData["bio"] = profile.biography
# 		data[profile.username] = jsonData

# 		print(f'{profile.username} Ended')
		
# 		with open(filename, 'w') as f:
# 			json.dump(data, f, indent=4)
# 	except instaloader.exceptions.ProfileNotExistsException:
# 		print("Error")
	

def getData():
	with open(filename, 'r') as f:
		data = json.loads(f.read())
		return data