<template>
    <loading-overlay v-if="loading" :can-cancel='false' :color="'#000'" :background="'black'">
    </loading-overlay>
    <div v-if="dataLoaded" class="informationHeader"></div>
    <div v-if="dataLoaded" class="informationDiv">
        <p class="name">{{ this.userName }}</p>
        <div class="friendsDiv">
            <p class="friendsP pClass">Friends</p>
            <p class="friendsValue valueClass">{{ this.friends_count }}</p>
        </div>
        <div class="expDiv">
            <p class="expP pClass">Exp</p>
            <p class="expValue valueClass">{{ this.experience }}</p>
        </div>
        <div class="wholeDamagesDiv">
            <p class="wholeDamagesP pClass">Whole Damages</p>
            <p class="wholeDamagesValue valueClass">{{ this.damage }}</p>
        </div>
        <div class="warsDiv">
            <p class="warsP pClass">Wars</p>
            <p class="warsValue valueClass">Recent</p>
        </div>
        <div class="workingExperienceDiv">
            <p class="workingExperienceP pClass">workingExperience</p>
            <p class="workingExperienceValue valueClass">{{ this.working_experience }}</p>
        </div>
        <div class="maxForSpecialityDiv">
            <p class="maxForSpecialityP pClass">Max For Speciality</p>
            <p class="maxForSpecialityValue valueClass">{{this.max_experience}}</p>
        </div>
        <div class="newsDiv">
            <p class="newsP pClass">Published News</p>
            <p class="newsValue valueClass">100.000</p>
        </div>
        <div class="showQuestDiv">
            <div class="showQuestButton">Show Quest</div>
        </div>
        <div class="itemsDiv">
            <div class="buyItemsButton">Buy Items</div>
        </div>
        <div class="donationHistoryDiv">
            <div class="seeDonationHistoryButton">See Donation History</div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'
import LoadingOverlay from 'vue-loading-overlay';
import 'vue-loading-overlay/dist/css/index.css';

export default {
    components:{
        LoadingOverlay
    },
    data(){
        return{
            userName:"",
            loading: true,
            dataLoaded: false,
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
            //  const path = 'http://192.168.4.48:80/profile';
            // const path = 'http://127.0.0.1:80/profile'
            const path = this.ip+'/profile'
             axios.post(path,{
                id: localStorage.getItem('id'),
                energy: -1
             })
             .then((res) => {
                 console.log(res.data)
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

                 let exp_percent = (100*this.experience)/100
                 this.dataLoaded = true
                 this.loading = false
                 console.log(exp_percent)
                 setTimeout(() => {
                    document.querySelector('.fillExperienceInformationIndicator').style.width = exp_percent+"%"
                 },10)
                 
                })
             .catch((err) => {
                 console.error(err)
             })
         },
    },
    created(){
        this.sendIdInfo()
    }
}
</script>

<style>
    .informationHeader{
        width: 25vw;
        height: 8.5vw;
        flex-shrink: 0;
        background: #D9D9D9;
        position: absolute;
        left: 0;
        margin: 5.5vw auto auto 69.25vw;
    }
    .informationDiv{
        width: 87.25vw;
        height: 80.75vw;
        flex-shrink: 0;
        border-radius: 10px 0px 10px 10px;
        background: #D9D9D9;
        position: absolute;
        left: 0;
        margin: 14vw auto auto calc((100% - 86vw)/2);
    }
    .informationDiv p{
        color: #000;
        text-align: center;
        font-family: Play;
        font-size: 3.75vw;
        font-style: normal;
        font-weight: 400;
        line-height: normal;
        margin-bottom: 0vw;
    }
    .valueClass{
        margin-right: 5vw;
    }
    .pClass{
        margin-left: 5vw;
    }
    .friendsDiv{
        display: flex;
        justify-content: space-between;
    }
    .expDiv{
        display: flex;
        justify-content: space-between;
    }
    .wholeDamagesDiv{
        display: flex;
        justify-content: space-between;
    }
    .warsDiv{
        display: flex;
        justify-content: space-between;
    }
    .workingExperienceDiv{
        display: flex;
        justify-content: space-between;
    }
    .maxForSpecialityDiv{
        display: flex;
        justify-content: space-between;
    }
    .newsDiv{
        display: flex;
        justify-content: space-between;
    }
    .showQuestDiv{
        width: 79.5vw;
        height: 5.25vw;
        flex-shrink: 0;
        background: #2f0101;
        margin: 4vw auto auto calc((100% - 79.5vw)/2);
        color: #fcfbfb;
        text-align: center;
        font-family: Play;
        font-size: 3.75vw;
        font-style: normal;
        font-weight: 400;
        line-height: 5.25vw;
    }
    .itemsDiv{
        width: 79.5vw;
        height: 5.25vw;
        flex-shrink: 0;
        background: #2f0101;
        margin: 0.5vw auto auto calc((100% - 79.5vw)/2);
        color: #fcfbfb;
        text-align: center;
        font-family: Play;
        font-size: 3.75vw;
        font-style: normal;
        font-weight: 400;
        line-height: 5.25vw;
    }
    .donationHistoryDiv{
        width: 79.5vw;
        height: 5.25vw;
        flex-shrink: 0;
        background: #2f0101;
        margin: 0.5vw auto auto calc((100% - 79.5vw)/2);
        color: #fcfbfb;
        text-align: center;
        font-family: Play;
        font-size: 3.75vw;
        font-style: normal;
        font-weight: 400;
        line-height: 5.25vw;
    }
    .textStyle{
        color: #FFF;
        text-align: left;
        font-family: Play;
        font-size: 3.75vw;
        font-style: normal;
        font-weight: 400;
        line-height: 10vw;
    }
    .name{
        color: red;
        width: 10vw;
        position: absolute;
        margin: -1vw auto auto calc((100% - 10vw)/2);
        font-size: 20px;
    }
</style>