# SSH Notes

## Create SSH Keys and Copy to Remote Hosts

Create a new key pair

	ssh-keygen -b 4096
	# save the key to: /home/USERNAME/.ssh/USERNAME_id_rsa
	# set passphrase

Add public key to remote hosts

	ssh-copy-id -i /home/USERNAME/.ssh/USERNAME_id_rsa remoteuser@remoteaddress
	# yes when prompted to trust the new host

If you get an error due to existing SSH configs interfering, such as `Permission denied (publickey,gssapi-keyex,gssapi-with-mic,password).`

	ssh-copy-id -i /home/USERNAME/.ssh/USERNAME_id_rsa -F none remoteuser@remoteaddress

Test connection

	ssh -i /home/USERNAME/.ssh/USERNAME_id_rsa remoteuser@remoteaddress

## SSH Config - Handle Multiple Keys or Destinations

Create the configuration at: `/home/USERNAME/.ssh/config`

SSH command **without** a config: `ssh -i /home/USERNAME/.ssh/USERNAME_id_rsa remoteuser@remoteaddress`

SSH command **with** a config: `ssh remoteaddress`

Settings
- `Host`: destination value, can be an alias
	- alias for `Hostname` when also specified
	- separate multiple values with a space
	- supports pattern matching:
		- asterisk (`*`) = 0 or more characters
		- question mark (`?`) = exactly 1 character
		- leading exclamation mark (`!`) = negate entire value
- `Hostname`: actual destination IP or hostname
- `Port`: destination port, if not 22
- `User`: remote username
- `IdentityFile`: private key for remote user
- `PreferredAuthentication`: specify preference for using keys or passwords first (this doesn't override server SSH settings)


### Example SSH Config Contents

**One config may contain multiple sections, such as all of the following at once**

Connect to internal networks using wildcards as the current user (no USER argument)

	Host 10.*.*.* 192.168.*.*
	IdentityFile ~/.ssh/USERNAME1_id_rsa
	PreferredAuthentication publickey

Match 172.16.0.0/12 using multiple Host values with wildcards; specify user and port

	Host 172.16.*.* 172.17.*.* 172.18.*.* 172.19.*.* 172.2?.*.* 172.30.*.* 172.31.*.*
	Port 2222
	User USERNAME2
	IdentityFile ~/.ssh/USERNAME2_id_rsa
	PreferredAuthentication publickey

Use a Host alias so the command `ssh appserver` will *actually* connect to `appserver.local:12345`

	Host appserver
	Hostname appserver.local
	Port 12345
	User USERNAME3
	IdentityFile ~/.ssh/USERNAME3_id_rsa
	PreferredAuthentication publickey

## SSH Agent

Start agent using `eval` to capture the agent's environment variables (notably the PID)

	eval "$(ssh-agent -s)"

Add a private key to the current agent session

	ssh-add /home/USERNAME/.ssh/USERNAME_id_rsa
	
Combo alias

	alias start-ssh='eval "$(ssh-agent -s)" && ssh-add /home/USERNAME/.ssh/USERNAME_id_rsa'
