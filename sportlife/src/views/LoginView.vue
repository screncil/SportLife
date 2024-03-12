<script>
import axios from "axios";
import router from "@/router/index.js";
import VueCookie from "vue-cookie";
export default {
  data() {
    return {
      username: "",
      password: "",
      error_: "",
      error_bool: false,
      password_visible: true,
    }
  },
  computed: {
    passwordTextVisible: function() {
      if (this.password_visible) {
        return "Показать пароль"
      }
      return "Скрыть пароль"
    }
  },
  methods: {
    login() {
      axios.post("http://localhost:8080/api/auth", {"username": this.username, "password": this.password}).then((response) => {
        if (response.data.status === "OK") {
          router.push("/")
          VueCookie.set("session_id", response.data.session_id, "1h")
        }
        else if (response.data.status === "Error") {
          this.error_bool = true
          this.error_ = response.data.msg
        }
      })
    }
  }
}
</script>

<template>
<div class="main_login">
  <div class="inputs">
    <label for="username">Имя администратора</label>
    <input id="username" class="input_login" v-model="username" type="text" required placeholder="Имя">
    <div class="test">
      <label for="password">Пароль</label>
      <input id="password" class="input_login" v-model="password" :type="password_visible ? 'password' : 'text'" required placeholder="Пароль">
      <button class="passwordVisiblee" @click="password_visible = !password_visible" type="button">{{ passwordTextVisible }}</button>
    </div>
    <button @click="login()" class="btn_login">Авторизоватся</button>
    <div class="error" v-if="error_bool === true">
      <p>{{ error_ }}</p>
    </div>
  </div>
</div>
</template>

<style scoped>

.error {
  background-color: rgba(255,0,0,0.7);
  margin: 10px;
  height: 60px;
  text-align: center;
  border: 1px red solid;
  border-radius: 10px;
  font-size: 17px;
  font-weight: bold;
}

.test {
  position: relative;
  display: inline-block;
}

.test button {
  background-color: transparent;
  border: 0;
}

.passwordVisiblee:hover {
  color: gray;
}

.input_login {
  width: 100%;
  height: 40px;
  border: 1px black solid;
  border-radius: 5px;
  font-size: 15px;
  text-indent: 8px;
  margin-top: 10px;
}

.inputs {
  font-family: "Open Sans", sans-serif;
  margin: auto;
  top: 0;
  margin-top: 20px;
  width: 1000px;
  display: flex;
  flex-direction: column;
}

.btn_login {
  width: 100%;
  margin-top: 15px;
  height: 50px;
  border: 1px black solid;
  border-radius: 10px;
  background-color: black;
  color: white;
  font-family: "Open Sans", sans-serif;
  font-size: 15px;
}

.btn_login:hover {
  background-color: white;
  color: black;
  cursor: pointer;
}
</style>