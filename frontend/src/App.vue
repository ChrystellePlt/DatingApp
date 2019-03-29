/* eslint-disable */

<template>
  <div v-if="!authenticated">
    <loginPage />
  </div>
  <div v-else>
    <homePage />
  </div>
</template>

<script>
import axios from 'axios';
import AuthService from './auth/AuthService';

import LoginPage from './Views/Login.vue';
import HomePage from './Views/Home.vue';

const API_URL = 'http://localhost:8000';
const auth = new AuthService();

export default {
  name: 'app',
  components: {
    LoginPage,
    HomePage,
  }
};

</script>
