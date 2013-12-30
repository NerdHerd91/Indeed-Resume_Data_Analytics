import matplotlib.pyplot as plt
import numpy as np

from extraction import Extraction

class Analysis:
	
	def __init__(self, file_path):
		self.file_path = file_path

	def run(self):
		# Get the resume data
		resume_extract = Extraction(self.file_path)
		resumes = resume_extract.get_resumes()
	
		# Create the map from years to counts for software_major
		software_map = {}
		for resume in resumes:
			for edu in resume.education:
				if "computer" in edu.major.lower() and edu.year:
					try:	
						software_map[edu.year] += 1
					except Exception as e:
						software_map[edu.year] = 1
		
		# Plot the data in numpy arrays				
		x = np.empty(len(software_map.keys()))
		y = np.empty(len(software_map.keys()))
		count = 0
		for key in software_map.keys():
			x[count] = key
			y[count] = software_map[key]
			count += 1
		plt.plot(x,y, 'bo')
		plt.show()
