function cb () {
    param (
        [Parameter(Mandatory = $true)]
        [string]$SourceFile
    )

    # Ensure file exists
    if (-not (Test-Path $SourceFile)) {
        Write-Error "File not found: $SourceFile"
        return
    }

    $exeName = [System.IO.Path]::GetFileNameWithoutExtension($SourceFile) + ".exe"
    $objName = [System.IO.Path]::GetFileNameWithoutExtension($SourceFile) + ".obj"

    try {
        cl /nologo /EHsc /std:c++latest /O2 /W4 $SourceFile

        if ($LASTEXITCODE -ne 0) {
            return
        }

        & ".\$exeName"
    }
    finally {
        Remove-Item $exeName, $objName -ErrorAction SilentlyContinue
    }
}

Export-ModuleMember -Function cb
