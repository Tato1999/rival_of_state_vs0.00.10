<template>
  <router-view/>
  <!-- <loginPage/> -->
</template>

<script>
import loginPage from './components/parlament_election.vue'

export default {
  name: 'App',
  components: {
    loginPage
  },
  data(){
    return{
      loginBool: false
    }
  },
  mounted(){
    if(localStorage.getItem('id')){
      this.loginBool = true
      this.$router.push({
              path: `/` })
    }else{
      this.loginBool = false
      this.$router.push({
              path: `/login` })
    }
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  /* margin-top: 60px; */
}
</style>
