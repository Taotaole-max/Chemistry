param(
    [string]$Path = "C:\Users\letaotao\Projects\Chemistry\projects\biopolymers-review\Biopolymers-review-DRAFT.docx"
)
$word = New-Object -ComObject Word.Application
$word.Visible = $false
$doc = $word.Documents.Open($Path, $false, $true)

$targets = @(
    "1. Introduction",
    "2. Types of Biopolymers",
    "3. Structure",
    "3.1 Polysaccharides",
    "3.2 Polyesters",
    "3.3 Protein-based",
    "3.4 Lignin",
    "3.5 Natural Rubber",
    "Table 2.",
    "4. Molecular Weight",
    "Table 3.",
    "5. General Property",
    "5.1 Thermal",
    "5.2 Mechanical",
    "5.3 Hydrophilicity",
    "5.4 Degradation",
    "6. Processing",
    "7. Advantages",
    "7.1 Where Biopolymers",
    "7.2 Where They Lose",
    "7.3 Case Study",
    "8. Applications",
    "Table 4.",
    "9. Current Status",
    "10. Conclusions",
    "References",
    "Appendix A"
)

foreach ($t in $targets) {
    $range = $doc.Content.Duplicate
    $find = $range.Find
    $find.ClearFormatting()
    $find.Text = $t
    $find.Forward = $true
    if ($find.Execute()) {
        $page = $range.Information(3)  # wdActiveEndPageNumber
        Write-Output "$t -> page $page"
    } else {
        Write-Output "$t -> NOT FOUND"
    }
}

$totalPages = $doc.ComputeStatistics(2)
Write-Output "TOTAL PAGES: $totalPages"

$doc.Close([ref]0)
$word.Quit()
