# Docker


## Build and Run Images with `docker compose`

	docker compose up
	docker compose up --build --force-recreate
	# CTRL+C to exit, or run detached (-d)
	docker compose up -d
	docker compose down


## Build with `docker build`

	docker build <context> -f <dockerfile> -t <tag>

	# same directory
	docker build . -f Dockerfile -t test-server
	# files below in a subdirectory
	docker build ./test-server/ -f ./test-server/Dockerfile -t test-server

	# if you include "helper" RUN commands, such as "ls <dir>"
	# add: --progess=plain


## Run with `docker run`

when using EXPOSE

	docker run -d --rm --name test-server \
	    --network host -p 5000:5000 \
	    test-server

host-only network; app runs on port 5000

	docker run -d --rm --name test-server \
	    --network host test-server


## Daemon Settings (`/etc/docker/daemon.json`)

must `systemctl restart docker` after updating `daemon.json`

	sudo vim /etc/docker/daemon.json
	# add the lines (note icc defaults to true)
	{
	    "dns": ["your-dns", "9.9.9.9", "1.1.1.1"],
	    "icc": true,
	    "ipv6": false
	}
	# notable mentions: userns-remap, ip, https-proxy, log-driver and log-opts


## Miscellaneous

interact with **running** container as user

	docker exec -it -u <user> <container-id|name> /bin/bash
	docker exec -it -u root 335fe840de5d /bin/bash
	docker exec -it -u root test-server /bin/bash

interact with **built but stopped** container as user

	docker ps -a
	docker run -it --rm --user <user> <container-id|name> /bin/bash

list, stop, remove containers

	docker ps -a
	docker inspect <container-id|name>
	docker stop <container-id|name>
	# among other things, prevent containers from re-launching automatically on service restart or reboot
	docker rm <container-id>

stop all containers

	docker stop $(docker ps -q)

force kill container that is stuck in a loop

	# if your entrypoint is an infinite loop script, and you ran the script manually
	# while inside the container with
	docker run -it --user root <container-id|name> /bin/bash
	# kill the container with
	docker ps -a
	docker rm --force <container-id|name>
	# then you can interact with it again
	docker run -it --user root <container-id|name> /bin/bash

create a new network; defaults to driver `bridge`

	docker network create testnet

	docker network create \
	    --driver \
	    --subnet 192.168.5.0/24 \
	    --gateway 192.168.5.1 \
	    testnet

ufw - allow traffic from other non-Docker apps to localhost 5000; substitute `lo` for an external interface if necessary

	sudo ufw allow in on lo to any port <port>
	# then this works from the host (outside the container)
	curl <container>:<port>

disable IPv6 - in compose file
```
services:
  your-service:
    image: your-image
    sysctls:
      net.ipv6.conf.all.disable_ipv6: 1
...
```

function to simplify running a container's `/bin/bash` (for `~/.bashrc` or `~/.zshrc`)
```
dexec () {
	docker exec -it -u root $1 /bin/bash
}
# usage
dexec <container-id|name>
```
