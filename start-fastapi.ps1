param(
    [string]$AppModule = "api:app",
    [int]$Port = 8000,
    [string]$Host = "127.0.0.1"
)

$ErrorActionPreference = "Stop"

Write-Host ("Checking port {0}..." -f $Port)

# Find any process listening on the given port and kill it
$matches = netstat -ano | Select-String (":$Port\s+LISTENING")
foreach ($line in $matches) {
    $pid = ($line -split '\s+')[-1]
    if ($pid -match '^\d+$') {
        try {
            Stop-Process -Id $pid -Force
            Write-Host ("Killed PID {0} on port {1}" -f $pid, $Port)
        } catch {
            Write-Host ("Could not kill PID {0}: {1}" -f $pid, $_.Exception.Message)
        }
    }
}

# Build uvicorn command safely (no quoting issues)
$reloadDir = (Get-Location).Path
$cmd = @(
    "-m","uvicorn",
    $AppModule,
    "--reload",
    "--reload-dir", $reloadDir,
    "--reload-exclude",".venv/*",
    "--host", $Host,
    "--port", $Port
)

Write-Host "Starting: python $($cmd -join ' ')"
python $cmd
