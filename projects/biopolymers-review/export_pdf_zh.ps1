$path = "C:\Users\letaotao\Projects\Chemistry\projects\biopolymers-review\Biopolymers-review-DRAFT-ZH.docx"
$pdfPath = "C:\Users\letaotao\Projects\Chemistry\projects\biopolymers-review\Biopolymers-review-DRAFT-ZH.pdf"
$word = New-Object -ComObject Word.Application
$word.Visible = $false
$doc = $word.Documents.Open($path, $false, $true)
$doc.SaveAs([ref]$pdfPath, [ref]17)
$doc.Close([ref]0)
$word.Quit()
Write-Output "done"
