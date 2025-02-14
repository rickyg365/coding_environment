
function hehehe {
    Write-Host "Hehhehe..."
}

function pyshort {
    param (
        [Parameter()]
        [string] $arg = ''
    )
    python $HOME/Documents/POWERSHELL/sample.py $arg
}
function pygam {
    python $HOME/Documents/POWERSHELL/game/main.py
}
function servepls {
    python -m http.server
}

function gs {
    git status
}
function gup {
    git pull
}

function qiksav {
    git status
    git add .
    git commit -m "Quicksave"
}

function short {
    if (Test-Path -Path $HOME) {
        $current = (Get-Content -Path $HOME/Documents/POWERSHELL/shorts.txt)[-1]
        Set-Location -Path "$current"
    }
}

function addto {
    if (Test-Path -Path $HOME) {
        Add-Content -Path $HOME/Documents/POWERSHELL/shorts.txt -Value (Get-Location)
    }
}


function goto {
    param (
        [Parameter()]
        [string]
        $chosen = ''
    )
    $current = (Get-Content -Path $HOME/Documents/POWERSHELL/shorts.txt)
    if (!$chosen) {    
        foreach($p in $current){
            $p    
        }
        $chosen = Read-Host "Choose path"
    }

    if (Test-Path -Path $HOME) {
        Set-Location -Path "$($current[[int]$chosen])"
    }
}

function nav {
    param (
        [Parameter()]
        [string]
        $chosen = ''
    )

    # $myJson.Accounts.Users.asmith.department = "Senior Leadership" 
    # $myJson | ConvertTo-Json -Depth 4 | Out-File .\test.json

    $current_json = (Get-Content -Raw $HOME/Documents/POWERSHELL/test.json) | ConvertFrom-Json
    
    if (!$chosen) {    
        foreach ($key in $current_json.psobject.properties.name) {
            # Write-Host "The value of '$key' is: $($current_json[$key])"
            Write-Host "$($key)"
        }
        $chosen = Read-Host "Choose path"
    }
    
    # Write-Host "$($current_json)"
    # Write-Host "$($chosen)"
    # Write-Host "$($current_json.$chosen)"

    if (Test-Path -Path $HOME) {
        # Write-Host "$($current_json[$chosen])"
        Set-Location -Path "$($current_json.$chosen)"
    }
}


function addnav {
    param (
        [Parameter()]
        [string]
        $chosen = ''
    )
    
    $current_json = (Get-Content -Raw $HOME/Documents/POWERSHELL/test.json) | ConvertFrom-Json -AsHashtable

    # Write-Host "$($current_json)"
    # Write-Host "$($chosen)"
    
    if (!$chosen) {
        $chosen = Read-Host "Choose key"
    }
    # $current_json | Add-Member -MemberType NoteProperty -Name $chosen -Value (Get-Location)
    $current_json[$chosen] = "$(Get-Location)"
    $current_json | ConvertTo-Json -Depth 4 | Out-File $HOME/Documents/POWERSHELL/test.json
}

function ytd {
    param (
        [Parameter()]
        [string]
        $url = ''
    )

    yt-dlp -f mp4 $url
}

function yta {
    param (
        [Parameter()]
        [string]
        $url = ''
    )

    yt-dlp -f m4a $url
}

function ytmp3 {
    param (
        [Parameter()]
        [string]
        $url = ''
    )

    yt-dlp -f "ba" $url
}


function yt_info {
    param (
        [Parameter()]
        [string] $url = '',
        [Parameter()]
        [string] $filename = 'extracted_info.md'
    )

    if (!$url) {
        return
    }
    
    yt-dlp --flat-playlist --print "%(id)s^%(title)s" "$($url)" > $filename
}


function create_electron_app {
    param (
        [Parameter()]
        [string] $project_name = 'my_electron_app',
        [Parameter()]
        [string] $template_choice = 'default'
    )
    $new_dir = "$(Get-Location)/$($project_name)"
    
    mkdir $new_dir
    Set-Location $new_dir
    
    # Add template files
    Copy-Item -Path "$($HOME)/Documents/Powershell/electron_templates/$($template_choice)" -Destination "$($new_dir)/src" -Recurse
    
    
    # Install Imports
    npm init
    npm install electron @electron-forge/cli --save-dev
    npx electron-forge import

    # Warning when making with electron forge
    $Env:NODE_OPTIONS = "--disable-warning=DEP0174"

}
