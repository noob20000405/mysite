<template>
  <div class="loglist">
    
    <el-row>
      <div>
      </div>
      <div v-for="item in logList">
        <div @click="showContent(item.pk, item.fields.content_text)" class="title">{{ item.fields.title_text }}
          <span class="time">{{ item.fields.created_time }}</span>
        </div>
        <div v-if="item.pk == content_pk" class="text" :style="'height: ' + textBlockHeight + 'px'">
            <div v-html="compiledMarkdown" class="mkd"></div>
        </div>
      </div>
    </el-row>
    
  </div>
</template>

<script>
function escape2Html(str) {
        var arrEntities={'lt':'<','gt':'>','nbsp':' ','amp':'&','quot':'"'};
        return str.replace(/&(lt|gt|nbsp|amp|quot);/ig,function(all,t){
            return arrEntities[t];
        });
}
export default {
  name: 'loglist',
  data () {
    return {
      logList: [],
      id: 0,
      url: '',
      content_pk: 0,
      content: 'empty',
      compiledMarkdown: '',
      textBlockHeight: document.documentElement.clientHeight - 300
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
    showContent(pk, text) {
      this.content_pk = pk
      this.content = text
      this.compiledMarkdown = escape2Html(marked(this.content, { sanitize: true }))
      this.compiledMarkdown = this.compiledMarkdown.replace(/\\n/g, '<br>')
    }
  }
}
</script>   

<style scoped>
  .title {
    padding: 6px 20px;
    font-size: 1.5em;
    transition: .4s;
    text-align:left;
  }
  .title:hover {
    background-color: #bbc3cd;
    cursor: pointer;
  }

  .text {
    padding: 20px 10px;
    overflow-y: scroll;
  }
  .time {
    position: absolute;
    right: 20px;
    font-size: 1em;
    color: #45505e;
  }  
</style>