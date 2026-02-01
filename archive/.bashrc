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

# Weather wttr api, curl wttr.in/:help  for detailed info
# Sample Params
#   ?T            forces plain text
#   .png          png format
#   ?format=3     One line output
# Formats
#   1:  Weather at location
#   2:  Detailed weather at location
#   3:  Name of location + Weather at location
#   4:  Name of location + Detailed weather at location
# Multi Query
#   curl -s 'wttr.in/{Nuremberg,Hamburg,Berlin}?format=3'
# Custom, use %-notation
#   c       Weather condition
#   C       Weather condition textual name
#   x       Weather condition, plain-text symbol
#   h       Humidity
#   t       Temperature (Actual)
#   f       Temperature (Feels Like)
#   w       Wind
#   l       Location
#   m       Moon Phase
#   M       Moon Day
#   P       Precipitation(mm/3 hours)
#   p       Pressure (hPa)
#   u       UV index (1-12)
#
#   D       Dawn*
#   S       Sunrise*
#   z       Zenith*
#   s       Sunset*
#   d       Dusk*
#   T       Current time*
#   Z       Local timezone
# [ *shown in local timezone ]
# Example(format=3): ?format="%l:+%c+%t\n"
# JSON: ?format=j1

# curl -s wttr.in/Moon?0
# curl -s wttr.in/San+Francisco?0

curl -s wttr.in/San+Francisco?format="%l:+%c+%t/%f %m\n"

echo ""  # Spacing
ls

