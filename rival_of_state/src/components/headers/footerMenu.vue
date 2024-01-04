<template>
    
      <div class="footerMenuDiv">
        <router-link to="/">
          <div class="menuFirst">Home</div>
        </router-link>
        <div class="menuSecond">News</div>
        <router-link to="/work">
          <div class="menuThird">Work</div>
        </router-link>
        <router-link to="/war">
          <div class="menuForth">War</div>
        </router-link>
        <!-- <router-link to="/profile"> -->
          <div class="menuFiveth" @click="this.getProfile()">Profile</div>
        <!-- </router-link> -->
      </div>
</template>
  
  <script>
  export default {
    components: {
  },
  methods:{
    getProfile(){
      this.$router.push({
        path: `/profile/${localStorage.getItem('id')}` })
        }
    },
  }
  </script>
  
  <style scoped>
    .footerMenuDiv{
        width: 92.5%;
        height: 15vw;
        flex-shrink: 0;
        border-radius: 5vw;
        background: #6F8B87;
        position: absolute;
        margin: auto auto 6.5vw calc((100vw - 92.5%)/2);
        bottom: 0;
    }
    .footerMenuDiv div{
        display: inline-block;
        color: #FFF;
        text-align: center;
        font-family: Poppins;
        font-size: 5vw;
        font-style: normal;
        font-weight: 700;
        line-height: 15vw;
        position: absolute;
        left: 0;
    }
    .menuFirst{
        margin-left: 6px;
    }
    .menuSecond{
        margin-left: 22.97%;
    }
    .menuThird{
        margin-left: 42.97%;
    }
    .menuForth{
        margin-left: 62.7%;
    }
    .menuFiveth{
        margin-left: 79.72%;
    }
  </style>