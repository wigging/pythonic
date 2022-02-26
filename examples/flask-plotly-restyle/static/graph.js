
window.onload(showGraph());

function showGraph() {
    var data = [{
        x: [1, 2, 3, 4, 5],
        y: [3, 2.1, 5, 8, 9],
        type: "line"
    }];

    var layout = {
        title: "Example data",
        xaxis: {
            title: "X points"
        },
        yaxis: {
            title: "Y points"
        },
        margin: {l: 50, r: 20, b: 50, t: 40}
    };

    Plotly.newPlot("graphDiv", data, layout);
}

function updateGraph() {

    const formData = new FormData();
    formData.append("xdata", document.getElementsByName("xdata")[0].value);
    formData.append("ydata", document.getElementsByName("ydata")[0].value);

    fetch("/update", {
        method: "POST",
        body: formData
    })
    .then(response => response.json())
    .then(jsonData => {
        var update = {
            x: [jsonData.xValues],
            y: [jsonData.yValues]
        };

        Plotly.restyle("graphDiv", update);
    });

    event.preventDefault();
}
