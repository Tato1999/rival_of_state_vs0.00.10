<template>
    <loading-overlay v-if="loading" :can-cancel='false' :color="'#000'" :background="'black'">
    </loading-overlay>
    <div class="mainDiv" v-if="dataLoaded" style="background-color: #0E0000; width:100%; height: 291.5vw; position: absolute; display: grid; top: 0; left: 0;">
        <AppHeader/>
        <div class="regionNameDiv">
            Region: Georgia
        </div>
        <div class="factorySearchFilter" @click="this.openCloseFilter">
            <p>Filter</p>
            <p style="color: rgb(48, 71, 48); font-size: 7vw;"></p>
        </div>
        <factorySearch v-if="this.fillterVisibility" @filter="handleFilter"/>
        <div class="allLocalFactoryDiv">
            <p class="allWarDivParagraph">World Active Wars</p>
            <div v-for="i in this.filteredFactories" :key="i" class="secondFactoryDiv">
                <div class="secondFactoryOwnerIcon"></div>
                <p class="FactoryName">{{i['name']}}</p>
                <p class="FactoryLevel">Factory Level: {{i['level']}}</p>
                <!-- <p style="display: none">{{i['id']}}</p> -->
                <!-- <router-link to="work/factory"> -->
                    <div class="WorkButton" @click="this.sendFactoryId">Work <span style="display: none">{{i['id']}}</span></div>
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
            factoryInfo: [],
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
                document.querySelector(".allLocalFactoryDiv").style.opacity = '0.6'
            }else{
                document.querySelector(".allLocalFactoryDiv").style.opacity = '1'
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

            const path = this.ip+'/get_all_factory'
             axios.post(path,{
                id: localStorage.getItem('id')
             }).then((res) => {
                this.factoryInfo = res.data
                console.log(this.factoryInfo)
                this.filteredFactories = this.factoryInfo
                this.dataLoaded = true
                this.loading = false
                // this.currentFactory = this.factoryInfo.find(item => item.id == this.currentFactoryId)
                // this.ownerExperience = this.currentFactory.owner.working_experience
                // this.ownerStat = this.currentFactory.owner
                // document.querySelector('.factoryIcon').style.backgroundImage = `url(${require('@/assets/factoryIcon/'+this.currentFactory.factory_icon)})`
                // document.querySelector('.firstFactoryOwnerIcon').style.backgroundImage = `url(${require('@/assets/factoryIcon/'+this.factoryInfo[0].factory_icon)})`
                // document.querySelectorAll('.secondFactoryOwnerIcon').style.backgroundImage = `url(${require('@/assets/factoryIcon/'+this.factoryInfo[1].factory_icon)})`
                // document.querySelector('.thirdFactoryOwnerIcon').style.backgroundImage = `url(${require('@/assets/factoryIcon/'+this.factoryInfo[2].factory_icon)})`
                setTimeout(() => {
                    this.setIcon()
                },10)
             }).catch((err) => {
                console.log(err)
             })
         },
         setIcon(){
            for(var i=0; i<this.factoryInfo.length; i++){
                console.log(i)
                document.querySelectorAll('.secondFactoryOwnerIcon')[i].style.backgroundImage = `url(${require('@/assets/factoryIcon/'+this.factoryInfo[i].factory_icon)})`
                localStorage.removeItem('reg')
            }
         },
         getCurrentFactory(){
            // const path = 'http://192.168.4.48:80/get_current_factory';
            //  const path = 'http://192.168.54.172:80/profile'
            const path = this.ip+'/get_current_factory'
            axios.post(path,{
            id: localStorage.getItem('id'),
             }).then((res) => {
                console.log(res.data)
                 this.currentFactoryId = res.data.currentFactory
                 console.log(this.currentRegion)
                })
             .catch((err) => {
                 console.error(err)
             })
         },
         sendFactoryId(event){
            console.log(event.target.firstElementChild.innerHTML)
            localStorage.setItem('factory',event.target.firstElementChild.innerHTML*1)
            // const path = 'http://192.168.4.48:80/change_work_factory'

            const path = this.ip+'/change_work_factory'
            axios.post(path,{
                id: localStorage.getItem('id'),
                nextFactoryId:{'id':event.target.firstElementChild.innerHTML*1}
             })
             .then((res) => {
                 console.log(res)
                })
             .catch((err) => {
                 console.error(err)
             })
            this.$router.push({
              path: `/work` })
            },

            handleFilter(filterText) {
    // Check if filterText is undefined or null
                if (filterText === undefined || filterText === null) {
                // Handle the case when filterText is not defined
                // For example, you might reset the filter or show all items
                    console.log(this.factoryInfo)
                    this.filteredFactories = [...this.factoryInfo];
                    console.log(filterText)
                } else {
                // Filter the factories based on the selected factory types
                console.log(this.factoryInfo)
                    this.filteredFactories = this.factoryInfo.filter(factory => {
                    // Assuming 'type' is a property in your factoryInfo objects
                        console.log(filterText)
                    return factory.type.toLowerCase().includes(filterText.toLowerCase());
                });
                console.log(this.filteredFactories)
    }
  },
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
    .allLocalFactoryDiv{
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
    .filterClass{
        display: none;
        visibility: hidden;
    }
    
</style>