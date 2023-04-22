<template>
  <Doughnut
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
import { Doughnut } from "vue-chartjs";

import {
  Chart as ChartJS,
  Title,
  Tooltip,
  Legend,
  ArcElement,
  CategoryScale,
} from "chart.js";

ChartJS.register(Title, Tooltip, Legend, ArcElement, CategoryScale);

export default {
  name: "DoughnutChart",
  components: {
    Doughnut,
  },
  props: {
    chartId: {
      type: String,
      default: "doughnut-chart",
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
    return {
      chartOptions: {
        responsive: true,
        maintainAspectRatio: false,
      },
    };
  },
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
            backgroundColor: [
              "#C0392B",
              "#9B59B6",
              "#2980B9",
              "#34495E",
              "#27AE60",
              "#F1C40F",
              "#E67E22",
            ],
            data: this.$store.state.chartDashboard.angleId,
            borderAlign: "center",
            borderColor: "transparent",
            borderRadius: 10,
            offset: 50,
            hoverOffset: 100,
            circumference: 180,
            rotation: -90,
          },
        ],
      };
    },
  },
};
</script>
  