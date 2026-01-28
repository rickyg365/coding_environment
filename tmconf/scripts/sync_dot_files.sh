#!/bin/bash

DOT="$HOME/github/coding_environment/.bashrc"
SCRIPTS="$HOME/github/coding_environment/scripts/"
TDOT="$HOME/github/coding_environment/.bashrc_old"

cp -r $TDOT "${HOME}/.bashrc"

echo "dotfile sync complete!"




