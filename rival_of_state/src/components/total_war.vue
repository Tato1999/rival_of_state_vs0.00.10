<template>
    <div class="mainDiv" style="background-color: #0E0000; width:100%; height: 291.5vw; position: absolute; display: grid; top: 0; left: 0;">
        <AppHeader/>
        <div class="allWarDiv">
            <p class="allWarDivParagraph">World Active Wars: 170</p>
            <div v-for="i in [0,1,2,3,4,3,2,33,2,432,32,4,,3,3,3,3,3,3,3,3,3,33,3,3,3,3,3]" class="mainDivOfAllWar">
                <div class="allWarFirstStateGerb"></div>
                <div class="allWarFirstStateInfo" style="text-align: left;">
                    <p>Tbilisi</p>
                    <p>Damage:10000000000</p>
                </div>
                <p class="overalWarDmg">1.000.000.000</p>
                <router-link to="/war/total/fight">
                    <div class="allWarFightButton">
                        Fight
                    </div>
                </router-link>
                <div class="allWarSecondStateGerb"></div>
                <div class="allWarSecondStateInfo" style="text-align: right;">
                    <p>Samachablo</p>
                    <p>10000000000:Damage</p>
                </div>
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
  export default {
    components: {
        AppHeader,
        AppFooterMenu
  }
  }
  </script>

<style scoped>
    .mainDiv{
        height: 291.5vw !important;
        background-image: url('/src/assets/png-transparent-flag-flag-countries-flags-spherical-flag-national-flag-spherical 1.png');
        background-size: 100vw 100vh;
    }
    .allWarDiv{
        width: 92.5vw;
        height: 204vw;
        flex-shrink: 0;
        border-radius: 5vw;
        background: #6F8B87;
        position: absolute;
        margin: 30.25vw auto auto calc((100vw - 92.5vw)/2);
        overflow-y: auto;
    }
    .allWarDivParagraph{
        color: #FFF;
        text-align: center;
        font-family: Play;
        font-size: 5.25vw;
        margin: 3vw auto 10vw auto;
        font-style: normal;
        font-weight: 400;
        line-height: normal;
    }
    .mainDivOfAllWar{
        background-color: rgba(31, 31, 31, 0.05);
        width: 100%;
        height: 10vw;
        margin-top: 2vw;
        display: grid;
    }
    .allWarFirstStateGerb{
        width: 10vw;
        height: 10vw;
        flex-shrink: 0;
        background-image: url('/src/assets/earth_icon.png');
        background-size: 100%;
        position: absolute;
        margin: auto auto auto 1.75vw;
    }
    .allWarFirstStateInfo{
        width: 25vw;
        height: 15vw;
        position: absolute;
        margin: auto auto auto 12vw;
        font-size: 2vw;
    }
    .overalWarDmg{
        font-size: 2.25vw;
        position: absolute;
        margin: 1vw auto auto 38.5vw;
    }
    .allWarFightButton{
        width: 15vw;
        height: 5vw;
        flex-shrink: 0;
        background: #D9D9D9;
        position: absolute;
        margin: 4.25vw auto auto 38.5vw;
        background: #F00;
        color: #FFFDFD;
        font-family: Inter;
        font-size: 3.75vw;
        font-style: normal;
        font-weight: 400;
        line-height: 4.75vw;
    }
    .allWarSecondStateGerb{
        width: 10vw;
        height: 10vw;
        flex-shrink: 0;
        background-image: url('/src/assets/earth_icon.png');
        background-size: 100%;
        position: absolute;
        margin: auto auto auto 80.5vw;
    }
    .allWarSecondStateInfo{
        width: 25vw;
        height: 15vw;
        position: absolute;
        margin: auto 12vw auto auto;
        right: 0;
        font-size: 2vw;
    }
    .allWarMoreButton{
        width: 82.25vw;
        height: 7.5vw;
        flex-shrink: 0;
        border-radius: 1.25vw;
        background: #064D9F;
        position: absolute;
        bottom: 0;
        margin: auto auto 5.5vw calc((100% - 82.25vw)/2);
        color: #FFF;
        text-align: center;
        font-family: Poppins;
        font-size: 3.25vw;
        font-style: normal;
        font-weight: 700;
        line-height: 7.5vw;
    }
    .warInfoDiv{
        width: 92.5vw;
        height: 17.75vw;
        flex-shrink: 0;
        border-radius: 5vw;
        background: #768C89;
        position: absolute;
        margin: 34vw auto auto calc((100vw - 92.5vw)/2);
    }
    .firstStateGerb{
        width: 10vw;
        height: 10vw;
        flex-shrink: 0;
        background-image: url('/src/assets/earth_icon.png');
        background-size: 100%;
        position: absolute;
        margin: 4.25vw auto auto 1.75vw;
    }
    .firstStateInfo{
        width: 25vw;
        height: 15vw;
        position: absolute;
        margin: 4.25vw auto auto 12vw;
        font-size: 2vw;
    }
    .fightButton{
        width: 15vw;
        height: 5vw;
        flex-shrink: 0;
        background: #D9D9D9;
        position: absolute;
        margin: 4.25vw auto auto 38.5vw;
        background: #F00;
        color: #FFFDFD;
        font-family: Inter;
        font-size: 3.75vw;
        font-style: normal;
        font-weight: 400;
        line-height: 4.75vw;
    }
    .secondStateGerb{
        width: 10vw;
        height: 10vw;
        flex-shrink: 0;
        background-image: url('/src/assets/earth_icon.png');
        background-size: 100%;
        position: absolute;
        margin: 4.25vw auto auto 80.5vw;
    }
    .secondStateInfo{
        width: 100%;
        height: 15vw;
        position: absolute;
        margin: 4.25vw 12vw auto auto;
        right: 0;
        font-size: 2vw;
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