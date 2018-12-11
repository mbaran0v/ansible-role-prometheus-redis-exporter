# Ansible role: prometheus-redis-exporter

[![Build Status](https://travis-ci.org/mbaran0v/ansible-role-prometheus-redis-exporter.svg?branch=master)](https://travis-ci.org/mbaran0v/ansible-role-prometheus-redis-exporter) [![License](https://img.shields.io/badge/license-MIT%20License-brightgreen.svg)](https://opensource.org/licenses/MIT) [![GitHub tag](https://img.shields.io/github/tag/mbaran0v/anansible-role-prometheus-redis-exporter.svg)](https://github.com/mbaran0v/ansible-role-prometheus-redis-exporter/tags) [![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/) [![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)

Ansible role for install and configure [Prometheus redis Exporter](https://github.com/oliver006/redis_exporter). Currently this works on Debian and RedHat based linux systems. Tested platforms are:

* Ubuntu 16.04
* Debian 9
* CentOS 7

Requirements
------------

No special requirements; note that this role requires root access, so either run it in a playbook with a global become: yes

Role Variables
--------------

The variables that can be passed to this role and a brief description about them are as follows. (For all variables, take a look at defaults/main.yml)

```yaml
redis_exporter_version: 0.23.0
```
version for installation

```yaml
redis_exporter_web_listen_address: "0.0.0.0:9121"
```
listen address and port

```yaml
redis_exporter_root_dir: /opt/redis_exporter
```
directory for installation

```yaml
redis_exporter_system_group: "redis-exp"
redis_exporter_system_user: "{{ redis_exporter_system_group }}"
```
user and group for service

```yaml
# see https://github.com/oliver006/redis_exporter#environment-variables
redis_exporter_config_vars: |
  REDIS_ADDR=redis://127.0.0.1:6379
```
config variables

Dependencies
------------

None

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

```yaml
- hosts: app
  become: yes
  roles:
      - mbaran0v.prometheus-redis-exporter
```

License
-------

MIT / BSD

Author Information
------------------

This role was created in 2018 by Maxim Baranov.
