let chart = null;

function createChart(labels, values) {
  if (chart) {
    chart.data.labels = labels;
    chart.data.datasets[0].data = values;
    chart.update();
    return;
  }

  const ctx = document.getElementById("myChart");

  chart = new Chart(ctx, {
    type: "line",
    data: {
      labels: labels,
      datasets: [{ label: "Cars", data: values }],
    },
  });
}

htmx.on("htmx:afterSwap", (evt) => {
  const div = document.getElementById("retain");
  const labels = JSON.parse(div.dataset.labels);
  const values = JSON.parse(div.dataset.values);
  createChart(labels, values);
});
