# GreenPiThumb Frontend

[![Build
Status](https://travis-ci.org/masterhui/GreenPiThumb_Frontend.svg?branch=master)](https://travis-ci.org/masterhui/GreenPiThumb_Frontend)
[![Coverage
Status](https://coveralls.io/repos/masterhui/GreenPiThumb_Frontend/badge.svg?branch=master&service=github)](https://coveralls.io/github/masterhui/GreenPiThumb_Frontend?branch=master)


The web frontend for GreenPiThumb.

## Installation

### Standard Installation

```bash
git clone --recursive https://github.com/masterhui/GreenPiThumb_Frontend.git
cd GreenPiThumb_Frontend
sudo pip install -r requirements.txt
```

### Dev Installation

```bash
git clone --recursive https://github.com/masterhui/GreenPiThumb_Frontend.git
cd GreenPiThumb_Frontend
sudo pip install -r requirements.txt
sudo pip install -r dev_requirements.txt
```

## Related Repositories

* [GreenPiThumb](https://github.com/masterhui/GreenPiThumb): The GreenPiThumb backend, which manages all the physical hardware and sensors for the GreenPiThumb device.
* [GreenPiThumb_Frontend_static](https://github.com/masterhui/GreenPiThumb_Frontend_static): An AngularJS web app for viewing GreenPiThumb status (the static portion of the web frontend).
* [ansible-role-greenpithumb](https://github.com/masterhui/ansible-role-greenpithumb): An [Ansible](https://www.ansible.com/how-ansible-works) role for deploying all parts of GreenPiThumb to a system.
