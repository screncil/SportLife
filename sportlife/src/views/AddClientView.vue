<script>
import axios from "axios";
import VueCookie from "vue-cookie";
import router from "@/router/index.js";

export default {
  data() {
    return {
      fio_client: "",
      phone: "",
      street: "",
      subs_type: null,
      sub_seller_hash: VueCookie.get("session_id"),
      birthday: "",
    }
  },
  methods: {
    addClient() {
      axios
          .post("http://localhost:8080/api/addclient", {"fio": this.fio_client, "phone": this.phone, "street": this.street, "sub_type": parseInt(this.subs_type), "seller_hash": this.sub_seller_hash, "birthday": this.birthday})
          .then((response) => {
            if (response.data.status === "OK") {
              router.push("/clients")
            } else {
              alert("Клиент не добавлен, посмотрите в консоль для уточнения почему")
            }
          })

    }
  }
}
</script>

<template>
<div class="main_login">
  <div class="inputs">
    <label for="username">ФИО клиента</label>
    <input id="username" class="input_login" v-model="fio_client" type="text" required placeholder="ФИО">
    <div class="test">
      <label for="phone">Номер телефона</label>
      <input type="text" id="phone" class="input_login" v-model="phone" required placeholder="Телефон">
    </div>
    <div class="test">
      <label for="street">Место проживания</label>
      <input class="input_login" id="street" v-model="street" type="text" placeholder="Адресс">
    </div>
    <div class="test">
      <label for="subs">Выбор абонимента</label>
      <select v-model="subs_type" class="input_login" id="subs" required>
        <option selected disabled="disabled">Выберите абонимент</option>
        <option value="1">Абонимент на 1 месяц</option>
        <option value="3">Абонимент на 3 месяца</option>
        <option value="6">Абонимент на 6 месяцев</option>
        <option value="12">Абонимет на 1 год</option>
      </select>
    </div>
    <div class="test">
      <label for="birthday">Дата рождения</label>
      <input v-model="birthday" id="birthday" type="date" class="input_login" required>
    </div>
    <button @click="addClient()" class="btn_login">Добавить клиента</button>
  </div>
</div>
</template>

<style scoped>


.test {
  position: relative;
  display: inline-block;
  margin-top: 10px;
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