import matplotlib.pyplot as plt
import numpy as np

from extraction import Extraction

class Analysis:
	
	def __init__(self, file_path):
		self.file_path = file_path

	def __build_degree_map(self, resumes, major):
		degree_map = {}
		for resume in resumes:
			for edu in resume.education:
				if major in edu.major.lower() and edu.year:
					try:	
						degree_map[edu.year] += 1
					except Exception as e:
						degree_map[edu.year] = 1
		return degree_map

	def __plot_degree_data(self, degree_map):
		x = np.empty(len(degree_map.keys()))
		y = np.empty(len(degree_map.keys()))
		max_y = count = 0
		for key in degree_map.keys():
			x[count] = key
			y[count] = degree_map[key]
			max_y = max(max_y, degree_map[key])
			count += 1
		
		#Linear Regression
		fit = np.polyfit(x,y,1)
		fit_fn = np.poly1d(fit)
		
		plt.plot(x,y, 'bo', x, fit_fn(x), '--k')
		plt.ylim(0, max_y + 1)
		plt.title("Computer Degrees")
		plt.xlabel("Year")
		plt.ylabel("Number of Degrees")
		plt.show()

	def run(self):
		resume_extract = Extraction(self.file_path)
		resumes = resume_extract.get_resumes()
	
		degree_map = self.__build_degree_map(resumes, "computer")
		self.__plot_degree_data(degree_map)
