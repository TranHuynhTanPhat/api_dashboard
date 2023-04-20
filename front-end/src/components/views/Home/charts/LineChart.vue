<template>
    <ChartLine :data="data" :options="options" />
</template>
  
<script>
// DataPage.vue
import { Line as ChartLine } from 'vue-chartjs'
import {
    Chart as ChartJS,
    Title,
    Tooltip,
    Legend,
    BarElement,
    CategoryScale,
    LinearScale,
    LineElement,
    PointElement,
    Colors,
    Filler
} from "chart.js";

ChartJS.register(
    Title,
    Tooltip,
    Legend,
    PointElement,
    BarElement,
    CategoryScale,
    LinearScale,
    LineElement,
    Colors,
    Filler
);

export default {
    name: 'LineChart',
    components: { ChartLine },
    props: {
        chartData: {
            type: Object,
            required: true
        }, options: {
            type: Object,
            required: true
        }
    },
    mounted: {
        data: {
            labels: [
                "1",
                "2",
                "3",
                "4",
                "5",
                "6",
                "7"
            ],
            datasets: [
                {
                    label: "Times",
                    data: chartData,
                    backgroundColor: "#ffc107",
                    borderColor: "#ffc107",
                    pointBackgroundColor: "#ffc107",
                    pointBorderColor: "white",
                    pointBorderWidth: 5,
                    pointRadius: 10,
                    tension: 0.3,
                    fill: {
                        target: 'origin',
                        above: 'rgb(255, 0, 0)',   // Area will be red above the origin
                        below: 'rgb(0, 0, 255)'    // And blue below the origin
                    }
                }
            ]
        },
        options: {
            title: {
                display: true,
                text: 'Đồ thị trạng thái Router theo mã toạ độ'
            },
            responsive: true,
            maintainAspectRatio: false,
            filler: {
                propagate: true
            }
        }
    }
}
</script>
  