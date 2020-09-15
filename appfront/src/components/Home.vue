<template>
  <div class="home" :key="time">
  Home :
  <!--<div>{{ headingList }}</div>-->
    <el-row>
      <div v-for="(item, index) in headingList">
        <div @click="re(item.pk)">{{ item.fields.heading_text }}, pk : {{ item.pk }}</div>

        <!--<router-link :to="{path:item.pk}" :key="item.pk" tag="a">
          link
        </router-link>-->

      </div>
    </el-row>
    <router-view></router-view>
  </div>

</template>

<script>
export default {
  name: 'home',
  data () {
    return {
      headingList: [],
      time: 1
    }
  },
  mounted: function () {
    this.showHeadings ()
  },
  watch: {
    '$route'(){
      this.time = new Date().getTime()
    }
  },
  methods: {
    showHeadings() {
      this.$axios.get('http://127.0.0.1:8000/api/show_headings')
        .then((res) => {
          var res = res.data;
          console.log(res)
          if (res.error_num == 0) {
            this.headingList = res['list']
          } else {
            this.$message.error('failed')
            console.log(res['msg'])
          }
        })
    },
    re(param) {
      var p = param.toString()
      this.$router.push({path: p})
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1, h2 {
  font-weight: normal;
}

ul {
  list-style-type: none;
  padding: 0;
}

li {
  display: inline-block;
  margin: 0 10px;
}

a {
  color: #42b983;
}
</style>
