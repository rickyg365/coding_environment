
function hehehe {
    Write-Host "Hehhehe..."
}

function pyshort {
    python $HOME/Documents/POWERSHELL/sample.py
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
    $current = (Get-Content -Path $HOME/Documents/POWERSHELL/shorts.txt)
    foreach($p in $current){
        $p    
    }
    $chosen = Read-Host "Choose path"
    if (Test-Path -Path $HOME) {
        Set-Location -Path "$($current[[int]$chosen])"
    }
}



