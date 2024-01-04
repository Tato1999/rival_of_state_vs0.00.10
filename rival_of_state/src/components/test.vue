<template>
    <GMapMap
        :center="center"
        :zoom="3"
        style="width: 100vw; height: 100vw"
    >
      <!-- <GMapCluster>
        <GMapMarker
            :key="index"
            v-for="(m, index) in markers"
            :position="m.position"
            :clickable="true"
            :draggable="true"
            @click="center=m.position"
        />
      </GMapCluster> -->
    </GMapMap>
  </template>
  <script>
  export default {
    name: 'App',
    data() {
      return {
        center: {lat: 51.093048, lng: 6.842120},
        markers: [
          {
            position: {
              lat: 51.093048, lng: 6.842120
            },
          }
          , // Along list of clusters
        ]
      }
    }
  }
  </script>
  