// Jesus Zamora
// Javascript Homework
// This homework should populate the table on the index.html page
// from our data.js form. This code fills the table but does not filter the result.


// from data.js
var tableData = data;

var tbody = d3.select("tbody");



function buildTable(data){
	tbody.html("");
	data.forEach(function(tableData) {
   let row = tbody.append("tr");

   Object.entries(tableData).forEach(function([key, value]) {
     // Append a cell to the row for each value
     // in the weather report object
     let cell = row.append("td");
   });
 });
 
 data.forEach(function(tableData) {
   let row = tbody.append("tr");
   Object.entries(tableData).forEach(function([key, value]) {
     // Append a cell to the row for each value
     // in the weather report object
     let cell = row.append("td");
     cell.text(value);
  });
 });
}

function filterClick(){}

buildTable(tableData);