
function hehehe {
    Write-Host "Hehhehe..."
}

function pyshort {
    python $HOME/Documents/POWERSHELL/sample.py
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
    git push
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

    Write-Host "$($current_json)"
    Write-Host "$($chosen)"
    
    if (!$chosen) {
        $chosen = Read-Host "Choose key"
    }
    # $current_json | Add-Member -MemberType NoteProperty -Name $chosen -Value (Get-Location)
    $current_json[$chosen] = "$(Get-Location)"
    $current_json | ConvertTo-Json -Depth 4 | Out-File $HOME/Documents/POWERSHELL/test.json
}


