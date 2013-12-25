import matplotlib.pyplot as plt
import numpy as np

from extraction import Extraction

class Analysis:
	
	def __init__(self, name):
		self.name = name

	def run(self):
		#print "We are Running: " + self.name
		#x = np.array(range(20))
		#y = 3 + 0.5 * x + np.random.randn(20)
		#plt.plot(x,y, 'bo')
		#plt.show()
		
		resume_extract = Extraction("resumes-json.json")

		resumes = resume_extract.get_resumes()
		count = 0
		for resume in resumes:
			print resume.name + str(count)
			count += 1
