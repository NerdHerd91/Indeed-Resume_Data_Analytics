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
		
		for resume in resumes:
			print resume.f_name + " " + resume.l_name
			for edu in resume.education:
				print "Year: " + str(edu.year)
			print
