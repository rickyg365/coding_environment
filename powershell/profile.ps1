
function hehehe {
    Write-Host "Hehhehe..."
}

function pyshort {
    python $HOME/Documents/POWERSHELL/sample.py
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



