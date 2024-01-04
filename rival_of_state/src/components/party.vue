<template>
    <div class="mainDiv" style="background-color: #0E0000; width:100%; height: 1100px !important; position: absolute; display: grid; top: 0; left: 0;">
        <AppHeader/>
            <div class="infoMainDiv">
                    <div class="partyDiv">
                        <div class="partyIcon"></div>
                        <div class="names">
                            <div class="partyName">Party: {{this.data.name}}</div>
                            <div class="partyRegion">{{this.data.region}}</div>
                        </div>
                        <div class="partyDivAdditionalInfo">
                            <div class="regionResidents regionDivAdditionalInfoClass">
                                <div class="regionAdditionalDivName">Members</div>
                                <div class="regionAdditionalDivValue">{{this.data.count}}</div>
                            </div>
                            <div class="regionCitizens regionDivAdditionalInfoClass">
                                <div class="regionAdditionalDivName">Leader</div>
                                <div class="regionAdditionalDivValue">{{this.leaderName}}</div>
                            </div>
                        </div>
                    </div>
                    <div v-if="this.isAdmin || this.isSupport" class="requestButton" @click="this.seeRequestTab()">See Requests</div>
                    <div v-if="this.isActive" class="requestDiv">
                        <div class="partyRequestValueDiv">
                            <div v-for="i in this.request" :key="i" class="partyRequestValueClass">
                                <div class="partyMembersIcon"></div>
                                <div class="partyMembersNameDivClass">{{i[0].name}}</div>
                                <div class="partyMembersNameDivClass" @click="this.addUserInParty" style="background: green">Accept<span style="display: none">{{i[0]['id']}}</span></div>
                                <div class="partyMembersNameDivClass" @click="this.removeUserFromRequest" style="background: red">Decline<span style="display: none">{{i[0]['id']}}</span></div>
                            </div>
                        </div>
                    </div>
                    <div v-else class="partyMembersDiv">
                        <div class="partyMembersNameDiv">Party Members</div>
                        <div class="partyMEmbersValueDiv">
                            <div v-for="i in this.data.members" :key="i" class="partyMembersValueClass">
                                <div class="partyMembersIcon"></div>
                                <div class="partyMembersNameDivClass">{{i[0].name}}</div>
                                <div class="partyMembersNameDivClass" style="margin-left: 1vw">{{i[0].position}}</div>
                                <div class="partyMembersNameDivClass" style="width: 35% !important; font-size: 3vw; margin-left: 1vw">
                                    <div v-if="(i[0].position != 'leader') && (this.isAdmin || i[0].id == this.user || this.isSupport)">
                                        <span style="background-color: red;" @click="this.removeUserFromParty">Remove<span style="display: none">{{i[0]['id']}}</span></span>
                                        <span style="background-color: green;" @click="this.promoteUserInParty" v-if="(this.leader.id == this.user*1)">/Promote<span style="display: none">{{i[0]['id']}}</span></span>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="additionalInfoDiv">
                        <div class="detailedInformationDiv">See Detailed Information</div>
                        <div class="agreementsDiv">Change Salary</div>
                        <div class="budgetDiv">See Budget</div>
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
            leaderName: '',
            leader: '',
            isAdmin: false,
            isActive: false,
            isSupport: false,
            request: '',
            user: localStorage.getItem('id'),
            // ip: 'http://94.43.110.179:80',
            // ip: 'http://127.0.0.1:80',
            ip: 'http://tato1999.pythonanywhere.com/'
        }
    },
    methods:{
        getData(){
            const path = this.ip+"/get_party_data"
            axios.post(path,{
                id: this.$route.params.id
            })
            .then((res) => {
                this.data = res.data
                console.log(this.data)
                this.leader = res.data.leader
                this.leaderName = res.data.leader.name
                this.data.members.forEach((el) => {
                    if(el[0]['position'] == 'support'){
                        console.log(el[0]['position'])
                        if(el[0]['id'] == this.user){
                            this.isSupport = true
                            if(this.data.waiters){
                                this.isAdmin = true
                                this.request = this.data.waiters
                            }
                        }else{
                            this.isSupport = false
                        }
                    }
                })
                if(res.data.leader.id == localStorage.getItem('id')){
                    if(this.data.waiters){
                        this.isAdmin = true
                        this.request = this.data.waiters
                    }
                }else{
                    this.isAdmin = false
                }
                // if res.data.
            })
            .catch((err) => {
                console.log(err)
            })
        },
        seeRequestTab(){
            this.isActive = !this.isActive
        },
        addUserInParty(event){
            const path = this.ip+'/add_user_in_party'
            axios.post(path,{
               id: event.target.firstElementChild.innerHTML*1,
               party: this.data.id
            })
            .then((res) => {
                console.log(res)
            })
            .catch((err) => {
                console.log(err)
            })
        },
        removeUserFromRequest(event){
            const path = this.ip+'/remove_user_from_request'
            axios.post(path,{
               id: event.target.firstElementChild.innerHTML*1,
               party: this.data.id
            })
            .then((res) => {
                console.log(res)
            })
            .catch((err) => {
                console.log(err)
            })
        },
        removeUserFromParty(event){
            const path = this.ip+'/remove_user_from_member'
            axios.post(path,{
               id: event.target.firstElementChild.innerHTML*1,
               party: this.data.id
            })
            .then((res) => {
                console.log(res)
            })
            .catch((err) => {
                console.log(err)
            })
        },
        promoteUserInParty(event){
            const path = this.ip+'/promote_user_in_party'
            axios.post(path,{
               id: event.target.firstElementChild.innerHTML*1,
               party: this.data.id
            })
            .then((res) => {
                console.log(res)
            })
            .catch((err) => {
                console.log(err)
            })
        }
    },
    mounted(){
        this.getData()
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
    .partyName{
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
    .partyMembersDiv{
        width: 72.25vw;
        height: 100vw;
        flex-shrink: 0;
        border-radius: 1.25vw;
        background: #7F9693;
        position: absolute;
        margin: 50vw auto auto calc((100% - 72.25vw)/2);
        /* display: none; */
    }
    .partyMembersNameDiv{
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
    .partyMembersIcon{
        width: 5vw;
        height: 5vw;
        flex-shrink: 0;
        background-image: url('/src/assets/geoGerb.gif');
        background-size: 100% 100%;
        margin: auto auto auto 1vw;
        border-radius: 5vw;
        position: absolute;
    }
    .partyMembersNameDivClass{
        width: 20%;
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
    
</style>