<template>
    <div class="informationHeader"></div>
    <div class="informationDiv">
        <div v-for="i in [0,1,2,3,4,3,2,33,2,432,32,4,,3,3,3,3,3,3,3,3,3,33,3,3,3,3,3]" class="mainDivOfAllFriend">
            <div class="chatDiv">
                <p class="chatP pClass">Jusepe Verdy</p>
            </div>
        </div>
    </div>
</template>

<script>
export default {

}
</script>

<style scoped>
    .informationHeader{
        width: 25vw;
        height: 8.5vw;
        flex-shrink: 0;
        background: #D9D9D9;
        position: absolute;
        left: 0;
        margin: 5.5vw auto auto 6.25vw;
    }
    .informationDiv{
        width: 87.25vw;
        height: 80.75vw;
        flex-shrink: 0;
        border-radius: 0 2.5vw 2.5vw 2.5vw;
        background: #D9D9D9;
        position: absolute;
        left: 0;
        margin: 14vw auto auto calc((100% - 87.5vw)/2);
        overflow-y: auto;
    }
    .mainDivOfAllFriend{
        background-color: rgba(31, 31, 31, 0.05);
        width: 100%;
        height: 10vw;
        margin-top: 2vw;
        display: grid;
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
    .pClass{
        margin-left: 5vw;
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
</style>