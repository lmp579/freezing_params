import itertools
import subprocess

parameters = [x for x in itertools.combinations(['mc', 'q', 'a1', 'a2', 'tilt1', 'tilt2'], 2)]
for pair in parameters:
	subprocess.call(["python", "2dcdfs.py", "--param1", pair[0], "--param2", pair[1], "--basepath", "/projects/b1011/spinning_runs/freezingparams_20160402", "--errors", "bounded", "--confidence", "90"])
