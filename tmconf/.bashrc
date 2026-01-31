# Alias

# File Exploring
alias ls="eza"
alias ll="eza -la --sort=extension"

alias cls="clear && ls"
alias cll="clear && ll"

alias lr="ranger"

# Shortcuts
alias rss="newsboat"

alias qe="nvim ."
alias edit="nvim ~/.bashrc"

# Nav
alias ytdir="cd ~/storage/downloads/yt"

# Obsidian
# alias osync="cd ~/storage/downloads/obsidian/osync"

# Python
alias serve="python -m http.server"

# Tmux
alias ta="tmux a"

# Github
alias gp="git pull"
alias ga="git add ."
alias gpu="git push"
alias gs="git status"

function gq(){
    git add . &&
    git commit -m "quick save" &&
    git push
}

alias ginit=". ~/docs/scripts/init_ssh.sh"

# Play in Terminal, using mpv
alias pit="mpv --vo=tct --vo-tct-256=yes --vo-tct-algo=half-blocks --profile=sw-fast --really-quiet"

# Functions

# yt-dlp
ytd() {
    yt-dlp -t mp4 --no-warnings "$1"
}

yta() {
    yt-dlp -t m4a --no-warnings "$1"
}

anime() {
    ani-cli 
}



# yrss() {
#     wget -q -O - "$1" | grep -o -P (?<= channelId":").{0,24} | tail -1
# }

yrss() { wget -q -O - "$1" | grep -oP '(?<=channelId":").{0,24}' | tail -1 ;}
cliprss() { wget -q -O - "$1" | grep -oP '(?<=channelId":").{0,24}' | tail -1 | termux-clipboard-set ;}

# timg | p: q-quarter h-half_blocks
# timg -pq filename.png
# timg -V -pq filename.mp4

# Exports
# export TIMG_ALLOW_FRAME_SKIP=1

# Display Start up
clear

timeout 1 curl wttr.in/San+Francisco?format=3
neofetch
ls

