import json
import errno

from resume import Resume

class Extraction:
	
	def __init__(self, file_path):
		self.file_path = file_path
		self.resume_json = self.extract_resumes()
		self.resumes = self.parse_resumes()

	def extract_resumes(self):
		resume_json = None
		try:
			resume_file = open(self.file_path, 'r')
			content = resume_file.read()
			if content:
				resume_json = json.loads(content)
			resume_file.close()
		except IOError as e:
			print "I/O error({0}): {1}".format(e.errno, e.strerror)
			raise
		return resume_json

	def parse_resumes(self):
		resumes = []
		print self.resume_json
		for res in self.resume_json["resumes"]:
			resume = self.parse_resume(res)
			resumes.append(resume)
		return resumes

	def parse_resume(self, resume_data):
		resume = Resume()
		resume.set_name("sean")
		return resume

	def get_resumes(self):
		return self.resumes
