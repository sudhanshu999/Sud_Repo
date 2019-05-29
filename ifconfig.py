import paramiko
import sys

ssh=paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

ssh.connect('10.193.114.29',username='root',password='root')

ssh_stdin,ssh_stdout,ssh_stderr=ssh.exec_command("ifconfig")

s=ssh_stdout.readlines()

for i in s:
	l=i.strip("")
	if "10.193.114.29" in l:
		
		print ("found")
		print ("The ip found is:{}".format(i))
		print (l.split(" ")[11].split(":")[1])
		print (l.split(" ")[13])
		print (l.split(" ")[15])
		
