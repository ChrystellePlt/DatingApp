<template>
  <div>
    <h1>Welcome to the homepage</h1>
    <button
      class="btn btn-primary btn-margin"
      @click="privateMessage()">
      Call Private
    </button>
    <button
      class="btn btn-primary btn-margin"
      @click="logout()">
      Log Out
    </button>
  </div>
</template>

<script>
  export default {
    name: 'homepage',
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
      handleAuthentication() {
        auth.handleAuthentication();
      },
      logout() {
        auth.logout();
      },
      privateMessage() {
        const url = `${API_URL}/api/private/`;
        return axios.get(url, { headers: { Authorization: `Bearer ${AuthService.getAuthToken()}` } }).then((response) => {
          console.log(response.data);
          this.message = response.data || '';
        });
      },
    },
  }
</script>
