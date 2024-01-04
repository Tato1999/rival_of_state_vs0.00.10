<template>
    <div class="mainDiv" style="background-color: #0E0000; width:100%; height: 1166px; position: absolute; display: grid; top: 0; left: 0;">
        <AppHeader/>
        <div class="globalInfoDiv">
            <router-link to="/map">
                <div class="earthIcon"></div>
            </router-link>
            <div class="globalInfoWorldDiv globalInfoDivSize">
                <p>
                    World
                </p>
                <p style="margin-top: -2vw;">
                    100000
                </p>
                <div class="globalWordImage"></div>
            </div>
            <div class="globalInfoActiveDiv globalInfoDivSize">
                <p>
                    Active
                </p>
                <p style="margin-top: -2vw;">
                    100000
                </p>
                <div class="globalWordImage"></div>

            </div>
            <div class="globalInfoRegionsDiv globalInfoDivSize">
                <p>
                    Regions
                </p>
                <p style="margin-top: -2vw;">
                    100000
                </p>
                <div class="globalWordImage"></div>

            </div>
            <div class="globalInfoStateDiv globalInfoDivSize">
                <p>
                    States
                </p>
                <p style="margin-top: -2vw;">
                    100000
                </p>
                <div class="globalWordImage"></div>

            </div>
        </div>
        <div class="flyDiv">
            <p>From:{{this.flyInfo.from}}</p>
            <p>{{this.formatTime()}}</p>
            <p>To:{{this.flyInfo.to}}</p>
        </div>
        <div class="localInfoDiv">
            <div class="regionInfoDiv" style="position: absolute;">
                <div class="regionGerb">
                </div>
                <div class="regionResident">
                    <p style="margin-top: 10px;">Residents</p>
                    <p style="margin-top: -10px;">10000</p>
                </div>
                <div class="regionParty">
                    <p style="margin-top: 10px;">Residents</p>
                    <p style="margin-top: -10px;">10000</p>
                </div>
                <div class="regionFactory">
                    <p style="margin-top: 10px;">Residents</p>
                    <p style="margin-top: -10px;">10000</p>
                </div>
            </div>
            <div class="localInfoSplitLine"></div>
            <div class="stateInfoDiv" style="position: absolute;">
                <div class="stateGerb"></div>
                <div class="stateResident">
                    <p style="margin-top: 10px;">Residents</p>
                    <p style="margin-top: -10px;">10000</p>
                </div>
                <div class="stateParty">
                    <p style="margin-top: 10px;">Residents</p>
                    <p style="margin-top: -10px;">10000</p>
                </div>
                <div class="stateFactory">
                    <p style="margin-top: 10px;">Residents</p>
                    <p style="margin-top: -10px;">10000</p>
                </div>
            </div>
        </div>
        <div class="warInfoDiv">
            <div class="firstStateGerb"></div>
            <div class="firstStateInfo" style="text-align: left;">
                <p>Tbilisi</p>
                <p>Damage:10000000000</p>
            </div>
            <router-link to="/war/total/fight">
                <div class="fightButton">
                    Fight
                </div>
            </router-link>
            <div class="secondStateGerb"></div>
            <div class="secondStateInfo" style="text-align: right;">
                <p>Samachablo</p>
                <p>10000000000:Damage</p>
            </div>
            <router-link to="/war">
                <div class="totalWarButton">Total Wars</div>
            </router-link>
            <div class="traningButton">Military Training</div>
        </div>
        <div class="chatDiv">
            <div class="userDiv">
                <div v-for="item in [0,1,2,3]" :key="item">
                    <div class="userChatContent" style="margin-top: 10px;">
                        <div class="userGerb"></div>
                            <p class="userName">tato</p>
                            <p class="chatContent">avttftad</p>
                    </div>
                </div>
            </div>
            <div class="commentInputDiv"></div>
            <div class="commentSendDiv">Send</div>
        </div>
        <router-link to="test">
        <div class="storageDiv">
            Storage
        </div>
        </router-link>
        <AppFooterMenu/>

        
        
    </div>
  
</template>

<script>
  import AppHeader from './headers/AppHeader.vue'
  import AppFooterMenu from './headers/footerMenu.vue'
  import axios from 'axios'
  export default {
    components: {
        AppHeader,
        AppFooterMenu
  },
  data(){
    return{
        flyInfo: {},
        // ip: 'http://94.43.110.179:80',
        // ip: 'http://127.0.0.1:80',
        ip: 'http://tato1999.pythonanywhere.com/'
    }
  },
  methods:{
    checkFlyTime(){
        const path = this.ip+"/check_fly"
        axios.post(path,{
            id: localStorage.getItem('id'),
            date: new Date()
        })
        .then((res) => {
            console.log(res)
            this.flyInfo = res.data
            setInterval(() => {
                this.flyInfo.time--
                if(this.flyInfo.time<=0){
                    location.reload();
                }
            },1000)
        })
        .catch((err) => {
            console.log(err)
        })
    },
    formatTime() {
    if (isNaN(this.flyInfo.time)) {
        return "0:00:00";
    }
    const hours = Math.floor(this.flyInfo.time / 3600); // Calculate hours
    const remainingSeconds = this.flyInfo.time % 3600; // Calculate remaining seconds
    const minutes = Math.floor(remainingSeconds / 60); // Calculate minutes
    const seconds = remainingSeconds % 60; // Calculate seconds

    // Format the time string with leading zeros for minutes and seconds
    const formattedTime = `${hours}:${minutes < 10 ? '0' : ''}${minutes}:${seconds < 10 ? '0' : ''}${seconds}`;

    return formattedTime;
}
  },
  mounted(){
    this.checkFlyTime()
  }
  }
  </script>

<style scoped>
    .mainDiv{
        height: 291.5vw !important;
        background-image: url('/src/assets/png-transparent-flag-flag-countries-flags-spherical-flag-national-flag-spherical 1.png');
        background-size: 100vw 100vh;
    }
    .globalInfoDiv{
        width: 92.5%;
        height: 25vw;
        flex-shrink: 0;
        border-radius: 5vw;
        background: #6F8B87;
        position: absolute;
        margin: 35.75vw auto auto calc((100vw - 92.5%)/2);
        align-items: center;
        display: grid;
    }
    .earthIcon{
        width: 17.5vw;
        height: 17.5vw;
        background-image: url('/src/assets/earth_icon.png');
        background-size: 100%;
    }
    .globalInfoDivSize{
        width: 18.25%;
        height: 25vw;
        /* background: red; */
        position: absolute;
    }
    .globalInfoDivSize p{
        color: #FFF;
        font-family: Inter;
        font-size: 3.75vw;
        font-style: normal;
        font-weight: 400;
        line-height: normal;
    }
    .globalInfoWorldDiv{
        margin: auto auto auto 20.75%;
    }
    .globalInfoActiveDiv{
        margin: auto auto auto 39.5%;
    }
    .globalInfoRegionsDiv{
        margin: auto auto auto 58.5%;
    }
    .globalInfoStateDiv{
        margin: auto auto auto 77.5%;
    }
    .globalWordImage{
        background-image: url('/src/assets/citizen-icon-11.png');
        width: 10vw;
        height: 10vw;
        background-size: 100% 100%;
        background-repeat: no-repeat;
        margin: -3.5vw auto auto calc((100% - 10vw)/2);
    }
    .flyDiv{
        width: 45.5%;
        height: 5vw;
        flex-shrink: 0;
        border-radius: 1vw;
        background: #6F8B87;
        position: absolute;
        margin: 62.75vw auto auto calc((100vw - 45.5%)/2);
        align-items: center;
        display: flex;
        justify-content: space-between;
    }
    .flyDiv p{
        /* position: absolute; */
        margin: 1vw;
    }
    .localInfoDiv{
        width: 92.5%;
        height: 40.75vw;
        flex-shrink: 0;
        border-radius: 5vw;
        background: #6F8B87;
        position: absolute;
        margin: 79.5vw auto auto calc((100vw - 92.5%)/2);
        color: #FFF;
        font-family: Inter;
        font-size: 3.75vw;
        font-style: normal;
        font-weight: 400;
        line-height: normal;
    }
    .localInfoSplitLine{
        width: 90vw;
        height: 1.2785vw;
        flex-shrink: 0;
        opacity: 0.5;
        background: #580D0D;
        position: absolute;
        margin: 17.5575vw auto auto calc((100% - 90vw)/2);
    }
    .regionGerb{
        width: 12.5vw;
        height: 12.5vw;
        background-image: url('/src/assets/earth_icon.png');
        background-size: 100%;
        position: absolute;
        margin: 3vw auto auto 2vw;
    }
    .regionResident{
        width: 17.5vw;
        height: 15vw;
        position: absolute;
        margin: 1vw auto auto 18.25vw;
    }
    .regionParty{
        width: 17.5vw;
        height: 15vw;
        position: absolute;
        margin: 1vw auto auto 45.5vw;
    }
    .regionFactory{
        width: 17.5vw;
        height: 15vw;
        position: absolute;
        margin: 1vw auto auto 73vw;
    }
    .stateGerb{
        width: 12.5vw;
        height: 12.5vw;
        background-image: url('/src/assets/earth_icon.png');
        background-size: 100%;
        position: absolute;
        margin: 22.5vw auto auto 2vw;
    }
    .stateResident{
        width: 17.5vw;
        height: 15vw;
        position: absolute;
        margin: 21.185vw auto auto 18.25vw;
    }
    .stateParty{
        width: 17.5vw;
        height: 15vw;
        position: absolute;
        margin: 21.185vw auto auto 45.5vw;
    }
    .stateFactory{
        width: 17.5vw;
        height: 15vw;
        position: absolute;
        margin: 21.185vw auto auto 73vw;
    }
    .warInfoDiv{
        width: 92.5vw;
        height: 40.75vw;
        flex-shrink: 0;
        border-radius: 5vw;
        background: #768C89;
        position: absolute;
        margin: 121.5vw auto auto calc((100vw - 92.5vw)/2);
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
        width: 25vw;
        height: 15vw;
        position: absolute;
        margin: 4.25vw 12vw auto auto;
        right: 0;
        font-size: 2vw;
    }
    .totalWarButton{
        width: 47.25vw;
        height: 9vw;
        flex-shrink: 0;
        background: #342828;
        position: absolute;
        margin: 16.75vw auto auto calc((92.5vw - 47.25vw)/2);
        color: #FEF3F3;
        font-family: Poppins;
        font-size: 3.75vw;
        font-style: normal;
        font-weight: 400;
        line-height: 8.75vw;
    }
    .traningButton{
        width: 47.25vw;
        height: 9vw;
        flex-shrink: 0;
        background: #D9D9D9;
        position: absolute;
        margin: 28.75vw auto auto calc((92.5vw - 47.25vw)/2);
        background: #888383;
        color: #1D0E0E;
        font-family: Poppins;
        font-size: 3.75vw;
        font-style: normal;
        font-weight: 400;
        line-height: 8.75vw;
    }
    .chatDiv{
        width: 92.5vw;
        height: 82vw;
        flex-shrink: 0;
        border-radius: 5vw;
        background: #412F26;
        position: absolute;
        margin: 164.5vw auto auto calc((100vw - 92.5vw)/2);
    }
    .userDiv{
        width:100%;
        display: grid;
        justify-content: left;
    }
    .userGerb{
        width: 7.5vw;
        height: 7.5vw;
        flex-shrink: 0;
        background-image: url('/src/assets/earth_icon.png');
        background-size: 100%;
        margin: 0px auto auto 2.5vw;
        top: 0;
    }
    .userName{
        color: #fff;
        font-family: Poppins;
        font-size: 2.5vw;
        font-style: normal;
        font-weight: 400;
        line-height: normal;
        margin: -7.155vw auto auto 7.5vw;
        top: 0;
    }
    .chatContent{
        color: #fff;
        font-family: Poppins;
        font-size: 3.75vw;
        font-style: normal;
        font-weight: 400;
        line-height: normal;
        top: 0;
        margin: 1.402vw auto auto 15vw;
    }
    .commentInputDiv{
        width: 69.25vw;
        height: 7vw;
        flex-shrink: 0;
        background: #D9D9D9;
        position: absolute;
        margin: auto auto 2.6vw 3vw;
        bottom: 0;
    }
    .commentSendDiv{
        width: 12.25vw;
        height: 7vw;
        flex-shrink: 0;
        background: #D9D9D9;
        position: absolute;
        margin: auto auto 2.6vw 77.5vw;
        bottom: 0;
        color: #000;
        font-family: Inter;
        font-size: 3.75vw;
        font-style: normal;
        font-weight: 400;
        line-height: normal;
        line-height: 7vw;
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