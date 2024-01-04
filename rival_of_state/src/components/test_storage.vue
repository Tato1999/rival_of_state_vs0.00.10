<template>
    <loading-overlay v-if="loading" :can-cancel='false' :color="'#000'" :background="'black'">
        <div class="loading-spinner"></div>
    </loading-overlay>
    <div class="mainDiv" v-if="dataLoaded" style="background-color: #0E0000; width:100%; height: 1166px; position: absolute; display: grid; top: 0; left: 0; overflow-y: auto">
        <AppHeader/>
        <h1>Storage</h1>
        <div class="storageOwerflow">
            <div @click="this.closeOPenMenu" class="resourceMainDiv goldClass">
                <div class="userResAmountDiv">
                    <div class="resourceName">Gold:</div>
                    <div class="resourceAmount">{{this.gold}} G</div>
                </div>
                <div class="buyResourceDiv visibilityClass">
                    <div class="BuyMainResDiv">
                        <div class="resourceName gold" style="line-height: 8.75vw !important;">{{this.exchangeMoney}} $</div>
                        <div class="resourceAmount" style="line-height: 8.75vw !important;">1/10</div>
                    </div>
                    <input class="buyDivInput goldInput" type="text" placeholder="How Many" v-model="changeValueOfChangableMoney">
                    <div class="buyButton" @click="this.sendInBaseGoldConvertation()">Sell</div>
                    <div class="ownerInfoDiv">Owner:<br>abshfbahsfbashbd</div>
                </div>
                <div class="sellResourceDiv visibilityClass">
                    <input class="sellDivInputAmount" type="text" placeholder="Amount">
                    <input class="sellDivInputPrice" type="text" placeholder="Price">
                    <div class="sellButton">Sell</div>
                </div>
            </div>
            <div @click="this.closeOPenMenu" class="resourceMainDiv oilClass">
                <div class="userResAmountDiv">
                    <div class="resourceName">Oil:</div>
                    <div class="resourceAmount">{{this.oil}} G</div>
                </div>
                <div class="buyResourceDiv visibilityClass">
                    <div class="BuyMainResDiv">
                        <div class="resourceName" style="line-height: 8.75vw !important;">{{this.oilAmount}}</div>
                        <div class="resourceAmount" style="line-height: 8.75vw !important;">1/{{this.oilPrice}}</div>
                    </div>
                    <input class="buyDivInput" id="buyOilAmount" type="text" placeholder="How Many">
                    <div class="buyButton" @click="this.buyOil()">Buy</div>
                    <div class="ownerInfoDiv">Owner:<br>{{this.oilOwnerName}}</div>
                </div>
                <div class="sellResourceDiv visibilityClass">
                    <input class="sellDivInputAmount" id="sellOilAmount" type="text" placeholder="Amount">
                    <input class="sellDivInputPrice" id="sellOilPrice" type="text" placeholder="Price">
                    <div class="sellButton" @click="this.addOilMarket()">Sell</div>
                </div>
            </div>
            <div @click="this.closeOPenMenu" class="resourceMainDiv coalClass">
                <div class="userResAmountDiv">
                    <div class="resourceName">Coal:</div>
                    <div class="resourceAmount">{{this.coal}} G</div>
                </div>
                <div class="buyResourceDiv visibilityClass">
                    <div class="BuyMainResDiv">
                        <div class="resourceName" style="line-height: 8.75vw !important;">{{this.coalAmount}}</div>
                        <div class="resourceAmount" style="line-height: 8.75vw !important;">1/{{this.coalPrice}}</div>
                    </div>
                    <input class="buyDivInput" id="buyCoalAmount" type="text" placeholder="How Many">
                    <div class="buyButton" @click="this.buyCoal()">Buy</div>
                    <div class="ownerInfoDiv">Owner:<br>{{this.coalOwnerName}}</div>
                </div>
                <div class="sellResourceDiv visibilityClass">
                    <input class="sellDivInputAmount" id="sellCoalAmount" type="text" placeholder="Amount">
                    <input class="sellDivInputPrice" id="sellCoalPrice" type="text" placeholder="Price">
                    <div class="sellButton" @click="this.addCoalMarket()">Sell</div>
                </div>
            </div>
            <div @click="this.closeOPenMenu" class="resourceMainDiv ironClass">
                <div class="userResAmountDiv">
                    <div class="resourceName">iron:</div>
                    <div class="resourceAmount">{{this.iron}} G</div>
                </div>
                <div class="buyResourceDiv visibilityClass">
                    <div class="BuyMainResDiv">
                        <div class="resourceName" style="line-height: 8.75vw !important;">{{this.ironAmount}}</div>
                        <div class="resourceAmount" style="line-height: 8.75vw !important;">1/{{this.ironPrice}}</div>
                    </div>
                    <input class="buyDivInput" id="buyIronAmount" type="text" placeholder="How Many">
                    <div class="buyButton" @click="this.buyIron()">Buy</div>
                    <div class="ownerInfoDiv">Owner:<br>{{this.ironOwnerName}}</div>
                </div>
                <div class="sellResourceDiv visibilityClass">
                    <input class="sellDivInputAmount" id="sellIronAmount" type="text" placeholder="Amount">
                    <input class="sellDivInputPrice" id="sellIronPrice" type="text" placeholder="Price">
                    <div class="sellButton" @click="this.addIronMarket()">Sell</div>
                </div>
            </div>
            <div @click="this.closeOPenMenu" class="resourceMainDiv silverClass">
                <div class="userResAmountDiv">
                    <div class="resourceName">silver:</div>
                    <div class="resourceAmount">{{this.silver}} G</div>
                </div>
                <div class="buyResourceDiv visibilityClass">
                    <div class="BuyMainResDiv">
                        <div class="resourceName" style="line-height: 8.75vw !important;">{{this.silverAmount}}</div>
                        <div class="resourceAmount" style="line-height: 8.75vw !important;">1/{{this.silverPrice}}</div>
                    </div>
                    <input class="buyDivInput" id="buySilverAmount" type="text" placeholder="How Many">
                    <div class="buyButton" @click="this.buySilver()">Buy</div>
                    <div class="ownerInfoDiv">Owner:<br>{{this.silverOwnerName}}</div>
                </div>
                <div class="sellResourceDiv visibilityClass">
                    <input class="sellDivInputAmount" id="sellSilverAmount" type="text" placeholder="Amount">
                    <input class="sellDivInputPrice" id="sellSilverPrice" type="text" placeholder="Price">
                    <div class="sellButton" @click="this.addSilverMarket()">Sell</div>
                </div>
            </div>
            <div @click="this.closeOPenMenu" class="resourceMainDiv oxygenClass">
                <div class="userResAmountDiv">
                    <div class="resourceName">oxygen:</div>
                    <div class="resourceAmount">{{this.oxygen}} G</div>
                </div>
                <div class="buyResourceDiv visibilityClass">
                    <div class="BuyMainResDiv">
                        <div class="resourceName" style="line-height: 8.75vw !important;">{{this.oxygenAmount}}</div>
                        <div class="resourceAmount" style="line-height: 8.75vw !important;">1/{{this.oxygenPrice}}</div>
                    </div>
                    <input class="buyDivInput" id="buyOxygenAmount" type="text" placeholder="How Many">
                    <div class="buyButton" @click="this.buyOxygen()">Buy</div>
                    <div class="ownerInfoDiv">Owner:<br>{{this.oxygenOwnerName}}</div>
                </div>
                <div class="sellResourceDiv visibilityClass">
                    <input class="sellDivInputAmount" id="sellOxygenAmount" type="text" placeholder="Amount">
                    <input class="sellDivInputPrice" id="sellOxygenPrice" type="text" placeholder="Price">
                    <div class="sellButton" @click="this.addOxygenMarket()">Sell</div>
                </div>
            </div>
            <div @click="this.closeOPenMenu" class="resourceMainDiv taiger1Class largeDivClass">
                <div class="userResAmountDiv">
                    <div class="resourceName">Taiger 1:</div>
                    <div class="resourceAmount">{{this.taiger_1}} G</div>
                </div>
                <div class="buyResourceDiv visibilityClass">
                    <div class="BuyMainResDiv">
                        <div class="resourceName" style="line-height: 8.75vw !important;">{{this.taiger_1Amount}}</div>
                        <div class="resourceAmount" style="line-height: 8.75vw !important;">1/{{this.taiger_1Price}}</div>
                    </div>
                    <input class="buyDivInput" id="buyTaiger1Amount" type="text" placeholder="How Many">
                    <div class="buyButton" @click="this.buyTaiger1">Buy</div>
                    <div class="ownerInfoDiv">Owner:<br>{{this.taiger_1OwnerName}}</div>
                </div>
                <div class="sellResourceDiv visibilityClass">
                    <input class="sellDivInputAmount" id="sellTaiger1Amount" type="terxt" placeholder="Amount">
                    <input class="sellDivInputPrice" id="sellTaiger1Price" type="text" placeholder="Price">
                    <div class="sellButton" @click="this.addTaiger1Market()">Sell</div>
                </div>
                <div class="craftDiv visibilityClass">
                    <input class="craftDivInput taiger1Input" type="text" placeholder="How Many" v-model="changeCraftPrice">
                    <div class="craftButton" @click="this.craftTiger1()">Craft</div>
                    <div class="usedResAmount taiger_1_resource">money:{{this.taiger1Craft[2]*this.amount}}<br><br>iron:{{this.taiger1Craft[0]*this.amount}},<br><br>oil:{{this.taiger1Craft[1]*this.amount}}</div>
                </div>
            </div>
            <div @click="this.closeOPenMenu" class="resourceMainDiv taiger2Class largeDivClass">
                <div class="userResAmountDiv">
                    <div class="resourceName">Taiger 2:</div>
                    <div class="resourceAmount">{{this.taiger_2}} G</div>
                </div>
                <div class="buyResourceDiv visibilityClass">
                    <div class="BuyMainResDiv">
                        <div class="resourceName" style="line-height: 8.75vw !important;">{{this.taiger_2Amount}}</div>
                        <div class="resourceAmount" style="line-height: 8.75vw !important;">1/{{this.taiger_2Price}}</div>
                    </div>
                    <input class="buyDivInput" id="buyTaiger2Amount" type="text" placeholder="How Many">
                    <div class="buyButton" @click="this.buyTaiger2()">Buy</div>
                    <div class="ownerInfoDiv">Owner:<br>{{this.taiger_2OwnerName}}</div>
                </div>
                <div class="sellResourceDiv visibilityClass">
                    <input class="sellDivInputAmount" id="sellTaiger2Amount" type="text" placeholder="Amount">
                    <input class="sellDivInputPrice" id="sellTaiger2Price" type="text" placeholder="Price">
                    <div class="sellButton" @click="this.addTaiger2Market">Sell</div>
                </div>
                <div class="craftDiv visibilityClass">
                    <input class="craftDivInput taiger2Input" type="text" placeholder="How Many" v-model="changeCraftPrice">
                    <div class="craftButton" @click="this.craftTiger2()">Craft</div>
                    <div class="usedResAmount">money:{{this.taiger2Craft[2]*this.amountT2}}<br><br>iron:{{this.taiger2Craft[0]*this.amountT2}},<br><br>oil:{{this.taiger2Craft[1]*this.amountT2}}</div>
                </div>
            </div>
            <div @click="this.closeOPenMenu" class="resourceMainDiv t-90Class largeDivClass">
                <div class="userResAmountDiv">
                    <div class="resourceName">T-90:</div>
                    <div class="resourceAmount">{{this.t_90}} G</div>
                </div>
                <div class="buyResourceDiv visibilityClass">
                    <div class="BuyMainResDiv">
                        <div class="resourceName" style="line-height: 8.75vw !important;">{{this.t_90Amount}}</div>
                        <div class="resourceAmount" style="line-height: 8.75vw !important;">1/{{this.t_90Price}}</div>
                    </div>
                    <input class="buyDivInput" id="buyT90Amount" type="text" placeholder="How Many">
                    <div class="buyButton" @click="this.buyT90()">Buy</div>
                    <div class="ownerInfoDiv">Owner:<br>{{this.t_90OwnerName}}</div>
                </div>
                <div class="sellResourceDiv visibilityClass">
                    <input class="sellDivInputAmount" id="sellT90Amount" type="text" placeholder="Amount">
                    <input class="sellDivInputPrice" id="selT90Price" type="text" placeholder="Price">
                    <div class="sellButton" @click="this.addT90Market()">Sell</div>
                </div>
                <div class="craftDiv visibilityClass">
                    <input class="craftDivInput t90Input" type="text" placeholder="How Many" v-model="changeCraftPrice">
                    <div class="craftButton" @click="this.craftT90()">Craft</div>
                    <div class="usedResAmount">money:{{this.t90Craft[2]*this.amountT90}}<br><br>iron:{{this.t90Craft[0]*this.amountT90}},<br><br>coal:{{this.t90Craft[1]*this.amountT90}}</div>
                </div>
            </div>
            <div @click="this.closeOPenMenu" class="resourceMainDiv himarsClass largeDivClass">
                <div class="userResAmountDiv">
                    <div class="resourceName">Himars:</div>
                    <div class="resourceAmount">{{this.haimars}} G</div>
                </div>
                <div class="buyResourceDiv visibilityClass">
                    <div class="BuyMainResDiv">
                        <div class="resourceName" style="line-height: 8.75vw !important;">{{this.haimarsAmount}}</div>
                        <div class="resourceAmount" style="line-height: 8.75vw !important;">1000/{{this.haimarsPrice}}</div>
                    </div>
                    <input class="buyDivInput" id="buyHaimarsAmount" type="text" placeholder="How Many">
                    <div class="buyButton" @click="this.buyHaimars">Buy</div>
                    <div class="ownerInfoDiv">Owner:<br>{{this.haimarsOwnerName}}</div>
                </div>
                <div class="sellResourceDiv visibilityClass">
                    <input class="sellDivInputAmount" id="sellHaimarsAmount" type="text" placeholder="Amount">
                    <input class="sellDivInputPrice" id="sellHaimarsPrice" type="text" placeholder="Price">
                    <div class="sellButton" @click="this.addHaimarsMarket()">Sell</div>
                </div>
                <div class="craftDiv visibilityClass">
                    <input class="craftDivInput haimarsInput" type="text" placeholder="How Many" v-model="changeCraftPrice">
                    <div class="craftButton" @click="this.craftHaimars()">Craft</div>
                    <div class="usedResAmount">money:{{this.haimarsCraft[0]*this.amountHaimars}},<br><br>Wolfram:{{this.haimarsCraft[1]*this.amountHaimars}}</div>
                </div>
            </div>
            <div @click="this.closeOPenMenu" class="resourceMainDiv bayraktarClass largeDivClass">
                <div class="userResAmountDiv">
                    <div class="resourceName">Bayraktar:</div>
                    <div class="resourceAmount">{{this.drone}} G</div>
                </div>
                <div class="buyResourceDiv visibilityClass">
                    <div class="BuyMainResDiv">
                        <div class="resourceName" style="line-height: 8.75vw !important;">{{this.droneAmount}}</div>
                        <div class="resourceAmount" style="line-height: 8.75vw !important;">1000/{{this.dronePrice}}</div>
                    </div>
                    <input class="buyDivInput" id="nuyDroneAmount" type="text" placeholder="How Many">
                    <div class="buyButton" @click="this.buyDrone()">Buy</div>
                    <div class="ownerInfoDiv">Owner:<br>{{this.droneOwnerName}}</div>
                </div>
                <div class="sellResourceDiv visibilityClass">
                    <input class="sellDivInputAmount" id="sellDroneAmount" type="text" placeholder="Amount">
                    <input class="sellDivInputPrice" id="sellDronePrice" type="text" placeholder="Price">
                    <div class="sellButton" @click="this.addDroneMarket()">Sell</div>
                </div>
                <div class="craftDiv visibilityClass">
                    <input class="craftDivInput droneInput" type="text" placeholder="How Many" v-model="changeCraftPrice">
                    <div class="craftButton" @click="this.craftDrone()">Craft</div>
                    <div class="usedResAmount">gold:{{this.bayraktarCraft[0]*this.amountBayraktar}},<br><br>Wolfram:{{this.bayraktarCraft[1]*this.amountBayraktar}}</div>
                </div>
            </div>
            <div @click="this.closeOPenMenu" class="resourceMainDiv wolframClass largeDivClass">
                <div class="userResAmountDiv">
                    <div class="resourceName">Wolfram:</div>
                    <div class="resourceAmount">{{this.wolfram}} G</div>
                </div>
                <div class="buyResourceDiv visibilityClass">
                    <div class="BuyMainResDiv">
                        <div class="resourceName" style="line-height: 8.75vw !important;">{{this.wolframAmount}}</div>
                        <div class="resourceAmount" style="line-height: 8.75vw !important;">1/{{this.wolframPrice}}</div>
                    </div>
                    <input class="buyDivInput" id="buyWolframAmount" type="text" placeholder="How Many">
                    <div class="buyButton" @click="this.buyWolfram()">Buy</div>
                    <div class="ownerInfoDiv">Owner:<br>{{this.wolframOwnerName}}</div>
                </div>
                <div class="sellResourceDiv visibilityClass">
                    <input class="sellDivInputAmount" id="sellWolframAmount" type="text" placeholder="Amount">
                    <input class="sellDivInputPrice" id="sellWolframPrice" type="text" placeholder="Price">
                    <div class="sellButton" @click="this.addWolframMarket()">Sell</div>
                </div>
                <div class="craftDiv visibilityClass">
                    <input class="craftDivInput wolframInput" type="text" placeholder="How Many" v-model="changeCraftPrice">
                    <div class="craftButton" @click="this.craftWolfraw()">Craft</div>
                    <div class="usedResAmount">gold:{{this.wolframCraft[0]*this.amountWolfram}}<br><br>iron:{{this.wolframCraft[1]*this.amountWolfram}},<br><br>coal:{{this.wolframCraft[2]*this.amountWolfram}}<br>
                    <br>Oil: {{this.wolframCraft[3]*this.amountWolfram}}<br><br>Silver: {{this.wolframCraft[4]*this.amountWolfram}}</div>
                </div>
            </div>
        </div>
        <AppFooterMenu/>        
    </div>
  
</template>

<script>
import AppHeader from './headers/AppHeader.vue'
import AppFooterMenu from './headers/footerMenu.vue'
import LoadingOverlay from 'vue-loading-overlay';
import 'vue-loading-overlay/dist/css/index.css';
  
import axios from 'axios'

export default {
    components: {
        AppHeader,
        AppFooterMenu,
    },
    data(){
        return{
            changeValueOfChangableMoney:null,
            loading: true,
            dataLoaded: false,
            changeCraftPrice:null,
            data:'',
            buySellVisibility: false,
            parent: "",
            gold: 0,
            oil:0,
            coal:0,
            silver:0,
            iron:0,
            t_90:0,
            wolfram:0,
            haimars:0,
            drone:0,
            taiger_1:0,
            taiger_2:0,
            oxygen:0,
            money: 0,
            exchangeMoney: 0,
            taiger1Craft: [],
            taiger2Craft: [],
            t90Craft: [],
            wolframCraft: [],
            haimarsCraft: [],
            bayraktarCraft: [],
            craftItemAmount: 0,
            tiger1CraftItems:{},
            oilAmount: 0,
            oilPrice: 0,
            oilOwner: 0,
            oilOwnerName: 0,
            coalAmount: 0,
            coalPrice: 0,
            coalOwner: 0,
            coalOwnerName: 0,
            ironAmount: 0,
            ironPrice: 0,
            ironOwner: 0,
            ironOwnerName: 0,
            silverAmount: 0,
            silverPrice: 0,
            silverOwner: 0,
            silverOwnerName: 0,
            oxygenAmount: 0,
            oxygenPrice: 0,
            oxygenOwner: 0,
            oxygenOwnerName: 0,
            taiger_1Amount: 0,
            taiger_1Price: 0,
            taiger_1Owner: 0,
            taiger_1OwnerName: 0,
            taiger_2Amount: 0,
            taiger_2Price: 0,
            taiger_2Owner: 0,
            taiger_2OwnerName: 0,
            t_90Amount: 0,
            t_90Price: 0,
            t_90Owner: 0,
            t_90OwnerName: 0,
            haimarsAmount: 0,
            haimarsPrice: 0,
            haimarsOwner: 0,
            haimarsOwnerName: 0,
            droneAmount: 0,
            dronePrice: 0,
            droneOwner: 0,
            droneOwnerName: 0,
            wolframAmount: 0,
            wolframPrice: 0,
            wolframOwner: 0,
            wolframOwnerName: 0,

            amount:1,
            amountT2:1,
            amountT90:1,
            amountWolfram:1,
            amountHaimars:1,
            amountBayraktar:1,
            // ip: 'http://94.43.110.179:80',
            // ip: 'http://127.0.0.1:80',
            ip: 'http://tato1999.pythonanywhere.com/'
        }
    },
    methods:{
        closeOPenMenu(event){
            if(!this.buySellVisibility){
                this.buySellVisibility = true;
                if(event.target.classList[0] != 'resourceMainDiv'){
                    this.parent = event.target.parentElement
                    while(this.parent.classList[0] != 'resourceMainDiv'){
                        this.parent = this.parent.parentElement
                     }
                    if(this.parent.classList[0] == 'resourceMainDiv'){
                        this.parent.style.position = 'relative'
                        this.parent.children[1].style.display = "flex"
                        this.parent.children[2].style.display = "flex"
            
                        if(this.parent.children[3] != undefined){
                            this.parent.children[3].style.display = "flex"
                            this.parent.style.height = '87.75vw'
                        }
                        else{
                            this.parent.style.height = '63.75vw'
                        }
                    }
                }else{
                    console.log("test")
                    event.target.style.height = "63.5vw"
                    event.target.style.position = 'relative'
        
                    this.parent.children[1].style.display = "flex"
                    this.parent.children[2].style.display = "flex"
                    if(this.parent.children[3] != undefined){
                        this.parent.children[3].style.display = "flex"
                        this.parent.style.height = '87.75vw'
                    }
                    else{
                        this.parent.style.height = '63.5vw'
                    }
                  }
                }
            else{
                if(event.target.classList[0] != 'resourceMainDiv'){
                    this.parent = event.target.parentElement
                    while(this.parent.classList[0] != 'resourceMainDiv'){
                        this.parent = this.parent.parentElement
                     }
                     console.log(event.target.parentElement.classList[0])
                    if(this.parent.classList[0] == 'resourceMainDiv'){
                        if(event.target.parentElement.classList[0] != 'buyResourceDiv' 
                        && event.target.parentElement.classList[0] != 'sellResourceDiv' 
                        && event.target.parentElement.classList[0] != 'craftDiv'){
                            this.buySellVisibility = false;
                            this.parent.style.height = '18vw'
                            this.parent.style.position = 'relative'
                            this.parent.children[1].style.display = "none"
                            this.parent.children[2].style.display = "none"
                            if(this.parent.children[3] != undefined){
                                this.parent.children[3].style.display = "none"
                            }
                        }else{
                            console.log('Upps Wrong Click')
                        }
                    }
                }else{
                    console.log("test")
                    if(event.target.parentElement.classList[0] != 'buyResourceDiv' 
                        && event.target.parentElement.classList[0] != 'sellResourceDiv' 
                        && event.target.parentElement.classList[0] != 'craftDiv'){
                            this.buySellVisibility = false;
                            event.target.style.height = "18vw"
                            event.target.style.position = 'relative'
                            this.parent.children[1].style.display = "none"
                            this.parent.children[2].style.display = "none"
                            if(this.parent.children[3] != undefined){
                                this.parent.children[3].style.display = "none"
                            }
                        }else{
                            console.log('Upps Wrong Click')
                        }
            
                }
            }
        },
         sendIdInfo(){
             const path = this.ip+'/send_storage_info';
            //  const path = 'http://94.43.110.179/send_storage_info'
            // const path = 'http://127.0.0.1:80/send_storage_info'

             axios.post(path,{
                id: localStorage.getItem('id')
             })
             .then((res) => {
                 console.log(res.data)
                 this.gold = res.data.gold
                 this.oil = res.data.oil
                 this.silver = res.data.silver
                 this.iron = res.data.iron
                 this.coal = res.data.coal
                 this.taiger_1 = res.data.tiger_1
                 this.taiger_2 = res.data.tiger_2
                 this.t_90 = res.data.t_90
                 this.drone = res.data.drone
                 this.haimars = res.data.haimars
                 this.wolfram = res.data.wolfram
                 this.money = res.data.money
        
                })
             .catch((err) => {
                 console.error(err)
             })
         },
         sendInBaseGoldConvertation(){
            
            const path = this.ip+'/send_storage_info_base'
            // const path = 'http://94.43.110.179:80//send_storage_info_base'

             axios.post(path,{
                id: localStorage.getItem('id'),
                money: this.exchangeMoney,
                gold: (this.gold - (this.exchangeMoney/10))
             })
             .then((res) => {
                 console.log(this.gold-(this.exchangeMoney/10))
                 this.gold = res.data.gold
                 this.money = res.data.money
        
                })
             .catch((err) => {
                 console.error(err)
             })
         },
         getWeaponCraft(){
            const path = this.ip+'/get_weapon_craft'
            // const path = 'http://94.43.110.179:80/get_weapon_craft'

             axios.post(path,{
                id: 1
             })
             .then((res) => {
                console.log(res.data)
                 this.gold = res.data.gold
                 this.money = res.data.money
                 this.taiger1Craft =[res.data.tiger_1.iron,res.data.tiger_1.oil,res.data.tiger_1.money,]
                 this.taiger2Craft = [res.data.tiger_2.iron,res.data.tiger_2.oil,res.data.tiger_2.money,]
                 this.t90Craft = [res.data.t_90.iron,res.data.t_90.coal,res.data.t_90.money,]
                 this.wolframCraft = [res.data.wolfram.gold,res.data.wolfram.iron,res.data.wolfram.oil,res.data.wolfram.coal,res.data.wolfram.silver]
                 this.haimarsCraft = [res.data.haimars.money,res.data.haimars.wolfram]
                 this.bayraktarCraft = [res.data.drone.money,res.data.drone.wolfram]

                 console.log(res.data.wolfram)
                })
             .catch((err) => {
                 console.error(err)
             })
         },
         craftTiger1(){
            const path = this.ip+'/craft_tiger_1'
            axios.post(path,{
                id:localStorage.getItem('id'),
                amount: this.amount
            }).then((res) => {
                console.log(res.data)
                if(res.data.tiger_1 != 0){
                    this.taiger_1 = res.data.tiger_1
                    this.oil = res.data.oil
                    this.iron = res.data.iron
                }else{
                    document.querySelector('.taiger_1_resource').style.background = "red"
                }
            }).catch((err) => {
                console.log(err)
            })
         },
         craftTiger2(){
            const path = this.ip+'/craft_tiger_2'
            axios.post(path,{
                id:localStorage.getItem('id'),
                amount: this.amountT2
            }).then((res) => {
                console.log(res.data)
                if(res.data.tiger_2 != 0){
                    this.taiger_2 = res.data.tiger_2
                    this.oil = res.data.oil
                    this.iron = res.data.iron
                }else{
                    document.querySelector('.taiger_1_resource').style.background = "red"
                }
            }).catch((err) => {
                console.log(err)
            })
         },
         craftT90(){
            const path = this.ip+'/craft_t_90'
            axios.post(path,{
                id:localStorage.getItem('id'),
                amount: this.amountT90
            }).then((res) => {
                console.log(res.data)
                if(res.data.t_90 != 0){
                    this.t_90 = res.data.t_90
                    this.coal = res.data.coal
                    this.iron = res.data.iron
                }else{
                    document.querySelector('.taiger_1_resource').style.background = "red"
                }
            }).catch((err) => {
                console.log(err)
            })
         },
         craftWolfraw(){
            const path = this.ip+'/craft_wolfram'
            axios.post(path,{
                id:localStorage.getItem('id'),
                amount: this.amountWolfram
            }).then((res) => {
                console.log(res.data)
                if(res.data.wolfram != 0){
                    this.wolfram = res.data.wolfram
                    this.coal = res.data.coal
                    this.iron = res.data.iron
                    this.silver = res.data.silver
                    this.oil = res.data.oil
                    this.gold = res.data.gold
                }else{
                    document.querySelector('.taiger_1_resource').style.background = "red"
                }
            }).catch((err) => {
                console.log(err)
            })
         },
         craftHaimars(){
            const path = this.ip+'/craft_haimars'
            axios.post(path,{
                id:localStorage.getItem('id'),
                amount: this.amountHaimars
            }).then((res) => {
                console.log(res.data)
                if(res.data.wolfram != 0){
                    this.wolfram = res.data.wolfram
                    this.haimars = res.data.haimars
                }else{
                    document.querySelector('.taiger_1_resource').style.background = "red"
                }
            }).catch((err) => {
                console.log(err)
            })
         },
         craftDrone(){
            const path = this.ip+'/craft_drone'
            axios.post(path,{
                id:localStorage.getItem('id'),
                amount: this.amountBayraktar
            }).then((res) => {
                console.log(res.data)
                if(res.data.wolfram != 0){
                    this.wolfram = res.data.wolfram
                    this.drone = res.data.drone
                }else{
                    document.querySelector('.taiger_1_resource').style.background = "red"
                }
            }).catch((err) => {
                console.log(err)
            })
         },
         addOilMarket(){
            const path = this.ip+'/add_market_oil_json'
            axios.post(path,{
                id: localStorage.getItem('id'),
                'oil': document.getElementById('sellOilAmount').value*1,
                'price': document.getElementById('sellOilPrice').value*1
            })
            .then((res) => {
                console.log(res)
            })
            .catch((err) => {
                console.log(err)
            })
         },
         addCoalMarket(){
            const path = this.ip+'/add_market_coal_json'
            axios.post(path,{
                id: localStorage.getItem('id'),
                'coal': document.getElementById('sellCoalAmount').value*1,
                'price': document.getElementById('sellCoalPrice').value*1
            })
            .then((res) => {
                console.log(res)
            })
            .catch((err) => {
                console.log(err)
            })
         },
         addIronMarket(){
            const path = this.ip+'/add_market_iron_json'
            axios.post(path,{
                id: localStorage.getItem('id'),
                'iron': document.getElementById('sellIronAmount').value*1,
                'price': document.getElementById('sellIronPrice').value*1
            })
            .then((res) => {
                console.log(res)
            })
            .catch((err) => {
                console.log(err)
            })
         },
         addSilverMarket(){
            const path = this.ip+'/add_market_silver_json'
            axios.post(path,{
                id: localStorage.getItem('id'),
                'silver': document.getElementById('sellSilverAmount').value*1,
                'price': document.getElementById('sellSilverPrice').value*1
            })
            .then((res) => {
                console.log(res)
            })
            .catch((err) => {
                console.log(err)
            })
         },
         addOxygenMarket(){
            const path = this.ip+'/add_market_oxygen_json'
            axios.post(path,{
                id: localStorage.getItem('id'),
                'oxygen': document.getElementById('sellOxygenAmount').value*1,
                'price': document.getElementById('sellOXygenPrice').value*1
            })
            .then((res) => {
                console.log(res)
            })
            .catch((err) => {
                console.log(err)
            })
         },
         addTaiger1Market(){
            const path = this.ip+'/add_market_taiger_1_json'
            axios.post(path,{
                id: localStorage.getItem('id'),
                'taiger_1': document.getElementById('sellTaiger1Amount').value*1,
                'price': document.getElementById('sellTaiger1Price').value*1
            })
            .then((res) => {
                console.log(res)
            })
            .catch((err) => {
                console.log(err)
            })
         },
         addTaiger2Market(){
            const path = this.ip+'/add_market_taiger_2_json'
            axios.post(path,{
                id: localStorage.getItem('id'),
                'taiger_2': document.getElementById('sellTaiger2Amount').value*1,
                'price': document.getElementById('sellTAiger2Price').value*1
            })
            .then((res) => {
                console.log(res)
            })
            .catch((err) => {
                console.log(err)
            })
         },
         addT90Market(){
            const path = this.ip+'/add_market_t_90_json'
            axios.post(path,{
                id: localStorage.getItem('id'),
                't_90': document.getElementById('sellT90Amount').value*1,
                'price': document.getElementById('sellT90Price').value*1
            })
            .then((res) => {
                console.log(res)
            })
            .catch((err) => {
                console.log(err)
            })
         },
         addHaimarsMarket(){
            const path = this.ip+'/add_market_haimars_json'
            axios.post(path,{
                id: localStorage.getItem('id'),
                'haimars': document.getElementById('sellHaimarsAmount').value*1,
                'price': document.getElementById('sellHaimarsPrice').value*1
            })
            .then((res) => {
                console.log(res)
            })
            .catch((err) => {
                console.log(err)
            })
         },
         addDroneMarket(){
            const path = this.ip+'/add_market_drone_json'
            axios.post(path,{
                id: localStorage.getItem('id'),
                'drone': document.getElementById('sellDroneAmount').value*1,
                'price': document.getElementById('sellDronePrice').value*1
            })
            .then((res) => {
                console.log(res)
            })
            .catch((err) => {
                console.log(err)
            })
         },
         addWolframMarket(){
            const path = this.ip+'/add_market_wolfram_json'
            axios.post(path,{
                id: localStorage.getItem('id'),
                'wolfram': document.getElementById('sellWolframAmount').value*1,
                'price': document.getElementById('sellWolframPrice').value*1
            })
            .then((res) => {
                console.log(res)
            })
            .catch((err) => {
                console.log(err)
            })
         },
         fletchMarketData(){
      // Define your API endpoints
            const endpoints = [
                { url: this.ip+'/get_market_oil', data: { id: localStorage.getItem('id') } },
                { url: this.ip+'/get_market_coal', data: { id: localStorage.getItem('id') } },
                { url: this.ip+'/get_market_iron', data: { id: localStorage.getItem('id') } },
                { url: this.ip+'/get_market_silver', data: { id: localStorage.getItem('id') } },
                { url: this.ip+'/get_market_oxygen', data: { id: localStorage.getItem('id') } },
                { url: this.ip+'/get_market_taiger_1', data: { id: localStorage.getItem('id') } },
                { url: this.ip+'/get_market_taiger_2', data: { id: localStorage.getItem('id') } },
                { url: this.ip+'/get_market_t_90', data: { id: localStorage.getItem('id') } },
                { url: this.ip+'/get_market_haimars', data: { id: localStorage.getItem('id') } },
                { url: this.ip+'/get_market_drone', data: { id: localStorage.getItem('id') } },
                { url: this.ip+'/get_market_wolfram', data: { id: localStorage.getItem('id') } },
                // Add more endpoints as needed
            ];

      // Create an array of promises for each axios.post request
      const requests = endpoints.map(endpoint => axios.post(endpoint.url, endpoint.data));

      // Use Promise.all to wait for all requests to complete
      Promise.all(requests)
        .then(res => {
          // Handle responses and update component data as needed
            // console.log(res[1])
            const firstKeyOil = Object.keys(res[0].data)[0];
            const firstValuesOil = res[0].data[firstKeyOil];
            
            if(firstValuesOil != undefined){
                const firstElementOil = firstValuesOil[0];
                this.oilAmount = firstElementOil['oil']['amount']
                this.oilPrice = firstElementOil['oil']['price']
                this.oilOwner = firstElementOil['id']
                this.oilOwnerName = firstElementOil['name']
            }
            const firstKeyCoal = Object.keys(res[1].data)[0];
            const firstValuesCoal = res[1].data[firstKeyCoal];
            
            if(firstValuesCoal !== undefined){
                const firstElementCoal = firstValuesCoal[0];
                this.coalAmount = firstElementCoal['coal']['amount']
                this.coalPrice = firstElementCoal['coal']['price']
                this.coalOwner = firstElementCoal['id']
                this.coalOwnerName = firstElementCoal['name']
            }
            const firstKeyIron = Object.keys(res[2].data)[0];
            const firstValuesIron = res[2].data[firstKeyIron];
            
            if(firstValuesIron !== undefined){
                const firstElementIron = firstValuesIron[0];
                this.ironAmount = firstElementIron['iron']['amount']
                this.ironPrice = firstElementIron['iron']['price']
                this.ironOwner = firstElementIron['id']
                this.ironOwnerName = firstElementIron['name']
            }
            const firstKeySilver = Object.keys(res[3].data)[0];
            const firstValuesSilver = res[3].data[firstKeySilver];
            
            if(firstValuesSilver !== undefined){
                const firstElementSilver = firstValuesSilver[0];
                this.silverAmount = firstElementSilver['silver']['amount']
                this.silverPrice = firstElementSilver['silver']['price']
                this.silverOwner = firstElementSilver['id']
                this.silverOwnerName = firstElementSilver['name']
            }
            const firstKeyOxygen = Object.keys(res[4].data)[0];
            const firstValuesOxygen = res[4].data[firstKeyOxygen];
            
            if(firstValuesOxygen !== undefined){
                const firstElementOxygen = firstValuesOxygen[0];
                this.oxygenAmount = firstElementOxygen['oxygen']['amount']
                this.oxygenPrice = firstElementOxygen['oxygen']['price']
                this.oxygenOwner = firstElementOxygen['id']
                this.oxygenOwnerName = firstElementOxygen['name']
            }

            const firstKeyTaiger1 = Object.keys(res[5].data)[0];
            const firstValuesTaiger1 = res[5].data[firstKeyTaiger1];
            
            if(firstValuesTaiger1 !== undefined){
                const firstElementTaiger1 = firstValuesTaiger1[0];
                this.taiger_1Amount = firstElementTaiger1['taiger_1']['amount']
                this.taiger_1Price = firstElementTaiger1['taiger_1']['price']
                this.Taiger_1Owner = firstElementTaiger1['id']
                this.taiger_1OwnerName = firstElementTaiger1['name']
            }
            const firstKeyTaiger2 = Object.keys(res[6].data)[0];
            const firstValuesTaiger2 = res[6].data[firstKeyTaiger2];
            
            if(firstValuesTaiger2 !== undefined){
                const firstElementTaiger2 = firstValuesTaiger2[0];
                this.taiger_2AmountAmount = firstElementTaiger2['taiger_2']['amount']
                this.taiger_2Price = firstElementTaiger2['taiger_2']['price']
                this.taiger_2Owner = firstElementTaiger2['id']
                this.taiger_2OwnerName = firstElementTaiger2['name']
            }
            const firstKeyT90 = Object.keys(res[7].data)[0];
            const firstValuesT90 = res[7].data[firstKeyT90];
            
            if(firstValuesT90 !== undefined){
                const firstElementT90 = firstValuesT90[0];
                this.t_90AmountAmount = firstElementT90['t_90']['amount']
                this.t_90Price = firstElementT90['t_90']['price']
                this.t_90Owner = firstElementT90['id']
                this.t_90OwnerName = firstElementT90['name']
            }
            const firstKeyHaimars = Object.keys(res[8].data)[0];
            const firstValuesHaimars = res[8].data[firstKeyHaimars];
            
            if(firstValuesHaimars !== undefined){
                const firstElementHaimars = firstValuesHaimars[0];
                this.haimarsAmount = firstElementHaimars['haiamrs']['amount']
                this.haimarsPrice = firstElementHaimars['haiamrs']['price']
                this.haimarsOwner = firstElementHaimars['id']
                this.haimarsOwnerName = firstElementHaimars['name']
            }
            this.loading = false
            this.dataLoaded = true
        })
        .catch(error => {
          // Handle errors
          console.error('Error:', error);

          // Data failed to load, hide loading screen
        //   this.loading = false;
        });
        },
        buyOil(){
            const path = this.ip+'/buy_oil'
            axios.post(path,{
                myId: localStorage.getItem('id'),
                ownerId: this.oilOwner,
                sellerResourceType: 'oil',
                sellerResourceTypeInside: 'oil', 
                buyerResource: 'Oil_Factory',
                amount: document.getElementById('buyOilAmount').value*1
            })
            .then((res) => {
                console.log(res)
            })
            .catch((err) => {
                console.log(err)
            })
        },
        buyCoal(){
            const path = this.ip+'/buy_oil'
            axios.post(path,{
                myId: localStorage.getItem('id'),
                ownerId: this.coalOwner,
                sellerResourceType: 'coal',
                sellerResourceTypeInside: 'coal', 
                buyerResource: 'Coal_Factory',
                amount: document.getElementById('buyCoalAmount').value*1
            })
            .then((res) => {
                console.log(res)
            })
            .catch((err) => {
                console.log(err)
            })
        },
        buyIron(){
            const path = this.ip+'/buy_oil'
            axios.post(path,{
                myId: localStorage.getItem('id'),
                ownerId: this.ironOwner,
                sellerResourceType: 'iron',
                sellerResourceTypeInside: 'iron', 
                buyerResource: 'Iron_Factory',
                amount: document.getElementById('buyIronAmount').value*1
            })
            .then((res) => {
                console.log(res)
            })
            .catch((err) => {
                console.log(err)
            })
        },
        buySilver(){
            const path = this.ip+'/buy_oil'
            axios.post(path,{
                myId: localStorage.getItem('id'),
                ownerId: this.silverOwner,
                sellerResourceType: 'silver',
                sellerResourceTypeInside: 'silver', 
                buyerResource: 'Silver_Factory',
                amount: document.getElementById('buySilverAmount').value*1
            })
            .then((res) => {
                console.log(res)
            })
            .catch((err) => {
                console.log(err)
            })
        },

        buyOxygen(){
            const path = this.ip+'/buy_oil'
            axios.post(path,{
                myId: localStorage.getItem('id'),
                ownerId: this.oxygenOwner,
                sellerResourceType: 'oxygen_market',
                sellerResourceTypeInside: 'oxygen', 
                buyerResource: 'oxygen',
                amount: document.getElementById('buyOxygenAmount').value*1
            })
            .then((res) => {
                console.log(res)
            })
            .catch((err) => {
                console.log(err)
            })
        },
        buyTaiger1(){
            const path = this.ip+'/buy_oil'
            axios.post(path,{
                myId: localStorage.getItem('id'),
                ownerId: this.taiger_1Owner,
                sellerResourceType: 'taiger_1_market',
                sellerResourceTypeInside: 'taiger_1', 
                buyerResource: 'tiger_1',
                amount: document.getElementById('buyTaiger1Amount').value*1
            })
            .then((res) => {
                console.log(res)
            })
            .catch((err) => {
                console.log(err)
            })
        },

        buyTaiger2(){
            const path = this.ip+'/buy_oil'
            axios.post(path,{
                myId: localStorage.getItem('id'),
                ownerId: this.taiger_2Owner,
                sellerResourceType: 'taiger_2_market',
                sellerResourceTypeInside: 'taiger_2', 
                buyerResource: 'tiger_2',
                amount: document.getElementById('buyTaiger2Amount').value*1
            })
            .then((res) => {
                console.log(res)
            })
            .catch((err) => {
                console.log(err)
            })
        },

        buyT90(){
            const path = this.ip+'/buy_oil'
            axios.post(path,{
                myId: localStorage.getItem('id'),
                ownerId: this.t_90Owner,
                sellerResourceType: 't_90_market',
                sellerResourceTypeInside: 't_90', 
                buyerResource: 't_90',
                amount: document.getElementById('buyT90Amount').value*1
            })
            .then((res) => {
                console.log(res)
            })
            .catch((err) => {
                console.log(err)
            })
        },
        buyHaimars(){
            const path = this.ip+'/buy_oil'
            axios.post(path,{
                myId: localStorage.getItem('id'),
                ownerId: this.haimarsOwner,
                sellerResourceType: 'haimars_market',
                sellerResourceTypeInside: 'haimars', 
                buyerResource: 'haimars',
                amount: document.getElementById('buyHaimarsAmount').value*1
            })
            .then((res) => {
                console.log(res)
            })
            .catch((err) => {
                console.log(err)
            })
        },
        buyDrone(){
            const path = this.ip+'/buy_oil'
            axios.post(path,{
                myId: localStorage.getItem('id'),
                ownerId: this.droneOwner,
                sellerResourceType: 'drone_market',
                sellerResourceTypeInside: 'drome', 
                buyerResource: 'drone',
                amount: document.getElementById('buyDroneAmount').value*1
            })
            .then((res) => {
                console.log(res)
            })
            .catch((err) => {
                console.log(err)
            })
        },
        buyWolfram(){
            const path = this.ip+'/buy_oil'
            axios.post(path,{
                myId: localStorage.getItem('id'),
                ownerId: this.wolframOwner,
                sellerResourceType: 'wolfram_market',
                sellerResourceTypeInside: 'wolfram', 
                buyerResource: 'wolfram',
                amount: document.getElementById('buyWolframAmount').value*1
            })
            .then((res) => {
                console.log(res)
            })
            .catch((err) => {
                console.log(err)
            })
        },
    },
    mounted(){
        setTimeout(() => {
            this.sendIdInfo()
        },200)
        this.getWeaponCraft()
        this.fletchMarketData()
        // const path = 'http://192.168.1.2:80/test_storage'
        // axios.post(path,{
        //     id: localStorage.getItem('id')
        // }).then((res) => {
        //     console.log(res.data)
        //     this.data = res.data
        // }).catch((err) => {
        //     console.log(err)
        // })
    },
    watch:{
        changeValueOfChangableMoney(){
            this.exchangeMoney = (document.querySelector('.goldInput').value*1)*10
        },
        changeCraftPrice(){
            console.log('test')
            console.log(document.querySelector('.taiger1Input').value*1)
            this.amount = (document.querySelector('.taiger1Input').value*1)
            this.amountT2 = (document.querySelector('.taiger2Input').value*1)
            this.amountT90 = (document.querySelector('.t90Input').value*1)
            this.amountWolfram = (document.querySelector('.wolframInput').value*1)
            this.amountHaimars = (document.querySelector('.haimarsInput').value*1)
            this.amountBayraktar = (document.querySelector('.droneInput').value*1)
        }
    }
}
</script>

<style>
    h1{
        position: absolute;
        margin: 30vw auto auto 38vw;
        color: #FFFEFE;
        text-align: center;
        font-family: Poppins;
        /* font-size: 20px; */
        font-style: normal;
        font-weight: 700;
        line-height: normal;
    }
    .storageOwerflow{
        width: 100vw;
        height: 110vh;
        overflow-x: auto;
        position: absolute;
        margin: 45vw auto auto auto;

    }
    .resourceMainDiv{
        width: 92.5vw;
        height: 18vw;
        /* height: 63.5vw;  */
        border-radius: 1.25vw;
        background: #7F9693;
        position: relative;
        margin: 0 auto auto calc((100vw - 92.5vw)/2);
    }
    .userResAmountDiv{
        width: 86.25vw;
        height: 10vw;
        border-radius: 1.25vw;
        background: #6F8B87;
        position: absolute;
        margin: 3.75vw auto auto calc((100% - 86.25vw)/2);
        display: flex;
        justify-content: space-between;
    }
    
    .resourceName{
        width: 37.5vw;
        height: 10vw;
        color: #FFFCFC;
        text-align: left;
        font-family: Poppins;
        font-size: 4vw;
        font-style: normal;
        font-weight: 700;
        line-height: 10vw;
        margin-left: 2vw;
    }
    .resourceAmount{
        width: 37.5vw;
        height: 10vw;
        color: #5c5b5b;
        text-align: right;
        font-family: Poppins;
        font-size: 4vw;
        font-style: normal;
        font-weight: 700;
        line-height: 10vw;
        margin-right: 2vw;
    }
    .buyResourceDiv{
        width: 86.25vw;
        height: 21.25vw;
        flex-shrink: 0;
        border-radius: 1.25vw;
        background: #6F8B87;
        position: absolute;
        margin: 16.75vw auto auto calc((100% - 86.25vw)/2);
    }
    .BuyMainResDiv{
        width: 81.75vw;
        height: 8.75vw;
        border-radius: 1.25vw;
        background: #7F9693;
        position: absolute;
        margin: 0.75vw auto auto calc((100% - 81.75vw)/2);
        display: flex;
        justify-content: space-between;
    }
    .buyDivInput{
        width: 140px;
        height: 6.25vw;
        border-radius: 1.25vw;
        flex-shrink: 0;
        background: #d9d9d920;
        margin: 11.75vw auto auto 2.2vw;
        left: 0;
        position: absolute;
        color: #FFFCFC;
        text-align: center;
        font-family: Poppins;
        font-size: 4vw;
        font-style: normal;
        font-weight: 300;
    }
    .buyButton{
        width: 18.5vw;
        height: 8vw;
        flex-shrink: 0;
        border-radius: 1.25vw;
        background: #126D10;
        position: absolute;
        color: #FFFCFC;
        text-align: center;
        font-family: Poppins;
        font-size: 4vw;
        font-style: normal;
        font-weight: 700;
        line-height: 8vw;
        margin: 11.75vw auto auto 42.25vw;
    }
    .ownerInfoDiv{
        width: 22.5vw;
        height: 8.75vw;
        flex-shrink: 0;
        position: absolute;
        margin: 11.75vw auto auto 62.25vw;
        /* background: red; */
        color: #535050;
        text-align: center;
        font-family: Poppins;
        font-size: 2vw;
        font-style: normal;
        font-weight: 700;
        line-height: 2.75vw;
    }
    .sellResourceDiv{
        width: 86.25vw;
        height: 21.25vw;
        flex-shrink: 0;
        background: #6F8B87;
        position: absolute;
        border-radius: 1.25vw;
        margin: 40vw auto auto calc((100% - 86.25vw)/2);
    }
    .sellDivInputAmount{
        width: 37.5vw;
        height: 6.75vw;
        flex-shrink: 0;
        border-radius: 1.25vw;
        background: #d9d9d920;
        position: absolute;
        left: 0;
        margin: 1.25vw auto auto 2vw;
        color: #FFFCFC;
        text-align: left;
        font-family: Poppins;
        font-size: 3vw;
        font-style: normal;
        font-weight: 200;
    }
    .sellDivInputPrice{
        width: 37.5vw;
        height: 6.75vw;
        flex-shrink: 0;
        border-radius: 1.25vw;
        background: #d9d9d920;
        position: absolute;
        left: 0;
        margin: 11.5vw auto auto 2vw;
        color: #FFFCFC;
        text-align: left;
        font-family: Poppins;
        font-size: 3vw;
        font-style: normal;
        font-weight: 200;
    }
    .sellButton{
        width: 38vw;
        height: 10vw;
        flex-shrink: 0;
        border-radius: 1.25vw;
        background: #FF0101;
        color: #FFFCFC;
        text-align: center;
        font-family: Poppins;
        font-size: 4vw;
        font-style: normal;
        font-weight: 700;
        line-height: 10vw;
        position: absolute;
        margin: 5.25vw auto auto 46.25vw;
    }
    .craftDiv{
        width: 86.25vw;
        height: 21.25vw;
        flex-shrink: 0;
        border-radius: 1.25vw;
        background: #6F8B87;
        position: absolute;
        margin: 62.75vw auto auto calc((100% - 86.25vw)/2);
    }
    .craftDivInput{
        width: 37.5vw;
        height: 8.75vw;
        flex-shrink: 0;
        background: #d9d9d920;
        position: absolute;
        left: 0;
        border-radius: 1.25vw;
        margin: 1vw auto auto 2vw;
        color: #FFFCFC;
        text-align: left;
        font-family: Poppins;
        font-size: 3vw;
        font-style: normal;
        font-weight: 200;
        line-height: 8.75vw;
    }
    .craftButton{
        width: 39.5vw;
        height: 8vw;
        flex-shrink: 0;
        border-radius: 1.25vw;
        background: #126D10;
        position: absolute;
        color: #FFFCFC;
        text-align: center;
        font-family: Poppins;
        font-size: 4vw;
        font-style: normal;
        font-weight: 700;
        line-height: 8vw;
        margin: 12vw auto auto 1.75vw;
    }
    .usedResAmount{
        width: 152px;
        height: 74px;
        flex-shrink: 0;
        background: #7F9693;
        position: absolute;
        margin: 1vw auto auto 46vw;
        color: #535050;
        text-align: left;
        font-family: Poppins;
        font-size: 4vw;
        font-style: normal;
        font-weight: 700;
        line-height: 2.75vw;
    }
    .oilClass{
        margin-top: 2vw;
        /* margin-top: 64.5vw; */
        /* stareter 20vw */
    }
    .coalClass{
        /* margin-top: 129vw; */
        margin-top: 2vw;
    }
    .ironClass{
        /* margin-top: 193.5vw; */
        margin-top: 2vw;
    }
    .silverClass{
        /* margin-top: 258vw; */
        margin-top: 2vw;
    }
    .oxygenClass{
        /* margin-top: 322.5vw; */
        margin-top: 2vw;
    }
    .taiger1Class{
        /* margin-top: 387vw; */
        margin-top: 2vw;
        /* height: 87.75vw !important; */
        background: #7F9693;
    }
    .taiger2Class{
        /* margin-top: 475.75vw; */
        margin-top: 2vw;
        /* height: 87.75vw !important; */
        background: #7F9693;
    }
    .t-90Class{
        /* margin-top: 564.5vw; */
        margin-top: 2vw;
        /* height: 87.75vw !important; */
        background: #7F9693;
    }
    .himarsClass{
        /* margin-top: 653.25vw; */
        margin-top: 2vw;
        /* height: 87.75vw !important; */
        background: #7F9693;
    }
    .bayraktarClass{
        /* margin-top: 742vw; */
        margin-top: 2vw;
        /* height: 87.75vw !important; */
        background: #7F9693;
    }
    .wolframClass{
        /* margin-top: 830.75vw; */
        margin-top: 2vw;
        /* height: 87.75vw !important; */
        background: #7F9693;
    }
    .visibilityClass{
        display: none;
    }
    .largeDivClass{
        height: 18vw
    }
</style>