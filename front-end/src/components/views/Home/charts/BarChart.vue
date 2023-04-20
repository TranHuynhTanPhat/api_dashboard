<template>
  <bar-chart
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
import { Bar as BarChart } from "vue-chartjs";

import {
  Chart as ChartJS,
  Title,
  Tooltip,
  Legend,
  BarElement,
  CategoryScale,
  LinearScale,
} from "chart.js";

ChartJS.register(
  Title,
  Tooltip,
  Legend,
  BarElement,
  CategoryScale,
  LinearScale
);

export default {
  name: "BarChart",
  components: {
    "bar-chart": BarChart,
  },
  props: {
    chartId: {
      type: String,
      default: "bar-chart",
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
        labels: [
          "Angle_id: 1",
          "Angle_id: 2",
          "Angle_id: 3",
          "Angle_id: 4",
          "Angle_id: 5",
          "Angle_id: 6",
          "Angle_id: 7",
        ],
        datasets: [
          {
            label: "Times",
            backgroundColor: "#079dd9",
            borderColor: "#079dd9",
            borderWidth: 1,
            hoverBackgroundColor:"#99d9f2",
            hoverBorderColor:"#99d9f2",
            data: this.$store.state.chartDashboard.count,
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
  