<template>
  <div class="home">
  <div>{{ headingList }}</div>
    <el-row>
        <table>
          <tr v-for="item in headingList">
            {{ item.fields.heading_text }}
          </tr>
        </table>
    </el-row>
  </div>

</template>

<script>
export default {
  name: 'home',
  data () {
    return {
      headingList: []
    }
  },
  mounted: function () {
    this.showHeadings ()
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
