<script>
import axios from "axios";
import VueCookie from "vue-cookie";
export default {
  created() {
    this.checkUser()
  },
  data() {
    return {
      username: ""
    }
  },
  methods: {
    checkUser() {
      if (VueCookie.get("session_id") !== null) {
        axios
            .get("http://localhost:8080/api/user?hash="+VueCookie.get("session_id"))
            .then((response) => {
              this.username = response.data.info.username
            })
      }
    }
  }
}
</script>

<template>
<header>
  <div class="container">
    <p class="title">SPORT LIFE</p>
    <p>|</p>
    <div v-if="username !== ''" class="button-header">
      <p class="login"><RouterLink class="textdecoration-none" to="/profile">Администратор: {{ username }}</RouterLink></p>
      <RouterLink class="textdecoration-none btn-header" to="/clients">Клиенты</RouterLink>
    </div>
    <p v-else><RouterLink class="login" to="/login">Авторизоваться</RouterLink></p>
  </div>
</header>
  <RouterView/>
</template>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Open+Sans:ital,wght@0,300..800;1,300..800&display=swap');

.exitbtn {
  border: none;
  background-color: black;
  width: 130px;
  height: 35px;
  margin-left: 20px;
  border-radius: 5px;
  color: white;
  font-size: 13px;
}

.exitbtn:hover {
  border: 1px black solid;
  background-color: transparent;
  color: black;
  cursor: pointer;
}

.textdecoration-none {
  text-decoration: none;
  color: black;
}

.textdecoration-none:hover {
  color: gray;
}

.login {
  text-decoration: none;
  color: black;
}

.login:hover {
  color: gray;
}

.title {
  font-weight: bold;
}

.container {
  width: 100%;
  height: 60px;
  font-family: "Open Sans", sans-serif;
  border: 1px black solid;
  border-radius: 15px;
  display: flex;
}

p {
  display: inline-block;
  margin-left: 15px;
}

.btn-header {
  padding-left: 30px;
}
</style>
