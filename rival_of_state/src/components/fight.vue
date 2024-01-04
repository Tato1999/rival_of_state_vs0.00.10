<template>
    <div class="mainDiv" style="background-color: #0E0000; width:100%; position: absolute; display: grid; top: 0; left: 0;">
        <AppHeader/>
        <div class="dmgBar">
            <div class="attackBarDiv">
                <div class="firstAttackCheckPoint"></div>
                <div class="secondAttackCheckPoint"></div>
                <div></div>
            </div>
            <div class="testDiv">
                <div class="defenceBarDiv">
                    <div class="firstDefenceCheckPoint"></div>
                    <div class="secondDefenceCheckPoint"></div>
                </div>
            </div>
        </div>
        <div class="warInfoDiv">
            <div class="firstStateGerb"></div>
            <div class="firstStateInfo" style="text-align: left;">
                <p>Tbilisi</p>
                <p>Damage:10000000000</p>
            </div>
            <div class="attackButton">Send Trophy</div>
            <div class="warChatDiv"></div>
            <p class="warEndTime">End in 24:00:00</p>
            <div class="secondStateGerb"></div>
            <div class="secondStateInfo" style="text-align: right;">
                <p>Samachablo</p>
                <p>10000000000:Damage</p>
            </div>
            <div class="defenceButton">Send Trophy</div>
            <div class="storageItemDiv">Items In Storage</div>
            <div class="fightManuallyDiv">Fight,200Energy</div>
            <div class="fightAutoPerTenMinute">Auto Every 5 Minute</div>
            <div class="fightAutoPerHour">Auto Every 30 Minute</div>
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
        height: 100% !important;
        background-image: url('/src/assets/png-transparent-flag-flag-countries-flags-spherical-flag-national-flag-spherical 1.png');
        background-size: 100vw 100vh;
    }
    .dmgBar{
        width: 93.75vw;
        height: 8.25vw;
        flex-shrink: 0;
        border-radius: 1.25vw;
        background: #D9D9D9;
        position: absolute;
        margin: 39.75vw auto auto calc((100% - 93.75vw)/2);
    }
    .attackBarDiv{
        width: 50%;
        height: 8.25vw;
        flex-shrink: 0;
        border-radius: 1.25vw 0px 0px 1.25vw;
        background: #FF0202;
        position: absolute;
    }
    .firstAttackCheckPoint{
        width: 7.5vw;
        height: 7.5vw;
        flex-shrink: 0;
        background: url('/src/assets/atack_castle.png');
        background-size: 100% 100%;
        position: absolute;
        bottom: 0;
        margin:auto auto 0px 7.75vw;
    }
    .secondAttackCheckPoint{
        width: 7.5vw;
        height: 7.5vw;
        flex-shrink: 0;
        background: url('/src/assets/atack_castle.png');
        background-size: 100% 100%;
        position: absolute;
        bottom: 0;
        margin:auto auto 0px 26.75vw;
    }
    .testDiv{
        width: 50%;
        height: 8.25vw;
        flex-shrink: 0;
        border-radius: 0px 1.25vw 1.25vw 0px;
        background: #0256ff00; 
        position: absolute;
        margin-left: 50%;
        display: flex;
        justify-content: end;
    }
    .defenceBarDiv{
        width: 100%;
        height: 8.25vw;
        flex-shrink: 0;
        border-radius: 0px 1.25vw 1.25vw 0px;
        background: #0258FF; 
        position: absolute;
        /* margin-left: 50%; */
    }
    .firstDefenceCheckPoint{
        width: 7.5vw;
        height: 7.5vw;
        flex-shrink: 0;
        background: url('/src/assets/def_castle.png');
        background-size: 100% 100%;
        position: absolute;
        margin-left: 11.25vw;
    }
    .secondDefenceCheckPoint{
        width: 7.5vw;
        height: 7.5vw;
        flex-shrink: 0;
        background: url('/src/assets/def_castle.png');
        background-size: 100% 100%;
        position: absolute;
        margin-left: 33.75vw;
    }
    .warInfoDiv{
        width: 92.5vw;
        height: 80vw;
        flex-shrink: 0;
        border-radius: 5vw;
        background: #768C89;
        position: absolute;
        margin: 64vw auto auto calc((100vw - 92.5vw)/2);
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
    .attackButton{
        width: 24.75vw;
        height: 6vw;
        flex-shrink: 0;
        border-radius: 1.25vw;
        background: #FF0202;
        position: absolute;
        margin: 19vw auto auto 5vw;
        color: #FFFCFC;
        font-family: Poppins;
        font-size: 10px;
        font-style: normal;
        font-weight: 400;
        line-height: 6vw;
    }
    .warChatDiv{
        width: 3.75vw;
        height: 3.75vw;
        flex-shrink: 0;
        background: url('/src/assets/chat_icon.png');
        background-size: 100% 100%;
        position: absolute;
        margin: 4vw auto auto calc((100% - 3.75vw)/2);
    }
    .warEndTime{
        color: #FFF;
        font-family: Inter;
        font-size: 6px;
        font-style: normal;
        font-weight: 400;
        line-height: normal;
        position: absolute;
        margin: 10.25vw auto auto calc((100% - 11.25vw)/2);
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
    .defenceButton{
        width: 24.75vw;
        height: 6vw;
        flex-shrink: 0;
        border-radius: 1.25vw;
        background: #0258FF;
        position: absolute;
        margin: 19vw auto auto 62.75vw;
        color: #FFFCFC;
        font-family: Poppins;
        font-size: 10px;
        font-style: normal;
        font-weight: 400;
        line-height: 6vw;
    }
    .storageItemDiv{
        width: 82.5vw;
        height: 11vw;
        flex-shrink: 0;
        background: #b0c7c4;
        position: absolute;
        margin: 29.5vw auto auto calc((100% - 82.5vw)/2);   
    }
    .fightManuallyDiv{
        width: 20vw;
        height: 5vw;
        flex-shrink: 0;
        background: #FF0202;
        position: absolute;
        border-radius: 1vw;
        margin: 47.25vw auto auto 7.5vw;
        color: #FFF;
        font-family: Poppins;
        font-size: 2vw;
        font-style: normal;
        font-weight: 400;
        line-height: 5vw;
    }
    .fightAutoPerTenMinute{
        width: 20vw;
        height: 5vw;
        flex-shrink: 0;
        background: #03530B;
        position: absolute;
        border-radius: 1vw;
        margin: 47.25vw auto auto 35.5vw;
        color: #FFF;
        font-family: Poppins;
        font-size: 2vw;
        font-style: normal;
        font-weight: 400;
        line-height: 5vw;
    }
    .fightAutoPerHour{
        width: 20vw;
        height: 5vw;
        flex-shrink: 0;
        background: #0258FF;
        position: absolute;
        border-radius: 1vw;
        margin: 47.25vw auto auto 63.5vw;
        color: #FFF;
        font-family: Poppins;
        font-size: 2vw;
        font-style: normal;
        font-weight: 400;
        line-height: 5vw;
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