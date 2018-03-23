print("start")

bashCommand = "ls -ls /"
import subprocess
process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
output, error = process.communicate()

print(type(output))
print(type(error))
print("output: " + str(output))
print("error:" + str(error))