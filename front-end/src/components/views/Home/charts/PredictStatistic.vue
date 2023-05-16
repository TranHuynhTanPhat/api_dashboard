<template>
    <line-chart
      :options="chartOptions"
      :data="chartData"
      :chart-id="chartId"
      :dataset-id-key="datasetIdKey"
      :plugins="plugins"
      :css-classes="cssClasses"
      :styles="styles"
      :width="width"
      :height="height"
    />
  </template>
      
    <script>
  import { Line as LineChart } from "vue-chartjs";
  
  import {
    Chart as ChartJS,
    Title,
    Tooltip,
    Legend,
    LineElement,
    CategoryScale,
    LinearScale,
    PointElement,
  } from "chart.js";
  
  ChartJS.register(
    Title,
    Tooltip,
    Legend,
    LineElement,
    CategoryScale,
    LinearScale,
    PointElement
  );
  
  export default {
    name: "PredictStatistic",
    components: {
      "line-chart": LineChart,
    },
    props: {
      chartId: {
        type: String,
        default: "line-chart",
      },
      datasetIdKey: {
        type: String,
        default: "label",
      },
      width: {
        type: Number,
        default: 400,
      },
      height: {
        type: Number,
        default: 400,
      },
      cssClasses: {
        default: "",
        type: String,
      },
      styles: {
        type: Object,
        default: () => {},
      },
      plugins: {
        type: Array,
        default: () => [],
      },
    },
    data() {
      return {};
    },
    // async mounted() {
    //     const { data } = await axios.get(CHART_TIMES_CHECK)
  
    //     this.chartDataBar.datasets[0].data = data.count
  
    //     console.log(this.chartDataBar)
    // },
    computed: {
      chartData() {
        return {
          labels: this.$store.state.chartDashboard.predicts,
          datasets: [
            {
              label: "Predict_result",
              backgroundColor: "rgb(222, 49, 99)",
              borderColor: "rgb(222, 49, 99)",
              borderWidth: 2,
              borderRadius: 3,
              hoverBackgroundColor: "rgb(222, 49, 99)",
              hoverBorderColor: "rgb(222, 49, 99)",
              pointBorderColor: "white",
              pointBorderWidth: 0,
              pointRadius: 2,
              data: this.$store.state.chartDashboard.predict_values,
            },
          ],
        };
      },
      chartOptions() {
        return {
          responsive: true,
          maintainAspectRatio: false,
          plugins: {
            legend: {
              labels: {
                // This more specific font property overrides the global property
                font: {
                  size: 14,
                },
              },
            },
          },
        };
      },
    },
  };
  </script>
      