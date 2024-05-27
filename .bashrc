# Aliases
# File Exploring
alias lr="ranger"
alias ll="exa -la --sort=extension"

alias cls="clear && ls"
alias cll="clear && ll"

# Tmux
alias ta="tmux a"

# Github
alias gp="git pull"
alias ga="git add ."
alias gpu="git push"
alias gs="git status"

function gsav(){
    git add . &&
    git commit -m "quick save" &&
    git push
}

# Obsidian
# alias osync="cd storage/Downloads/obsidian/osync"

# Python
alias serve="python -m http.server"

# yt-dlp
ytd() {
    yt-dlp -f mp4 "$1"
}

yta() {
    yt-dlp -f m4a "$1"
}



# Start up
clear
# date
# neofetch
# curl -s wttr.in/Moon?0
curl -s wttr.in/San+Francisco?0
echo ""
ls

