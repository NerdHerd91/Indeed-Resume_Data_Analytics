import sys
from computation.analysis import Analysis

try:
	file_path = sys.argv[1]
	a = Analysis(file_path)
	a.run()
except Exception as e:
	print "Invalid file_path was entered."
	print e
