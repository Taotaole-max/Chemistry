param(
    [string]$Path = "C:\Users\letaotao\Projects\Chemistry\projects\biopolymers-review\Biopolymers-review-DRAFT-ZH.docx"
)
$word = New-Object -ComObject Word.Application
$word.Visible = $false
$doc = $word.Documents.Open($Path, $false, $true)

$targets = @(
    "1. 引言",
    "2. 生物聚合物的类型",
    "3. 主要生物聚合物家族",
    "3.1 多糖",
    "3.2 聚酯",
    "3.3 蛋白质类聚合物",
    "3.4 木质素",
    "3.5 天然橡胶",
    "表 2.",
    "4. 分子量",
    "表 3.",
    "5. 性质的横向规律",
    "5.1 热行为",
    "5.2 力学行为",
    "5.3 亲水性",
    "5.4 降解作为",
    "6. 加工",
    "7. 与合成聚合物相比",
    "7.1 生物聚合物真正占优",
    "7.2 生物聚合物落后",
    "7.3 案例研究",
    "8. 应用",
    "表 4.",
    "9. 当前状态",
    "10. 结论",
    "参考文献",
    "附录 A"
)

foreach ($t in $targets) {
    $range = $doc.Content.Duplicate
    $find = $range.Find
    $find.ClearFormatting()
    $find.Text = $t
    $find.Forward = $true
    if ($find.Execute()) {
        $page = $range.Information(3)
        Write-Output "$t -> page $page"
    } else {
        Write-Output "$t -> NOT FOUND"
    }
}

$totalPages = $doc.ComputeStatistics(2)
Write-Output "TOTAL PAGES: $totalPages"

$doc.Close([ref]0)
$word.Quit()
