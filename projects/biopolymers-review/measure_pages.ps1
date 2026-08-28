param(
    [string]$Path = "C:\Users\letaotao\Projects\Chemistry\projects\biopolymers-review\Biopolymers-review-DRAFT.docx"
)
$word = New-Object -ComObject Word.Application
$word.Visible = $false
$doc = $word.Documents.Open($Path, $false, $true)
$totalPages = $doc.ComputeStatistics(2)   # wdStatisticPages
$totalWords = $doc.ComputeStatistics(0)   # wdStatisticWords

# Find the References *heading* paragraph, not the word "References" wherever it appears in
# body text (§7.3 cites "... expanded in the References [10,18-32]", which the old plain-text
# Find matched instead — it under-reported the body by ~2 pages). The heading paragraph is the
# only one whose text *starts* with "References " followed by the italic count note.
$refsPage = -1
foreach ($p in $doc.Paragraphs) {
    $txt = $p.Range.Text.Trim()
    # The "References" heading is now clean ("## References"); it is the only paragraph in the
    # built doc that is exactly "References" (the §7.3 in-text mention was reworded away).
    if ($txt -ceq 'References') {
        $refsPage = $p.Range.Information(3)
        break
    }
}

Write-Output "Total pages: $totalPages"
Write-Output "Total words: $totalWords"
if ($refsPage -gt 0) {
    Write-Output "References section starts on page: $refsPage"
    Write-Output "Body page count (excl. references): $($refsPage - 1)"
} else {
    Write-Output "Could not locate References heading."
}

$doc.Close([ref]0)
$word.Quit()
