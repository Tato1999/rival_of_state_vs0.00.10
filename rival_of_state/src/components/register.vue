<template>
  <div class="mainDiv" style="background-color: #0E0000; width:100%; height: 912px; position: absolute; display: grid; top: 0; left: 0;">
    <div class="rivalIcon">
    </div>
    <div class="welcomeIcon">
    </div>
    <input class="registerInput fullName" type="text" placeholder="Enter Your emale">
    <input class="registerInput email" type="text" placeholder="Enter Your emale">
    <input class="registerPassword password" type="text" placeholder="Enter Your Password">
    <input class="registerPassword confirmPassword" type="text" placeholder="Enter Your Password">
    <div class="loginButton" @click="this.getValue">
      <p class="loginText">Sign In</p>
    </div>
    <p class="or">or</p>
    <div class="googleAuth">
      <img class="googleIcon" :src='require("@/assets/Google_ G _Logo.png")'>
      <b style="margin-left: 50px;">Google</b>
    </div>
    <div class="facebookAuth">
      <img class="facebookIcon" :src='require("@/assets/facebook_icon.png")'>
      <b style="margin-left: 50px;">Facebook</b>
    </div>
    <p class="haveAccText" @click="this.getLoginForm()">Already have an account? <span>Sign Up</span></p>
  </div>
 
</template>

<script>
import axios from 'axios'

export default {
  data(){
    return{
      nameForSend:'',
      email:'',
      password:'',
      confirmPassword:'',
      // ip: 'http://94.43.110.179:80',
      // ip: 'http://127.0.0.1:80',
      ip: 'http://tato1999.pythonanywhere.com/'
    }
  },
  methods:{
    getLoginForm(){
      this.$router.push({
              path: `/login` })
    },
    getValue(){
      this.nameForSend = document.querySelector('.fullName').value;
      this.emailForSend = document.querySelector('.email').value;
      this.passwordForSend = document.querySelector('.password').value;
      this.confirmPassword = document.querySelector('.confirmPassword').value;
      if (this.passwordForSend == this.confirmPassword){
        this.sendInfo()
        this.$router.push({
              path: `/login` })
      }else{
        console.log("Error")
      }
    },
    sendInfo(){
      console.log(this.nameForSend)
      // const path = 'http://localhost:5000/register';

      // const path = 'http://192.168.4.48:80/register'
      // const path = 'http://127.0.0.1:80/register'

            const path = this.ip+'/register'
            axios.post(path,{
              name:this.nameForSend,
              email:this.emailForSend,
              password:this.passwordForSend
            })
            .then((res) => {
              console.log(res.data)
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
    background-image: url('/src/assets/png-transparent-flag-flag-countries-flags-spherical-flag-national-flag-spherical 1.png');
    background-size: 100vw 100vh;
  }
  .rivalIcon{
    position: absolute;
    width: 81.25%;
    height: 28.25vw;
    margin: 27.74vw auto auto calc((100vw - 81.25%)/2);
    background-image: url("/src/assets/Screen_Shot_2023-04-03_at_00.08 1.png");
    background-size: 100% 100%;
    
  }
  .welcomeIcon{
    position: absolute;
    width: 41.9vw;
    height: 5.4vw;
    margin: 77.75vw auto auto calc((100vw - 41.9vw)/2);
    background-image: url("/src/assets/Vector.png");
    background-size: 100% 100%;
  }
  .fullName{
    margin-top: 91.5vw !important;
    height: 5vw !important;
    
  }
  .registerInput{
    position: absolute;
    width: 89.25%;
    height: 5vw;
    flex-shrink: 0;
    margin: 99.75vw auto auto calc((100vw - 89.25%)/2);
    border-radius: 8vw;
  }
  .registerPassword{
    position: absolute;
    width: 89.25%;
    height: 5vw;
    flex-shrink: 0;
    margin: 107.5vw auto auto calc((100vw - 89.25%)/2);
    border-radius: 8vw;
    background-color: #fff;
  }
  .confirmPassword{
    margin-top: 115vw !important;
  }
  .loginButton{
    width: 89.25%;
    height: 12.5vw;
    flex-shrink: 0;
    background-color: rgba(111, 139, 135, 1);
    border-radius: 12.5vw;
    position: absolute;
    margin: 189vw auto auto calc((100vw - 89.25%)/2);
  }
  .loginText{
    color: #FFF;
    text-align: center;
    font-family: Poppins;
    font-size: 4vw;
    font-style: normal;
    font-weight: 700;
    line-height: 5vw;
  }
  .or{
    margin-top: 131.5vw;
    color: #FFF;
    text-align: center;
    font-family: Poppins;
    font-size: 8.5vw;
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
    margin: 150vw auto auto calc((100vw - 62.5%)/2);
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
    margin-left: -1.5vw;
  }
  .facebookAuth{
    width: 62.5%;
    height: 10vw;
    flex-shrink: 0;
    background-color: rgb(10, 71, 213);
    border-radius: 2.5vw;
    position: absolute;
    margin: 162.5vw auto auto calc((100vw - 62.5%)/2);
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
    margin: 210vw auto auto calc((100vw - 76.75%)/2);
    cursor: pointer;
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