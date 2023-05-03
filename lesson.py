# subprocess
import os
import subprocess

# os.system('ls')
# subprocess.run(['ls', '-al'])
# subprocess.run('ls -al | grep test', shell=True, check=True)

p1 = subprocess.Popen(['ls', '-al'], stdout=subprocess.PIPE)
p2 = subprocess.Popen(['grep', 'test'], stdin=p1.stdout, stdout=subprocess.PIPE)
p1.stdout.close()
output = p2.communicate()[0]
print(output)
