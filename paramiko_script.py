from connection_detail import HOST, PORT, USER_NAME, PASSWORD, LOCAL_FILE_PATH, REMOTE_FILE_PATH, OIL_PATH_REMOTE

import paramiko

# PHP command to execute
php_command = f'php {OIL_PATH_REMOTE} import {REMOTE_FILE_PATH}'

# Create SSH client
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# Connect to remote server
ssh.connect(hostname=HOST, port=PORT, username=USER_NAME, password=PASSWORD)

# Open SFTP client for file transfer
sftp = ssh.open_sftp()

# Upload file
sftp.put(LOCAL_FILE_PATH, REMOTE_FILE_PATH)

# Close SFTP client
sftp.close()

# Execute PHP command
stdin, stdout, stderr = ssh.exec_command(php_command)

# Print output and errors
print(stdout.read().decode())
print(stderr.read().decode())

# Close SSH client
ssh.close()
