<template>
  <v-app class="body">
    <v-app-bar app>
      2階
    </v-app-bar>
    <v-main class="main">
      <v-container class="container">
        <div class="sec1">
          <div>
            <h3>上り</h3>
            <p>待ち時間：約{{waiting_up}}秒</p>
            <p>予想混雑度：混んでいる（約{{up_persons}}人）</p>
          </div>
          <div>
            <h3>下り</h3>
            <p>待ち時間：約{{waiting_down}}秒</p>
            <p>予想混雑度：空いている（約{{down_persons}}人）</p>
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
        waiting_up: 130,
        waiting_down: 20,
        up_persons: 5,
        down_persons: 1,
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
    mounted: function() {
      this.$vuetify.application.bottom = 0;
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
</style>