import paramiko
import sys

def run_ssh_command(host, port, username, password, command):
    try:
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(host, port=port, username=username, password=password, timeout=10)
        stdin, stdout, stderr = client.exec_command(command)
        output = stdout.read().decode('utf-8')
        error = stderr.read().decode('utf-8')
        client.close()
        return output, error
    except Exception as e:
        return "", str(e)

def write_remote_file(host, port, username, password, remote_path, content):
    try:
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(host, port=port, username=username, password=password, timeout=10)
        
        # Use cat to write to remote file
        stdin, stdout, stderr = client.exec_command(f"cat > {remote_path}")
        stdin.write(content)
        stdin.flush()
        stdin.close()
        
        err = stderr.read().decode('utf-8')
        client.close()
        return True, err
    except Exception as e:
        return False, str(e)

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python ssh_command.py [cmd|write] ...")
        sys.exit(1)
        
    mode = sys.argv[1]
    host = "192.168.3.1"
    user = "root"
    pas = "mewpas7835"
    
    if mode == "cmd":
        cmd = sys.argv[2]
        out, err = run_ssh_command(host, 22, user, pas, cmd)
        if out: print(out)
        if err: print("ERROR:", err, file=sys.stderr)
    elif mode == "write":
        local_file = sys.argv[2]
        remote_path = sys.argv[3]
        with open(local_file, "r") as f:
            content = f.read()
        success, err = write_remote_file(host, 22, user, pas, remote_path, content)
        if success:
            print(f"Written to {remote_path}")
        else:
            print("ERROR:", err, file=sys.stderr)
