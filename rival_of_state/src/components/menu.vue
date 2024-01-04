<template>
    <div class="mainDiv" style="background-color: #0E0000; width:100%; height: 912px; position: absolute; display: grid; top: 0; left: 0;">
      <AppHeader/>
      <input class="searchInput" type="search" placeholder="  &#128269  Search...">
      <div class="button first buttonText">State</div>
      <div class="button second buttonText">Party</div>
      <router-link to="/work">
        <div class="button third buttonText">Work</div>
      </router-link>
      <router-link to="/war">
        <div class="button fourth buttonText">War</div>
      </router-link>
      <router-link to="/map">
        <div class="button fiveth buttonText">Map</div>
      </router-link>
      <div class="button sixth buttonText">Shop</div>
      <div class="button seventh buttonText">Parlament</div>
      <div class="button eighth buttonText">News</div>
      <div class="bugsButton">Report Bugs</div>
      <!-- <div class="footerMenuDiv">
        <div class="menuFirst">Home</div>
        <div class="menuSecond">News</div>
        <div class="menuThird">Work</div>
        <div class="menuForth">War</div>
        <div class="menuFiveth">Profile</div>
      </div> -->
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
      background-image: url('/Users/programing/Desktop/programing/rival/rival_of_state/src/assets/png-transparent-flag-flag-countries-flags-spherical-flag-national-flag-spherical 1.png');
      background-size: 100vw 100vh;
    }
    .searchInput{
        width: 79%;
        height: 34px;
        flex-shrink: 0;
        border-radius: 10px;
        position: absolute;
        margin: 190px auto auto calc((100vw - 79%)/2);
        opacity: 0.69;
        /* background: transparent url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='16' height='16' class='bi bi-search' viewBox='0 0 16 16'%3E%3Cpath d='M11.742 10.344a6.5 6.5 0 1 0-1.397 1.398h-.001c.03.04.062.078.098.115l3.85 3.85a1 1 0 0 0 1.415-1.414l-3.85-3.85a1.007 1.007 0 0 0-.115-.1zM12 6.5a5.5 5.5 0 1 1-11 0 5.5 5.5 0 0 1 11 0z'%3E%3C/path%3E%3C/svg%3E") no-repeat 30px right ; */
    }
    .button{
        width: 39.75%;
        height: 43px;
        border-radius: 5vw;
        background: #6F8B87;
        position: absolute;
        top: 326px;
        left: 5.5%;
    }
    .second{
        margin-left: 49.25%;
    }
    .third{
        margin-top: 98px;
    }
    .fourth{
        margin: 98px auto auto 49.25%;
    }
    .fiveth{
        margin: 179px auto auto auto;
    }
    .sixth{
        margin: 179px auto auto 49.25%;
    }
    .seventh{
        margin: 277px auto auto auto;
    }
    .eighth{
        margin: 277px auto auto 49.25%;
    }
    .buttonText{
        color: #FFF;
        text-align: center;
        font-family: Poppins;
        font-size: 5vw;
        font-style: normal;
        font-weight: 700;
        line-height: 43px;
    }
    .bugsButton{
        width: 92.5%;
        height: 76px;
        flex-shrink: 0;
        border-radius: 5vw;
        background-color: #6F8B87;
        position: absolute;
        margin: 705px auto auto calc((100vw - 92.5%)/2);
        color: #FFF;
        text-align: center;
        font-family: Poppins;
        font-size: 5vw;
        font-style: normal;
        font-weight: 700;
        line-height: 76px;
    }

  </style>