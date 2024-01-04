 <template>
    <!-- <div v-if="this.isLoading" class="mainDiv" style="background-color: #0E0000; width:100%; height: 291.5vw; position: absolute; display: grid; top: 0; left: 0;"></div> -->
    <loading-overlay v-if="loading" :can-cancel='false' :color="'#000'" :background="'black'">
        <div class="loading-spinner"></div>
    </loading-overlay>
    <div class="mainDiv" v-if="dataLoaded" style="background-color: #0E0000; width:100%; height: 291.5vw; position: absolute; display: grid; top: 0; left: 0;">
        <AppHeader/>
        <div class="regionResDiv">
            <p class="resRegionName">Resources: Georgia</p>
            <div class="resInsideDiv resInsideDivFirst">
                <p>Gold</p>
                <span class="goldText">500</span>
            </div>
            <div class="resInsideDiv resInsideDivSecond">
                <p>Oil</p>
                <span class="oilText">500</span>
            </div>
            <div class="resInsideDiv resInsideDivThird">
                <p>Ore</p>
                <span class="oreText">100</span>
            </div>
            <div class="resInsideDiv resInsideDivFour" style="width: 22.75vw !important;">
                <p>Uranium</p>
                <span class="uraniumText">100</span>
            </div>
        </div>
        <div class="currentFactoryDiv">
                <div class="factoryInformationDiv">
                    <div class="informationDivFirst">
                        <p>Current Working Place: {{this.currentFactory.type}}</p>
                        <div class="firstSplitLine"></div>
                    </div>
                    <div class="informationDivSecond">
                        <p>Working experience: {{this.ownerStat.working_experience}}</p>
                        <div class="secondSplitLine"></div>
                    </div>
                    <div class="informationDivThird">
                        <p>{{this.currentFactory.name}}</p>
                        <div class="thirdSplitLine"></div>
                    </div>
                </div>
            <div class="factoryInformationDivCreation">
                <div class="factoryIcon"></div>
                <div style="position: absolute; margin-left: 21.75vw; display: grid; text-align: left;">
                    <div class="factoryOwner">
                        <p>Owner: {{this.ownerStat.user_name}}</p>
                    </div>
                    <div class="factoryLevel">
                        <p>Factory Level: {{this.currentFactory.level}}</p>
                    </div>
                    <div class="factoryCreation">
                        <p>Create Data: 12/10/2023</p>
                    </div>
                </div>
            </div>
            <div class="energyAndWorkBar">
                <div class="emptyEnergyBar">
                    <div :v-model="watchWidthFunction" class="fullEnergyBar"></div>
                </div>
                <div class="fillButton" @click="this.manualRefilEnergy()">{{this.fill_button}}</div>
                <!-- <router-link to="/work/factory"> -->
                    <div class="workButton" @click="this.workInFactory()">Work</div>
                    <div v-if="this.autoWorkButtonBoolian" class="autoWorkButton" @click="this.autoWork()">Auto 5 Min</div>
                    <div v-else class="autoWorkButton" style="background-color: green !important" @click="this.autoWork()">{{formatTime()}}</div>
                <!-- </router-link> -->
                <div type="range" class="energyForFilling" @click="this.openCloseFill()">{{this.fillingEnergyValue}}</div>
                <div class="changeEnergySize">
                    <div class="changeableButton" @click="this.setFillSize" v-for="i in 200/5" :key="i">{{(this.fillingEnergyValue+5)-(i*5)}}</div>
                </div>
            </div>
        </div>
        <div class="factorySearchDiv">
            <p class="topicOfFactorySearchDiv">Factorys</p>
            <div class="firstFactoryDiv">
                <div class="firstFactoryOwnerIcon"></div>
                <p class="FactoryName">Factory Name: {{this.factoryInfo[0]['name']}}</p>
                <p class="FactoryLevel">Factory Level: {{this.factoryInfo[0].level}}</p>
                <!-- <router-link to="work/factory"> -->
                <div class="WorkButton" style="text-decoration: none;" @click="this.changeFactoryFirst()">Work</div>
                <!-- </router-link> -->
                <div class="splitLine"></div>
            </div>
            <div class="secondFactoryDiv">
                <div class="secondFactoryOwnerIcon"></div>
                <p class="FactoryName">Factory Name: {{this.factoryInfo[1]['name']}}</p>
                <p class="FactoryLevel">Factory Level: {{this.factoryInfo[1].level}}</p>
                <!-- <router-link to="work/factory"> -->
                <div class="WorkButton" @click="this.changeFactorySecond()">Work</div>
                <!-- </router-link> -->
                <div class="splitLine"></div>
            </div>
            <div class="thirdFactoryDiv">
                <div class="thirdFactoryOwnerIcon"></div>
                <p class="FactoryName">Factory Name: {{this.factoryInfo[2]['name']}}</p>
                <p class="FactoryLevel">Factory Level: {{this.factoryInfo[2].level}}</p>
                <!-- <router-link to="work/factory"> -->
                <div class="WorkButton" @click="this.changeFactoryThird()">Work</div>
                <!-- </router-link> -->
                <div class="splitLine"></div>
            </div>
            <div class="factoryButtonDiv">
                <!-- <router-link to="/work/factory/local/search"> -->
                    <div class="allFactorysInYourState" @click="this.sendRegion()">All Factory In Your State</div>
                <!-- </router-link> -->
                <router-link to="/work/factory/global/search">
                    <div class="allFactorysInWholeWorld">All Factory In Whole World</div>
                </router-link>
            </div>
        </div>
        <div class="storageDiv" @click="this.createFactory()">
            Storage
        </div>
        <AppFooterMenu/>
    </div>
  
</template>

      <!-- Fallback slot for error state -->
<script>
  import AppHeader from './headers/AppHeader.vue'
  import AppFooterMenu from './headers/footerMenu.vue'
  import axios from 'axios'
  import LoadingOverlay from 'vue-loading-overlay';
  import 'vue-loading-overlay/dist/css/index.css';
  export default {
    components: {
        AppHeader,
        AppFooterMenu,
        LoadingOverlay
    },
    data(){
        return{
            loading: true,
            dataLoaded: false,
            watchWidthFunction: null,
            factoryType:'Gold Factory',
            energy: -1,
            money: 0,
            currentRegion: '',
            factoryInfo:[{},{},{}],
            currentFactoryId:0,
            currentFactory:[],
            ownerExperience:0,
            ownerStat:{},
            fillingEnergyValue:200,
            changeFillButton: false,
            autoWorkBoolian: 0,
            fillDate: 0,
            lastFillTime: 0,
            lastFillInfo: 0,
            lastFiilDay: 0,
            regionHealthIndex: 1,
            workTimeBoolian: false,
            refilClickTime: 0,
            fill_button: 'Fill Energy',
            interval: '',
            last_fill_manual: 0,
            last_fill_hour_manual: 0,
            last_fill_day_manual: 0,
            manualAutoFilling: 0,
            manualAutoFillingResponse: 0,
            autoWorkBoolian: 0,
            lft: 0,
            newRefilManualDate:0,
            startAutoWork: 0,
            manualRefillButton: 0,
            
            autoWorkStartTime: 0,
            interval: 0,
            autoTume: 0,
            autoWorkTimeDifference: 0,
            autoWorkInactiveCount: 0,
            autoFillTime: 0,
            education: 0,
            regionHealth:0,
            curMoney: 0,
            autoRefillTime: 1000,
            refillTimerObject: 0,
            autoWorkTIme: 300,
            autoWorkObject: 0,
            autoWorkButtonBoolian: true,
            // ip: 'http://94.43.110.179:80',
            // ip: 'http://127.0.0.1:80/',
            ip: 'http://tato1999.pythonanywhere.com/'
        }
    },
    methods:{
        openCloseFill(){
            if(!this.changeFillButton){
                this.changeFillButton = true
                this.fillingEnergyValue = 200
                document.querySelector('.changeEnergySize').style.visibility = 'visible'
            }else{
                this.changeFillButton = false
                document.querySelector('.changeEnergySize').style.visibility = 'hidden'
            }
        },
        setFillSize(event){
            this.fillingEnergyValue = parseInt(event.target.textContent)
            this.changeFillButton = false
                document.querySelector('.changeEnergySize').style.visibility = 'hidden'

        },
        getInfo(){
            // const path = 'http://192.168.4.48:80/profile';
            //  const path = 'http://192.168.54.172:80/profile'
            const path = this.ip+'/profile'
            axios.post(path,{
            id: localStorage.getItem('id'),
             }).then((res) => {
                console.log(res.data)
                 this.energy = res.data.energy
                //  this.money = res.data.gold,
                 this.education = res.data.education
                 this.currentRegion = res.data.living_region,
                 this.currentFactoryId = res.data.current_factory
                 console.log(this.currentRegion)
                //  console.log(res.data)
                //  console.log(this.currentFactoryId)
                 document.querySelector('.fullEnergyBar').style.width = res.data.energy/2 + '%'
                })
             .catch((err) => {
                 console.error(err)
             })
         },
         get_all_factory(){
            const path = 'http://192.168.4.48:80/get_all_factory'
         },
         send_factoryType(){
            //    const path = 'http://192.168.4.48:80//profile';
            //  const path = 'http://192.168.54.172:80/profile'
            const path = this.ip+'/profile'
            if(!this.workTimeBoolian){
                axios.post(path,{
                id: localStorage.getItem('id'),
                factory: this.factoryType
             }).then((res) => {
                console.log(res.data)
                //  console.log(res.data)
                //  console.log(this.currentFactoryId)
                })
             .catch((err) => {
                 console.error(err)
             })
            }else{
             axios.post(path,{
                id: localStorage.getItem('id'),
                factory: this.factoryType
             }).then((res) => {
                console.log(res.data)
                 this.workTimeBoolian = false
                //  console.log(res.data)
                //  console.log(this.currentFactoryId)
                })
             .catch((err) => {
                 console.error(err)
             })
            }
         },
         sendReffilInfo(){
            const path = this.ip+'/refill'
            //  const path = 'http://192.168.4.48:80/refill';
            axios.post(path,{
                id: localStorage.getItem('id'),
                energy: this.energy,
                lastFill: this.lastFillTime,
                lastFillInfo: this.lastFillInfo,
                lastFiilDay: this.lastFiilDay,
                refilClickTime: this.refilClickTime,
                lastFillManual: this.last_fill_manual,
                lastFillHourManual: this.last_fill_hour_manual,
                lastFillDayManual: this.last_fill_day_manual,
                manualAutoFilling: this.manualAutoFilling,
                lft: this.lft
             })
             .then((res) => {
                 console.log(res)
                //  this.lastFillTime = res.data.last_fill
                 this.manualAutoFillingResponse = res.data.manualFIllingRealMinute
                //  console.log(this.currentFactoryId)
                 this.currentRegion = res.data.living_region,
                 this.currentFactoryId = res.data.current_factory
                 document.querySelector('.fullEnergyBar').style.width = res.data.energy/2 + '%'
                })
             .catch((err) => {
                 console.error(err)
             })
         },
         sendReffilInfo(){
            const path = this.ip+'/refill'
            //  const path = 'http://192.168.4.48:80/refill';
            axios.post(path,{
                id: localStorage.getItem('id'),
                energy: this.energy,
                manualAutoFilling: this.manualAutoFilling,
                lft: this.lft
             })
             .then((res) => {
                 console.log(res)
                 this.manualAutoFillingResponse = res.data.manualFIllingRealMinute
                 document.querySelector('.fullEnergyBar').style.width = res.data.energy/2 + '%'
                })
             .catch((err) => {
                 console.error(err)
             })
         },
         workInFactory(){

            if(this.energy != 0 && this.energy > 0){
                this.workTimeBoolian = true
                this.factoryType = this.currentFactory.type
                console.log(this.regionHealth)
                if(this.factoryType == 'Gold Factory'){
                    this.curMoney = ((this.education*0.06)+(this.regionHealth*0.04)) * this.fillingEnergyValue
                    // console.log((this.education*0.06)+(this.regionHealth*0.04))
                }else{
                    this.curMoney = ((this.education*0.06)+(this.regionHealth*0.04)) * this.fillingEnergyValue
                    // console.log("Sjdjsandjansd"+(this.education*0.06)+(this.regionHealth*0.04))
                }
                // console.log("ajsdasjkdjasdj"+this.curMoney)
                this.money += this.curMoney
                this.energy -= this.fillingEnergyValue
                if(this.energy >= 0){
                    this.sendWorkInfo()
                    console.log(this.energy)
                    // console.log(this.money)
                }else{
                    console.log("Not Enough Energy")
                }
            }else if(this.energy == 0){
                console.log("Not Enough Energy")
            }
         },
         sendWorkInfo(){
            // const path = 'http://192.168.4.48:80/send_work_info'

            const path = this.ip+'/send_work_info'
            axios.post(path,{
                id: localStorage.getItem('id'),
                resource: this.curMoney,
                energy: this.energy,
                factory: this.factoryType
            }).then((res) => {
                console.log(res)
                this.energy = res.data.energy
                document.querySelector('.fullEnergyBar').style.width = this.energy + '%'
            }).catch((err) => {
                console.log(err)
            })
         },
         changeFactoryFirst(){
            const path = this.ip+'//change_work_factory'

            //  const path = 'http://192.168.4.48:80//change_work_factory';
            axios.post(path,{
                id: localStorage.getItem('id'),
                nextFactoryId:this.factoryInfo[0]
             })
             .then((res) => {
                 console.log(res)
                 this.currentFactoryId = res.data.nextFactory
                 this.getFactory()
                })
             .catch((err) => {
                 console.error(err)
             })
         },
         changeFactorySecond(){
            const path = this.ip+'//change_work_factory'

            //  const path = 'http://192.168.4.48:80//change_work_factory';
            axios.post(path,{
                id: localStorage.getItem('id'),
                nextFactoryId:this.factoryInfo[1]
             })
             .then((res) => {
                 console.log(res)
                 this.currentFactoryId = res.data.nextFactory
                 this.getFactory()
                })
             .catch((err) => {
                 console.error(err)
             })
         },
         changeFactoryThird(){
            const path = this.ip+'//change_work_factory'
            //  const path = 'http://192.168.4.48:80//change_work_factory';
            axios.post(path,{
                id: localStorage.getItem('id'),
                nextFactoryId:this.factoryInfo[2]
             })
             .then((res) => {
                 console.log(res)
                 this.currentFactoryId = res.data.nextFactory
                 this.getFactory()
                })
             .catch((err) => {
                 console.error(err)
             })
         },
         getLastFillDate(){
            const path = this.ip+'/get_last_fill'
            //  const path = 'http://192.168.4.48:80/get_last_fill';
            axios.post(path,{
                id: localStorage.getItem('id')
            }).then((res) => {
                console.log(res)
                this.newRefilManualDate = (new Date() - new Date(res.data.lastFillTime))/60000
                if(this.newRefilManualDate >= 5){
                    this.fill_button = 'Fill Energy'
                    this.manualRefillButton = 1
                    // this.manualRefilEnergy()
                    console.log(new Date() - new Date(res.data.lastFillTime)/60000)
                }else{
                    console.log((new Date() - new Date(res.data.lastFillTime))/60000)
                    this.fill_button = "Not Yet"
                    this.manualRefillButton = 0
                }
            }).catch((err) => {
                console.log(err)
            })
         },
         sendManualRefillInfo(){
                // const path = 'http://192.168.4.48:80/send_manual_refill_info';

                const path = this.ip+'/send_manual_refill_info'
                axios.post(path,{
                    id: localStorage.getItem('id'),
                    energy: this.energy,
                    lft: this.lft
                }).then((res) => {
                    this.energy = res.data.energy
                    document.querySelector('.fullEnergyBar').style.width = this.energy/2 + '%'
                }).catch((err) => {
                    console.log(err)
                })
            },
         manualRefilEnergy(){
            this.getLastFillDate()
            if(this.manualRefillButton == 1){
                if(this.energy < 200){
                    this.manualAutoFilling = 1
                    this.lft = new Date()
                    this.energy = 200
                    this.sendManualRefillInfo()
                    this.fill_button = "Not Yet"
                    this.manualRefillButton = 0
                }
            // }else{
            //     console.log("test")
            //     this.getLastFillDate()
            }
         },      
         createFactory(){
            const path = 'http://192.168.4.48:80/create_factory'
            // const path =this.ip+'/create_factory'
             axios.post(path,{
                id: localStorage.getItem('id'),
             }).then((res) => {
                console.log(res)
             }).catch((err) => {
                console.log(err)
             })
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
         getFactory(){
            // const path = 'http://192.168.4.48:80/get_all_factory'
            const path = this.ip+'/get_all_factory'
             axios.post(path,{
                region: this.currentRegion,
                id: localStorage.getItem('id')
             }).then((res) => {
                this.factoryInfo = res.data
                console.log(this.factoryInfo)
                this.factoryLevel = res.data.level
                this.factoryExp = res.data.experience
                this.currentFactory = this.factoryInfo.find(item => item.id == this.currentFactoryId)
                console.log(this.currentFactoryId)
                // this.ownerExperience = this.currentFactory.owner.working_experience
                this.ownerStat = this.currentFactory.owner
                this.factoryType = this.currentFactory.type
                setTimeout(() => {
                    document.querySelector('.factoryIcon').style.backgroundImage = `url(${require('@/assets/factoryIcon/'+this.currentFactory.factory_icon)})`
                    document.querySelector('.firstFactoryOwnerIcon').style.backgroundImage = `url(${require('@/assets/factoryIcon/'+this.factoryInfo[0].factory_icon)})`
                    document.querySelector('.secondFactoryOwnerIcon').style.backgroundImage = `url(${require('@/assets/factoryIcon/'+this.factoryInfo[1].factory_icon)})`
                    document.querySelector('.thirdFactoryOwnerIcon').style.backgroundImage = `url(${require('@/assets/factoryIcon/'+this.factoryInfo[2].factory_icon)})`
                    localStorage.removeItem('factory')
                },1000)
             }).catch((err) => {
                console.log(err)
             })
         },
         sendRegion(){
            localStorage.setItem('reg', this.currentRegion)
            this.$router.push({
              path: `/work/factory/local/search` })
         },
         getRegion(){
            const path = this.ip+'/get_region_info'
            // const path = 'http://192.168.4.48:80/get_region_info'
            axios.post(path,{
                id: this.currentRegion,
                user: localStorage.getItem('id')
            }).then((res) => {
                console.log(this.currentRegion)
                console.log(res.data)
                this.regionHealth = res.data.medicinIndex
            }).catch((err) => {
                console.log(err)
            })
         },
         autoRefillTest(){
            // const path = 'http://192.168.4.48:80/auto_refill'

            const path = this.ip+'/auto_refill'
            axios.post(path,{
                id: localStorage.getItem('id'),
                date: new Date()
            }).then((res) => {
                console.log(res.data)
                this.energy = res.data.energy
                this.autoRefillTime = (res.data.timer*1)*1000
                clearInterval(this.refillTimerObject)
                if(document.querySelector('.fullEnergyBar')){
                    document.querySelector('.fullEnergyBar').style.width = this.energy/2 + '%'
                }
                console.log(this.autoRefillTime)
                setTimeout(() => {
                    this.refillTimerObject = setInterval(() => {
                    this.autoRefillTest()
                }, (this.autoRefillTime ))
                },500)
            }).catch((err) => {
                console.log(err)
            })
         },
         autoWork(){
            // const path = 'http://192.168.4.48:80/auto_work_start_end'

            const path = this.ip+'/auto_work_start_end'
            axios.post(path,{
                id: localStorage.getItem('id'),
                date: new Date(),
                energy: this.energy
            }).then((res) => {
                console.log(res)
                this.autoWorkTIme = 300
                if(res.data.start == 1){
                    // this.startAutoWorkNew()
                    this.autoWorkButtonBoolian = false
                    document.querySelector('.autoWorkButton').style.backgroundColor = 'green'
                    this.autoWorkObject = setInterval(() => {
                        this.autoWorkTIme--
                        if(this.autoWorkTIme <=1 ){
                            this.autoWorkTIme = 300
                            // this.manualRefilEnergy()

                                this.manualRefilEnergy()
                                this.workInFactory()
                                this.sendAutoWorkNewDate()
                        }
                        
                    },1000)
                }else{
                    // clearInterval(this.interval)
                    clearInterval(this.autoWorkObject)
                    this.autoWorkButtonBoolian = true
                    document.querySelector('.autoWorkButton').style.backgroundColor = '#6d2110'
                }
            }).catch((err) => {
                console.log(err)
            })
         },
         sendAutoWorkNewDate(){
            const path = this.ip+'send_auto_work_new_date'
            axios.post(path,{
                id: localStorage.getItem('id'),
                date: new Date()
            })
            .then((res) => {
                console.log(res)
            })
            .catch((err) => {
                console.log(err)
            })
         },
         startAutoWorkNew(){
            console.log('asduhsadasbndsnadnasidjasn'+this.autoWorkTIme*1000)
            this.interval = setInterval(() => {
                this.manualRefilEnergy()
                setTimeout(() => {
                    this.manualRefilEnergy()
                    setTimeout(() => {
                        this.workInFactory()
                    },300)
                },300)
            },this.autoWorkTIme*1000)
         },
         checkPrevAutoWork(){
            // const path = 'http://127.0.0.1:80/check_auto_work_start_end'

            const path = this.ip+'/check_auto_work_start_end'
            axios.post(path,{
                id: localStorage.getItem('id'),
                date: new Date(),
                factory: this.factoryType
            }).then((res) => {
                console.log(res)
                // clearInterval(this.interval)
                this.autoWorkTIme = res.data.timer
                if(res.data.start == 1){
                    // this.startAutoWorkNew()
                    this.autoWorkButtonBoolian = false
                    console.log('fajnfjasnfjanfjasnfjasnfajsnfa'+res.data.timer)
                    document.querySelector('.autoWorkButton').style.backgroundColor = 'green'
                    this.autoWorkTIme = res.data.timer
                    this.autoWorkObject =  setInterval(() => {
                        this.autoWorkTIme--
                        if(this.autoWorkTIme <= 1 ){
                            this.autoWorkTIme = 300
                            // clearInterval(this.autoWorkObject)
                            if(this.energy >= 200){
                                this.workInFactory()
                                this.sendAutoWorkNewDate()
                            }else{
                                this.getLastFillDate()
                                setTimeout(() => {
                                    this.manualRefilEnergy()
                                },100)
                                setTimeout(() => {
                                    this.workInFactory()
                                    this.sendAutoWorkNewDate()
                                },500)
                            }
                                // setTimeout(() => {
                                // },300)
                            // },300)
                        }
                    },1000)
                }else{
                    // clearInterval(this.interval)
                    clearInterval(this.autoWorkObject)
                    this.autoWorkButtonBoolian = true
                    document.querySelector('.autoWorkButton').style.backgroundColor = '#6d2110'
                }
            }).catch((err) => {
                console.log(err)
            })
         },
         formatTime() {
            if (isNaN(this.autoWorkTIme)) {
                console.log(this.autoWorkTIme)
                return "Invalid Time";
            }

            const minutes = Math.floor(this.autoWorkTIme / 60);
            const seconds = this.autoWorkTIme % 60;
            return `${minutes}:${seconds < 10 ? '0' : ''}${seconds}`;
        },
         fletchData(){
            const endpoints = [
                { url: this.ip+'/profile', data: { id: localStorage.getItem('id') } },
                { url: this.ip+'/get_last_fill', data: { id: localStorage.getItem('id') } },
                { url: this.ip+'/get_region_info', data: { id: localStorage.getItem('id') } },
                { url: this.ip+'/get_current_factory', data: { id: localStorage.getItem('id') } },
                { url: this.ip+'/get_all_factory', data: { id: localStorage.getItem('id')}}
                // Add more endpoints as needed
            ];

      // Create an array of promises for each axios.post request
            const requests = endpoints.map(endpoint => axios.post(endpoint.url, endpoint.data));

      // Use Promise.all to wait for all requests to complete
            Promise.all(requests)
            .then((res) => {
                console.log(res)
                this.energy = res[0].data.energy
                // this.money = res[0].data.gold,
                this.education = res[0].data.education
                this.currentRegion = res[0].data.living_region,
                this.currentFactoryId = res[0].data.current_factory
                this.newRefilManualDate = (new Date() - new Date(res[1].data.lastFillTime))/60000
                if(this.newRefilManualDate >= 5){
                    this.fill_button = 'Fill Energy'
                    // this.manualRefilEnergy()
                    console.log(new Date() - new Date(res[1].data.lastFillTime)/60000)
                }else{
                    console.log((new Date() - new Date(res[1].data.lastFillTime))/60000)
                    this.fill_button = "Not Yet"
                }
                this.currentRegion = res[3].data.currentRegion
                this.regionHealth = res[2].data.medicinIndex
                if(res[4].data != undefined){
                    this.factoryInfo = res[4].data
                    console.log(this.factoryInfo)
                
                    this.factoryLevel = res[2].data.level
                    this.factoryExp = res[2].data.experience
                    this.currentFactory = res[3].data.currentFactoryList[0]
                    console.log(this.currentFactory)
                    // if((this.currentFactory = this.factoryInfo.find(item => item.id == this.currentFactoryId) ) != undefined){
                    //     console.log(this.currentFactoryId)
                    //     this.currentFactory = this.factoryInfo.find(item => item.id == this.currentFactoryId)
                    //     // this.ownerExperience = this.currentFactory.owner.working_experience
                    this.ownerStat = this.currentFactory.owner
                    this.factoryType = this.currentFactory.type
                    // }else{
                        
                    //     this.ownerStat = "you Cant Work distance"
                    //     this.factoryType = 'You Are here' + this.currentRegion
                    // }
                }
                this.dataLoaded = true
                this.loading = false
                setTimeout(() => {
                    document.querySelector('.factoryIcon').style.backgroundImage = `url(${require('@/assets/factoryIcon/'+this.currentFactory.factory_icon)})`
                    document.querySelector('.firstFactoryOwnerIcon').style.backgroundImage = `url(${require('@/assets/factoryIcon/'+this.factoryInfo[0].factory_icon)})`
                    document.querySelector('.secondFactoryOwnerIcon').style.backgroundImage = `url(${require('@/assets/factoryIcon/'+this.factoryInfo[1].factory_icon)})`
                    document.querySelector('.thirdFactoryOwnerIcon').style.backgroundImage = `url(${require('@/assets/factoryIcon/'+this.factoryInfo[2].factory_icon)})`
                    document.querySelector('.fullEnergyBar').style.width = res[0].data.energy/2 + '%'
                    localStorage.removeItem('factory')
                },100)
                
                
                return res
            })
            .catch((err) => {
                console.log(err)
            })
         },
         isLoadingFunction(){

         }
    },
    mounted(){
        // this.sendIdInfo()
        // this.getInfo()
        // setTimeout(() => {
        //     console.log(this.currentFactoryId)
        // },500)
        // this.refillAfterInactiveSection()
        // this.getAutoWorkBool()
        // this.autoRefill()
        // this.getFactory()
        setTimeout(() => {
            this.fletchData()
        },300)
        setTimeout(() => {
            this.getLastFillDate()
        },650)
        setTimeout(() => {
            this.checkPrevAutoWork()
        }, 1000)
        // this.refillTimerObject =  setInterval(() => {
            this.autoRefillTest()
        // }, this.autoRefillTime);
    },
    watch:{
        watchWidthFunction(){
            document.querySelector('.fullEnergyBar').style.width = res.data.energy/2 + '%'
        },

    }
  }
  </script>

<style scoped>
    .mainDiv{
        height: 291.5vw !important;
        background-image: url('/src/assets/png-transparent-flag-flag-countries-flags-spherical-flag-national-flag-spherical 1.png');
        background-size: 100vw 100vh;
    }
    .regionResDiv{
        width: 92.5vw;
        height: 37vw;
        flex-shrink: 0;
        border-radius: 5vw;
        background: #6F8B87;
        position: absolute;
        margin: 35.75vw auto auto calc((100vw - 92.5vw)/2);
    }
    .resRegionName{
        color: #FFF;
        text-align: center;
        font-family: Poppins;
        font-size: 5vw;
        font-style: normal;
        font-weight: 700;
        line-height: normal;
        position: absolute;
        top: 0;
        margin: 2.75vw auto auto 4vw;
    }
    .resInsideDiv{
        width: 12.25vw;
        height: 15vw;
        position: absolute;
        margin-top: 13vw;
        display: grid;
    }
    .resInsideDivFirst{
        margin-left: 6.25vw
    }
    .resInsideDivSecond{
        margin-left: 26.25vw
    }
    .resInsideDivThird{
        margin-left: 46.25vw
    }
    .resInsideDivFour{
        margin-left: 66.25vw
    }

    .resInsideDivFive{
        margin-left: 90.25vw
    }
    .resInsideDiv p{
        margin-top: -.25vw;
        color: #FFFFFE;
        text-align: center;
        font-family: Poppins;
        font-size: 5vw;
        font-style: normal;
        font-weight: 700;
        line-height: normal;
    }
    .goldText{
        /* position: absolute; */
        margin: -5.5vw;
        color: #FFD705;
        text-align: center;
        font-family: Poppins;
        font-size: 5vw;
        font-style: normal;
        font-weight: 700;
        line-height: normal;
        justify-content: center;
        align-items: center;
    }
    .oilText{
        /* position: absolute; */
        margin: -5.5vw;
        color: #0E0000;
        text-align: center;
        font-family: Poppins;
        font-size: 5vw;
        font-style: normal;
        font-weight: 700;
        line-height: normal;
        justify-content: center;
        align-items: center;
    }
    .oreText{
        /* position: absolute; */
        margin: -5.5vw;
        color: #840707;
        text-align: center;
        font-family: Poppins;
        font-size: 5vw;
        font-style: normal;
        font-weight: 700;
        line-height: normal;
        justify-content: center;
        align-items: center;
    }
    .uraniumText{
        /* position: absolute; */
        margin: -5.5vw;
        color: #4DE306;
        text-align: center;
        font-family: Poppins;
        font-size: 5vw;
        font-style: normal;
        font-weight: 700;
        line-height: normal;
        justify-content: center;
        align-items: center;
    }
    .currentFactoryDiv{
        z-index: 1;
        width: 92.5vw;
        height: 46.75vw;
        flex-shrink: 0;
        border-radius: 20px;
        background: #6F8B87;
        position: absolute;
        margin: 79.5vw auto auto calc((100vw - 92.5vw)/2);
    }
    .factoryInformationDiv{
        width: 100%;
        height: 17vw;
        margin-top: 1vw;
        /* background-color: red; */
    }
    .informationDivFirst{
        width: 100%;
        height: 5.6vw;
        /* background-color: rgb(115, 115, 15); */
    }
    .informationDivFirst p{
        margin: 0;
        color: #FFF;
        text-align: center;
        font-family: Play;
        font-size: 3.75vw;
        font-style: normal;
        font-weight: 400;
        line-height: normal;
    }
    .firstSplitLine{
        width: 89vw;
        height: 0.25vw;
        background: #000;
        margin: auto auto auto calc((100% - 89vw)/2);
    }
    .informationDivSecond{
        width: 100%;
        height: 5.6vw;
        /* background-color: rgb(76, 76, 42); */
    }
    .informationDivSecond p{
        margin: 0;
        color: #FFF;
        text-align: center;
        font-family: Play;
        font-size: 3.75vw;
        font-style: normal;
        font-weight: 400;
        line-height: normal;
    }
    .secondSplitLine{
        width: 89vw;
        height: 0.25vw;
        background: #000;
        margin: auto auto auto calc((100% - 89vw)/2);
    }
    .informationDivThird{
        width: 100%;
        height: 5.6vw;
        /* background-color: rgb(48, 27, 88); */
    }
    .informationDivThird p{
        margin: 0;
        color: #FFF;
        text-align: center;
        font-family: Play;
        font-size: 3.75vw;
        font-style: normal;
        font-weight: 400;
        line-height: normal;
    }
    .thirdSplitLine{
        width: 89vw;
        height: 0.25vw;
        background: #000;
        margin: auto auto auto calc((100% - 89vw)/2);
    }
    .factoryInformationDivCreation{
        width: 100%;
        height: 12.75vw;
    }
    .factoryInformationDivCreation p{
        margin: 0;
        color: #FFF;
        text-align: left;
        font-family: Play;
        font-size: 3.75vw;
        font-style: normal;
        font-weight: 400;
        line-height: normal;
    }
    .factoryIcon{
        width: 12.5vw;
        height: 12.5vw;
        margin-left: 4vw;
        position: absolute;
        background-image: url('/src/assets/factoryIcon/silverFactory.png');
        background-size: 100% 100%;
    }
    .energyAndWorkBar{
        width: 100%;
        height: 13.75vw;
    }
    .emptyEnergyBar{
        width: 48vw;
        height: 3.75vw;
        background: #D9D9D9;
        margin-left: 22.5vw;
        margin-top: 4vw;
    }
    .fullEnergyBar{
        width: 90%;
        height: 3.75vw;
        background: #B28F0F;
    }
    .fillButton{
        color: #FFA903;
        text-align: center;
        font-family: Play;
        font-size: 3.75vw;
        font-style: normal;
        font-weight: 400;
        line-height: normal;
        margin: -4vw auto auto 73.5vw;
    }
    .workButton{
        width: 20.5vw;
        height: 5.25vw;
        flex-shrink: 0;
        background: #126D10;
        margin-left: 11.5vw;
        margin-top: 1.25vw;
        color: #fff;
        text-align: center;
        font-family: Play;
        font-size: 3.75vw;
        font-style: normal;
        font-weight: 400;
        line-height: 5.25vw;
        cursor: pointer;
    }
    .autoWorkButton{
        position: absolute;
        width: 25.5vw;
        height: 5.25vw;
        flex-shrink: 0;
        background: #6d2110;
        margin-left: 35.5vw;
        margin-top: -5.2vw;
        color: #fff;
        text-align: center;
        font-family: Play;
        font-size: 3.75vw;
        font-style: normal;
        font-weight: 400;
        line-height: 5.25vw;
        cursor: pointer;
    }
    .energyForFilling{
        width: 16.75vw;
        height: 5.25vw;
        flex-shrink: 0;
        background: #FFD705;
        margin-left: 64vw;
        margin-top: -5.25vw;
        color: #000;
        text-align: center;
        font-family: Play;
        font-size: 3.75vw;
        font-style: normal;
        font-weight: 400;
        line-height: 5.25vw;
        cursor: pointer;
    }
    .changeEnergySize{
        width: 16.75vw;
        height: 20.25vw;
        flex-shrink: 0;
        background: #54706b;
        margin-left: 64vw;
        /* margin-top: -5.25vw; */
        z-index: 1;
        color: #000;
        text-align: center;
        font-family: Play;
        font-size: 3.75vw;
        font-style: normal;
        font-weight: 400;
        line-height: 5.25vw;
        border-top: 0.1vw solid black;
        overflow-y: auto;
        visibility: hidden;
    }
    .changeableButton{
        border-top: 0.1vw solid black;
    }
    .topicOfFactorySearchDiv{
        color: #FFF;
        text-align: center;
        font-family: Play;
        font-size: 5vw;
        font-style: normal;
        font-weight: 400;
        line-height: normal;
    }
    .firstFactoryDiv{
        width: 100%;
        height: 20vw;
        margin-top: 5.5vw;
    }
    .factorySearchDiv{
        z-index: 0;
        width: 92.5vw;
        height: 104.5vw;
        flex-shrink: 0;
        border-radius: 5vw;
        background: #6F8B87;
        position: absolute;
        margin: 130.25vw auto auto calc((100vw - 92.5vw)/2);
    }
    .firstFactoryOwnerIcon{
        width: 17.5vw;
        height: 17.5vw;
        margin-left: 4vw;
        position: absolute;
        background-image: url('/src/assets/profile_icon.png');
        background-size: 100% 100%;
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
    }
    .secondFactoryOwnerIcon{
        width: 17.5vw;
        height: 17.5vw;
        margin-left: 4vw;
        position: absolute;
        background-image: url('/src/assets/profile_icon.png');
        background-size: 100% 100%;
    }
    .thirdFactoryDiv{
        width: 100%;
        height: 20vw;
    }
    .thirdFactoryOwnerIcon{
        width: 17.5vw;
        height: 17.5vw;
        margin-left: 4vw;
        position: absolute;
        background-image: url('/src/assets/profile_icon.png');
        background-size: 100% 100%;
    }
    .allFactorysInYourState{
        width: 78vw;
        height: 7.5vw;
        flex-shrink: 0;
        background: #4A1111;
        margin: 2vw auto auto calc((100% - 78vw)/2);
        color: #fff;
        text-align: center;
        font-family: Play;
        font-size: 3.75vw;
        font-style: normal;
        font-weight: 400;
        line-height: 7.5vw;
    }
    .allFactorysInWholeWorld{
        width: 78vw;
        height: 7.5vw;
        flex-shrink: 0;
        background: #4A1111;
        margin: 2vw auto auto calc((100% - 78vw)/2);
        color: #fff;
        text-align: center;
        font-family: Play;
        font-size: 3.75vw;
        font-style: normal;
        font-weight: 400;
        line-height: 7.5vw;
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
    .loading-spinner {
        border: 4px solid rgba(0, 0, 0, 0.1);
        border-radius: 50%;
        border-top: 4px solid #3498db; /* Use your preferred color */
        width: 40px;
        height: 40px;
        animation: spin 1s linear infinite;
        margin: 20px auto;
        z-index: 99999999;
    }

    @keyframes spin {
        0% { transform: rotate(0deg); }
        100% { transform: rotate(360deg); }
    }
</style>