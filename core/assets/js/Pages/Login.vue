<template>
  <Layout>
    <h2 class="page-title">Login</h2>
    <div class="flex flex-col items-start">
      <input
        class="border-4 border-purple-700 rounded w-2/3 text-l p-2 my-2"
        type="text"
        v-model="username"
        placeholder="your_username"
      >
      <input
        class="border-4 border-purple-700 rounded w-2/3 text-l p-2 my-2"
        type="password"
        v-model="password"
        placeholder="mysecretsauce"
      >
      <button
        @click="login"
        class="bg-green-500 hover:bg-green-400 focus:bg-green-600 rounded mt-2 px-3 py-1 text-white font-bold text-l"
        type="button"
      >Login</button>
    </div>
  </Layout>
</template>

<script>
import Layout from "@/Components/Layout";
import Inertia from "inertia";
import axios from "axios";

export default {
  props: ["csrf_token", "error"],
  data() {
    return {
      username: "",
      password: ""
    };
  },
  components: {
    Layout
  },
  methods: {
    login() {
      Inertia.post("/login/", {
        username: this.username,
        password: this.password
      })
    }
  }
};
</script>

