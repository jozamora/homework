Sub stockDataEasy()

'********************************************************************
'Jesus Zamora
'This script that will loop through one year of stock data for
'each run and return the total volume each stock had over that year.
'*********************************************************************

'Initialize variables
Dim tickerName As String
Dim volumeTotal As Double
volumeTotal = 0
summaryTableRow = 2

'This code will get us to the last row in worksheet
lastRow = Cells(Rows.Count, 2).End(xlUp).Row

    'Initialize for loop
    For i = 2 To lastRow
        
        'Storing current and next ticker name to compare
        currentTicker = Cells(i, 1).Value
        nextTicker = Cells(i + 1, 1).Value
        
        'If ticker names change then
        If nextTicker <> currentTicker Then
        
            'Prints Ticker and Total Stock Volume in header cells
            Range("I" & 1).Value = "Ticker"
            Range("J" & 1).Value = "Total Stock Volume"
            
            tickerName = Cells(i, 1).Value 'Stores ticker name
            volumeTotal = volumeTotal + Cells(i, 7).Value 'Add to volume total
            
            'Print ticker name and volume in summary table
            Range("I" & summaryTableRow).Value = tickerName
            Range("J" & summaryTableRow).Value = volumeTotal
            
            summaryTableRow = summaryTableRow + 1 'Add one to summary table row
            
            volumeTotal = 0 'reset volume total
        Else
           volumeTotal = volumeTotal + Cells(i, 7).Value 'add to volume total
        End If
    Next i
End Sub