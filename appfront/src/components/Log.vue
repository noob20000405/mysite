<template>
  <div class="log">
    <el-row>
      <div>
        that's log.
      </div>
      <div v-for="item in logList">
        {{ item.fields.title_text }}
        {{ item.fields.content_text }}
      </div>
    </el-row>
  </div>
</template>

<script>
export default {
  name: 'log',
  data () {
    return {
      logList: [],
      id: 0,
      url: ''
    }
  },
  mounted: function () {
    this.id = this.$route.params.id,
    this.url = 'http://127.0.0.1:8000/api/show_contents/' + this.id,
    this.showlogs ()
  },
  methods: {
    showlogs() {
      this.$axios.get(this.url)
        .then((res) => {
          var res = res.data;
          console.log(res)
          if (res.error_num == 0) {
            this.logList = res['list']
          } else {
            this.$message.error('failed')
            console.log(res['msg'])
          }
        })
    }
  }
}
</script>
/* url : http://127.0.0.1:8080/#/log */
