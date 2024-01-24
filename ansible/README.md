# Ansible

## SSH Setup
[SSH Notes](https://github.com/bonifield/helpers/tree/main/ssh)

## Ad-Hoc Commands
[Ad-Hoc Command Documentation](https://docs.ansible.com/ansible/latest/command_guide/intro_adhoc.html)

`ansible [pattern] -m [module] -a "[module options]"`

run command module (default) on target ("pattern") host
```
# as user to IP
ansible 127.1.2.3 -a "id"
# as superuser to hostname
ansible localhost --become --ask-become-pass -a "id"
```

run shell module on target host
```
# as user to IP
ansible 127.1.2.3 -m shell -a "id"
# as superuser to hostname
ansible localhost --become --ask-become-pass -m shell -a "id"
```

reboot or shutdown inventory group
```
ansible webservers --become --ask-become-pass -i inventory.yml -m reboot
ansible webservers --become --ask-become-pass -i inventory.yml -m community.general.shutdown
```

transfer (SCP) local file to remote host or group
```
ansible webservers -m copy -a "src=/dev/index.html dest=/var/www/mysite/public_html/index.html"
```

start(ed), restart(ed), or stop(ped) a service
```
ansible webservers -m service -a "name=httpd state=restarted"
ansible webservers -m systemd_service -a "name=apache2 daemon_reload=true enabled=true state=restarted"
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
ansible-playbook -i inventory.yml playbook_webservers.yml
```

run a playbook using localhost connections (for this example repo)
```
ansible-playbook --ask-become-pass --connection=local -i inventory.yml playbook_webservers.yml
```

run a playbook that specifies a private key, becomes root, and asks for the user password for sudo to elevate
```
ansible-playbook --private-key ~/.ssh/project_key --ask-vault-pass --ask-become-pass -i inventory.yml playbook_webservers.yml
```

sample output from above connection=local playbook
```
$ ansible-playbook --ask-become-pass --connection=local -i inventory.yml playbook_webservers.yml 
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
