import time
import paramiko

results = []


def ssh_con():

    time.sleep(300)
    client = paramiko.SSHClient()
    client.load_system_host_keys()
    client.connect('192.168.2.1', username='root', password='Pr0L1@nt')

    ssh_stdin, ssh_stdout, ssh_stderr = client.exec_command(
        'arp 192.168.2.5 -d')
    for i in range(2, 256):
        ssh_stdin, ssh_stdout, ssh_stderr = client.exec_command(
            f'arp 192.168.2.{i} -d')

    for line in ssh_stdout:
        results.append(line.strip('\n'))
    print(results)


while True:
    if __name__ == 'main':
        ssh_con()
