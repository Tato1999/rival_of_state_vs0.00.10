<template>
    <div class="mainDiv" style="background-color: #0E0000; width:100%; height: 190.5vw; position: absolute; display: grid; top: 0; left: 0;">
        <AppHeader/>
        <div class="factoryInfoDiv">
            <div class="factoryIcon"></div>
            <div class="factoryMainInfo">
                <p class="factoryWorkers">Workers: 0/20</p>
                <p class="factoryLevelAndExp">Level: 175,      exp: 1.000.000.000</p>
                <p class="factoryRegionInfo">Region: Georgia</p>
                <p class="factoryStateInfo">State: Georgia</p>
            </div>
        </div>
        <div class="workButtonDiv">
            Start Working
        </div>
        <div class="factoryOwnerInformation">
            <div class="ownerIcon"></div>
            <p class="ownerParagraph">Owner: Tato</p>
            <p class="factoryCreateParagraph">Foundation Date: 14/10/2020</p>
        </div>
        <div class="organizationInformationDiv">
            <div class="ownerIcon"></div>
            <p class="ownerParagraph">Organization</p>
            <p class="factoryCreateParagraph">raagasfadasdasda</p>
        </div>
        <div class="additionalInformation">
            <p class="additionalInformationTopic">Additional Information</p>
            <div class="wageDiv">
                <p class="wageInformationName">Wage</p>
                <p class="wageInformationValue">100%</p>
            </div>
            <div class="potentialWageInformationDiv">
                <p>Potentional Wage:</p>
                <p>15.000.000$</p>
            </div>
            <div class="potentialWageWithoutRegionTaxes">
                <p>Real Wage exclude region taxes:</p>
                <p>13.000.000$</p>
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
  export default {
    components: {
        AppHeader,
        AppFooterMenu
  }
  }
  </script>

<style scoped>
    .mainDiv{
        height: 230.5vw !important;
        background-image: url('/src/assets/png-transparent-flag-flag-countries-flags-spherical-flag-national-flag-spherical 1.png');
        background-size: 100vw 100vh;
    }
    .factoryInfoDiv{
        width: 92.5vw;
        height: 30.75vw;
        flex-shrink: 0;
        border-radius: 5vw;
        background: #6F8B87;
        position: absolute;
        margin: 35.75vw auto auto calc((100vw - 92.5vw)/2);
    }
    .factoryIcon{
        width: 20vw;
        height: 20vw;
        flex-shrink: 0;
        background-image: url('/src/assets/profile_icon.png');
        background-size: 100% 100%;
        position: absolute;
        margin: 5.25vw auto auto 1.75vw;
/* background: url(<path-to-image>), lightgray 50% / cover no-repeat; */
    }
    .factoryMainInfo{
        width: 60.5vw;
        height: 19vw;
        position: absolute;
        margin: 5.75vw auto auto 25.5vw;
        justify-content: left;
    }
    .factoryWorkers{
        /* position: absolute; */
        color: #FFF;
        text-align: left;
        font-family: Poppins;
        font-size: 3.75vw;
        font-style: normal;
        font-weight: 400;
        line-height: normal;
        margin: 0;
    }
    .factoryLevelAndExp{
        position: absolute;
        margin: 0;
        color: #5A5A5A;
        text-align: left;
        font-family: Poppins;
        font-size: 3vw;
        font-style: normal;
        font-weight: 400;
        line-height: normal;
    }
    .factoryRegionInfo{
        color: #FFF;
        text-align: left;
        font-family: Poppins;
        font-size: 3.75vw;
        font-style: normal;
        font-weight: 400;
        line-height: normal;
        margin: 7vw auto 0 auto;
    }
    .factoryStateInfo{
        color: #5A5A5A;
        text-align: left;
        font-family: Poppins;
        font-size: 12px;
        font-style: normal;
        font-weight: 400;
        line-height: normal;
        margin: 0;
    }
    .workButtonDiv{
        width: 92.5vw;
        height: 7vw;
        flex-shrink: 0;
        border-radius: 5vw;
        background: #126D10;
        color: #FCFDFC;
        text-align: center;
        font-family: Play;
        font-size: 3.75;
        font-style: normal;
        font-weight: 400;
        line-height: 7vw;
        position: absolute;
        margin: 75.25vw auto auto calc((100vw - 92.5vw)/2);
    }
    .factoryOwnerInformation{
        width: 92.5vw;
        height: 15vw;
        flex-shrink: 0;
        border-radius: 2.5vw;
        background: #6F8B87;
        position: absolute;
        margin: 85.25vw auto auto calc((100vw - 92.5vw)/2);
    }
    .ownerIcon{
        width: 12.5vw;
        height: 12.5vw;
        flex-shrink: 0;
        background-image: url('/src/assets/profile_icon.png');
        background-size: 100% 100%;
        margin: 1.25vw auto auto 5.75vw;
        position: absolute;
    }
    .ownerParagraph{
        color: #FFF;
        text-align: center;
        font-family: Poppins;
        font-size: 3.75vw;
        font-style: normal;
        font-weight: 400;
        line-height: normal;
        position: absolute;
        margin: 3vw auto auto 25.25vw;
    }
    .factoryCreateParagraph{
        color: #5A5A5A;
        text-align: center;
        font-family: Poppins;
        font-size: 3vw;
        font-style: normal;
        font-weight: 400;
        line-height: normal;
        position: absolute;
        margin: 8vw auto auto 25.25vw;
    }
    .organizationInformationDiv{
        width: 92.5vw;
        height: 15vw;
        flex-shrink: 0;
        border-radius: 2.5vw;
        background: #6F8B87;
        position: absolute;
        margin: 101vw auto auto calc((100vw - 92.5vw)/2);
    }
    .additionalInformation{
        width: 92.5vw;
        height: 31vw;
        flex-shrink: 0;
        border-radius: 2.5vw;
        background: #6F8B87;
        position: absolute;
        margin: 120vw auto auto calc((100vw - 92.5vw)/2);
    }
    .additionalInformationTopic{
        color: #FFF;
        text-align: center;
        font-family: Poppins;
        font-size: 3.75vw;
        margin: 0;
        font-style: normal;
        font-weight: 400;
        line-height: normal;
    }
    .wageDiv{
        width: 90%;
        display: flex;
        justify-content: space-between;
        margin: 5vw 0 0 calc((100% - 90%)/2);
        /* margin-left: calc((100% - 90%)/2); */
    }
    .wageDiv p{
        margin: 1vw;
        color: #FFF;
        text-align: center;
        font-family: Poppins;
        font-size: 3vw;
        font-style: normal;
        font-weight: 400;
        line-height: normal;
    }
    .potentialWageInformationDiv{
        width: 90%;
        display: flex;
        justify-content: space-between;
        margin-left: calc((100% - 90%)/2);
    }
    .potentialWageInformationDiv p{
        margin: 1vw;
        color: #FFF;
        text-align: center;
        font-family: Poppins;
        font-size: 3vw;
        font-style: normal;
        font-weight: 400;
        line-height: normal;
    }
    .potentialWageWithoutRegionTaxes{
        width: 90%;
        display: flex;
        justify-content: space-between;
        margin-left: calc((100% - 90%)/2);
    }
    .potentialWageWithoutRegionTaxes p{
        color: #FFF;
        text-align: center;
        font-family: Poppins;
        font-size: 3vw;
        font-style: normal;
        font-weight: 400;
        line-height: normal;
        margin: 1vw;
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