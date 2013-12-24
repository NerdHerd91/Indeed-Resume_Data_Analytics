import json

if __name__ == "__main__":
	resume_file = open('resumes-json.txt', 'r')
	content = resume_file.read()
	resume_data = ''
	if content:
		resume_data = json.loads(content)
	resume_file.close()

	for x in range(0,3):
		print resume[data]
