# This script retrieves running services and logs them to a file.

# Get the current date to use in the log file name
$currentDate = Get-Date -Format "yyyyMMdd_HHmmss"

# Define the log file path
$logFilePath = "C:\Temp\ServiceLog_$currentDate.log"

# Get all running services
$runningServices = Get-Service | Where-Object {$_.Status -eq "Running"}

# Write the running services to the log file
$runningServices | Out-File -FilePath $logFilePath

Write-Host "Running services logged to: $logFilePath"
