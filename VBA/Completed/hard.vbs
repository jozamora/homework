Sub stockDataHard()

'********************************************************************
'Jesus Zamora
'This script that will loop through one year of stock data for
'each run and return the ticker name, yearly change, percentage change
'and total stock volume
'*********************************************************************

'Initialize variables
Dim tickerName As String
Dim volumeTotal As Double
volumeTotal = 0
yearlyChange = 0
percentChange = 0
summaryTableRow = 2

'This code will get us to the last row in worksheet
lastRow = Cells(Rows.Count, 2).End(xlUp).Row
openingPrice = Cells(2, 3).Value 'grab the first initial price in sheet

    'Initialize for loop
    For i = 2 To lastRow
        
        
        'Storing current and next ticker name to compare
        currentTicker = Cells(i, 1).Value
        nextTicker = Cells(i + 1, 1).Value
        
        
        
        'If ticker names change then
        If nextTicker <> currentTicker Then
        
            'Prints Ticker and Total Stock Volume in header cells
            Range("I" & 1).Value = "Ticker"
            Range("J" & 1).Value = "Yearly Change"
            Range("K" & 1).Value = "Percent Change (%) "
            Range("L" & 1).Value = "Total Stock Volume"
            
            tickerName = Cells(i, 1).Value 'Stores ticker name
            volumeTotal = volumeTotal + Cells(i, 7).Value 'Add to volume total
            
            closingPrice = Cells(i, 6).Value  'Store closing price
            
            yearlyChange = closingPrice - openingPrice 'Calculate yearly change
            
            'If statement to take care of cases where we are dealing 0 for values
            If openingPrice = 0 And closingPrice = 0 Then
                percentageChange = 0
            ElseIf openingPrice = 0 And closingPrice <> 0 Then
                percentageChange = 1
            Else
                percentChange = (yearlyChange / openingPrice) * 100 'Calculate the percentage change
            End If
            
            'Print ticker name and volume in summary table
            Range("I" & summaryTableRow).Value = tickerName
            Range("J" & summaryTableRow).Value = yearlyChange
            Range("K" & summaryTableRow).Value = percentChange
            Range("L" & summaryTableRow).Value = volumeTotal
            
            'Store value of yearly change to compare
            colorYearly = Range("J" & summaryTableRow).Value
            
            'Comparison to see what color cell should be, 0 is left out so cell should be white
            If colorYearly > 0 Then
                    Range("J" & summaryTableRow).Interior.ColorIndex = 4
            ElseIf colorYearly < 0 Then
                    Range("J" & summaryTableRow).Interior.ColorIndex = 3
            End If
            
            summaryTableRow = summaryTableRow + 1 'Add one to summary table row
            
            openingPrice = Cells(i, 3)
            volumeTotal = 0 'reset volume total
        Else
           volumeTotal = volumeTotal + Cells(i, 7).Value 'add to volume total
        End If
    Next i
    
'Using worksheet functions to return max and min values in column
maxVal = Application.WorksheetFunction.Max(Range("K:K"))
minVal = Application.WorksheetFunction.Min(Range("K:K"))
maxVolume = Application.WorksheetFunction.Max(Range("L:L"))
Cells(2, 16).Value = maxVal
Cells(3, 16).Value = minVal
Cells(4, 16).Value = maxVolume
Range("O" & 2).Value = "Greatest % Increase"
Range("O" & 3).Value = "Greatest % Decrease"
Range("O" & 4).Value = "Greatest Total Volume"
Range("P" & 1).Value = "Value"
Range("Q" & 1).Value = "Ticker"


  
End Sub



