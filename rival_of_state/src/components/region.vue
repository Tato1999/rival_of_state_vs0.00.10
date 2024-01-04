<template>
    <div class="mainDiv" style="background-color: #0E0000; width:100%; height: 1166px; position: absolute; display: grid; top: 0; left: 0;">
        <AppHeader/>
            <div class="infoMainDiv">
                <div class="regionDiv">
                    <div class="regionIcon"></div>
                     <!-- :style="{backgroundImage:`url(${require('@/assets/regionIcon/'+this.data.gerb)})`}" -->
                    <div class="names">
                        <div class="regionName">{{this.data.name}}</div>
                        <div class="regionState">{{this.data.country}}</div>
                        <div v-if="this.data.country == 'None' && this.livingRegionId == this.data.name && this.resRegionId == this.data.id" class="makeState" @click="this.makeTheState()">Make State</div>
                    </div>
                    <div class="regionDivAdditionalInfo">
                        <div class="regionResidents regionDivAdditionalInfoClass">
                            <div class="regionAdditionalDivName">Residents</div>
                            <div class="regionAdditionalDivValue">{{this.data.residendalCount}}</div>
                        </div>
                        <div class="regionCitizens regionDivAdditionalInfoClass">
                            <div class="regionAdditionalDivName">Citizens</div>
                            <div class="regionAdditionalDivValue">{{ this.data.liverCount }}</div>
                        </div>
                        <div class="regionParty regionDivAdditionalInfoClass" @click="this.enterRegionalParty()">
                            <div class="regionAdditionalDivName">Party</div>
                            <div class="regionAdditionalDivValue">{{this.data.party}}</div>
                        </div>
                        <div class="regionFactory regionDivAdditionalInfoClass">
                            <div class="regionAdditionalDivName">Factory</div>
                            <div class="regionAdditionalDivValue">{{ this.data.factory }}</div>
                        </div>
                    </div>
                </div>
                <div class="actionDiv">
                    <div class="actionDivClass actionFly" @click="this.starTravel()">Fly</div>
                    <div class="actionDivClass actionTravel">Car Travel</div>
                    <div class="actionDivClass actionSeeOnMap" @click="this.createParty()">Create PArty</div>
                    <div class="actionDivClass actionResRequest" @click="this.sendResidencyRequest()">Send Residency Request</div>
                </div>
                <div class="indexDiv">
                    <div class="indexDivClass medicalIndexDiv">
                        <div class="idexDivName">Medicine</div>
                        <div class="indexDivValue">{{this.data.medicinIndex}}/10</div>
                    </div>
                    <div class="indexDivClass educationIndexDiv">
                        <div class="idexDivName">Education</div>
                        <div class="indexDivValue">{{this.data.educationIndex}}/10</div>
                    </div>
                    <div class="indexDivClass militaryIndexDiv">
                        <div class="idexDivName">Military</div>
                        <div class="indexDivValue">{{this.data.militaryIndex}}/10</div>
                    </div>
                    <div class="indexDivClass developmentIndexDiv">
                        <div class="idexDivName">Depelopment</div>
                        <div class="indexDivValue">{{this.data.developmentIndex}}/10</div>
                    </div>
                </div>
                <div class="buildingInfo">
                    <div class="buildingDivClass hospitalDiv">
                        <div class="buildingDivName">Hospital</div>
                        <div class="buildingDivValue">{{this.data.clinicsCount}}</div>
                    </div>
                    <div class="buildingDivClass schoolDiv">
                        <div class="buildingDivName">School</div>
                        <div class="buildingDivValue">{{this.data.schoolsCount}}</div>
                    </div>
                    <div class="buildingDivClass militaryBaseDiv">
                        <div class="buildingDivName">Military Base</div>
                        <div class="buildingDivValue">{{this.data.militaryBases}}</div>
                    </div>
                    <div class="buildingDivClass houseDiv">
                        <div class="buildingDivName">House</div>
                        <div class="buildingDivValue">{{this.data.house}}</div>
                    </div>
                    <div class="buildingDivClass nuclearPowerDiv">
                        <div class="buildingDivName">Nuclear Power Plant</div>
                        <div class="buildingDivValue">{{this.data.hesCount}}</div>
                    </div>
                </div>
                <div class="workersInfo">
                    <div class="workerDivClass teacherDiv">
                        <div class="workerDivName">Teachers</div>
                        <div class="workerDivValue">{{this.data.teachersCount}}</div>
                    </div>
                    <div class="workerDivClass doctorDiv">
                        <div class="workerDivName">Doctors</div>
                        <div class="workerDivValue">{{this.data.doctorsCount}}</div>
                    </div>
                    <div class="workerDivClass generalDiv">
                        <div class="workerDivName">Generals</div>
                        <div class="workerDivValue">{{this.data.generalCount}}</div>
                    </div>
                    <div class="workerDivClass defensiveSystemDiv">
                        <div class="workerDivName">Defensive System</div>
                        <div class="workerDivValue">{{this.data.defenceSystems}}</div>
                    </div>
                    <div class="moreInfoButton">Detailed Information</div>
                </div>
            </div>
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
        AppFooterMenu,
    },
    data(){
        return{
           data: {},
           regionImage: '/src/assets/geoGerb.gif',
        //    ip: 'http://94.43.110.179:80',
        //    ip: 'http://127.0.0.1:80',
            ip: 'http://tato1999.pythonanywhere.com/',
        //    backgroundImage: `url(${require('@/assets/regionIcon/andora.jpeg')})`
        //    backgroundImage: 'geoGerb.gif'
           citizen: 0,
           livingRegionId: '',
           resRegionId:''
        }
    },
    methods:{
        getRegionInformation(){
            // const path = 'http://192.168.1.2:80/get_region_info'
            // const path = 'http://192.168.0.23:80/get_region_info'
            // const path = 'http://127.0.0.1:80/get_region_info'
            const path = this.ip+'/get_region_info_region'
            axios.post(path,{
                id: this.$route.params.id
            })
            .then((res) => {
                this.data = res.data
                console.log(this.data)
                document.querySelector('.regionIcon').style.backgroundImage = `url(${require('@/assets/regionIcon/'+this.data.gerb)})`
                // this.backgroundImage = this.data.gerb
            })
            .catch((err) => {
                console.error(err)
                this.err = err
            })
        },
        getLivingRegion(){
            const path = this.ip+'/enter_res_region'
            axios.post(path,{
                id: localStorage.getItem('id')
            })
            .then((res) => {
                console.log(res)
                this.livingRegionId = res.data.regionId
                this.resRegionId = res.data.livingRegion
            })
            .catch((err) => {
                console.log(err)
            })
        },
        starTravel(){
            const path = this.ip+'/start_fly'
            axios.post(path,{
                myId: localStorage.getItem('id'),
                region: this.$route.params.id
            })
            .then((res) => {
                console.log(res)
                this.data.liverCount = res.data.citizen
            })
            .catch((err) => {
                console.log(err)
            })
        },
        makeTheState(){
            const path = this.ip+'/create_state'
            axios.post(path,{
                id: this.resRegionId,
                date: new Date()
            })
            .then((res) => {
                console.log(res)
                this.$router.push({
                    path: `/state/${res.data.id}` })
            })
            .catch((err) => {
                console.log(err)
            })
        },
        sendResidencyRequest(){
            const path = this.ip+'/send_residancy'
            axios.post(path,{
                myId: localStorage.getItem('id'),
                region: this.$route.params.id
            })
            .then((res) => {
                console.log(res)
                this.data.residendalCount = res.data.residental
            })
            .catch((err) => {
                console.log(err)
            })
        },
        createParty(){
            const path = this.ip+'/create_party'
            axios.post(path,{
                id:localStorage.getItem('id'),
                region: this.$route.params.id
            })
            .then((res) => {
                console.log(res)
                if(res.data.id != 0){
                    this.$router.push({
                        path: `/party/${res.data['id']}` 
                    })
                }else{
                    alert(res.data.Res)
                }
            })
            .catch((err) => {
                console.log(err)
            })
        },
        enterRegionalParty(){
            this.$router.push({
                path: `/party/region/${this.$route.params.id}` 
            })
        }
    },
    mounted(){
        this.getRegionInformation()
        this.getLivingRegion()
    }
  }
  </script>

<style scoped>
    .mainDiv{
        height: 291.5vw !important;
        background-image: url('/src/assets/png-transparent-flag-flag-countries-flags-spherical-flag-national-flag-spherical 1.png');
        background-size: 100vw 100vh;
    }
    .infoMainDiv{
        width: 86.75vw;
        height: 204.25vw;
        flex-shrink: 0;
        border-radius: 2.5vw;
        position: absolute;
        margin: 45.25vw auto auto calc((100vw - 86.75vw)/2);
        background: #6F8B87;
    }
    .regionDiv{
        width: 72.25vw;
        height: 28.75vw;
        flex-shrink: 0;
        border-radius: 1.25vw;
        background: #7F9693;
        position: absolute;
        margin: 3.25vw auto auto calc((100% - 72.25vw)/2);
        /* background: red; */
    }
    .regionIcon{
        width: 20.5vw;
        height: 15.5vw;
        flex-shrink: 0;
        background: red;
        position: absolute;
        margin: 3.25vw auto auto 1.75vw;
        background-image: url('/src/assets/geoGerb.gif');
        background-size: 100% 100%;
        border-radius: 2vw;
    }
    .names{
        width: 43.5vw;
        height: 9.75vw;
        flex-shrink: 0;
        border-radius: 5px;
        background: #6F8B87;
        position: absolute;
        margin: 1.25vw auto auto 25vw;
    }
    .regionName{
        width: 20.5vw;
        height: 3.75vw;
        flex-shrink: 0;
        border-radius: 1.25vw;
        /* background: #7F9693; */
        position: absolute;
        margin: 1vw auto auto calc((100% - 42.5vw)/2);
        padding-left: 1vw;
        color: #FFF;
        text-align: left;
        font-family: Poppins;
        font-size: 3vw;
        font-style: normal;
        font-weight: 700;
        line-height: 3.75vw;
    }
    .regionState{
        width: 20.5vw;
        height: 3.75vw;
        flex-shrink: 0;
        border-radius: 1.25vw;
        /* background: #7F9693; */
        position: absolute;
        margin: 5.25vw auto auto calc((100% - 42.5vw)/2);
        padding-left: 1vw;
        color: #FFF;
        text-align: left;
        z-index: 0;
        font-family: play;
        font-size: 2vw;
        font-style: normal;
        font-weight: 400;
        line-height: 3.75vw;
    }
    .makeState{
        width: 20vw;
        height: 5vw;
        margin-right: 1vw;
        font-size: 4vw;
        text-align: center !important;
        background: #064D9F;
        color: white;
        line-height: 5vw;
        border-radius: 1vw;
        font-family: play;
        font-size: 3vw;
        font-style: normal;
        font-weight: 400;
        z-index: 99999;
        margin: 3.25vw auto auto calc((100% + 1.5vw)/2);
    }
    .regionDivAdditionalInfo{
        width: 43.5vw;
        height: 16.75vw;
        flex-shrink: 0;
        border-radius: 1.25vw;
        background: #6F8B87;
        position: absolute;
        margin: 11.25vw auto auto 25vw;
    }
    .regionDivAdditionalInfoClass{
        width: 39vw;
        height: 3vw;
        flex-shrink: 0;
        background: #7f969354;
        position: absolute;
        margin-left: calc((100% - 39vw)/2);
        color: #FFF;
        text-align: left;
        font-family: play;
        font-size: 2.5vw;
        font-style: normal;
        font-weight: 400;
        line-height: 3vw;
        display: flex;
        justify-content: space-between;
    }
    .regionResidents{
        margin-top: 1.75vw;
    }
    .regionCitizens{
        margin-top: 5.25vw;
    }
    .regionParty{
        margin-top: 8.75vw;
    }
    .regionFactory{
        margin-top: 12.25vw;
    }
    .regionAdditionalDivName{
        width: 10vw;
        height: 3vw;
        margin-left: 1vw;
    }
    .regionAdditionalDivValue{
        width: 10vw;
        height: 3vw;
        margin-right: 1vw;
        text-align: right !important;
    }
    .actionDiv{
        width: 72.25vw;
        height: 34.5vw;
        flex-shrink: 0;
        border-radius: 1.25vw;
        background: #7F9693;
        position: absolute;
        margin: 32.75vw auto auto calc((100% - 72.25vw)/2)
    }
    .actionDivClass{
        width: 50vw;
        height: 5vw;
        flex-shrink: 0;
        /* opacity: 0.2; */
        background: #D9D9D9;
        position: absolute;
        margin-left: calc((100% - 50vw)/2);
        color: #FFF;
        text-align: center;
        font-family: Poppins;
        font-size: 4vw;
        font-style: normal;
        font-weight: 700;
        line-height: 5vw;
        border-radius: 1vw;
    }
    .actionFly{
        margin-top: 3.25vw;
        background: #126D10;
    }
    .actionTravel{
        margin-top: 11vw;
        background: #126D10;
    }
    .actionSeeOnMap{
        margin-top: 18.5vw;
        background: #7a0101;
    }
    .actionResRequest{
        margin-top: 26.25vw;
        background: #7a0101;
    }
    .indexDiv{
        width: 72.25vw;
        height: 34.25vw;
        flex-shrink: 0;
        border-radius: 1.25vw;
        background: #7F9693;
        position: absolute;
        margin: 70vw auto auto calc((100% - 72.25vw)/2)
    }
    .indexDivClass{
        width: 63.75vw;
        height: 5vw;
        flex-shrink: 0;
        background: #6f8b87a7;
        position: absolute;
        margin-left: calc((100% - 63.75vw)/2);
        color: #FFF;
        text-align: center;
        font-family: Poppins;
        font-size: 3vw;
        font-style: normal;
        font-weight: 700;
        line-height: 5vw;
        border-radius: 1vw;
        display: flex;
        justify-content: space-between;
    }
    .medicalIndexDiv{
        margin-top: 2.75vw;
    }
    .educationIndexDiv{
        margin-top: 10.5vw;
    }
    .militaryIndexDiv{
        margin-top: 18.25vw;
    }
    .developmentIndexDiv{
        margin-top: 26vw;
    }
    .idexDivName{
        width: 15vw;
        height: 5vw;
        margin-left: 1vw;
        /* background: red; */
        text-align: left !important;
    }
    .indexDivValue{
        width: 10vw;
        height: 5vw;
        margin-right: 1vw;
        text-align: right !important;
        /* background: red; */
    }
    .buildingInfo{
        width: 72.25vw;
        height: 41vw;
        flex-shrink: 0;
        border-radius: 1.25vw;
        background: #7F9693;
        position: absolute;
        margin: 107vw auto auto calc((100% - 72.25vw)/2)
    }
    .buildingDivClass{
        width: 63.75vw;
        height: 5vw;
        flex-shrink: 0;
        background: #6f8b87a7;
        position: absolute;
        margin-left: calc((100% - 63.75vw)/2);
        color: #FFF;
        text-align: center;
        font-family: Poppins;
        font-size: 3vw;
        font-style: normal;
        font-weight: 700;
        line-height: 5vw;
        border-radius: 1vw;
        display: flex;
        justify-content: space-between;
    }
    .hospitalDiv{
        margin-top: 2.75vw;
    }
    .schoolDiv{
        margin-top: 10.5vw;
    }
    .militaryBaseDiv{
        margin-top: 18.25vw;
    }
    .houseDiv{
        margin-top: 26vw;
    }
    .nuclearPowerDiv{
        margin-top: 33.75vw;
    } 
    .buildingDivName{
        width: 30vw;
        height: 5vw;
        margin-left: 1vw;
        /* background: red; */
        text-align: left !important;
    }
    .buildingDivValue{
        width: 10vw;
        height: 5vw;
        margin-right: 1vw;
        text-align: right !important;
        /* background: red; */
    }
    .workersInfo{
        width: 72.25vw;
        height: 48.5vw;
        flex-shrink: 0;
        border-radius: 1.25vw;
        background: #7F9693;
        position: absolute;
        margin: 150.75vw auto auto calc((100% - 72.25vw)/2)
    }
    .moreInfoButton{
        width: 47vw;
        height: 6.25vw;
        background: #064D9F;
        color: #FFF;
        font-family: Inter;
        font-size: 3vw;
        font-style: normal;
        font-weight: 700;
        line-height: 6.25vw;
        margin: 37vw auto auto calc((100% - 47vw)/2);
        border-radius: 1vw;
        cursor: pointer;
    }
    .workerDivClass{
        width: 63.75vw;
        height: 5vw;
        flex-shrink: 0;
        background: #6f8b87a7;
        position: absolute;
        margin-left: calc((100% - 63.75vw)/2);
        color: #FFF;
        text-align: center;
        font-family: Poppins;
        font-size: 3vw;
        font-style: normal;
        font-weight: 700;
        line-height: 5vw;
        border-radius: 1vw;
        display: flex;
        justify-content: space-between;
    }
    .teacherDiv{
        margin-top: 2.75vw;
    }
    .doctorDiv{
        margin-top: 10.5vw;
    }
    .generalDiv{
        margin-top: 18.25vw;
    }
    .defensiveSystemDiv{
        margin-top: 26vw;
    }
    .workerDivName{
        width: 30vw;
        height: 5vw;
        margin-left: 1vw;
        /* background: red; */
        text-align: left !important;
    }
    .workerDivValue{
        width: 10vw;
        height: 5vw;
        margin-right: 1vw;
        text-align: right !important;
        /* background: red; */
    }
    
</style>