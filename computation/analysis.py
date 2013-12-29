import matplotlib.pyplot as plt
import numpy as np

from extraction import Extraction

class Analysis:
	
	def __init__(self):
		pass

	def run(self):
		#x = np.array(range(20))
		#y = 3 + 0.5 * x + np.random.randn(20)
		#plt.plot(x,y, 'bo')
		#plt.show()
		
		resume_extract = Extraction("resumes-json.json")
		resumes = resume_extract.get_resumes()
	
		software_map = {}
		for resume in resumes:
			for edu in resume.education:
				if "computer" in edu.major.lower() and edu.year:
					try:	
						software_map[edu.year] += 1
					except Exception as e:
						software_map[edu.year] = 1
		x = np.empty(shape=(len(software_map.keys()), 1))
		y = np.empty(shape=(len(software_map.keys()), 1))
		count = 0
		for key in software_map.keys():
			x[count] = key
			y[count] = software_map[key]
			count += 1
		plt.plot(x,y, 'bo')
		plt.show()
