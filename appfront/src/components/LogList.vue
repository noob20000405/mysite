<template>
  <div class="loglist">
    <el-row>
      <div>
        Loglist :
      </div>
      <div v-for="item in logList">
        <div @click="showContent(item.pk)">{{ item.fields.title_text }}</div>
        <div v-if="item.pk == content_pk">{{ item.fields.content_text }}</div>
      </div>
    </el-row>
  </div>
</template>

<script>
export default {
  name: 'loglist',
  data () {
    return {
      logList: [],
      id: 0,
      url: '',
      content_pk: 0
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
    },
    showContent(pk) {
      this.content_pk = pk
    }
  }
}
</script>
