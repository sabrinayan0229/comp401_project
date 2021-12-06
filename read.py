import pandas as pd
import numpy as np
import math


data_titles = ['NOSE_TIP', 'PH_BULB', 'NERVE_RING']

def calc_angle(da):
	x = []
	for s in data_titles:
		x.append(np.array([da[s]['x'], da[s]['y']]))
	x10 = x[0] - x[1]
	x12 = x[2] - x[1]

	cosine_angle = np.dot(x10, x12) / (np.linalg.norm(x10) * np.linalg.norm(x12))
	orientation = 1 if np.cross(x12, x10) >= 0 else -1
	angle = 180 - np.arccos(cosine_angle) * (180 / math.pi)
	angle = round(angle * orientation,2) 
	
	

	return angle



if __name__ == '__main__':
	import argparse

	parser = argparse.ArgumentParser()
	parser.add_argument('input', action='store', help='input file name')

	args = parser.parse_args()
	data = pd.read_csv(args.input, header=[1, 2])

	df = pd.DataFrame(data)
	data = list(zip(list(df[s]) for s in data_titles))

	clean_data = []
	for i in range(len(df[data_titles[0]])):
		d = {}
		for name in data_titles:
			d[name] = dict(df[name].T[i])
		good_data = True
		for name in data_titles:
			if d[name]['likelihood'] <= 0.90:
				good_data = False
		if good_data:
			clean_data.append(d)
	data = clean_data

	for d in data:
		d['angle']= calc_angle(d)

	df = pd.DataFrame(columns=['NOSE_TIP', 'PH_BULB', 'NERVE_RING','angle'])
	
	i = 1
	for d in data:
		new = {
			'NOSE_TIP': str([d['NOSE_TIP']['x'], d['NOSE_TIP']['y']]),
			'PH_BULB': str([d['PH_BULB']['x'], d['PH_BULB']['y']]),
			'NERVE_RING': str([d['NERVE_RING']['x'], d['NERVE_RING']['y']]),
			'angle': d['angle']
		}
		# print(new)
		df = df.append(new, ignore_index=True)
	
	df.to_csv('out.csv')
