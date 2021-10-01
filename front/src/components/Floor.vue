<template>
  <v-app class="body">
    <v-app-bar app>
      {{this.floorNum}}階
    </v-app-bar>
    <v-main class="main">
      <v-container class="container">
        <div class="sec1">
          <div>
            <h3>上り</h3>
            <p>待ち時間：約{{waitingUp}}秒</p>
            <p>予想混雑度：<span v-bind:class="{ crowded: isCrowdedUp }">{{congestedStateUp}}</span>（約{{upPersons}}人）</p>
          </div>
          <div>
            <h3>下り</h3>
            <p>待ち時間：約{{waitingDown}}秒</p>
            <p>予想混雑度：<span v-bind:class="{ crowded: isCrowdedDown }">{{congestedStateDown}}</span>（約{{downPersons}}人）</p>
          </div>
        </div>
        <div class="sec2">
          <h3>どちらを使うといいか</h3>
          <v-data-table :headers="headers" :items="whichtouse" :items-per-page="5" class="elevation-1"></v-data-table>
        </div>
      </v-container>
    </v-main>
  </v-app>
  <!-- <v-data-table
    :headers="headers"
    :items="whichtouse"
    :items-per-page="5"
    class="elevation-1"
  ></v-data-table> -->
</template>

<script>
  export default {
    data () {
      return {
        height: 6,
        maxNumber: 5,
        floorNum: 1,
        waitingUp: 130,
        waitingDown: 20,
        upPersons: 5,
        downPersons: 1,
        headers: [
          { text: '1階', value: 'one' },
          { text: '2階', value: 'two' },
          { text: '3階', value: 'three' },
          { text: '4階', value: 'four' },
          { text: '5階', value: 'five' },
          { text: '6階', value: 'six' },
          { text: '7階', value: 'seven' },
        ],
        whichtouse: [
          {
            one: 'エスカレーター',
            two: 'ここ',
            three: 'エスカレーター',
            four: 'エスカレーター',
            five: 'エスカレーター',
            six: 'エレベーター',
            seven: 'エレベーター'
          },
        ],
      }
    },
    computed: {
      threshold: function () {
        return this.maxNumber - 2;
      },
      isCrowdedUp: function () {
        return this.upPersons >= this.threshold;
      },
      isCrowdedDown: function () {
        return this.downPersons >= this.threshold;
      },
      congestedStateUp: function () {
        return this.upPersons >= this.threshold ? "混んでいる" : "空いている";
      },
      congestedStateDown: function () {
        return this.downPersons >= this.threshold ? "混んでいる" : "空いている";
      }
    },
    mounted: function() {
      this.$vuetify.application.bottom = 0;
      // 1秒ごとにhelloをコンソールに出す処理を書く
      this.floorNum = this.$route.params.floorNum;
      const cb = () => {
        fetch(`/api/floors/${this.floorNum}`)
          .then(response => {
            console.log(response.status); 
            // エラーレスポンスが返されたことを検知する
            if (!response.ok) {
              console.error("エラーレスポンス", response);
              return;
            }
            response.json()
              .then(resJson => {
                console.log(resJson);
                this.waitingUp = resJson.waiting_up;
                this.waitingDown = resJson.waiting_down;
                this.upPersons = resJson.up_persons;
                this.downPersons = resJson.down_persons;
              });
          }).catch(error => {
            console.error(error);
          });
      };
      window.setInterval(cb, 1000);
    },
  }
</script>

<style scoped>
.body {
  height: 100%;
}
.main {
  /* min-height: calc(100% - 56px);
  height: calc(100% - 56px);
  max-height: calc(100% - 56px); */
  position: absolute;
  width: 100%;
  height: 100%;
  max-height: 100%;
}
.container {
  display: flex;
  flex-direction: column;
  height: 100%;
  /* max-height: calc(100% - 56px); */
}
.sec1 {
  flex: 1;
}
.sec2 {
  /* flex: 1; */
  height: 200px;
  min-height: 200px;
  bottom: 0;
}
.crowded {
  color: red;
}
</style>