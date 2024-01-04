<template>
    <div class="mainDiv" style="background-color: #0E0000; width:100%; height: 291.5vw; position: absolute; display: grid; top: 0; left: 0;">
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
                    <div class="autoWorkButton" @click="this.startAutoWorkFunction()">Auto 5 Min</div>
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
            
            autoWorkStartTime: 0,
            interval: 0,
            autoTume: 0,
            autoWorkTimeDifference: 0,
            autoWorkInactiveCount: 0,
            autoFillTime: 0,
            education: 0,
            regionHealth:0,
            curMoney: 0
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
        sendIdInfo(){
             const path = 'http://127.0.0.1:80/profile';
            //  const path = 'http://192.168.54.172:80/profile'
            // const path = 'http://94.43.110.179:80/profile'
            if(!this.workTimeBoolian){
                axios.post(path,{
                id: localStorage.getItem('id'),
                money: this.money,
                energy: this.energy,
                factory: this.factoryType
             }).then((res) => {
                console.log(res.data)
                 this.energy = res.data.energy
                 this.money = res.data.gold,
                 this.education = res.data.education
                 this.currentRegion = res.data.living_region,
                 this.currentFactoryId = res.data.current_factory
                 this.refilClickTime = res.data.refilClickTime

                 console.log(this.currentRegion)
                //  console.log(res.data)
                //  console.log(this.currentFactoryId)
                 document.querySelector('.fullEnergyBar').style.width = res.data.energy/2 + '%'
                })
             .catch((err) => {
                 console.error(err)
             })
            }else{
             axios.post(path,{
                id: localStorage.getItem('id'),
                money: this.money,
                energy: this.energy,
                factory: this.factoryType
             }).then((res) => {
                console.log(res.data)
                 this.energy = res.data.energy
                 this.money = res.data.gold,
                 this.currentRegion = res.data.living_region,
                 this.currentFactoryId = res.data.current_factory
                 this.workTimeBoolian = false
                 console.log(this.currentRegion)
                //  console.log(this.currentFactoryId)
                 document.querySelector('.fullEnergyBar').style.width = res.data.energy/2 + '%'
                })
             .catch((err) => {
                 console.error(err)
             })
            }
             
         },
         send_factoryType(){
               const path = 'http://127.0.0.1:80//profile';
            //  const path = 'http://192.168.54.172:80/profile'
            // const path = 'http://94.43.110.179:80/profile'
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
            // const path = 'http://94.43.110.179:80/refill'
             const path = 'http://127.0.0.1:80/refill';
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
         workInFactory(){

            if(this.energy != 0 && this.energy > 0){
                this.workTimeBoolian = true
                this.factoryType = this.currentFactory.type
                console.log(this.factoryType)
                if(this.factoryType == 'Gold Factory'){
                    this.curMoney = ((this.education*0.06)+(this.regionHealth*0.04)) * this.fillingEnergyValue
                }else{
                    this.curMoney = ((this.education*0.12)+(this.regionHealth*0.08)) * this.fillingEnergyValue
                }
                console.log(this.curMoney)
                this.money += this.curMoney
                this.energy -= this.fillingEnergyValue
                if(this.energy >= 0){
                    this.sendIdInfo()
                    // console.log(this.energy)
                    // console.log(this.money)
                }else{
                    console.log("Not Enough Energy")
                }
            }else if(this.energy == 0){
                console.log("Not Enough Energy")
            }
         },
         startAutoWorkFunction(){
            if(this.startAutoWork == 0){
                this.checkAutoWork()
                document.querySelector('.autoWorkButton').style.backgroundColor = 'green'
                this.startAutoWork = 1
            }else{
                clearInterval(this.interval)
                this.startAutoWork = 0
                this.sendAutoWorkInfo()
                document.querySelector('.autoWorkButton').style.backgroundColor = '#6d2110'
                console.log('asdasdasdas')
            }
         },
         changeFactoryFirst(){
            // const path = 'http://94.43.110.179:80//change_work_factory'

             const path = 'http://127.0.0.1:80//change_work_factory';
            axios.post(path,{
                id: localStorage.getItem('id'),
                nextFactoryId:this.factoryInfo[0]
             })
             .then((res) => {
                 console.log(res)
                 this.currentFactoryId = res.data.nextFactory
                 this.getFactory()
                 this.sendAutoWorkInfo()
                })
             .catch((err) => {
                 console.error(err)
             })
         },
         changeFactorySecond(){
            // const path = 'http://94.43.110.179:80//change_work_factory'

             const path = 'http://127.0.0.1:80//change_work_factory';
            axios.post(path,{
                id: localStorage.getItem('id'),
                nextFactoryId:this.factoryInfo[1]
             })
             .then((res) => {
                 console.log(res)
                 this.currentFactoryId = res.data.nextFactory
                 this.getFactory()
                 this.sendAutoWorkInfo()
                })
             .catch((err) => {
                 console.error(err)
             })
         },
         changeFactoryThird(){
            // const path = 'http://94.43.110.179:80//change_work_factory'
             const path = 'http://127.0.0.1:80//change_work_factory';
            axios.post(path,{
                id: localStorage.getItem('id'),
                nextFactoryId:this.factoryInfo[2]
             })
             .then((res) => {
                 console.log(res)
                 this.currentFactoryId = res.data.nextFactory
                 this.getFactory()
                 this.sendAutoWorkInfo()
                })
             .catch((err) => {
                 console.error(err)
             })
         },
         getAutoWorkBool(){
            // const path = 'http://94.43.110.179:80/get_auto_work_bool'
             const path = 'http://127.0.0.1:80/get_auto_work_bool';
            axios.post(path,{
                id: localStorage.getItem('id'),
                })
                .then((res) => {
                    console.log(res)
                    this.startAutoWork = res.data.autoWorkbool
                    this.autoTume =  res.data.autoWorkStartTime
                    this.inactivAutoWork(this.autoTume, this.startAutoWork)
                }).catch((err) => {
                    console.log(err)
                })
         },
         checkAutoWork(){
            // const path = 'http://94.43.110.179:80/check_auto_work'
             const path = 'http://127.0.0.1:80/check_auto_work';
            axios.post(path,{
                id: localStorage.getItem('id'),
                })
                .then((res) => {
                    console.log(res)
                    this.autoTume = new Date(res.data.autoWorkTime)
                    this.autoWorkStartTime = ((new Date() - new Date(res.data.autoWorkTime))/60000)
                    console.log((new Date() - new Date(res.data.autoWorkTime))/60000)
                    if(res.data.autoWorkTime == null){
                        this.startAutoWorkWork()
                        document.querySelector('.autoWorkButton').style.backgroundColor = 'green'
                    }else if(this.autoWorkStartTime>=5){
                        this.startAutoWorkWork()
                        document.querySelector('.autoWorkButton').style.backgroundColor = 'green'
                    }else{
                        console.log('none')
                        this.startAutoWork = 0 
                        document.querySelector('.autoWorkButton').style.backgroundColor = '#6d2110'
                        alert(Math.round(5-this.autoWorkStartTime) + ' Minute: Left')
                    }
                }).catch((err) => {
                    console.log(err)
                })
         },
         sendAutoWorkInfo(){
            // const path = 'http://94.43.110.179:80/send_auto_info'
             const path = 'http://127.0.0.1:80/send_auto_info';
            if(this.startAutoWork == 1){
                axios.post(path,{
                    id: localStorage.getItem('id'),
                    autoWorkTime: new Date(),
                    autoWorkBoolian: this.startAutoWork
                }).then((res) => {
                    console.log(res)
                }).catch((err) => {
                    console.log(err)
                })
            }else{
                axios.post(path,{
                    id: localStorage.getItem('id'),
                    autoWorkTime: this.autoTume,
                    autoWorkBoolian: this.startAutoWork
                }).then((res) => {
                    console.log(res)
                }).catch((err) => {
                    console.log(err)
                })
            }
         },
         startAutoWorkWork(){
            if(this.energy < 200){
                    this.lft = new Date()
                    this.energy = 200
                    this.sendReffilInfo()
                    this.workInFactory()
                    this.sendAutoWorkInfo()
                    this.sendIdInfo()
            }else{
                this.workInFactory()
                this.sendAutoWorkInfo()
                this.sendIdInfo()
            }
            this.interval = setInterval(() => {
                if(this.energy < 200){
                    this.lft = new Date()
                    this.energy = 200
                    this.sendReffilInfo()
                    this.workInFactory()
                    this.sendAutoWorkInfo()
                    this.sendIdInfo()
                }else{
                // if(this.energy < 200){
                //     alert("First Reffil Energy")
                //     clearInterval(this.interval)
                //     this.startAutoWork = 0
                // }else{
                    this.workInFactory()
                    this.sendAutoWorkInfo()
                    this.sendIdInfo()
                }
                // }
            },300000)
         },
         inactivAutoWork(n,m){
            this.autoWorkTimeDifference = ((new Date() - new Date(n))/86400000)
            console.log('asdasdasda' + this.autoWorkTimeDifference)
            if(this.autoWorkTimeDifference < 1){
                this.autoWorkInactiveCount = ((new Date() - new Date(n))/60000)
                console.log(Math.floor(this.autoWorkInactiveCount/5))
                    this.curMoney = (((this.education*0.06)+(this.regionHealth*0.04))*40)*Math.floor(this.autoWorkInactiveCount)
                this.money += this.curMoney
                console.log(this.money)
                if(m === 1){
                    document.querySelector('.autoWorkButton').style.backgroundColor = 'green'
                    this.sendIdInfo()
                    this.startAutoWorkWork()
                }else{
                    this.startAutoWork = 0
                    document.querySelector('.autoWorkButton').style.backgroundColor = '#6d2110'
                    this.sendAutoWorkInfo()
                }
            }else{
                if(m === 1){
                    this.autoWorkInactiveCount = ((new Date() - new Date(n))/60000)
                    console.log(Math.floor(this.autoWorkInactiveCount/5))
                    this.curMoney = (((this.education*0.06)+(this.regionHealth*0.04))*40)*Math.floor(this.autoWorkInactiveCount)
                    this.money += this.curMoney
                    console.log('+'+(((this.education*0.06)+(this.regionHealth*0.04))*40))
                    this.sendIdInfo()
                    this.startAutoWork = 0
                    document.querySelector('.autoWorkButton').style.backgroundColor = '#6d2110'
                    this.sendAutoWorkInfo()
                }else{
                    console.log('auto not asjndjas')
                    document.querySelector('.autoWorkButton').style.backgroundColor = '#6d2110'
                }
            }
         },
        //  refillEnergy(){
        //     if(this.energy < 200){
        //         let date = new Date()
        //             this.lastFillTime = date.getMinutes()
        //             this.lastFillInfo = date.getHours()
        //             this.lastFiilDay = date.getDate()
        //             this.energy = 200
        //             this.manualAutoFilling = 0
        //     }
        //     this.sendReffilInfo()
        //  },
         getLastFillDate(){
            // const path = 'http://94.43.110.179:80/get_last_fill'
             const path = 'http://127.0.0.1:80/get_last_fill';
            axios.post(path,{
                id: localStorage.getItem('id')
            }).then((res) => {
                console.log(res)
                this.newRefilManualDate = (new Date() - new Date(res.data.lastFillTime))/60000
                if(this.newRefilManualDate >= 5){
                    this.fill_button = 'Fill Energy'
                    // this.manualRefilEnergy()
                    console.log(new Date() - new Date(res.data.lastFillTime)/60000)
                }else{
                    console.log((new Date() - new Date(res.data.lastFillTime))/60000)
                    this.fill_button = "Not Yet"
                }
            }).catch((err) => {
                console.log(err)
            })
         },
         manualRefilEnergy(){
            if(this.fill_button == 'Fill Energy'){
                if(this.energy < 200){
                    this.manualAutoFilling = 1
                    this.lft = new Date()
                    this.energy = 200
                    this.sendReffilInfo()
                    this.fill_button = "Not Yet"
                        // this.sendReffilInfo()
                }
            }else{
                this.getLastFillDate()
                if(this.energy < 200){
                    if(this.fill_button == 'Fill Energy'){
                        this.manualAutoFilling = 1
                        this.lft = new Date()
                        this.energy = 200
                        this.sendReffilInfo()
                        this.fill_button = "Not Yet"
                            // this.sendReffilInfo()
                        }
                    }
                }
            },
        //  refillEnergySequence(){

        //     if(this.energy < 200){
        //         this.energy = this.energy + (5+this.regionHealthIndex)
        //         let date = new Date()
        //         this.lastFillTime = date.getMinutes()
        //         this.lastFillInfo = date.getHours()
        //         this.lastFiilDay = date.getDate()
        //         this.sendReffilInfo()
        //     }
        //  },
        //  checkRefillSequence(){
        //     const path = 'http://94.43.110.179:80/calc_sequence_time'
        //     axios.post(path,{
        //         id: localStorage.getItem('id'),
        //         lastFill: this.lastFillTime,
        //         lastFillInfo: this.lastFillInfo,
        //         lastFiilDay: this.lastFiilDay,
        //      }).then((res) => {
        //         console.log(res)
        //         let inactiveRefillCount = res.data.inactiveRefillCount + ((res.data.inactiveRefillCount/5) * this.regionHealthIndex)
        //         document.querySelector('.fullEnergyBar').style.width = (this.energy + (inactiveRefillCount/2)) + '%'
        //         if((this.energy + (inactiveRefillCount)*1) > 200){
        //             this.energy = 200
        //             document.querySelector('.fullEnergyBar').style.width = this.energy/2 + '%'
        //         }else{
        //             document.querySelector('.fullEnergyBar').style.width = (this.energy + (inactiveRefillCount/2)) + '%'
        //             this.energy = this.energy + (inactiveRefillCount)*1
        //         }
        //         if(res.data.inactiveRefillCount > 0){
        //             this.workTimeBoolian = true
        //         }
        //         this.sendIdInfo()
        //      }).catch((err) => {
        //         console.log(err)
        //      })
        //  },
        //  refillAfterInactiveSection(){
        //     if(this.energy < 200){
        //         let date = new Date()
        //         this.lastFillTime = date.getMinutes()
        //         this.lastFillInfo = date.getHours()
        //         this.lastFiilDay = date.getDate()
        //         console.log(date)
        //         this.checkRefillSequence()
        //     }
        //  },
         autoRefill(){
            // const path ='http://94.43.110.179:80/refill_auto'
             const path = 'http://127.0.0.1:80/refill_auto';
             axios.post(path,{
                id: localStorage.getItem('id'),
             }).then((res) => {
                console.log(res)
                if(res.data.lastAutoFill == null){
                    if(this.energy < 200){
                        this.energy = this.energy + (5+this.regionHealthIndex)
                        if(this.energy > 200){
                            this.energy = 200
                        }
                        let date = new Date()
                        this.autoFillTime = new Date()
                        document.querySelector('.fullEnergyBar').style.width = (this.energy/2) + '%'
                        this.sendAutoRefillInfo()
                    }
                }else if(((new Date() - new Date(res.data.lastAutoFill))/60000) >= 5){
                    if(this.energy < 200){
                        this.energy = this.energy + (Math.round(((new Date() - new Date(res.data.lastAutoFill))/60000))+this.regionHealthIndex)
                        if(this.energy > 200){
                            this.energy = 200
                        }
                        let date = new Date()
                        console.log('ahbnhebfhbsdhjbfhajnbdhjasj' + Math.round(((new Date() - new Date(res.data.lastAutoFill))/60000)))
                        this.autoFillTime = new Date()
                        console.log(this.energy/2 + 'asdasdasdasdasd')
                        document.querySelector('.fullEnergyBar').style.width = (this.energy/2) + '%'
                        this.sendAutoRefillInfo()
                    }
                }
             }).catch((err) => {
                console.log(err)
             })
         },
         sendAutoRefillInfo(){
            // const path ='http://94.43.110.179:80/send_refill_auto'
            const path ='http://127.0.0.1:80/send_refill_auto'
            axios.post(path,{
                id: localStorage.getItem('id'),
                energy: this.energy,
                time: this.autoFillTime
            }).then((res) => {
                console.log(res)
            }).catch((err) => {
                console.log(err)
            })
         },      
         createFactory(){
            const path = 'http://127.0.0.1:80/create_factory'
            // const path ='http://94.43.110.179:80/create_factory'
             axios.post(path,{
                id: localStorage.getItem('id'),
             }).then((res) => {
                console.log(res)
             }).catch((err) => {
                console.log(err)
             })
         },
         getFactory(){
            const path = 'http://127.0.0.1:80/get_regional_factory'
            // const path = 'http://94.43.110.179:80/get_regional_factory'
             axios.post(path,{
                region: this.currentRegion,
             }).then((res) => {
                this.factoryInfo = res.data
                console.log(this.factoryInfo)
                this.factoryLevel = res.data.level
                this.factoryExp = res.data.experience
                console.log(this.factoryExp)
                this.currentFactory = this.factoryInfo.find(item => item.id == this.currentFactoryId)
                console.log(this.currentFactory)
                // this.ownerExperience = this.currentFactory.owner.working_experience
                this.ownerStat = this.currentFactory.owner
                document.querySelector('.factoryIcon').style.backgroundImage = `url(${require('@/assets/factoryIcon/'+this.currentFactory.factory_icon)})`
                document.querySelector('.firstFactoryOwnerIcon').style.backgroundImage = `url(${require('@/assets/factoryIcon/'+this.factoryInfo[0].factory_icon)})`
                document.querySelector('.secondFactoryOwnerIcon').style.backgroundImage = `url(${require('@/assets/factoryIcon/'+this.factoryInfo[1].factory_icon)})`
                document.querySelector('.thirdFactoryOwnerIcon').style.backgroundImage = `url(${require('@/assets/factoryIcon/'+this.factoryInfo[2].factory_icon)})`
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
            // const path = 'http://94.43.110.179:80/get_region_info'
            const path = 'http://127.0.0.1:80/get_region_info'
            axios.post(path,{
                id: this.currentRegion
            }).then((res) => {
                console.log(this.currentRegion)
                console.log(res.data)
                this.regionHealth = res.data.medicinIndex
            }).catch((err) => {
                console.log(err)
            })
         },
         autoRefillTest(){

         },

    },
    mounted(){
        this.getLastFillDate()
        this.sendIdInfo()
        // this.refillAfterInactiveSection()
        this.getAutoWorkBool()
        // this.autoRefill()
        // this.getFactory()
        setTimeout(() => {
            this.getRegion()
            this.getFactory()
            // this.checkInactiveAutoWorkCount()
        },650)
        setInterval(() => {
            // this.refillEnergySequence()
            // this.autoRefill()
            this.sendIdInfo()
            // this.refillEnergy()
            // console.log('t')
        }, 300000);
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
</style>