<template>
    <div class="mainDiv" style="background-color: #0E0000; width:100%; height: 1166px; position: absolute; display: grid; top: 0; left: 0;">
        <AppHeader/>
        <div class="globalInfoDiv">
            <div class="factoryIcon"></div>
            <input class="newTitle">
            <div class="changeTitle">Change Title</div>
            <p class="currentTitle">Title</p>
        </div>
        <div class="editDescription">Edit Description</div>
        <input class="descriptionDiv" type="text" placeholder="Description">
        <div class="changeWageTypeDiv">
            <div class="wageType">Resource %</div>
            <input class="wageAmount" type="number">
            <div class="wageTypeMoney">Money $</div>
            <input class="wageAmountMoney" type="text">
            <div class="changeWageTypeButton">Change Wage Type</div>
        </div>
        <div class="budgetDiv">
            <div class="budgetTitle">Budget</div>
            <div class="moneyBudget"><span>Money:</span><span>100000</span></div>
            <div class="moneyAdd">Add</div>
            <div class="moneyWithdraw">Withdraw</div>
            <div class="resourceBudget"><span>Resource:</span><span>100000</span></div>
            <div class="resourceWithdraw">Withdraw</div>
        </div>
        <router-link to="test">
        <div class="storageDiv">
            Storage
        </div>
        </router-link>
        <AppFooterMenu/>

        
        
    </div>
  
</template>

<script>
  import AppHeader from './headers/AppHeader.vue'
  import AppFooterMenu from './headers/footerMenu.vue'
  export default {
    components: {
        AppHeader,
        AppFooterMenu
  }
  }
  </script>

<style scoped>
    .mainDiv{
        height: 291.5vw !important;
        background-image: url('/src/assets/png-transparent-flag-flag-countries-flags-spherical-flag-national-flag-spherical 1.png');
        background-size: 100vw 100vh;
    }
    .globalInfoDiv{
        width: 92.5%;
        height: 25vw;
        flex-shrink: 0;
        border-radius: 5vw;
        background: #6F8B87;
        position: absolute;
        margin: 35.75vw auto auto calc((100vw - 92.5%)/2);
        align-items: center;
        display: grid;
    }
    .factoryIcon{
        width: 17.5vw;
        height: 17.5vw;
        background-image: url('/src/assets/earth_icon.png');
        background-size: 100%;
        margin-left: 3vw;
    }
    .changeTitle{
        width: 30vw;
        height: 7vw;
        border-radius: 1.25vw;
        background: #064D9F;
        color: #fff;
        text-align: center;
        font-family: Play;
        font-size: 5vw;
        font-style: normal;
        font-weight: 400;
        line-height: 7vw;
        position: absolute;
        margin: auto auto 10vw 60vw
    }
    .newTitle{
        width: 33vw;
        height: 6vw;
        border-radius: 1.25vw;
        background: #172b43;
        color: #fff;
        text-align: center;
        font-family: Play;
        font-size: 4vw;
        font-style: normal;
        font-weight: 200;
        position: absolute;
        margin: auto auto 10vw 24vw
    }
    .currentTitle{
        color: #FFFCFC;
        text-align: center;
        font-family: Play;
        font-size: 5vw;
        font-style: normal;
        font-weight: 400;
        line-height: normal;
        position: absolute;
        margin: 8vw auto auto 24.5vw;
    }
    .editDescription{
        width: 80.75vw;
        height: 11vw;
        border-radius: 1.25vw;
        background: #064D9F;
        color: #fff;
        text-align: center;
        font-family: Play;
        font-size: 5vw;
        font-style: normal;
        font-weight: 400;
        line-height: 11vw;
        position: absolute;
        margin: 79vw auto auto calc((100vw - 80.75vw)/2);
    }
    .descriptionDiv{
        width: 80.75vw;
        height: 10.75vw;
        flex-shrink: 0;
        border-radius: 1vw;
        background: #6F8B87;
        position: absolute;
        margin: 95.5vw auto auto calc((100vw - 82vw)/2);
        color: #FFF;
        font-family: Inter;
        font-size: 3.75vw;
        font-style: normal;
        font-weight: 400;
        line-height: normal;
    }
    .changeWageTypeDiv{
        width: 92.5vw;
        height: 40.75vw;
        flex-shrink: 0;
        border-radius: 5vw;
        background: #768C89;
        position: absolute;
        margin: 121.5vw auto auto calc((100vw - 92.5vw)/2);
    }
    .wageType{
        width: 40.5vw;
        height: 6vw;
        border-radius: 1.25vw;
        background: #185601;
        color: #fff;
        text-align: center;
        font-family: Play;
        font-size: 5vw;
        font-style: normal;
        font-weight: 400;
        line-height: 6vw;
        position: absolute;
        margin: 5vw auto auto 5vw;
    }
    .wageAmount{
        width: 30.5vw;
        height: 5vw;
        border-radius: 1.25vw;
        background: #D9D9D9;
        color: #fff;
        text-align: center;
        font-family: Play;
        font-size: 5vw;
        font-style: normal;
        font-weight: 400;
        line-height: 12vw;
        position: absolute;
        margin: 5vw auto auto 5vw;
    }
    .wageTypeMoney{
        width: 40.5vw;
        height: 6vw;
        border-radius: 1.25vw;
        background: #f90101;
        color: #fff;
        text-align: center;
        font-family: Play;
        font-size: 5vw;
        font-style: normal;
        font-weight: 400;
        line-height: 6vw;
        position: absolute;
        margin: 15vw auto auto 5vw;
    }
    .wageAmountMoney{
        width: 30.5vw;
        height: 5vw;
        border-radius: 1.25vw;
        background: #D9D9D9;
        color: #fff;
        text-align: center;
        font-family: Play;
        font-size: 5vw;
        font-style: normal;
        font-weight: 400;
        line-height: 12vw;
        position: absolute;
        margin: 15vw auto auto 5vw;
    }
    .changeWageTypeButton{
        width: 50vw;
        height: 8.5vw;
        border-radius: 1.25vw;
        position: absolute;
        background: #0258FF;
        margin: 25vw auto auto calc((100% - 50vw)/2);
        color: #fff;
        text-align: center;
        font-family: Play;
        font-size: 5vw;
        font-style: normal;
        font-weight: 400;
        line-height: 8.5vw;
    }
    .budgetDiv{
        width: 92.5vw;
        height: 82vw;
        flex-shrink: 0;
        border-radius: 5vw;
        background: #768C89;
        position: absolute;
        margin: 164.5vw auto auto calc((100vw - 92.5vw)/2);
    }
    .budgetTitle{
        width: 40.5vw;
        height: 10vw;
        background: #658984;
        color: #433232;
        text-align: center;
        font-family: Play;
        font-size: 5vw;
        border-radius: 1.25vw;
        font-style: normal;
        font-weight: 400;
        line-height: 10vw;
        margin: 5.5vw auto auto calc((100% - 40.5vw)/2);
    }
    .moneyBudget{
        width: 77vw;
        height: 12.5vw;
        border-radius: 1.25vw;
        background: #126D10;
        color: #fff;
        text-align: center;
        font-family: Play;
        font-size: 5vw;
        font-style: normal;
        font-weight: 400;
        line-height: 12.5vw;
        position: absolute;
        display: flex;
        justify-content: space-between;
        margin: 5vw auto auto calc((100% - 77vw)/2);
    }
    .moneyAdd{
        width: 97px;
        height: 8vw;
        border-radius: 1.25vw;
        background: #126D10;
        color: #fff;
        text-align: center;
        font-family: Play;
        font-size: 20px;
        font-style: normal;
        font-weight: 400;
        line-height: 8vw;
        position: absolute;
        margin: 20vw auto auto 12vw;
    }
    .moneyWithdraw{
        width: 35vw;
        height: 8vw;
        border-radius: 5px;
        background: #FF0202;
        color: #fff;
        text-align: center;
        font-family: Play;
        font-size: 20px;
        font-style: normal;
        font-weight: 400;
        line-height: 8vw;
        position: absolute;
        margin: 20vw auto auto 45vw;
    }
    .resourceBudget{
        width: 77vw;
        height: 12.5vw;
        border-radius: 1.25vw;
        background: #660202;
        color: #fff;
        text-align: center;
        font-family: Play;
        font-size: 5vw;
        font-style: normal;
        font-weight: 400;
        line-height: 12.5vw;
        position: absolute;
        display: flex;
        justify-content: space-between;
        margin: 35vw auto auto calc((100% - 77vw)/2);
    }
    .resourceWithdraw{
        width: 35vw;
        height: 8vw;
        border-radius: 5px;
        background: #FF0202;
        color: #fff;
        text-align: center;
        font-family: Play;
        font-size: 20px;
        font-style: normal;
        font-weight: 400;
        line-height: 8vw;
        position: absolute;
        margin: 52vw auto auto calc((100% - 35vw)/2);
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