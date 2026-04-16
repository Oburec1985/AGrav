import paramiko
import sys

def verify_hybrid(host, user, password):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh.connect(host, username=user, password=password, timeout=10)
        
        # Check both tpws and nfqws
        stdin, stdout, stderr = ssh.exec_command('ps | grep -E "tpws|nfqws" | grep -v grep')
        processes = stdout.read().decode().strip()
        
        if "tpws" in processes and "nfqws" in processes:
            print("SUCCESS: Both TPWS and NFQWS are running!")
        else:
            print("WARNING: One or more processes are missing.")
        print(f"Current processes:\n{processes}")
        
        # Check firewall rules for redirection
        stdin, stdout, stderr = ssh.exec_command('nft list chain inet fw4 zapret_prerouting')
        print(f"Firewall (Redirect):\n{stdout.read().decode().strip()}")
        
        ssh.close()
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    verify_hybrid("192.168.2.2", "root", "mewpas7835")
