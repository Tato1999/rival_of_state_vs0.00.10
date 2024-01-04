<template>
    <loading-overlay v-if="loading" :can-cancel='false' :color="'#000'" :background="'black'">
    </loading-overlay>
    <div class="mainDiv" v-if="dataLoaded" style="background-color: #0E0000; width:100%; height: 291.5vw; position: absolute; display: grid; top: 0; left: 0;">
        <AppHeader/>
        <div class="regionNameDiv">
            Region: Georgia
        </div>
        <factorySearch v-if="this.fillterVisibility" @filter="handleFilter"/>
        <div class="allLocalPartyDiv">
            <p class="allPartyDivParagraph">World Active Wars</p>
            <div v-for="i in this.filteredFactories" :key="i" class="secondFactoryDiv">
                <div class="secondPartyOwnerIcon" @click="this.enterParty"><span style="display: none">{{i['id']}}</span></div>
                <p class="PartyName" @click="this.enterParty">{{i['name']}}<span style="display: none">{{i['id']}}</span></p>
                <p class="PartyLeader" @click="this.enterParty">Leader: {{i['leader']}}<span style="display: none">{{i['id']}}</span></p>
                <div class="requestButton" @click="this.sendPartyRequest">Request<span style="display: none">{{i['id']}}</span></div>
                <!-- </router-link> -->
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
  import axios from 'axios'
  import LoadingOverlay from 'vue-loading-overlay';
  import 'vue-loading-overlay/dist/css/index.css';
  export default {
    components: {
        AppHeader,
        AppFooterMenu,
        factorySearch,
        LoadingOverlay
    },
    data(){
        return{
            fillterVisibility: false,
            loading: true,
            dataLoaded: false,
            partyInfo: [],
            value: 0,
            filteredFactories: [],
            currentRegion: '',
            // ip: 'http://94.43.110.179:80',
            // ip: 'http://127.0.0.1:80',
            ip: 'http://tato1999.pythonanywhere.com/'
        }
    },
    methods:{
        openCloseFilter(){
            this.fillterVisibility = !this.fillterVisibility
            if(this.fillterVisibility){
                document.querySelector(".allLocalPartyDiv").style.opacity = '0.6'
            }else{
                document.querySelector(".allLocalPartyDiv").style.opacity = '1'
            }
        },
        getInfo(){
            // const path = 'http://192.168.4.48:80/profile';
            //  const path = 'http://192.168.54.172:80/profile'
            const path = this.ip+'/profile'
            axios.post(path,{
            id: localStorage.getItem('id'),
             }).then((res) => {
                console.log(res.data)
                this.currentRegion = res.data.living_region
             })
             .catch((err) => {
                 console.error(err)
             })
        },
        getFactory(){
            // const path = 'http://192.168.4.48:80/get_all_factory'
            // const path = 'http://127.0.0.1:80/get_regional_factory'

            const path = this.ip+'/get_all_regional_party'
             axios.post(path,{
                id: this.$route.params.id
             }).then((res) => {
                this.partyInfo = res.data.party
                console.log(this.partyInfo)
                this.filteredFactories = this.partyInfo
                this.dataLoaded = true
                this.loading = false
                setTimeout(() => {
                    this.setIcon()
                },10)
             }).catch((err) => {
                console.log(err)
             })
         },
         setIcon(){
            for(var i=0; i<this.partyInfo.length; i++){
                console.log(i)
                // document.querySelectorAll('.secondPartyOwnerIcon')[i].style.backgroundImage = `url(${require('@/assets/factoryIcon/'+this.partyInfo[i].factory_icon)})`
                // localStorage.removeItem('reg')
            }
         },
         sendPartyRequest(event){
            const path = this.ip+'/send_party_request'
            axios.post(path,{
                id: localStorage.getItem('id'),
                party: {'id':event.target.firstElementChild.innerHTML*1}
            })
            .then((res) => {
                console.log(res)
            })
            .catch((err) => {
                console.log(err)
            })
         },
         enterParty(event){
            let id = event.target.firstElementChild.innerHTML
            this.$router.push({
                path: `/party/${id}` 
            })
         }
        },
    mounted(){
        setTimeout(() => {
            this.getInfo()
        },50)
        setTimeout(() => {
            this.getFactory()
        },1000)
    }
  }
  </script>

<style scoped>
    .mainDiv{
        height: 291.5vw !important;
        background-image: url('/src/assets/png-transparent-flag-flag-countries-flags-spherical-flag-national-flag-spherical 1.png');
        background-size: 100vw 100vh;
    }
    .allLocalPartyDiv{
        width: 92.5vw;
        height: 154.5vw;
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
    .PartyName{
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
    .secondPartyOwnerIcon{
        width: 17.5vw;
        height: 17.5vw;
        margin-left: 4vw;
        position: absolute;
        background-image: url('/src/assets/profile_icon.png');
        background-size: 100% 100%;
    }
    .PartyLeader{
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
    .requestButton{
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