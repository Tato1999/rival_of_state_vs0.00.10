<template>
    <div class="filterHeader"></div>
    <div class="filterDiv">
        <div v-for="i in this.factoryTypeList" :key="i" class="mainDivOfAllWar textStyle" @click="applyFilter(i)">
                {{i}}
        </div>
    </div>
</template>

<script>
import axios from 'axios'

export default {
    data(){
        return{
            factoryTypeList:['Oil Factory','Coal Factory','Iron Factory','Silver Factory','Gold Factory']
        }
    },
    methods:{
       applyFilter(factoryType) {
      // Check if factoryType is undefined or null before emitting
      console.log(factoryType)
      if (factoryType !== undefined && factoryType !== null) {
        this.$emit('filter', factoryType);
      }
       }
    }
}
</script>

<style>
    .filterHeader{
        width: 19.75vw;
        height: 10.75vw;
        flex-shrink: 0;
        background: #6F8B87;
        position: absolute;
        left: 0;
        margin: 52vw auto auto 76.5vw;
    }
    .filterDiv{
        width: 92.5vw;
        height: 89.75vw;
        flex-shrink: 0;
        border-radius: 2.25vw 0px 2.25vw 2.25vw;
        background: #6F8B87;
        position: absolute;
        left: 0;
        margin: 62.75vw auto auto calc((100% - 92.5vw)/2);
        z-index: 1;
    }
    .textStyle{
        color: #FFF;
        text-align: left;
        font-family: Play;
        font-size: 3.75vw;
        font-style: normal;
        font-weight: 400;
        line-height: 10vw;
        margin-left: 2vw;
    }
</style>