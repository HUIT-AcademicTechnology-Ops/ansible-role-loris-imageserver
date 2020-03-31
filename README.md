# Ansible Role: Loris Image Server

Installs and configures the [Loris Image Server](https://github.com/loris-imageserver) with Apache and mod_wsgi (python3).

## Requirements

- Ansible 2.0+
- Ubuntu 18.04 Bionic

## Role Variables

| parameter     | required | default                                        | comments                              |
|---------------|----------|------------------------------------------------|---------------------------------------|
| loris_repo    | no       | https://github.com/loris-imageserver/loris.git | Loris git repository                  |
| loris_version | no       | v3.0.0                                         | Git tag, branch, or commit to use     |
| loris_port    | no       | 80                                             | Server port                           |
| loris_prefix  | no       | loris                                          | Server prefix for IIIF image requests |


## Dependencies

None

## Example Playbook

Playbook `playbook.yml`:

```yaml
  - hosts: server
    remote_user: ubuntu
    become: yes
    roles:
      - huit-academictechnology-ops.ansible-role-loris-imageserver
```

Inventory `inventory`:

```ini
  [server]
  127.0.0.1 ansible_python_interpreter=/usr/bin/python3
```

Run Ansible:

```
  $ ansible-playbook -i inventory playbook.yml -v
```

To test:

- Add an image to `/usr/local/share/images/loris` 
- Access image info.json at http://127.0.0.1/loris/myimage.jpg/info.json
- Access image at http://127.0.0.1/loris/myimage.jpg/full/full/0/default.jpg

## License

MIT/BSD

## Author Information

This role was created in 2020 by Arthur Barrett as a member of the Harvard University IT Academic Technology group.
