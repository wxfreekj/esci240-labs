# Canvas API Directory Cleanup Script
# This script reorganizes the directory structure to match the new grading workflow

Write-Host "=" -NoNewline -ForegroundColor Cyan
Write-Host ("=" * 79) -ForegroundColor Cyan
Write-Host "Canvas API Directory Cleanup" -ForegroundColor Cyan
Write-Host "=" -NoNewline -ForegroundColor Cyan
Write-Host ("=" * 79) -ForegroundColor Cyan
Write-Host ""

# Define paths
$rootPath = $PSScriptRoot
$rootOutputPath = Join-Path $rootPath "output"
$rootDownloadsPath = Join-Path $rootPath "downloads"
$canvasApiPath = Join-Path $rootPath "canvas-api"
$canvasApiOutputPath = Join-Path $canvasApiPath "output"
$canvasApiDownloadsPath = Join-Path $canvasApiPath "downloads"

Write-Host "Current Directory Structure:" -ForegroundColor Yellow
Write-Host ""

# Check what exists
$issues = @()

if (Test-Path $rootOutputPath) {
    $items = Get-ChildItem $rootOutputPath
    if ($items.Count -gt 0) {
        Write-Host "  ⚠️  Found: output/ (root level - WRONG LOCATION)" -ForegroundColor Red
        Write-Host "      Contains: $($items.Count) files (student data!)" -ForegroundColor Red
        $issues += "root-output"
    }
}

if (Test-Path $rootDownloadsPath) {
    $items = Get-ChildItem $rootDownloadsPath
    if ($items.Count -eq 0) {
        Write-Host "  📁 Found: downloads/ (root level - EMPTY)" -ForegroundColor Yellow
        $issues += "root-downloads-empty"
    }
}

if (Test-Path $canvasApiDownloadsPath) {
    $items = Get-ChildItem $canvasApiDownloadsPath
    if ($items.Count -eq 0) {
        Write-Host "  📁 Found: canvas-api/downloads/ (EMPTY)" -ForegroundColor Yellow
        $issues += "canvas-downloads-empty"
    }
}

if (Test-Path $canvasApiOutputPath) {
    Write-Host "  ✅ Found: canvas-api/output/ (CORRECT LOCATION)" -ForegroundColor Green
}

Write-Host ""
Write-Host ("=" * 80) -ForegroundColor Cyan
Write-Host "Cleanup Plan:" -ForegroundColor Yellow
Write-Host ("=" * 80) -ForegroundColor Cyan
Write-Host ""

if ($issues.Count -eq 0) {
    Write-Host "✅ No cleanup needed! Directory structure is correct." -ForegroundColor Green
    exit 0
}

# Plan cleanup actions
$actions = @()

if ($issues -contains "root-output") {
    Write-Host "1. Move student data from root output/ to canvas-api/output/" -ForegroundColor Yellow
    Write-Host "   • Students list files contain PII and should be in canvas-api/" -ForegroundColor Gray
    $actions += "move-output"
}

if ($issues -contains "root-downloads-empty") {
    Write-Host "2. Delete empty downloads/ directory from root" -ForegroundColor Yellow
    $actions += "delete-root-downloads"
}

if ($issues -contains "canvas-downloads-empty") {
    Write-Host "3. Delete empty canvas-api/downloads/ directory" -ForegroundColor Yellow
    $actions += "delete-canvas-downloads"
}

Write-Host ""
Write-Host ("=" * 80) -ForegroundColor Cyan

# Ask for confirmation
$confirmation = Read-Host "Do you want to proceed with cleanup? (yes/no)"

if ($confirmation -ne "yes" -and $confirmation -ne "y") {
    Write-Host ""
    Write-Host "❌ Cleanup cancelled." -ForegroundColor Red
    exit 1
}

Write-Host ""
Write-Host ("=" * 80) -ForegroundColor Cyan
Write-Host "Executing Cleanup..." -ForegroundColor Green
Write-Host ("=" * 80) -ForegroundColor Cyan
Write-Host ""

# Execute cleanup
$success = $true

try {
    # Action 1: Move output files
    if ($actions -contains "move-output") {
        Write-Host "📦 Moving files from output/ to canvas-api/output/..." -ForegroundColor Cyan
        
        $files = Get-ChildItem $rootOutputPath -File
        foreach ($file in $files) {
            $destPath = Join-Path $canvasApiOutputPath $file.Name
            
            # Check if file already exists in destination
            if (Test-Path $destPath) {
                Write-Host "   ⚠️  File already exists in destination: $($file.Name)" -ForegroundColor Yellow
                Write-Host "      Comparing files..." -ForegroundColor Gray
                
                # Compare file sizes
                $sourceSize = (Get-Item $file.FullName).Length
                $destSize = (Get-Item $destPath).Length
                
                if ($sourceSize -eq $destSize) {
                    Write-Host "      Files are identical - removing duplicate from root" -ForegroundColor Gray
                    Remove-Item $file.FullName -Force
                } else {
                    Write-Host "      Files differ! Keeping both:" -ForegroundColor Yellow
                    $newName = "$($file.BaseName)_from_root$($file.Extension)"
                    $newDestPath = Join-Path $canvasApiOutputPath $newName
                    Move-Item $file.FullName $newDestPath -Force
                    Write-Host "      Moved as: $newName" -ForegroundColor Gray
                }
            } else {
                Move-Item $file.FullName $destPath -Force
                Write-Host "   ✅ Moved: $($file.Name)" -ForegroundColor Green
            }
        }
        
        # Remove empty output directory
        if ((Get-ChildItem $rootOutputPath).Count -eq 0) {
            Remove-Item $rootOutputPath -Force
            Write-Host "   ✅ Removed empty output/ directory" -ForegroundColor Green
        }
    }
    
    # Action 2: Delete root downloads
    if ($actions -contains "delete-root-downloads") {
        Write-Host "🗑️  Deleting empty downloads/ directory from root..." -ForegroundColor Cyan
        Remove-Item $rootDownloadsPath -Force
        Write-Host "   ✅ Deleted: downloads/" -ForegroundColor Green
    }
    
    # Action 3: Delete canvas-api downloads
    if ($actions -contains "delete-canvas-downloads") {
        Write-Host "🗑️  Deleting empty canvas-api/downloads/ directory..." -ForegroundColor Cyan
        Remove-Item $canvasApiDownloadsPath -Force
        Write-Host "   ✅ Deleted: canvas-api/downloads/" -ForegroundColor Green
    }
    
} catch {
    Write-Host ""
    Write-Host "❌ Error during cleanup: $_" -ForegroundColor Red
    $success = $false
}

Write-Host ""
Write-Host ("=" * 80) -ForegroundColor Cyan

if ($success) {
    Write-Host "✅ Cleanup Complete!" -ForegroundColor Green
    Write-Host ""
    Write-Host "New Directory Structure:" -ForegroundColor Yellow
    Write-Host "  canvas-api/" -ForegroundColor Cyan
    Write-Host "    ├── output/          # API metadata (assignments, students)" -ForegroundColor Gray
    Write-Host "    ├── submissions/     # Downloaded submissions (organized by lab)" -ForegroundColor Gray
    Write-Host "    └── scripts...       # Python scripts" -ForegroundColor Gray
    Write-Host ""
    Write-Host "Next Steps:" -ForegroundColor Yellow
    Write-Host "  1. Run: git status" -ForegroundColor Gray
    Write-Host "  2. Verify changes look correct" -ForegroundColor Gray
    Write-Host "  3. Commit if needed" -ForegroundColor Gray
} else {
    Write-Host "❌ Cleanup failed. Please review errors above." -ForegroundColor Red
}

Write-Host ("=" * 80) -ForegroundColor Cyan
