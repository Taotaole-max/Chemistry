param(
    [string]$Path = "C:\Users\letaotao\Projects\Chemistry\projects\biopolymers-review\Biopolymers-review-DRAFT.docx"
)
$word = New-Object -ComObject Word.Application
$word.Visible = $false
$doc = $word.Documents.Open($Path, $false, $true)
$totalPages = $doc.ComputeStatistics(2)   # wdStatisticPages
$totalWords = $doc.ComputeStatistics(0)   # wdStatisticWords

$refsPage = -1
$find = $doc.Content.Find
$find.ClearFormatting()
$find.Text = "References"
if ($find.Execute()) {
    $refsPage = $find.Parent.Information(3)  # wdActiveEndPageNumber
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
