<template>
    <div class="mainDiv" style="background-color: #0E0000; width:100%; height: 400.5vw; position: absolute; display: grid; top: 0; left: 0;">
        <AppHeader/>
        <div class="regionNameDiv">
            Region: Georgia
        </div>
        <div class="factorySearchFilter" @click="this.openCloseFilter">
            <p>Filter</p>
            <p style="color: rgb(48, 71, 48); font-size: 7vw;"></p>
        </div>
        <factorySearch v-if="this.fillterVisibility"/>
        <div class="allLocalFactoryDiv">
            <p class="allWarDivParagraph">World Active Factorys</p>
            <div v-for="i in [0,1,2,3,4,2,22,2,2,2,2,2,2,22,2,2]" :key="i" class="secondFactoryDiv">
                <div class="secondFactoryOwnerIcon"></div>
                <p class="FactoryName">Factory Name</p>
                <p class="FactoryLevel">Factory Level: 175</p>
                <router-link to="work/factory">
                    <div class="WorkButton">Work</div>
                </router-link>
                <div class="splitLine"></div>
            </div>
        </div>
        <div class="storageDiv">
            Storage
        </div>
        <AppFooterMenu/>
    </div>
  
</template>

<script>
  import AppHeader from './headers/AppHeader.vue'
  import AppFooterMenu from './headers/footerMenu.vue'
  import factorySearch from './headers/filter.vue'
  export default {
    components: {
        AppHeader,
        AppFooterMenu,
        factorySearch
    },
    data(){
        return{
            fillterVisibility: false
        }
    },
    methods:{
        openCloseFilter(){
            this.fillterVisibility = !this.fillterVisibility
            if(this.fillterVisibility){
                document.querySelector(".allLocalFactoryDiv").style.opacity = '0.6'
            }else{
                document.querySelector(".allLocalFactoryDiv").style.opacity = '1'
            }
        }
    }
  }
  </script>

<style>
    .mainDiv{
        height: 291.5vw !important;
        background-image: url('/src/assets/png-transparent-flag-flag-countries-flags-spherical-flag-national-flag-spherical 1.png');
        background-size: 100vw 100vh;
    }
    .allLocalFactoryDiv{
        width: 92.5vw;
        height: 154.75vw;
        flex-shrink: 0;
        border-radius: 5vw;
        background: #6F8B87;
        position: absolute;
        margin: 79.25vw auto auto calc((100vw - 92.5vw)/2);
        overflow-y: auto;
    }
    .regionNameDiv{
        width: 92.5vw;
        height: 8.5vw;
        flex-shrink: 0;
        border-radius: 1.25vw;
        background: #768C89;
        position: absolute;
        margin: 34vw auto auto calc((100vw - 92.5vw)/2);
        color: #FFF;
        text-align: center;
        font-family: Poppins;
        font-size: 3.75vw;
        font-style: normal;
        font-weight: 400;
        line-height: 8.5vw;
    }
    .factorySearchFilter{
        width: 92.5vw;
        height: 8vw;
        flex-shrink: 0;
        border-radius: 1.25vw;
        background: #6F8B87;
        position: absolute;
        margin: 48.25vw auto auto calc((100vw - 92.5vw)/2);
        display: flex;
        justify-content: space-between;
    }
    .factorySearchFilter p{
        margin:0 5vw 0 5vw;
        color: #FFF;
        text-align: center;
        font-family: Poppins;
        font-size: 3.75vw;
        font-style: normal;
        font-weight: 400;
        line-height: 8vw;
    }
    .FactoryName{
        position: absolute;
        margin: 3vw auto auto 26.5vw;
        color: #FFF;
        text-align: center;
        font-family: Play;
        font-size: 3.75vw;
        font-style: normal;
        font-weight: 400;
        line-height: normal;
    }
    .secondFactoryOwnerIcon{
        width: 17.5vw;
        height: 17.5vw;
        margin-left: 4vw;
        position: absolute;
        background-image: url('/src/assets/profile_icon.png');
        background-size: 100% 100%;
    }
    .FactoryLevel{
        position: absolute;
        margin: 9vw auto auto 26.5vw;
        color: #FFF;
        text-align: center;
        font-family: Play;
        font-size: 3.75vw;
        font-style: normal;
        font-weight: 400;
        line-height: normal;
    }
    .WorkButton{
        position: absolute;
        margin: 5.5vw auto auto 71.75vw;
        width: 15.75vw;
        height: 6vw;
        flex-shrink: 0;
        background: #126D10;
        color: #fff;
        text-align: center;
        font-family: Play;
        font-size: 3.75vw;
        font-style: normal;
        font-weight: 400;
        line-height: 6vw;
    }
    .splitLine{
        width: 89vw;
        height: 0.25vw;
        background-color: #000;
        position: absolute;
        margin: 19vw auto auto calc((100% - 89vw)/2);
    }
    .secondFactoryDiv{
        width: 100%;
        height: 20vw;
        overflow-y: auto;
    }
    .storageDiv{
        width: 93.5vw;
        height: 15vw;
        flex-shrink: 0;
        border-radius: 5vw;
        background: #6F8B87;
        position: absolute;
        margin: auto auto 24vw calc((100vw - 93.5vw)/2);
        bottom: 0;
        color: #FFF;
        font-family: Poppins;
        font-size: 5vw;
        font-style: normal;
        font-weight: 700;
        line-height: 15vw;
    }
    
</style>