<template>
    <div class="mainDiv" style="background-color: #0E0000; width:100%; height: 1100px !important; position: absolute; display: grid; top: 0; left: 0;">
        <AppHeader/>
            <div class="infoMainDiv">
                    <div class="partyDiv">
                        <div class="partyIcon"></div>
                        <div class="names">
                            <div class="stateName">State: {{this.data.state}}</div>
                        </div>
                    </div> 
                    <div class="electionTimer">{{this.formatTime()}}</div>
                    <div class="electionDiv">
                        <div class="electionMemberDIv">election Members</div>
                        <div class="partyMEmbersValueDiv">
                            <div v-for="i in this.data.party" :key="i" class="partyMembersValueClass">
                                <div class="partyInElectionIcon"></div>
                                <div class="partyInElectionClass">{{i.name}}</div>
                                <div class="partyInElectionClass">{{i.vote}}</div>
                                <div  @click="this.voteUp"  v-if="this.data.visibility == 1" class="partyInElectionClass" style="width: 15% !important; font-size: 3vw; background: green; text-align: center !important; margin-right: 1vw;">
                                    Vote <span style="display:none;">{{i['id']}}</span>
                                </div>
                            </div>
                        </div>
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
            data: '',
            time: null,
            timerInterval: '',
            // ip: 'http://94.43.110.179:80',
            // ip: 'http://127.0.0.1:80',
            ip: 'http://tato1999.pythonanywhere.com/'
        }
    },
    methods:{
        getData(){
            const path = this.ip+"/get_parlament_election_data"
            axios.post(path,{
                id: this.$route.params.id,
                user: localStorage.getItem('id')
            })
            .then((res) => {
                this.data = res.data
                console.log(this.data)
            })
            .catch((err) => {
                console.log(err)
            })
        },
        voteUp(event){
            const path = this.ip+"/vote_up_parlament_election"
            axios.post(path,{
                id: this.$route.params.id,
                user: localStorage.getItem('id'),
                party: event.target.firstElementChild.innerHTML*1,
            })
            .then((res) => {
                this.data = res.data
                console.log(this.data)
            })
            .catch((err) => {
                console.log(err)
            })
        },
        checkElectionTime(){
            console.log(this.data.state)
            const path = this.ip+"/check_parlament_election_time"
            axios.post(path,{
                id: this.$route.params.id,
                state: this.data.state,
                date: new Date()
            })
            .then((res) => {
                // this.data = res.data
                console.log(res.data)
                this.time = res.data.time
                if(this.time <= 0){
                    this.sendElectionInfo()
                }else{
                this.timerInterval = setInterval(() => {
                    this.time -= 1
                    if(this.time <= 0){
                            clearInterval(this.timerInterval)
                            this.checkElectionTime()
                        }
                    }, 1000)
                }
            })
            .catch((err) => {
                console.log(err)
            })
        },
        sendElectionInfo(){
            const path = this.ip+"/send_election_info_in_db"
            axios.post(path,{
                id: this.$route.params.id,
                state: this.data.state,
                date: new Date()
            })
            .then((res) => {
                console.log(res)
                if(res.data.isElection === 0){
                    this.$router.push({
                        path: `/state/${res.data.state}` 
                    })
                }
            })
            .catch((err) => {
                console.log(err)
            })
        },
        formatTime() {
            if (isNaN(this.time)) {
                return "0:00:00";
            }
            const hours = Math.floor(this.time / 3600); // Calculate hours
            const remainingSeconds = this.time % 3600; // Calculate remaining seconds
            const minutes = Math.floor(remainingSeconds / 60); // Calculate minutes
            const seconds = Math.round(remainingSeconds % 60); // Calculate seconds

            // Format the time string with leading zeros for minutes and seconds
            const formattedTime = `${hours}:${minutes < 10 ? '0' : ''}${minutes}:${seconds < 10 ? '0' : ''}${seconds}`;

            return formattedTime;
        }
    },
    mounted(){
        this.getData()
        setTimeout(() => {
            this.checkElectionTime()
            // this.sendElectionInfo()
        },150)
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
        height: 190.25vw;
        flex-shrink: 0;
        border-radius: 2.5vw;
        position: absolute;
        margin: 45.25vw auto auto calc((100vw - 86.75vw)/2);
        background: #6F8B87;
    }
    .partyDiv{
        width: 72.25vw;
        height: 23.75vw;
        flex-shrink: 0;
        border-radius: 1.25vw;
        background: #7F9693;
        position: absolute;
        margin: 3.25vw auto auto calc((100% - 72.25vw)/2);
        /* background: red; */
    }
    .partyIcon{
        width: 17.5vw;
        height: 17.5vw;
        flex-shrink: 0;
        background: red;
        position: absolute;
        margin: 3.25vw auto auto 1.75vw;
        background-image: url('/src/assets/geoGerb.gif');
        background-size: 100% 100%;
        border-radius: 1vw;
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
    .stateName{
        width: 42.5vw;
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
    .partyRegion{
        width: 42.5vw;
        height: 3.75vw;
        flex-shrink: 0;
        border-radius: 1.25vw;
        /* background: #7F9693; */
        position: absolute;
        margin: 5.25vw auto auto calc((100% - 42.5vw)/2);
        padding-left: 1vw;
        color: #FFF;
        text-align: left;
        font-family: play;
        font-size: 2vw;
        font-style: normal;
        font-weight: 400;
        line-height: 3.75vw;
    }
    .partyDivAdditionalInfo{
        width: 43.5vw;
        height: 10.75vw;
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
    .requestButton{
        width: 70vw;
        height: 6.75vw;
        flex-shrink: 0;
        border-radius: 1.25vw;
        background: #061744;
        color: #FFF;
        font-family: Inter;
        font-size: 3vw;
        font-style: normal;
        font-weight: 900;
        line-height: 6.75vw;
        position: absolute;
        margin: 34.75vw auto auto calc((100% - 70vw)/2);
        cursor: pointer;
    }
    .requestDiv{
        width: 72.25vw;
        height: 50vw;
        flex-shrink: 0;
        border-radius: 1.25vw;
        background: #6c7b79;
        position: absolute;
        margin: 45vw auto auto calc((100% - 72.25vw)/2);
        z-index: 999;
    }
    .partyRequestValueDiv{
        width: 66.75vw;
        height: 45vw;
        flex-shrink: 0;
        border-radius: 1.25vw;
        background: #d9d9d936;
        position: absolute;
        margin: 3.5vw auto auto calc((100% - 66.75vw)/2);
        overflow: auto;
        z-index: 999;
    }
    .partyRequestValueClass{
        width: 63.75vw;
        height: 5vw;
        flex-shrink: 0;
        background: #d9d9d91e;
        margin: 1vw auto auto calc((100% - 63.75vw)/2);
        text-align: center;
        display: flex;
        justify-content: space-between;
        z-index: 999;
    }
    .electionDiv{
        width: 72.25vw;
        height: 100vw;
        flex-shrink: 0;
        border-radius: 1.25vw;
        background: #7F9693;
        position: absolute;
        margin: 50vw auto auto calc((100% - 72.25vw)/2);
        /* display: none; */
    }
    .electionMemberDIv{
        width: 66.75vw;
        height: 5vw;
        flex-shrink: 0;
        border-radius: 1.25vw;
        background: #d9d9d936;
        position: absolute;
        margin: 2.5vw auto auto calc((100% - 66.75vw)/2);
        color: #FFF;
        font-family: Inter;
        font-size: 3vw;
        font-style: normal;
        font-weight: 900;
        line-height: 5vw;
    }
    .partyMEmbersValueDiv{
        width: 66.75vw;
        height: 85vw;
        flex-shrink: 0;
        border-radius: 1.25vw;
        background: #d9d9d936;
        position: absolute;
        margin: 8.5vw auto auto calc((100% - 66.75vw)/2);
        overflow: auto;
    }
    .partyMembersValueClass{
        width: 63.75vw;
        height: 5vw;
        flex-shrink: 0;
        background: #d9d9d91e;
        margin: 1vw auto auto calc((100% - 63.75vw)/2);
        text-align: center;
        display: flex;
        justify-content: space-between;
    }
    .partyInElectionIcon{
        width: 5vw;
        height: 5vw;
        flex-shrink: 0;
        background-image: url('/src/assets/geoGerb.gif');
        background-size: 100% 100%;
        margin: auto auto auto 1vw;
        border-radius: 5vw;
        position: absolute;
    }
    .partyInElectionClass{
        width: 30%;
        text-align: left;
        color: #FFF;
        font-family: Inter;
        font-size: 3vw;
        font-style: normal;
        font-weight: 400;
        line-height: 5vw;
        margin-top: auto !important;
        margin-left: 10vw;
        overflow-y: hidden;
    }
    .additionalInfoDiv{
        width: 72.25vw;
        height: 26vw;
        flex-shrink: 0;
        border-radius: 1.25vw;
        background: #7F9693;
        position: absolute;
        margin: 157.25vw auto auto calc((100% - 72.25vw)/2);
        color: #FFF;
        font-family: Inter;
        font-size: 3vw;
        font-style: normal;
        font-weight: 400;
        line-height: 6.25vw;
    }
    .detailedInformationDiv{
        width: 70vw;
        height: 6.25vw;
        flex-shrink: 0;
        border-radius: 1.25vw;
        background: #126D10;
        position: absolute;
        margin: 2.5vw auto auto calc((100% - 70vw)/2);
        cursor: pointer;
    }
    .agreementsDiv{
        width: 70vw;
        height: 6.25vw;
        flex-shrink: 0;
        border-radius: 1.25vw;
        background: #126D10;
        position: absolute;
        margin: 10.5vw auto auto calc((100% - 70vw)/2);
        cursor: pointer;
    }
    .budgetDiv{
        width: 70vw;
        height: 6.25vw;
        flex-shrink: 0;
        border-radius: 1.25vw;
        background: #126D10;
        position: absolute;
        margin: 18.5vw auto auto calc((100% - 70vw)/2);
        cursor: pointer;
    }
    .electionTimer{
        width: 70vw;
        height: 6.25vw;
        flex-shrink: 0;
        border-radius: 1.25vw;
        background: #126D10;
        position: absolute;
        margin: 30.5vw auto auto calc((100% - 70vw)/2);
        cursor: pointer;
    }
    
</style>