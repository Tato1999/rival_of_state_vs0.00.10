<template>
    <loading-overlay v-if="loading" :can-cancel='false' :color="'#000'" :background="'black'">
    </loading-overlay>
    <div v-if="dataLoaded" class="mainDiv" style="background-color: #0E0000; width:100%; height: 1166px; position: absolute; display: grid; top: 0; left: 0;">
        <AppHeader/>
        <div class="profilePictureDiv"></div>
        <div class="energyBar">
            <div class="fillEnergyBarIndicator"></div>
            <p class="energyBarParagraph">Energy: {{this.energy}}/200</p>
        </div>
        <div class="infoBarBackDiv">
            <div class="experienceInformationBackDiv">
                <div class="fillExperienceInformationIndicator"></div>
                <p class="informationDivLevel">LVL: {{ this.level }}</p>
                <p class="informationDivExperience">{{this.experience}}/100EXP</p>
            </div>
            <div class="moneyBackDiv">
                <!-- <div class="fillMoneyIndicator"></div> -->
                <p class="moneyParagraph">Money: {{this.money}}</p>
            </div>
            <div class="goldBarBackDiv">
            <!-- <div class="fillGoldIndicator"></div> -->
            <p class="goldParagraph">Gold: {{this.gold}}</p>
        </div>
        </div>
        <div class="topHeaderControlDiv">
            <div class="chatButtonDiv" @click="this.openCloseChat">Chat</div>
            <div class="chatVisibilityClass">
                <chatInformation/>
            </div>
            <div class="friendButtonDiv" @click="this.openCloseFriend">Friend</div>
            <div class="friendVisibilityClass">
                <friendInformation/>
            </div>
            <div class="informationButtonDiv" @click="this.openCloseInformation">Information</div>
            <div class="infoDivVisibilityClass">
                <profileInformation/>
            </div>
        </div>
        <div class="everyDivVisibilityClass" style="position: absolute;">
            <div class="goldPurchaseDiv">Buy Gold</div>
            <div class="vipPurchaseDiv">Buy Vip</div>
            <div class="perkBackDiv">
                <div class="strenghtBackDiv">
                    <div class="strenghtValue">Strenght: {{this.strenght}}</div>
                    <div class="strenghtButton">Increse Ability</div>
                </div>
                <div class="educationBackDiv">
                    <div class="educationValue">Education: {{ this.education }}</div>
                    <div class="educationButton">Increse Ability</div>
                </div>
                <div class="enduranceBackDiv">
                    <div class="enduranceValue">Endurance: {{ this.endurance }}</div>
                    <div class="enduranceButton">Increse Ability</div>
                </div>
                <div class="boostAbilityInfoDiv">
                    <p class="first">Boost Your Ability  +100: </p>
                    <p class="second">low: Price:10kkk. duration: 5 Hour</p>
                    <p class="third">Hight: Price: 500gold. duration: 24 Hour</p>
                </div>
                <div class="lowBoost">Low Boost</div>
                <div class="hightBoost">Hight Boost</div>
            </div>
            <div class="informationResidPartRegion">
                <div class="regionInformation">
                    <div class="regionIcon"></div>
                    <p class="regionName" @click="this.enterLivingRegion()">Living Region: {{this.data.living_region_name}}</p>
                    <p class="regionState">State: {{this.data.living_region_country}}</p>
                </div>
                <div class="residInformation">
                    <div class="resisRegionIcon" @click="this.enterResRegion()"></div>
                    <p class="residRegionName" @click="this.enterResRegion()">Residental Region: {{this.res_region}}</p>
                    <p class="residRegionState" @click="this.enterResState()">State: {{this.res_state}}</p>
                </div>
                <div class="partyInformation" @click="this.enterParty()">
                    <div class="resisRegionIcon"></div>
                    <p class="residRegionName">Party: {{this.data.party_name}}</p>
                    <p class="residRegionState">Region: {{this.data.party_region}}</p>
                    <div class="checkPermitDiv">Check Work Permit</div>
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
  import profileInformation from './headers/information.vue'
  import friendInformation from './headers/friend.vue'
  import chatInformation from './headers/chat.vue'
  import LoadingOverlay from 'vue-loading-overlay';
  import 'vue-loading-overlay/dist/css/index.css';


  import axios from 'axios'
  export default {
    components: {
        AppHeader,
        AppFooterMenu,
        profileInformation,
        friendInformation,
        chatInformation,
        LoadingOverlay
    },
    data(){
        return{
            data:'',
            loading: true,
            dataLoaded: false,
            openInfoBoolian: false,
            openFriendBoolian: false,
            openChatBoolian: false,
            test:null,
            userName:"",
            money:0,
            gold:0,
            level: 0,
            res_region:'',
            res_state:'',
            experience:0,
            strenght:0,
            education:0,
            endurance:0,
            premium:0,
            friends_count:0,
            damage:0,
            working_experience:0,
            max_experience:0,
            // ip: 'http://94.43.110.179:80',
            // ip: 'http://127.0.0.1:80',
            ip: 'http://tato1999.pythonanywhere.com/'
        }
    },
    methods:{
        sendIdInfo(){
            //  const path = 'http://192.168.1.2:80/profile';
            //  const path = 'http://192.168.54.172:80/profile'
            // const path = 'http://192.168.4.48:80/profile'
            const path = this.ip+'/profile'

             axios.post(path,{
                id: localStorage.getItem('id'),
                energy: -1
             })
             .then((res) => {
                console.log(res.data)
                 this.data = res.data
                 console.log(res.data.gold)
                 this.level = res.data.level
                 this.energy = res.data.energy
                 this.money = res.data.money
                 this.userName = res.data.name
                 this.res_region = res.data.res_region
                 this.res_state = res.data.res_state
                 this.experience = res.data.experience
                 this.strenght = res.data.strenght
                 this.education = res.data.education
                 this.endurance = res.data.endurance
                 this.premium = res.data.premium
                 this.friends_count = res.data.friends_count
                 this.damage = res.data.damage
                 this.working_experience = res.data.working_experience
                 this.max_experience = res.data.max_experience
                 this.gold = res.data.gold

                 let exp_percent = (100*this.experience)/100
                 this.dataLoaded = true
                 this.loading = false
                //  console.log(res.data)
                 setTimeout(() => {
                    document.querySelector('.fillExperienceInformationIndicator').style.width = exp_percent+"%"
                    document.querySelector('.fillEnergyBarIndicator').style.width = res.data.energy/2 + '%'
                 },10)
                })
             .catch((err) => {
                 console.error(err)
             })
         },
         getProfileInfo(){
            // const path = 'http://192.168.54.172:80/profile'

            const path = this.ip+'/profile'
        //  const path = 'http://192.168.4.48:80/profile'
            axios.get(path)
             .then((res) => {
                 console.log(res.data)
             })
             .catch((err) => {
                 console.error(err)
             })
         },
    
        openCloseInformation(){
            if(this.openInfoBoolian == false){
                document.querySelector('.infoDivVisibilityClass').style.display = 'inline'
                document.querySelector('.chatVisibilityClass').style.display = 'none'
                document.querySelector('.everyDivVisibilityClass').style.display = 'none'
                document.querySelector('.friendVisibilityClass').style.display = 'none' 
                this.openInfoBoolian = true
                this.openFriendBoolian = false
                this.openChatBoolian = false
            }
            else{
                document.querySelector('.infoDivVisibilityClass').style.display = 'none'
                document.querySelector('.everyDivVisibilityClass').style.display = 'inline'
                this.openInfoBoolian = false
            }
        },
        openCloseFriend(){
            if(this.openFriendBoolian == false){
                document.querySelector('.friendVisibilityClass').style.display = 'inline'
                document.querySelector('.chatVisibilityClass').style.display = 'none'
                document.querySelector('.everyDivVisibilityClass').style.display = 'none'
                document.querySelector('.infoDivVisibilityClass').style.display = 'none'
                this.openFriendBoolian = true
                this.openInfoBoolian = false
                this.openChatBoolian = false
            }
            else{
                document.querySelector('.friendVisibilityClass').style.display = 'none'
                document.querySelector('.everyDivVisibilityClass').style.display = 'inline'
                this.openFriendBoolian = false
            }
        },
        openCloseChat(){
            if(this.openChatBoolian == false){
                document.querySelector('.chatVisibilityClass').style.display = 'inline'
                document.querySelector('.friendVisibilityClass').style.display = 'none'
                document.querySelector('.everyDivVisibilityClass').style.display = 'none'
                document.querySelector('.infoDivVisibilityClass').style.display = 'none'
                this.openChatBoolian = true
                this.openFriendBoolian = false
                this.openInfoBoolian = false
            }
            else{
                document.querySelector('.chatVisibilityClass').style.display = 'none'
                document.querySelector('.everyDivVisibilityClass').style.display = 'inline'
                this.openChatBoolian = false
            }
        },
        enterLivingRegion(){
            const path = this.ip+'/enter_living_region'
            axios.post(path,{
                id: localStorage.getItem('id')
            })
            .then((res) => {
                console.log(res)
                this.$router.push({
                    path: `/region/${res.data.regionId}` 
                })
            })
            .catch((err) => {
                console.log(err)
            })
        },
        enterResRegion(){
            const path = this.ip+'/enter_residental_region'
            axios.post(path,{
                id: localStorage.getItem('id')
            })
            .then((res) => {
                console.log(res)
                this.$router.push({
                    path: `/region/${res.data.resRegionId}` 
                })
            })
            .catch((err) => {
                console.log(err)
            })
        },
        enterResState(){
            if(this.res_state != "None"){
                const path = this.ip+'/enter_residental_state'
                axios.post(path,{
                    id: localStorage.getItem('id')
                })
                .then((res) => {
                    console.log(res)
                    this.$router.push({
                        path: `/state/${res.data.resStateId}` 
                    })
                })
                .catch((err) => {
                    console.log(err)
                })
            }
        },
        enterParty(){
            this.$router.push({
                path: `/party/${this.data.party_id}` 
            })
        }
    },
    mounted(){
        this.sendIdInfo()
    }
  }
  </script>

<style scoped>
    .mainDiv{
        height: 291.5vw !important;
        background-image: url('/src/assets/png-transparent-flag-flag-countries-flags-spherical-flag-national-flag-spherical 1.png');
        background-size: 100vw 100vh;
    }
    .infoDivVisibilityClass{
        display: none;
    }
    .friendVisibilityClass{
        display: none;
    }
    .chatVisibilityClass{
        display: none;
    }
    .profilePictureDiv{
        width: 37.5vw;
        height: 37.5vw;
        background-color: red;
        position:absolute;
        border-radius: 5vw;
        margin: 28.25vw auto auto 6.25vw;
        background-image: url('/src/assets/profile_picture_1.png');
        background-size: 100% 100%;
    }
    .energyBar{
        width: 29.75vw;
        height: 4.5vw;
        flex-shrink: 0;
        background: #D9D9D9;
        display:flex;
        position: absolute;
        transform:rotateZ(270deg);
        margin: 44.5vw auto auto 34.5vw;
    }
    .fillEnergyBarIndicator{
        width: 100%;
        height: 4.5vw;
        flex-shrink: 0;
        background: #FFA903;
        display:flex;
        position: absolute;
    }
    .energyBarParagraph{
        position: absolute;
        display: grid;
        margin: 0;
        color: #2D2516;
        text-align: center;
        font-family: Play;
        font-size: 2.75vw;
        font-style: normal;
        font-weight: 400;
        line-height: 4.5vw;
        margin-left: calc((100% - 18vw)/2);
    }
    .infoBarBackDiv{
        width: 40.5vw;
        height: 30vw;
        position: absolute;
        margin: 31.8vw auto auto 53.25vw;
    }
    .experienceInformationBackDiv{
        width: 40.6vw;
        height: 5vw;
        background: #D9D9D9;
        position: absolute;
        margin-top: 0;
    }
    .fillExperienceInformationIndicator{
        width: 90%;
        height: 5vw;
        flex-shrink: 0;
        background: #9AB293;
        position: absolute;
    }
    .informationDivLevel{
        position: absolute;
        color: #754D4D;
        text-align: center;
        font-family: Play;
        font-size: 2.75vw;
        font-style: normal;
        font-weight: 400;
        line-height: 5vw;
        margin: 0 auto auto 2vw;
    }
    .informationDivExperience{
        position: absolute;
        color: #754D4D;
        text-align: center;
        font-family: Play;
        font-size: 2.75vw;
        font-style: normal;
        font-weight: 400;
        line-height: 5vw;
        margin: 0 auto auto 19.25vw;
    }
    .moneyBackDiv{
        width: 40.5vw;
        height: 5vw;
        flex-shrink: 0;
        background: #9AB293;
        position: absolute;
        margin-top: 12.75vw;
    }
    .moneyParagraph{
        color: #754D4D;
        text-align: center;
        font-family: Play;
        font-size: 2.75vw;
        font-style: normal;
        font-weight: 400;
        line-height: 5vw;
        margin: 0;
    }
    .goldBarBackDiv{
        width: 40.5vw;
        height: 5vw;
        flex-shrink: 0;
        background: #9AB293;
        position: absolute;
        margin-top: 25vw;
    }
    .goldParagraph{
        color: #754D4D;
        text-align: center;
        font-family: Play;
        font-size: 2.75vw;
        font-style: normal;
        font-weight: 400;
        line-height: 5vw;
        margin: 0;
    }
    .topHeaderControlDiv{
        width: 100%;
        height: 7.5vw;
        /* background: red; */
        position: absolute;
        margin-top: 71.75vw;
    }
    .chatButtonDiv{
        cursor: pointer;
        width: 25vw;
        height: 7.5vw;
        flex-shrink: 0;
        border-radius: 1.25vw;
        background: #D9D9D9;
        position: absolute;
        margin-left: 6.25vw;
        color: #000;
        text-align: center;
        font-family: Play;
        font-size: 3.75vw;
        font-style: normal;
        font-weight: 400;
        line-height: 7.5vw;
    }
    .friendButtonDiv{
        cursor: pointer;
        width: 25vw;
        height: 7.5vw;
        flex-shrink: 0;
        border-radius: 1.25vw;
        background: #D9D9D9;
        position: absolute;
        margin-left: 38vw;
        color: #000;
        text-align: center;
        font-family: Play;
        font-size: 3.75vw;
        font-style: normal;
        font-weight: 400;
        line-height: 7.5vw;
    }
    .informationButtonDiv{
        cursor: pointer;
        width: 25vw;
        height: 7.5vw;
        flex-shrink: 0;
        border-radius: 1.25vw;
        background: #D9D9D9;
        position: absolute;
        margin-left: 69.25vw;
        color: #000;
        text-align: center;
        font-family: Play;
        font-size: 3.75vw;
        font-style: normal;
        font-weight: 400;
        line-height: 7.5vw;
    }
    .goldPurchaseDiv{
        width: 88vw;
        height: 7.5vw;
        flex-shrink: 0;
        border-radius: 1.25vw;
        background: #FFA903;
        position: absolute;
        margin: 85.25vw auto auto calc((100vw - 88vw)/2);
        color: #FFFDFD;
        text-align: center;
        font-family: Play;
        font-size: 5vw;
        font-style: normal;
        font-weight: 400;
        line-height: 7.5vw;
    }
    .vipPurchaseDiv{
        width: 88vw;
        height: 7.5vw;
        flex-shrink: 0;
        border-radius: 1.25vw;
        background: #87C9A9;
        position: absolute;
        margin: 94.75vw auto auto calc((100vw - 88vw)/2);
        color: #FFFDFD;
        text-align: center;
        font-family: Play;
        font-size: 5vw;
        font-style: normal;
        font-weight: 400;
        line-height: 7.5vw;
    }
    .perkBackDiv{
        width: 88vw;
        height: 63vw;
        flex-shrink: 0;
        border-radius: 2.5vw;
        background: #9BABA9;
        position: absolute;
        margin: 106vw auto auto calc((100vw - 88vw)/2);
    }
    .strenghtBackDiv{
        width: 100%;
        height: 8.25vw;
        border-radius: 1.25vw;
        /* background: #fb0303; */
        position: absolute;
        margin-top: 4.5vw;
        color: #FFF;
        text-align: center;
        font-family: Play;
        font-size: 5vw;
        font-style: normal;
        font-weight: 400;
        line-height: 8.25vw;
    }
    .strenghtValue{
        width: 47.7vw;
        height: 8.25vw;
        border-radius: 1.25vw;
        background: #3F3131;
        margin: auto auto auto 1.5vw;
        position: absolute;
    }
    .strenghtButton{
        width: 33.25vw;
        height: 8.25vw;
        border-radius: 1.25vw;
        background: #3F3131;
        position: absolute;
        right: 0;
        margin: auto 2.5vw auto auto;
    }
    .educationBackDiv{
        width: 100%;
        height: 8.25vw;
        border-radius: 1.25vw;
        /* background: #fb0303; */
        position: absolute;
        margin-top: 15.5vw;
        color: #FFF;
        text-align: center;
        font-family: Play;
        font-size: 5vw;
        font-style: normal;
        font-weight: 400;
        line-height: 8.25vw;
    }
    .educationValue{
        width: 47.7vw;
        height: 8.25vw;
        border-radius: 1.25vw;
        background: #3F3131;
        margin: auto auto auto 1.5vw;
        position: absolute;
    }
    .educationButton{
        width: 33.25vw;
        height: 8.25vw;
        border-radius: 1.25vw;
        background: #3F3131;
        position: absolute;
        right: 0;
        margin: auto 2.5vw auto auto;
    }
    .enduranceBackDiv{
        width: 100%;
        height: 8.25vw;
        border-radius: 1.25vw;
        /* background: #fb0303; */
        position: absolute;
        margin-top: 26.5vw;
        color: #FFF;
        text-align: center;
        font-family: Play;
        font-size: 5vw;
        font-style: normal;
        font-weight: 400;
        line-height: 8.25vw;
    }
    .enduranceValue{
        width: 47.7vw;
        height: 8.25vw;
        border-radius: 1.25vw;
        background: #3F3131;
        margin: auto auto auto 1.5vw;
        position: absolute;
    }
    .enduranceButton{
        width: 33.25vw;
        height: 8.25vw;
        border-radius: 1.25vw;
        background: #3F3131;
        position: absolute;
        right: 0;
        margin: auto 2.5vw auto auto;
    }
    .boostAbilityInfoDiv{
        width: 84vw;
        height: 12.25vw;
        flex-shrink: 0;
        border-radius: 1.25vw;
        background: #3F3131;
        margin: 36.5vw auto auto calc((100% - 84vw)/2);
        color: #FFF;
        text-align: center;
        font-family: Play;
        font-size: 2.75vw;
        font-style: normal;
        font-weight: 400;
        line-height: normal;
    }
    .boostAbilityInfoDiv p{
        position: absolute;
    }
    .first{
        margin: 4.475vw auto auto 0.5vw;
    }
    .second{
        margin: 1.5vw auto auto 35.25vw;
    }
    .third{
        margin: 7.25vw auto auto 33.5vw
    }
    .lowBoost{
        width: 40vw;
        height: 7.5vw;
        flex-shrink: 0;
        background: #754D4D;
        border-radius: 1.25vw;
        margin: auto auto 4vw 1.5vw;
        color: #FFF;
        text-align: center;
        font-family: Play;
        font-size: 5vw;
        font-style: normal;
        font-weight: 400;
        line-height: 7.5vw;
        bottom: 0;
        top: 0;
        position: absolute;
    }
    .hightBoost{
        width: 40vw;
        height: 7.5vw;
        flex-shrink: 0;
        background: #754D4D;
        border-radius: 1.25vw;
        margin: auto auto 4vw 45.5vw;
        color: #FFF;
        text-align: center;
        font-family: Play;
        font-size: 5vw;
        font-style: normal;
        font-weight: 400;
        line-height: 7.5vw;
        position: absolute;
        top: 0;
        bottom: 0;
    }
    .informationResidPartRegion{
        width: 88vw;
        height: 55.5vw;
        flex-shrink: 0;
        background-color: #9BB2AF;
        border-radius: 2.5vw;
        position: absolute;
        margin: 175.75vw auto auto calc((100vw - 88vw)/2);
    }
    .regionInformation{
        width: 100%;
        height: 12.5vw;
        /* background-color: red; */
        position: absolute;
        margin-top: 1vw;
    }
    .regionInformation p{
        position: absolute;
        /* margin: 0;
         */
         margin: 0 auto auto 20.57vw;
    }
    .regionIcon{
        width: 12.5vw;
        height: 12.5vw;
        background-image: url('/src/assets/profile_icon.png');
        background-size: 100% 100%;
        position: absolute;
        margin-left: 4.25vw;
        /* background-color: #000; */
    }
    .regionName{
        color: #000;
        text-align: center;
        font-family: Play;
        font-size: 3.75vw;
        font-style: normal;
        font-weight: 400;
        line-height: normal;
        margin-top: 2vw !important;
    }
    .regionState{
        color: #595454;
        text-align: center;
        font-family: Play;
        font-size: 3.25vw;
        font-style: normal;
        font-weight: 400;
        line-height: normal;
        margin-top: 7.25vw !important;
    }
    .residInformation{
        width: 100%;
        height: 12.5vw;
        /* background-color: red; */
        position: absolute;
        margin-top: 15.25vw;
    }
    .resisRegionIcon{
        width: 12.5vw;
        height: 12.5vw;
        background-image: url('/src/assets/profile_icon.png');
        background-size: 100% 100%;
        position: absolute;
        margin-left: 4.25vw;
        /* background-color: #000; */
    }
    .residInformation p{
        position: absolute;
        /* margin: 0;
         */
         margin: 0 auto auto 20.57vw;
    }
    .residRegionName{
        color: #000;
        text-align: center;
        font-family: Play;
        font-size: 3.75vw;
        font-style: normal;
        font-weight: 400;
        line-height: normal;
        margin-top: 2vw !important;
    }
    .residRegionState{
        color: #595454;
        text-align: center;
        font-family: Play;
        font-size: 3.25vw;
        font-style: normal;
        font-weight: 400;
        line-height: normal;
        margin-top: 7.25vw !important;
    }
    .partyInformation{
        width: 100%;
        height: 12.5vw;
        /* background-color: red; */
        position: absolute;
        margin-top: 29.5vw;
    }
    .partyInformation p{
        position: absolute;
        /* margin: 0;
         */
         margin: 0 auto auto 20.57vw;
    }
    .checkPermitDiv{
        position: absolute;
        width: 37.5vw;
        height: 7vw;
        flex-shrink: 0;
        border-radius: 1.25vw;
        background: #D9D9D9;
        margin: 15.25vw auto auto calc((100% - 37.5vw)/2);
        color: #000;
        text-align: center;
        font-family: Play;
        font-size: 3.75vw;
        font-style: normal;
        font-weight: 400;
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