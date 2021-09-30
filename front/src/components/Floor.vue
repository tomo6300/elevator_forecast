<template>
 <div>
    <table id="cal-main">
      <thead>
        <th v-for="floorname in floors" :key="floorname">{{ floorname}}</th>
      </thead>
      <tbody>
        <tr class="cal-day" v-for="(weekData, index) in floorData" :key="index">
          <td v-for="(floorNum, index) in floorData" :key="index" >
            <span v-if="isElevator(floorNum)">
              <strong>today</strong>
            </span>
            <span v-else>{{ dayNum }}</span>
          </td>
        </tr>
      </tbody>
    </table>

 </div>
</template>