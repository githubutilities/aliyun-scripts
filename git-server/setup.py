#!/usr/bin/env python

import os
import sys

git_server_config_url = "https://github.com/githubutilities/git-server-config.git"

# get parameter
if len(sys.argv) < 2 or len(sys.argv) > 3:
    sys.stderr.write("setup.py <directory>")
    sys.exit(1)
if len(sys.argv) == 3:
    git_server_config_url = sys.argv[2]
directory_path = sys.argv[1]

# make directory
if os.path.exists(directory_path):
    sys.stderr.write("{0} already exists".format(directory_path))
    sys.exit(1)

os.makedirs(directory_path)
os.chdir(directory_path)

# checkout git server config
os.system("git clone {0} .".format(git_server_config_url))
os.system("rm -rf .git")

# init git server
os.system('git init --bare')
