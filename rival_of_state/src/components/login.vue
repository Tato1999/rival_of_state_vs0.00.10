<template>
  <div class="mainDiv" style="background-color: #0E0000; width:100%; height: 100vh; position: absolute; display: grid; top: 0; left: 0;">
    <div class="rivalIcon">
    </div>
    <div class="welcomeIcon">
    </div>
    <input class="loginInput" type="text" placeholder="Enter Your emale">
    <input class="loginPassword" type="text" placeholder="Enter Your Password">
    <p class="resetPassword">Forgot Password</p>
    <div class="loginButton">
      <p class="loginText" @click="this.sendValue">Sign In</p>
    </div>
    <p class="or">or</p>
    <div class="googleAuth">
      <img class="googleIcon" :src='require("@/assets/Google_ G _Logo.png")'>
      <b style="margin-left: 50px;">Google{{ this.err }}</b>
    </div>
    <div class="facebookAuth">
      <img class="facebookIcon" :src='require("@/assets/facebook_icon.png")'>
      <b style="margin-left: 50px;">Facebook</b>
    </div>
    <p class="haveAccText" @click="this.getRegisterForm()">Don’t have an account? <span>Sign Up</span></p>
  </div>
 
</template>

<script>
import axios from 'axios'
import {useRouter} from 'vue-router'
export default {
  data(){
    return{
      emailForCheck:'',
      passwordForCheck:'',
      err:'',
      // ip: 'http://94.43.110.179:80',
      // ip: 'http://127.0.0.1:80',
      ip: 'http://tato1999.pythonanywhere.com/'
    }
  },
  methods:{
    getRegisterForm(){
      this.$router.push({
                // name: 'user',
                // params:{id:res.data['id']}})
              // this.sendIdLocal(path)
              path: `/register` })
    },
    getValue(){
      this.emailForCheck = document.querySelector('.loginInput').value;
      this.passwordForCheck = document.querySelector('.loginPassword').value
    },
    sendValue(){
      this.getValue()
      const path = this.ip+'/login';
        //  const path = 'http://192.168.1.2:80/login'
        // const path = 'http://192.168.54.172:80/login'

            // const path = 'http://192.168.4.48:80/login'
            axios.post(path,{
              email:this.emailForCheck,
              password:this.passwordForCheck
            })
            .then((res) => {
              console.log(res.data)
              localStorage.setItem('id', res.data['id'])
              // this.sendIdLocal(path)
              this.$router.push({
                // name: 'user',
                // params:{id:res.data['id']}})
                
              path: `/profile/${res.data['id']}` 
            })
            })
            .catch((err) => {
                console.error(err)
                this.err = err
            })
    },
    sendIdLocal(path){
            axios.get(path)
            .then((res) => {
              console.log(res.data)
              localStorage.setItem('id', res.data['id'])
            })
            .catch((err) => {
                console.error(err)
            })
      
    }
  }

}
</script>

<style scoped>
  .mainDiv{
        height: 291.5vw !important;
        background-image: url('/src/assets/png-transparent-flag-flag-countries-flags-spherical-flag-national-flag-spherical 1.png');
        background-size: 100vw 100vh;
  }
  .rivalIcon{
    position: absolute;
    width: 81.25%;
    height: 28.25vw;
    margin: 27.5vw auto auto calc((100vw - 81.25%)/2);
    background-image: url("/src/assets/Screen_Shot_2023-04-03_at_00.08 1.png");
    background-size: 100% 100%;
    
  }
  .welcomeIcon{
    position: absolute;
    width: 41.9vw;
    height: 5.4vw;
    margin: 77.5vw auto auto calc((100vw - 41.9vw)/2);
    background-image: url("/src/assets/Welcome Back.png");
    background-size: 100% 100%;
  }
  .loginInput{
    width: 89.25%;
    height: 5vw;
    flex-shrink: 0;
    margin: 96vw auto auto calc((100vw - 89.25%)/2);
    border-radius: 8vw;
  }
  .loginPassword{
    position: absolute;
    width: 89.25%;
    height: 4vw;
    flex-shrink: 0;
    margin: 103.75vw auto auto calc((100vw - 89.25%)/2);
    border-radius: 8vw;
    background-color: #fff;
  }
  .resetPassword{
    width: 76.75vw;
    height: 14vw;
    flex-shrink: 0;
    color: rgba(254, 234, 243, 0.80);
    text-align: center;
    font-family: Poppins;
    font-size: 4.5vw;
    font-style: normal;
    font-weight: 500;
    line-height: normal;
    position: absolute;
    margin: 164vw auto auto calc((100vw - 76.75vw)/2);
  }
  .loginButton{
    width: 89.25%;
    height: 19vw;
    flex-shrink: 0;
    background-color: rgba(111, 139, 135, 1);
    border-radius: 12.25vw;
    position: absolute;
    margin: 174.5vw auto auto calc((100vw - 89.25%)/2);
  }
  .loginText{
    color: #FFF;
    text-align: center;
    font-family: Poppins;
    font-size: 5vw;
    font-style: normal;
    font-weight: 700;
    line-height: 10vw;
  }
  .or{
    position: absolute;
    margin: 122.5vw auto auto 50vw;
    color: #FFF;
    text-align: center;
    font-family: Poppins;
    font-size: 7.5vw;
    font-style: normal;
    font-weight: 700;
    line-height: 5vw;
  }
  .googleAuth{
    width: 62.5%;
    height: 10vw;
    flex-shrink: 0;
    background-color: rgb(126, 57, 46);
    border-radius: 2.5vw;
    position: absolute;
    margin: 137.5vw auto auto calc((100vw - 62.5%)/2);
    line-height: 10vw;
    text-align: center;
    color: white;
    font-size: 4.5vw;
  }
  .googleIcon{
    position: absolute;
    width: 8.75vw;
    height: 8.75vw;
    margin-top: 0.5vw;
    margin-left: -0.125vw;
  }
  .facebookAuth{
    width: 62.5%;
    height: 10vw;
    flex-shrink: 0;
    background-color: rgb(10, 71, 213);
    border-radius: 2.5vw;
    position: absolute;
    margin: 150vw auto auto calc((100vw - 62.5%)/2);
    line-height: 10vw;
    text-align: center;
    color: white;
    font-size: 4.5vw;
  }
  .facebookIcon{
    position: absolute;
    width: 10vw;
    height: 10vw;
    margin-top: 0.25vw;
    border-radius: 25vw;
  }
  .haveAccText{
    width: 76.75%;
    height: 9vw;
    flex-shrink: 0;
    color: rgba(255, 255, 255, 0.80);
    text-align: center;
    font-family: Poppins;
    font-size: 4.5vw;
    font-style: normal;
    font-weight: 500;
    line-height: normal;
    position: absolute;
    margin: 204.5vw auto auto calc((100vw - 76.75%)/2);
  }
  .haveAccText span{
    color: #9AB293;
    font-family: Poppins;
    font-size: 4.5vw;
    font-style: normal;
    font-weight: 700;
    line-height: normal;
  }
</style>