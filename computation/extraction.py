import json
import errno

from resume import Resume

class Extraction:
	
	def __init__(self, file_path):
		self._file_path = file_path
		self._resume_json = self.__extract_resumes()
		self._resumes = self.__parse_resumes()

	def __extract_resumes(self):
		resume_json = None
		try:
			resume_file = open(self._file_path, 'r')
			content = resume_file.read()
			if content:
				resume_json = json.loads(content)
			resume_file.close()
		except IOError as e:
			print "I/O error({0}): {1}".format(e.errno, e.strerror)
			raise
		return resume_json

	def __parse_resumes(self):
		resumes = []
		for res in self._resume_json["resumes"]:
			resume = self.__parse_resume(res)
			resumes.append(resume)
		return resumes

	def __parse_resume(self, resume_data):
		resume = Resume()
		resume.name = "Sean Ventrella"
		return resume

	def get_resumes(self):
		return self._resumes
