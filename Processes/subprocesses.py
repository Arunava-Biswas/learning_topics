# Importing the module
import subprocess

# Here we are going to learn how to call external commands using python with the sub process module.
# 1st we need to import the sub process module.
# Now to run an external command we just need to say subprocess.run('command name')

# Now running a command
try:
    subprocess.run('dir')       # This will throw an error
except Exception as err:
    print(err)

'''
Here we will find an error: 
FileNotFoundError: [WinError 2] The system cannot find the file specified
It is because the command 'dir' is built into the shell, so we need to pass in an argument that 'shell=True'.
With the argument 'shell=True' we can pass an entire command as a string. So we can pass more arguments along with the command.
But it has a security hazard with untrusted inputs.
'''

print("\n")
subprocess.run('dir', shell=True)   # This will return the correct result
print("\n")
# subprocess.run('dir Get-Acl', shell=True)   # This will return the correct result

'''
Volume in drive F is New Volume
 Volume Serial Number is 18B3-E82C

 Directory of F:\Pycharm_python\learning_topics\Processes

01-Sep-22  06:22 AM    <DIR>          .
01-Sep-22  06:22 AM    <DIR>          ..
01-Sep-22  06:22 AM               495 subprocesses.py
01-Sep-22  06:17 AM               234 subprocesses.txt
               2 File(s)            729 bytes
               2 Dir(s)  64,491,442,176 bytes free

Process finished with exit code 0
'''


'''
- Now let's catch the result inside a variable and try to print it.
- But if we just take the output inside a variable then it will not work as the standard out will still get printed on the screen.
- And if we try to print the variable it will return as an object
CompletedProcess(args='dir', returncode=0)
- To capture the output inside a variable we need to pass another argument 'capture_output=True'
- To see the newlines as strings:
we can use the 'decode()'
or we can pass an argument in the run method 'text=True'
- With the 'capture_output' argument the standard output and standard error are sent to the sub process pipe which allows the values to get captured.
- We can also write the argument as 'stdout=subprocess.PIPE'. This will also do the same as 'capture_output=True'
'''
print("\n")
p1 = subprocess.run('dir', shell=True)
print("\n")
print(p1)                # It will return an object
print(p1.args)           # This will show the arguments we passed in the command as here it is 'dir'
print(p1.returncode)     # This will return the returncode
print(p1.stdout)         # This will return 'None' as all the output is directed to the console
print("\n")
p2 = subprocess.run('dir', shell=True, capture_output=True)
print(p2)                # Now we can see the result in the variables
print("\n")
print(p2.stdout)         # This will show the newline in bytes
print("\n")
print(p2.stdout.decode())   # Now we can see the output like we want
print("\n")
p3 = subprocess.run('dir', shell=True, capture_output=True, text=True)
print(p3.stdout)        # printing the output in our way without using decode()
print("\n")
p4 = subprocess.run('dir', shell=True, stdout=subprocess.PIPE, text=True)
print(p4.stdout)

'''
- We can also direct the standard out to a desired location like in a file which can be used for login or anything like that.
- So instead of the 'subprocess.PIPE' we need to provide the file name there.
'''
'''
print("\n")
with open('output.txt', 'w') as f:
    p5 = subprocess.run('dir', shell=True, stdout=f, text=True)
'''

'''
- Let's see what will happen if the command is not successful?
- In python it returns a Non zero code instead of the exception.
- So we can use the returncode as a condition also like 
if p.returncode != 0
    pass
else:
    pass

- To get an exception in case of external command we need to pass another argument 'check=True'
- Another thing to do with the errors is that to ignore them by redirecting them to dev null. Here again we will do like we did for the 'subprocess.PIPE' but here instead of 'stdout' we will use 'stderr' and it will redirected to 'subprocess.DEVNULL'.
'''
print("\n")
p6 = subprocess.run(['dir', 'dne'], shell=True, capture_output=True, text=True)
print(p6.returncode)                # Here it will return a code 1
print(p6.stderr)                    # To see the error. Here it is "file not found"
print("\n")

# p7 = subprocess.run(['dir', 'dne'], shell=True, capture_output=True, text=True, check=True)
# print(p7.stderr)

# Traceback (most recent call last):
# File "F:\Pycharm_python\learning_topics\Processes\subprocesses.py", line 99, in <module>
# p7 = subprocess.run(['dir', 'dne'], shell=True, capture_output=True, text=True, check=True)
# File "C:\Users\Arunava\anaconda3\envs\learning_topics\lib\subprocess.py", line 528, in run
# raise CalledProcessError(retcode, process.args,
# subprocess.CalledProcessError: Command '['dir', 'dne']' returned non-zero exit status 1.

p8 = subprocess.run(['dir', 'dne'], shell=True, stderr=subprocess.DEVNULL)
print(p8.stderr)        # Here it will return "None"
print("\n")

'''
- Now if we want to take the output from one command and use it as input for another.
- Here we will concatenate the 'test.txt', because we are in windows so we will use 'type' instead of the 'cat' command.
- Now we will use the output as input and use 'findstr' as an alternative to the 'grep' command in linux, which is widely used for parsing files and searching for useful data in the outputs of different commands.
- We need to pass another argument 'input=p8.stdout' where we will provide the input as here it is the output of the p8.
'''

p8 = subprocess.run(['type', 'test.txt'], shell=True, capture_output=True, text=True)
print(p8.stdout)
print("\n")

# Now using the output as an input
p9 = subprocess.run(['findstr', '-n', 'test'], shell=True, capture_output=True, text=True, input=p8.stdout)
print(p9.stdout)

# Here we will find the line number '-n' along with the string we are searching
