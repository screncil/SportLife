<script>
import VueCookie from "vue-cookie";
import router from "@/router/index.js";
import axios from "axios";

export default {
  created() {
    this.getClients()
  },
  data() {
    return {
      search_input: "",
      filter_value: null,
      clients: null,
      filter_selected: false,
      count_clients_: ""
    }
  },
  methods: {
    checkLogged() {
      if (VueCookie.get("session_id") !== null) {
        return true
      } else {
        return false
      }
    },
    searchClient() {
      axios
          .get("http://localhost:8080/api/clients?name=" + this.search_input)
          .then((response) => {
            this.clients = response.data.clients
            this.count_clients_ = response.data.count_clients
          })
    },
    setFilters() {

    },
    addClient() {
      router.push("/addclient")
    },
    getClients() {
      axios
        .get("http://localhost:8080/api/clients")
        .then((response) => {
          this.clients = response.data.clients
          this.count_clients_ = response.data.count_clients
        })
    },
    lengthClients() {
      if (this.clients.length > 0) {
        return true
      } else {
        return false
      }
    }
  }
}
</script>

<template>
<div class="cont">
  <div v-if="checkLogged()" class="top-menu">
    <button @click="addClient()" class="addclient-btn" type="button">Добавить клиента</button>
    <img @click="searchClient()" class="searchbtn" v-if="search_input.length > 0" src="../assets/imgs/search_black.svg" width="30" height="30" alt="">
    <img class="disabled-searchbtn" v-else src="../assets/imgs/search_gray.webp" width="30" height="30">
    <div class="clients-box">
      <input v-model="search_input" class="searchclient_input" type="text" placeholder="Поиск по ФИО">
      <div class="clients" v-if="clients.length > 0">
        <p class="count-client">Найден(-о) {{ count_clients_ }} клиент(-ов)</p>
        <div v-for="client in clients" class="client">
          <p class="fio">{{ client.fio }}</p>
          <div class="info">
            <p class="birthday">Дата рождения: {{ client.birthday }}</p>
            <p class="subs">Абонимент: {{ client.sub_type }}</p>
            <p class="street">Место проживания: {{ client.street }}</p>
            <p class="phone">Номер телефона: {{ client.phone }}</p>
          </div>
        </div>
      </div>
      <div class="clients" v-else>
        <p class="records-none">Записей не найдено</p>
        <div class="test">
          <button @click="getClients()" class="load-all-clients">Загрузить всех клиентов</button>
      </div>
      </div>
    </div>
    <div class="filters">
      <p>Фильтры</p>
      <div class="filterss">
        <div class="filter-btns">
          <input @click="filter_selected = true" v-model="filter_value" name="filter" type="radio" id="for-subscription" value="for-sub">
          <label for="for-subscription">По абонименту</label>
        </div>
        <div class="filter-btn">
          <input @click="filter_selected = true" v-model="filter_value" name="filter" type="radio" id="subscription-end" value="sub-end">
          <label for="for-subscription">По окончанию абонимента</label>
        </div>
        <button v-if="filter_selected === true" @click="setFilters()" class="confirm-filters">Применить</button>
        <button v-else class="confirm-filters-disabled">Применить</button>
      </div>
    </div>
  </div>
  <p v-else>Нету доступа</p>

</div>
</template>

<style scoped>

.count-client {
  font-weight: bold;
  font-family: "Open Sans", sans-serif;
  margin-left: 10px;
}

.load-all-clients {
  border-radius: 5px;
  border: none;
  width: 90%;
  height: 40px;
  margin-left: 50px;
  background-color: black;
  color: white;
}

.load-all-clients:hover {
  border: 1px black solid;
  background-color: transparent;
  color: black;
  cursor: pointer;
}

.records-none {
  text-align: center;
  font-family: "Open Sans", sans-serif;
  font-weight: bold;
}

.info {
  display: flex;
  flex-direction: row;
}

.street {
  font-size: 10px;
  padding-left: 10px;
  color: gray;
}

.subs {
  font-size: 10px;
  padding-left: 15px;
  color: gray;
}

.birthday {
  font-size: 10px;
  padding-left: 15px;
  padding-bottom: 10px;
  color: gray;
}

.phone {
  font-size: 10px;
  padding-left: 10px;
  color: gray;
}

.fio {
  margin: 10px;
}

.client {
  flex-direction: column;
  display: flex;
  width: 890px;
  height: 70px;
  background-color: rgba(0,0,0,.1);
  border-radius: 5px;
  margin-top: 10px;
  margin-bottom: 10px;
  font-family: "Open Sans", sans-serif;
}

.client:hover {
  background-color: rgba(0,0,0,.2);
}

.clients {
  margin-left: 10px;
  background-color: rgba(220,220,220,1);
  margin-top: 20px;
  border-radius: 10px;
  height: auto;
  width: 890px;
  padding: 10px;
}

.confirm-filters-disabled {
  border: none;
  width: 270px;
  height: 40px;
  background-color: rgba(220,220,220,.5);
  margin-top: 20px;
  border-radius: 5px;
  color: gray;
  font-size: 15px;
}

.confirm-filters {
  width: 270px;
  height: 40px;
  border: 1px black solid;
  border-radius: 5px;
  background-color: black;
  color: white;
  font-size: 15px;
  margin-top: 20px;
}

.confirm-filters:hover {
  background-color: transparent;
  color: black;
  cursor: pointer;
}

.filterss {
  margin-top: 30px;
  margin-bottom: 30px;
  margin-left: 20px;
}

.filters {
  background-color: transparent;
  border: 1px black solid;
  border-radius: 10px;
  width: 20%;
  margin: 20px;
  height: auto;
  position: absolute;
  right: 0;
  font-family: "Open Sans", sans-serif;
}

.filters p {
  font-size: 20px;
  margin: auto;
  margin-left: 35%;
  margin-top: 30px;
  font-weight: bold;
}

.searchbtn, .disabled-searchbtn {
  margin-top: 32px;
}

.searchbtn:hover {
  cursor: pointer;
}

.top-menu {
  height: 100px;
  display: flex;
}

.top-menu .searchclient_input {
  height: 35px;
  border: 1px black solid;
  border-radius: 10px;
  font-size: 14px;
  text-indent: 8px;
  width: 900px;
  margin-left: 10px;
  margin-top: 30px;
  color: gray;
}

.top-menu .addclient-btn {
  border: none;
  background-color: black;
  border-radius: 10px;
  color: white;
  font-size: 17px;
  width: 200px;
  height: 70px;
  margin: 15px;
}

.top-menu .addclient-btn:hover {
  color: black;
  cursor: pointer;
  background-color: white;
  border: 1px black solid;
}
</style>