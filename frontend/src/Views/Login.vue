<template>
  <button
    class="btn btn-primary btn-margin"
    v-if="!authenticated"
    @click="login()">
    Log In
  </button>
</template>

<script>

  export default {
    name: 'login',
    data() {
      this.handleAuthentication();
      this.authenticated = false;

      auth.authNotifier.on('authChange', (authState) => {
        this.authenticated = authState.authenticated;
      });

      return {
        authenticated: false,
      };
    },
    methods: {
      // this method calls the AuthService login() method
      login() {
        auth.login();
      },
      handleAuthentication() {
        auth.handleAuthentication();
      },
    },
  }

</script>
