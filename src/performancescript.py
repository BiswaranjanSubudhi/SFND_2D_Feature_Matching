import subprocess
import os

os.chdir("../build")
detector_list = ['SHITOMASI','HARRIS', 'FAST', 'BRISK', 'ORB', 'AKAZE', 'SIFT']
descriptor_list = ['BRISK','BRIEF', 'ORB', 'FREAK', 'AKAZE', 'SIFT']

performance_result = []
count = 1

print("----Execution in process---")
for detector in detector_list:
    for descriptor in descriptor_list:
        state,output_string = subprocess.getstatusoutput(f"./2D_feature_tracking {detector} {descriptor}")
        performance_result.append(str(count) + ":" + output_string + "\n")
        count+=1

results = "\n".join(performance_result)

with open("performance.txt","w") as f:
    f.write(results)

print("----Execution completed---")