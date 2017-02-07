var requi
function init() {
  console.log("Initialized")
  makeChart("../data/counts.csv");
}


function clear() {
  d3.selectAll("svg > *").remove();
}

let swap = false;

function toggleChart() {
  clear();
  if(swap) {
    makeChart("../data/counts.csv")
    swap = !swap;

  } else {
    makeChart("../data/topten.csv");
    swap = !swap
  }
}


function makeChart(csv_path) {

    var constants = {};
    switch (csv_path) {
      case "../data/topten.csv":
        constants.rotate = 0;
        constants.anchor = "center";
        constants.font_size = "20px"
        constants.y_shift = 20;
        constants.title = "Top Ten Skills"
        break;
      case "../data/counts.csv":
        constants.rotate = 90;
        constants.anchor = "start"
        constants.font_size = "14px"
        constants.y_shift = 0;
        constants.title = "Software Engineering Skills"
        break;
    }

    var svg = d3.select("svg"),
        margin = {top: 20, right: 20, bottom: 135, left: 40},
        width = +svg.attr("width") - margin.left - margin.right,
        height = +svg.attr("height") - margin.top - margin.bottom;

    var x = d3.scaleBand().rangeRound([0, width]).padding(0.1),
        y = d3.scaleLinear().rangeRound([height, 0]);

    var g = svg.append("g")
        .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

    d3.csv(csv_path, function(d) {
      d.Percentage = +d.Percentage;
      return d;
    }, function(error, data) {
      if (error) throw error;

      x.domain(data.map(function(d) { return d.Skill; }));
      y.domain([0, d3.max(data,function(d){return d.Percentage})]);

      g.append("g")
          .attr("class", "axis axis--x")
          .attr("transform", "translate(0," + height + ")")
          .call(d3.axisBottom(x))
          .selectAll("text")
          .attr("y", constants.y_shift)
          .attr("x", 9)
          .attr("dy", ".35em")
          .attr("transform","rotate("+constants.rotate+")")
          .style("text-anchor",constants.anchor)
          .style("font-size",constants.font_size);

      g.append("g")
          .attr("class", "axis axis--y")
          .call(d3.axisLeft(y).ticks(10))
        .append("text")
          .attr("transform", "rotate(-90)")
          .attr("y", 6)
          .attr("dy", "0.71em")
          .attr("text-anchor", "end")
          .text("Frequency");

      g.selectAll(".bar")
        .data(data)
        .enter().append("rect")
          .attr("class", "bar")
          .attr("x", function(d) { return x(d.Skill); })
          .attr("y", function(d) { return y(+d.Percentage); })
          .attr("width", x.bandwidth())
          .attr("height", function(d) { return height - y(+d.Percentage); });

      svg.append("text")
          .attr("x", (width / 2))
          .attr("y", margin.top*1.5)
          .attr("text-anchor", "middle")
          .style("font-size", "30px")
          .text(constants.title);

    });


}
