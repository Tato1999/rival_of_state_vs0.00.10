<template>
    <div class="mainDiv" style="background-color: #0E0000; width:100%; height: 1100px !important; position: absolute; display: grid; top: 0; left: 0;">
        <AppHeader/>
            <div class="infoMainDiv">
                    <div class="regionDiv">
                        <div class="regionIcon"></div>
                        <div class="names">
                            <div class="regionName">State: Georgia</div>
                            <div class="regionState">Goverment Form: Presidential Republic</div>
                        </div>
                        <div class="regionDivAdditionalInfo">
                            <div class="regionResidents regionDivAdditionalInfoClass">
                                <div class="regionAdditionalDivName">Residents</div>
                                <div class="regionAdditionalDivValue">1</div>
                            </div>
                            <div class="regionCitizens regionDivAdditionalInfoClass">
                                <div class="regionAdditionalDivName">Citizens</div>
                                <div class="regionAdditionalDivValue">1</div>
                            </div>
                            <div class="regionParty regionDivAdditionalInfoClass">
                                <div class="regionAdditionalDivName">Party</div>
                                <div class="regionAdditionalDivValue">1</div>
                            </div>
                            <div class="regionFactory regionDivAdditionalInfoClass">
                                <div class="regionAdditionalDivName">Factory</div>
                                <div class="regionAdditionalDivValue">1</div>
                            </div>
                        </div>
                    </div>
                    <div class="parlamentButton">See Parlament</div>
                    <div v-if="this.isElection == 1" class="electionButton" @click="this.enterElectionPage()">Election</div>
                    <div class="govermentDiv">
                        <div class="leaderDiv govermendDivClass">
                            <div class="govermentDivName">President:</div>
                            <div class="govermentDivValue">
                                <div class="govermentDivValueNameClass">Minister of Foreign Affairs</div>
                                <div class="govermentDivValueWageClass">500G</div>
                            </div>
                        </div>
                        <div class="economyDiv govermendDivClass">
                            <div class="govermentDivName">Minister of Economy:</div>
                            <div class="govermentDivValue">
                                <div class="govermentDivValueNameClass">Minister of Foreign Affairs</div>
                                <div class="govermentDivValueWageClass">500G</div>
                            </div>
                        </div>
                        <div class="seflDefenceDiv govermendDivClass">
                            <div class="govermentDivName">Minister of Self-Defence:</div>
                            <div class="govermentDivValue">
                                <div class="govermentDivValueNameClass">Minister of Foreign Affairs</div>
                                <div class="govermentDivValueWageClass">500G</div>
                            </div>
                        </div>
                        <div class="foreignDiv govermendDivClass">
                            <div class="govermentDivName">Minister of Foreign Affairs:</div>
                            <div class="govermentDivValue">
                                <div class="govermentDivValueNameClass">Minister of Foreign Affairs</div>
                                <div class="govermentDivValueWageClass">500G</div>
                            </div>
                        </div>
                    </div>
                    <div class="actionDiv">
                        <div class="workPermitDiv">Work Permit</div>
                        <div class="donationDiv">Donation in the budget</div>
                    </div>
                    <div class="stateRegionDiv">
                        <div class="stateRegionNameDiv">State Region</div>
                        <div class="stateRegionValueDiv">
                            <div v-for="i in [0,1,2,3,4,5,6,7,8,9,10]" :key="i" class="stateRegionValueClass">
                                <div class="stateRegionValueClassIcon"></div>
                                <div class="stateRegionValueClassName">Georgia</div>
                            </div>
                        </div>
                    </div>
                    <div class="additionalInfoDiv">
                        <div class="detailedInformationDiv">See Detailed Information</div>
                        <div class="agreementsDiv">See Agreements</div>
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
        //    ip: 'http://127.0.0.1:80',
            ip: 'http://tato1999.pythonanywhere.com/',
            isElection: 0,
            electionId: 0,
        }
    },
    methods:{
        getData(){
            const path = this.ip+'/get_state_data'
            axios.post(path,{
                id: this.$route.params.id
            })
            .then((res) => {
                console.log(res)
            })
            .catch((err) => {
                console.log(err)
            })
        },
        getElectionData(){
            const path = this.ip+'/get_state_election_data'
            axios.post(path,{
                id: this.$route.params.id,
                date: new Date(),
            })
            .then((res) => {
                this.isElection = res.data.isElection
                this.electionId = res.data.electionId
                console.log(res)
            })
            .catch((err) => {
                console.log(err)
            })
        },
        enterElectionPage(){
            this.$router.push({
                path: `/parlament/election/${this.electionId}` 
            })
        }
    },
    mounted(){
        // this.getData()
        this.getElectionData()
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
    .regionName{
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
    .regionState{
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
    .parlamentButton{
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
        margin: 37.75vw auto auto calc((100% - 70vw)/2);
        cursor: pointer;
    }
    .electionButton{
        width: 70vw;
        height: 6.75vw;
        flex-shrink: 0;
        border-radius: 1.25vw;
        background: #165e2d;
        color: #FFF;
        font-family: Inter;
        font-size: 3vw;
        font-style: normal;
        font-weight: 900;
        line-height: 6.75vw;
        position: absolute;
        margin: 45.75vw auto auto calc((100% - 70vw)/2);
        cursor: pointer;
    }
    .govermentDiv{
        width: 72.25vw;
        height: 29vw;
        flex-shrink: 0;
        border-radius: 1.25vw;
        background: #7F9693;
        position: absolute;
        margin: 56.5vw auto auto calc((100% - 72.25vw)/2)
    }
    .govermendDivClass{
        width: 67vw;
        height: 5.25vw;
        flex-shrink: 0;
        background: #d9d9d936;
        position: absolute;
        margin-left: calc((100% - 67vw)/2);
        display: flex;
        justify-content: space-between !important;
    }
    .leaderDiv{
        margin-top: 1vw;
    }
    .economyDiv{
        margin-top: 8.25vw;
    }
    .seflDefenceDiv{
        margin-top: 15.5vw;
    }
    .foreignDiv{
        margin-top: 22.75vw;
    }
    .govermentDivName{
        /* background: red; */
        width: 30vw;
        height: 5.25vw;
        color: #FFF;
        font-family: Inter;
        font-size: 2.5vw;
        font-style: normal;
        font-weight: 400;
        line-height: 5.25vw;
        text-align: left;
        margin-left: 1vw;
    }
    .govermentDivValue{
        /* background: red; */
        width: 30vw;
        height: 5.25vw;
        color: #FFF;
        font-family: Inter;
        font-size: 2.5vw;
        font-style: normal;
        font-weight: 400;
        text-align: left;
        margin-right: 1vw;
    }
    .govermentDivValueNameClass{
        text-align: right;
    }
    .govermentDivValueWageClass{
        text-align: right;
        width: 30vw;
        margin-right: 1vw !important;
        color: #595757;
        font-family: Inter;
        font-size: 2vw;
        font-style: normal;
        font-weight: 500;
        line-height: normal;
    }
    .actionDiv{
        width: 72.25vw;
        height: 17.5vw;
        flex-shrink: 0;
        border-radius: 1.25vw;
        background: #7F9693;
        position: absolute;
        margin: 87.5vw auto auto calc((100% - 72.25vw)/2);
    }
    .workPermitDiv{
        width: 70vw;
        height: 6.25vw;
        flex-shrink: 0;
        border-radius: 1.25vw;
        background: #126D10;
        position: absolute;
        margin: 1.25vw auto auto calc((100% - 70vw)/2);
        color: #FFF;
        font-family: Inter;
        font-size: 12px;
        font-style: normal;
        font-weight: 900;
        line-height: 6.25vw;
        cursor: pointer;
    }
    .donationDiv{
        width: 70vw;
        height: 6.25vw;
        flex-shrink: 0;
        border-radius: 1.25vw;
        background: #126D10;
        position: absolute;
        margin: 9.25vw auto auto calc((100% - 70vw)/2);
        color: #FFF;
        font-family: Inter;
        font-size: 12px;
        font-style: normal;
        font-weight: 900;
        line-height: 6.25vw;
        cursor: pointer;
    }
    .stateRegionDiv{
        width: 72.25vw;
        height: 45vw;
        flex-shrink: 0;
        border-radius: 1.25vw;
        background: #7F9693;
        position: absolute;
        margin: 107vw auto auto calc((100% - 72.25vw)/2);
    }
    .stateRegionNameDiv{
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
    .stateRegionValueDiv{
        width: 66.75vw;
        height: 35vw;
        flex-shrink: 0;
        border-radius: 1.25vw;
        background: #d9d9d936;
        position: absolute;
        margin: 8.5vw auto auto calc((100% - 66.75vw)/2);
        overflow: auto;
    }
    .stateRegionValueClass{
        width: 63.75vw;
        height: 5vw;
        flex-shrink: 0;
        background: #d9d9d91e;
        margin: 1vw auto auto calc((100% - 63.75vw)/2);
        text-align: center;
    }
    .stateRegionValueClassIcon{
        width: 5vw;
        height: 5vw;
        flex-shrink: 0;
        background-image: url('/src/assets/geoGerb.gif');
        background-size: 100% 100%;
        margin: auto auto auto 1vw;
        border-radius: 5vw;
        position: absolute;
    }
    .stateRegionValueClassName{
        color: #FFF;
        font-family: Inter;
        font-size: 3vw;
        font-style: normal;
        font-weight: 400;
        line-height: 5vw;
        margin-top: auto !important;
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