<template>
      <div style="width: 100vw; height: 80px;">
        <router-link to="/menu">
          <div class="profileIcon"></div>
        </router-link>
        <router-link to="/">
          <div class="titleIcon">Clash Of State</div>
        </router-link>
        <div class="settingIcon"></div>
      </div>
   
  </template>
  
  <script>
  export default {
    
  }
  </script>
  
  <style>
    .mainDiv{
      background-image: url('/src/assets/png-transparent-flag-flag-countries-flags-spherical-flag-national-flag-spherical 1.png');
      background-size: 100vw 100vh;
    }
    .profileIcon{
        width: 17.5vw;
        height: 17.5vw;
        background-image: url('/src/assets/profile_icon.png');
        background-size: 100% 100%;
        margin: 10px;
    }
    .titleIcon{
        width: 50%;
        height: 20px;
        /* background-image: url('/src/assets/Clash_Of_State.png'); */
        background-size: 100% 100%;
        position: absolute;
        margin: 30px auto auto calc((100vw - 50%)/2);
        top: 0;
        color: #FFFCFC;
        text-align: center;
        font-family: Poppins;
        font-size: 5vw;
        font-style: normal;
        font-weight: 700;
        line-height: normal;
    }
    .settingIcon{
        width: 12.22vw;
        height: 12.22vw;
        flex-shrink: 0;
        background-image: url('/src/assets/settings.png');
        position: absolute;
        top: 0;
        margin: 15px auto auto 83.25%;
        background-size: 100% 100%;
    }
  </style>