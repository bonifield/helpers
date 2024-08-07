# Ansible

## SSH Setup
[SSH Notes](https://github.com/bonifield/helpers/tree/main/ssh)

## Useful Ansible CLI Options
```
# ansible and ansible-playbook
-K, --ask-become-pass
   ask for privilege escalation password

-b, --become
   run operations with become (does not imply password prompting)

-i, --inventory, --inventory-file
   specify  inventory  host  path  or comma separated host list. This argument may be specified multiple times.

# ansible-playbook only
-J, --ask-vault-password, --ask-vault-pass
   ask for vault password
```

## Inventories

group hosts in INI/CONF or YAML formats
- [inventory.ini](inventory.ini)
- [inventory.yml](inventory.yml)

convert INI/CONF to YAML
```
ansible-inventory -i inventory.ini --list --yaml
```

convert YAML to INI/CONF: [StackOverflow Answer](https://stackoverflow.com/questions/74311307/how-can-i-change-yaml-format-to-ini-format)

## Ad-Hoc Commands
[Ad-Hoc Command Documentation](https://docs.ansible.com/ansible/latest/command_guide/intro_adhoc.html)

`ansible [pattern] -i [inventory.yml] -m [module] -a "[module options]"`

run shell module on target group "webservers" ("pattern")
```
# as user to IP
ansible webservers -i inventory.yml -m shell -a "id"
# as superuser to hostname
ansible webservers -Kbi inventory.yml -m shell -a "id"
```

locally run command module (default) on target ("pattern") host
```
# as user to IP
ansible 127.1.2.3 -a "id"
# as superuser to hostname
ansible localhost --become --ask-become-pass -a "id"
```

reboot or shutdown inventory group
```
ansible webservers -Kbi inventory.yml -m reboot
ansible webservers -Kbi inventory.yml -m community.general.shutdown
```

transfer (SCP) local file to remote host or group
```
ansible webservers -Kbi inventory.yml -m copy -a "src=/dev/index.html dest=/var/www/mysite/public_html/index.html"
```

start(ed), restart(ed), or stop(ped) a service
```
ansible webservers -Kbi inventory.yml -m service -a "name=httpd state=restarted"
ansible webservers -Kbi inventory.yml -m systemd_service -a "name=apache2 daemon_reload=true enabled=true state=restarted"
```

## Vaults
[Vault Documentation](https://docs.ansible.com/ansible/latest/vault_guide/index.html)

prevent logging at task or play level
```
- name: sensitive task
  ...
  no_log: true
```
```
- hosts: all
  no_log: true
```

create vault and set password
```
ansible-vault create vars/vault.yml
```

edit vault
```
ansible-vault edit vars/vault.yml
```

edit default editor
```
export EDITOR=/usr/bin/nano
```

vault file format
```
key: value
```

## Variables and Jinja
[Templating Documentation](https://docs.ansible.com/ansible/latest/playbook_guide/playbooks_templating.html)

[Special Variables Documentation](https://docs.ansible.com/ansible/latest/reference_appendices/special_variables.html)

- add `welcome_message: "Hello, world!"` to `vars/vars.yml`
- use the `template` module in a task, such as inside `tasks/copy-template.yml`
- the file `templates/index.html.j2` contains `<h1>{{ welcome_message }}</h1>`, and is used to generate `index.html` which contains `<h1>Hello, world!</h1>`
- variables should be quoted when used in a task
- inventory variables can be used like `"{{ hostvars[inventory_hostname].basename }}.index.html"` to create `westweb.index.html`

## Playbooks
[Playbook Documentation](https://docs.ansible.com/ansible/latest/playbook_guide/playbooks_intro.html)

assumes directory at `/home/j/projects/helpers/ansible`

playbook "plays" specify which groups or hosts perform the tasks

playbooks can reference external tasks or run them directly

run a playbook using an inventory
```
ansible-playbook -JKbi inventory.yml playbook_myservers.yml
```

run a playbook using localhost connections (for this example repo)
```
ansible-playbook -K --connection=local -i inventory.yml playbook_myservers.yml
```

run a playbook that specifies a private key, becomes root, and asks for the user password for sudo to elevate
```
ansible-playbook --private-key ~/.ssh/project_key -JKbi inventory.yml playbook_myservers.yml
```

sample output from above connection=local playbook
```
$ ansible-playbook --connection=local -Ki inventory.yml playbook_myservers.yml 
BECOME password: 

PLAY [webservers] **************************************************************************************

TASK [Gathering Facts] *********************************************************************************
ok: [eastweb]
ok: [westweb]

TASK [Install Webserver] *******************************************************************************
included: /home/j/projects/helpers/ansible/tasks/webserver.yml for westweb, eastweb

TASK [Simulate RHEL Webserver Install] *****************************************************************
skipping: [westweb]
skipping: [eastweb]

TASK [Simulate Debian Webserver Install] ***************************************************************
ok: [westweb] => {
    "msg": "Installed webserver on Debian."
}
ok: [eastweb] => {
    "msg": "Installed webserver on Debian."
}

TASK [Copy index.html to Remote] **********************************************************************
included: /home/j/projects/helpers/ansible/tasks/copy-template.yml for westweb, eastweb

TASK [Copy index.html to Remote] **********************************************************************
ok: [westweb]
ok: [eastweb]

TASK [Copy index.html with Hostname to Remote] ********************************************************
ok: [westweb]
ok: [eastweb]

TASK [Copy Dynamic Template index.html with Hostname to Remote] ***************************************
ok: [westweb]
ok: [eastweb]

PLAY [databases] **************************************************************************************

TASK [Debug Message Simulating Success] ***************************************************************
ok: [westdb] => {
    "msg": "Installed databases."
}
ok: [eastdb] => {
    "msg": "Installed databases."
}

PLAY RECAP ********************************************************************************************
eastdb                     : ok=1    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
eastweb                    : ok=7    changed=0    unreachable=0    failed=0    skipped=1    rescued=0    ignored=0   
westdb                     : ok=1    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
westweb                    : ok=7    changed=0    unreachable=0    failed=0    skipped=1    rescued=0    ignored=0
```
