#!/bin/bash

# Goals:
# fzf ?
# Make sure that if files already exist they get backed up
# Copy chosen config onto chosen locations(having defaults)

# Setup: Choose config file to use
CONFIG="$HOME/github/coding_environment/tmconf"
# TBD: fzf choice instead of manual input

# DOT
CHOSEN_DOT="$CONFIG/.bashrc"
cp -r $CHOSEN_DOT "${HOME}/.bashrc"

# SCRIPTS
SCRIPTS="$CONFIG/scripts/"
cp -r $SCRIPTS "${HOME}/docs/scripts/"

# RSSFEED
RSSFEED="$CONFIG/rss_feed.txt"
cp -r $RSSFEED "${HOME}/.newsboat/urls"

RSS_CONFIG="$CONFIG/rss_config.txt"
cp -r $RSS_CONFIG "${HOME}/.newsboat/config"

# NVIM
NVIM_CONFIG="$CONFIG/nvim/"
cp -r $NVIM_CONFIG "${HOME}/.config/"

# In future add check after each step
echo "Environment Setup complete!"




