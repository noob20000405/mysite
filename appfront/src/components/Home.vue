<template>
  <div class="home" :key="time">

    <nav class="navbar navbar-default" role="navigation">
        <div class="container-fluid">
        <div class="navbar-header">
            <a class="navbar-brand" href="#">Log</a>
        </div>
        <div>
            <ul class="nav navbar-nav navbar-right" v-for="(item, index) in headingList">
                <li ><div class="nav-item" @click="re(item.pk)">{{ item.fields.heading_text }}</div></li>
            </ul>
        </div>
        </div>
    </nav>

    <div class="content">
      <el-row>
        <el-col :span="8" :offset="5">
          <div class="left-card">
            <router-view></router-view>
          </div>
        </el-col>
        <el-col :span="4" :offset="1">
          <el-card>Personal infos</el-card>
        </el-col>
      </el-row>
    </div>

    <footer :style="'position: absolute;top: ' + screenHeight + 'px;'">{{ copyright }}</footer>

  </div>
</template>

<script>
import Markdown from 'vue-meditor';
export default {
  name: 'home',
  data () {
    return {
      headingList: [],
      time: 1,
      screenHeight: document.documentElement.clientHeight - 50,
      copyright: '©2020 Renwen'
    }
  },
  components: {
    Markdown
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
      this.$router.push({path: '/home/' + p})
    },
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

/* navbar */
.navbar-default .navbar-brand {
  color: #f2f2f2;
}
.navbar {
  background-color: #65758a;
  border: 0ch;
  border-radius: 0ch;
  font-size: 1.25em;
  color: #f2f2f2;
}

.nav-item {
  height: 50px;
  display: inline-block;
  font-size: 1.25em;
  color: #f2f2f2;
  padding: 15px 15px;
  transition: .4s;
}

.nav-item:hover {
  padding-top: 10px;
  padding-bottom: 20px;
  cursor: pointer;
}

/* content */
.content {
  margin-top: 40px;
}

/* left card */
.left-card {
  border: 1px solid #EBEEF5;
  border-radius: 3px;
}

.markdown-content {
  display: none;
}

/* footer */
footer {
  width: 100%;
  text-align: center;
}
</style>