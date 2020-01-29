//Jesus Zamora
// This homework creates a scatter plot using D3 to show the correlation
// between poverty and the lack of healthcare in the USA. Users get a toolTip
// with more in depth information when they hover over the data points. 

var svgWidth = 960;
var svgHeight = 500;

var margin = {
  top: 20,
  right: 40,
  bottom: 60,
  left: 100
};

var width = svgWidth - margin.left - margin.right;
var height = svgHeight - margin.top - margin.bottom;

// svg wrapper point to our scatter div in our html file
var svg = d3.select("#scatter")
  .append("svg")
  .attr("width", svgWidth)
  .attr("height", svgHeight);

var chartGroup = svg.append("g")
  .attr("transform", `translate(${margin.left}, ${margin.top})`);
  
  
d3.csv('assets/data/data.csv').then(function(stateData) {
	
	// read in data
	//==============================
	  stateData.forEach(function(data) {
      data.state = data.state;
      data.abbr = data.abbr;
	  data.poverty = +data.poverty;
	  data.healthcare = +data.healthcare;
	  
    });
	
    // Create scale functions
    // ==============================
    var xLinearScale = d3.scaleLinear()
      .domain([8, d3.max(stateData, d => d.poverty)])
      .range([0, width]);

    var yLinearScale = d3.scaleLinear()
      .domain([4, d3.max(stateData, d => d.healthcare)])
      .range([height, 0]);

    //  Create axis functions
    // ==============================
    var bottomAxis = d3.axisBottom(xLinearScale);
    var leftAxis = d3.axisLeft(yLinearScale);

    //  Append Axes to the chart
    // ==============================
    chartGroup.append("g")
      .attr("transform", `translate(0, ${height})`)
      .call(bottomAxis);

    chartGroup.append("g")
      .call(leftAxis);

    //  Create Circles
    // ==============================
    var circlesGroup = chartGroup.selectAll("circle")
    .data(stateData)
    .enter()
    .append("circle")
    .attr("cx", d => xLinearScale(d.poverty))
    .attr("cy", d => yLinearScale(d.healthcare))
    .attr("r", "7")
    .attr("fill", "SteelBlue")
    .attr("opacity", ".7")
	
    //  Initialize tool tip
    // ==============================
    var toolTip = d3.tip()
      .attr("class", "tooltip")
      
      .html(function(d) {
        return (`${d.state} <br> Poverty: ${d.poverty} <br> Lack Healthcare: ${d.healthcare} `);
      });

    //  Create tooltip in the chart
    // ==============================
    chartGroup.call(toolTip);

    // on mouseover show tooltip
    // ==============================
    circlesGroup.on("mouseover", function(data) {
	  toolTip.show(data, this)
		.style("opacity", "0.9");
	  
    })
      // onmouseout event
      .on("mouseout", function(data, index) {
        toolTip.hide(data);
      });
	
	


    // Create axes labels
    chartGroup.append("text")
      .attr("transform", "rotate(-90)")
      .attr("y", 0 - margin.left+40)
      .attr("x", 0 - (height / 2))
      .attr("dy", "1em")
      .attr("class", "axisText")
      .text("Lacks Healthcare (%)");

    chartGroup.append("text")
      .attr("transform", `translate(${width / 2}, ${height + margin.top + 30})`)
      .attr("class", "axisText")
      .text("In Poverty (%)");
  }).catch(function(error) {
    console.log(error);

})