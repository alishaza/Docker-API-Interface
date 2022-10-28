from sys import stdout
import paramiko


def ssh(command):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

   
    ssh.connect(hostname='10.0.0.1', port=22,username='USERNAME', password='PASSWORD!')
    print('the commnd is executing ....')

    ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command(command=command)
    output=ssh_stdout.readlines()
    ssh.close()
    return output


