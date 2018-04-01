(function() {
var d3 = Plotly.d3;

var WIDTH_IN_PERCENT_OF_PARENT = 60,
    HEIGHT_IN_PERCENT_OF_PARENT = 80;

var gd3 = d3.select('body')
    .append('div')
    .style({
        width: WIDTH_IN_PERCENT_OF_PARENT + '%',
        'margin-left': (100 - WIDTH_IN_PERCENT_OF_PARENT) / 2 + '%',

        height: HEIGHT_IN_PERCENT_OF_PARENT + 'vh',
        'margin-top': (100 - HEIGHT_IN_PERCENT_OF_PARENT) / 2 + 'vh'
    });

var gd = gd3.node();

var trace1 = {
  x: [0.0, 0.64, -0.58, -0.32, 0.32, -0.8999999999999999, -0.25999999999999995, 0.0, 0.64, -0.58, -0.32, 0.32, -0.8999999999999999, -0.25999999999999995, 0.0, 0.64, -0.58, -0.32, 0.32, -0.8999999999999999, -0.25999999999999995], 
  y: [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2],
  z: [0.0, 14.03910001730775, 3.863137138648348, -7.019550008653876, 7.019550008653875, -3.156412870005528, 10.88268714730222, -12.0, 2.0391000173077485, -8.136862861351652, -19.019550008653876, -4.980449991346125, -15.156412870005527, -1.1173128526977778, 12.0, 26.039100017307746, 15.863137138648348, 4.980449991346124, 19.019550008653873, 8.843587129994471, 22.88268714730222], 
  mode: 'markers',
  marker: {
    size: 12,
    line: {
      color: 'rgba(217, 217, 217, 0.14)',
      width: 0.5
    },
    opacity: 0.8
  },
  type: 'scatter3d'
};

var layout = {
      dragmode: true,
      margin: {
        l: 0,
        r: 0,
        b: 0,
        t: 0
  }};

Plotly.newPlot(gd, [trace1, ], layout, );

window.onresize = function() {
    Plotly.Plots.resize(gd);
};

})();