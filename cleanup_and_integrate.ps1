# ESCI 240 Labs - Automated Directory Cleanup and Integration
# This script reorganizes the project structure to merge grading-system into canvas-api

param(
    [switch]$DryRun = $false
)

$ErrorActionPreference = "Stop"

# Colors
function Write-Header($text) {
    Write-Host ""
    Write-Host ("=" * 80) -ForegroundColor Cyan
    Write-Host $text -ForegroundColor Cyan
    Write-Host ("=" * 80) -ForegroundColor Cyan
    Write-Host ""
}

function Write-Step($num, $text) {
    Write-Host ""
    Write-Host "Step $num`: $text" -ForegroundColor Yellow
    Write-Host ("-" * 80) -ForegroundColor Gray
}

function Write-Success($text) {
    Write-Host "  ✅ $text" -ForegroundColor Green
}

function Write-Info($text) {
    Write-Host "  ℹ️  $text" -ForegroundColor Cyan
}

function Write-Warning($text) {
    Write-Host "  ⚠️  $text" -ForegroundColor Yellow
}

function Write-Error2($text) {
    Write-Host "  ❌ $text" -ForegroundColor Red
}

# Define paths
$rootPath = Split-Path -Parent $PSScriptRoot
if (-not $rootPath) { $rootPath = $PSScriptRoot }

$canvasApiPath = Join-Path $rootPath "canvas-api"
$gradingSystemPath = Join-Path $rootPath "grading-system"
$rootOutputPath = Join-Path $rootPath "output"
$rootDownloadsPath = Join-Path $rootPath "downloads"

Write-Header "ESCI 240 Labs - Directory Cleanup and Integration"

if ($DryRun) {
    Write-Warning "DRY RUN MODE - No changes will be made"
}

Write-Info "Root Path: $rootPath"
Write-Info "Canvas API Path: $canvasApiPath"

# Pre-flight checks
Write-Step 1 "Pre-flight Checks"

$canvasApiExists = Test-Path $canvasApiPath
$gradingSystemExists = Test-Path $gradingSystemPath

if (-not $canvasApiExists) {
    Write-Error2 "canvas-api directory not found!"
    exit 1
}

if (-not $gradingSystemExists) {
    Write-Warning "grading-system directory not found - skipping grading system migration"
}

Write-Success "All required directories found"

# Analyze current state
Write-Step 2 "Analyzing Current Structure"

$actions = @()

# Check root output directory
if (Test-Path $rootOutputPath) {
    $files = @(Get-ChildItem $rootOutputPath -File)
    if ($files.Count -gt 0) {
        Write-Info "Found $($files.Count) files in root output/ directory"
        foreach ($file in $files) {
            Write-Host "    - $($file.Name)" -ForegroundColor Gray
        }
        $actions += @{
            Type = "MoveFiles"
            Source = $rootOutputPath
            Dest = Join-Path $canvasApiPath "output"
            Files = $files
        }
    }
}

# Check empty directories
if (Test-Path $rootDownloadsPath) {
    $items = @(Get-ChildItem $rootDownloadsPath)
    if ($items.Count -eq 0) {
        Write-Info "Found empty downloads/ directory in root"
        $actions += @{
            Type = "DeleteDir"
            Path = $rootDownloadsPath
            Name = "downloads/ (root)"
        }
    }
}

$canvasDownloadsPath = Join-Path $canvasApiPath "downloads"
if (Test-Path $canvasDownloadsPath) {
    $items = @(Get-ChildItem $canvasDownloadsPath)
    if ($items.Count -eq 0) {
        Write-Info "Found empty canvas-api/downloads/ directory"
        $actions += @{
            Type = "DeleteDir"
            Path = $canvasDownloadsPath
            Name = "canvas-api/downloads/"
        }
    }
}

# Check for grading system migration
if ($gradingSystemExists) {
    Write-Info "Grading system found - will integrate into canvas-api"
    
    $lab01GraderPath = Join-Path $gradingSystemPath "lab01\grader.py"
    $sharedGraderPath = Join-Path $gradingSystemPath "shared\grader_base.py"
    
    if (Test-Path $lab01GraderPath) {
        $actions += @{
            Type = "MoveFile"
            Source = $lab01GraderPath
            Dest = Join-Path $canvasApiPath "graders\lab01_grader.py"
            Name = "Lab 1 grader"
        }
    }
    
    if (Test-Path $sharedGraderPath) {
        $actions += @{
            Type = "MoveFile"
            Source = $sharedGraderPath
            Dest = Join-Path $canvasApiPath "graders\base_grader.py"
            Name = "Base grader"
        }
    }
}

# Check for scripts to organize
$scriptsToMove = @(
    @{ File = "list_students.py"; Dest = "downloads" },
    @{ File = "list_assignments.py"; Dest = "downloads" },
    @{ File = "download_lab01_submissions.py"; Dest = "downloads" }
)

foreach ($script in $scriptsToMove) {
    $sourcePath = Join-Path $canvasApiPath $script.File
    if (Test-Path $sourcePath) {
        $destDir = Join-Path $canvasApiPath $script.Dest
        $destPath = Join-Path $destDir $script.File
        
        $actions += @{
            Type = "MoveScript"
            Source = $sourcePath
            Dest = $destPath
            DestDir = $destDir
            Name = $script.File
        }
    }
}

# Summary of actions
Write-Step 3 "Planned Actions"

if ($actions.Count -eq 0) {
    Write-Success "No cleanup needed! Directory structure is already clean."
    exit 0
}

Write-Info "The following actions will be performed:"
Write-Host ""

$actionNum = 1
foreach ($action in $actions) {
    switch ($action.Type) {
        "MoveFiles" {
            Write-Host "  $actionNum. Move $($action.Files.Count) files from output/ to canvas-api/output/" -ForegroundColor Yellow
        }
        "DeleteDir" {
            Write-Host "  $actionNum. Delete empty directory: $($action.Name)" -ForegroundColor Yellow
        }
        "MoveFile" {
            Write-Host "  $actionNum. Move $($action.Name)" -ForegroundColor Yellow
            Write-Host "     From: $($action.Source)" -ForegroundColor Gray
            Write-Host "     To:   $($action.Dest)" -ForegroundColor Gray
        }
        "MoveScript" {
            Write-Host "  $actionNum. Organize $($action.Name) into $($action.DestDir)" -ForegroundColor Yellow
        }
    }
    $actionNum++
}

# Confirm
Write-Host ""
if (-not $DryRun) {
    $confirmation = Read-Host "Proceed with cleanup? (yes/no)"
    if ($confirmation -ne "yes" -and $confirmation -ne "y") {
        Write-Host ""
        Write-Error2 "Cleanup cancelled by user"
        exit 1
    }
}

# Execute actions
Write-Step 4 "Executing Cleanup"

$successCount = 0
$errorCount = 0

foreach ($action in $actions) {
    try {
        switch ($action.Type) {
            "MoveFiles" {
                Write-Info "Moving files from root output/ to canvas-api/output/..."
                
                foreach ($file in $action.Files) {
                    $destPath = Join-Path $action.Dest $file.Name
                    
                    if (Test-Path $destPath) {
                        # Compare files
                        $sourceHash = (Get-FileHash $file.FullName).Hash
                        $destHash = (Get-FileHash $destPath).Hash
                        
                        if ($sourceHash -eq $destHash) {
                            Write-Info "  $($file.Name) - identical file exists, removing duplicate"
                            if (-not $DryRun) {
                                Remove-Item $file.FullName -Force
                            }
                        } else {
                            $newName = "$($file.BaseName)_from_root$($file.Extension)"
                            $newDestPath = Join-Path $action.Dest $newName
                            Write-Warning "  $($file.Name) - different file exists, saving as $newName"
                            if (-not $DryRun) {
                                Move-Item $file.FullName $newDestPath -Force
                            }
                        }
                    } else {
                        Write-Success "  Moved: $($file.Name)"
                        if (-not $DryRun) {
                            Move-Item $file.FullName $destPath -Force
                        }
                    }
                }
                
                # Remove empty directory
                if (-not $DryRun) {
                    $remaining = @(Get-ChildItem $action.Source)
                    if ($remaining.Count -eq 0) {
                        Remove-Item $action.Source -Force
                        Write-Success "Removed empty output/ directory"
                    }
                }
                
                $successCount++
            }
            
            "DeleteDir" {
                Write-Info "Deleting empty directory: $($action.Name)"
                if (-not $DryRun) {
                    Remove-Item $action.Path -Force -Recurse
                }
                Write-Success "Deleted: $($action.Name)"
                $successCount++
            }
            
            "MoveFile" {
                Write-Info "Moving $($action.Name)..."
                
                $destDir = Split-Path $action.Dest -Parent
                if (-not (Test-Path $destDir)) {
                    Write-Info "  Creating directory: $destDir"
                    if (-not $DryRun) {
                        New-Item -ItemType Directory -Path $destDir -Force | Out-Null
                    }
                }
                
                if (-not $DryRun) {
                    Move-Item $action.Source $action.Dest -Force
                }
                Write-Success "Moved: $($action.Name)"
                $successCount++
            }
            
            "MoveScript" {
                Write-Info "Organizing $($action.Name)..."
                
                if (-not (Test-Path $action.DestDir)) {
                    Write-Info "  Creating directory: $($action.DestDir)"
                    if (-not $DryRun) {
                        New-Item -ItemType Directory -Path $action.DestDir -Force | Out-Null
                    }
                }
                
                if (-not $DryRun) {
                    Move-Item $action.Source $action.Dest -Force
                }
                Write-Success "Moved: $($action.Name)"
                $successCount++
            }
        }
    } catch {
        Write-Error2 "Failed: $_"
        $errorCount++
    }
}

# Create __init__.py files for Python packages
if (-not $DryRun) {
    $gradersPath = Join-Path $canvasApiPath "graders"
    if (Test-Path $gradersPath) {
        $initPath = Join-Path $gradersPath "__init__.py"
        if (-not (Test-Path $initPath)) {
            Write-Info "Creating graders/__init__.py"
            Set-Content $initPath "# ESCI 240 Lab Graders`n"
        }
    }
    
    $downloadsPath = Join-Path $canvasApiPath "downloads"
    if (Test-Path $downloadsPath) {
        $initPath = Join-Path $downloadsPath "__init__.py"
        if (-not (Test-Path $initPath)) {
            Write-Info "Creating downloads/__init__.py"
            Set-Content $initPath "# Canvas API Download Scripts`n"
        }
    }
}

# Clean up empty grading-system if everything was moved
if ($gradingSystemExists -and -not $DryRun) {
    $remainingItems = @(Get-ChildItem $gradingSystemPath -Recurse -File)
    if ($remainingItems.Count -eq 0) {
        Write-Info "Removing empty grading-system directory..."
        Remove-Item $gradingSystemPath -Recurse -Force
        Write-Success "Removed grading-system/ (all contents migrated)"
    } else {
        Write-Info "grading-system/ still has $($remainingItems.Count) files - keeping it"
    }
}

# Final summary
Write-Step 5 "Summary"

Write-Host ""
Write-Host "  Successful actions: $successCount" -ForegroundColor Green
if ($errorCount -gt 0) {
    Write-Host "  Errors: $errorCount" -ForegroundColor Red
}

if ($DryRun) {
    Write-Host ""
    Write-Warning "DRY RUN - No actual changes were made"
    Write-Info "Run without -DryRun to apply changes"
} else {
    Write-Host ""
    Write-Success "Cleanup complete!"
    
    Write-Host ""
    Write-Header "New Structure"
    
    Write-Host "canvas-api/" -ForegroundColor Cyan
    Write-Host "  ├── downloads/          📥 Download scripts" -ForegroundColor Gray
    Write-Host "  ├── graders/            🎓 Grading logic" -ForegroundColor Gray
    Write-Host "  ├── submissions/        💾 Student submissions" -ForegroundColor Gray
    Write-Host "  ├── output/             📊 API metadata" -ForegroundColor Gray
    Write-Host "  ├── config.py           ⚙️  Configuration" -ForegroundColor Gray
    Write-Host "  └── README.md           📖 Documentation" -ForegroundColor Gray
    
    Write-Host ""
    Write-Header "Next Steps"
    
    Write-Host "1. Review changes:" -ForegroundColor Yellow
    Write-Host "   git status" -ForegroundColor Gray
    Write-Host ""
    Write-Host "2. Test the structure:" -ForegroundColor Yellow
    Write-Host "   cd canvas-api/downloads" -ForegroundColor Gray
    Write-Host "   python list_students.py" -ForegroundColor Gray
    Write-Host ""
    Write-Host "3. Update imports in moved files if needed" -ForegroundColor Yellow
    Write-Host ""
    Write-Host "4. Commit changes:" -ForegroundColor Yellow
    Write-Host "   git add ." -ForegroundColor Gray
    Write-Host "   git commit -m 'Reorganize Canvas API structure'" -ForegroundColor Gray
}

Write-Host ""
Write-Host ("=" * 80) -ForegroundColor Cyan
