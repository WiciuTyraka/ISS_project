<template>
  <div>
   <apexchart 
     width="500" type="line" 
     :options="options" :series="series">
   </apexchart>  
  </div>
</template>

<script>
export default {
  data: () => ({
    options: {
      chart: {
        id: 'vuechart'
      },
      xaxis: {
        categories: [
         "Jan",
         "Feb",
         "Mar",
         "Apr",
         "May",
         "Jun",
         "Jul",
         "Aug",
         "Sep",
         "Oct",
         "Nov",
         "Dec"
        ]
      }
    },
    series: [{
      name: 'series-1',
      data: []
    }]
  })
}
</script>