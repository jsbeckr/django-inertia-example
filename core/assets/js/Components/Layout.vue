<template>
  <div class="h-screen flex flex-col">
    <div class="px-8 py-6 mb-8 bg-purple-800 text-white flex items-center justify-between">
      <h1>
        <inertia-link class="text-4xl font-bold" href="/">{{page.props.shared.title}}</inertia-link>
      </h1>
      <p
        v-if="page.props.shared.user.email"
        class="font-medium text-xl font-bold px-3 py-2 rounded hover:bg-purple-700 focus:bg-purple-900"
      >
        <inertia-link href="#">Logout</inertia-link>
      </p>
      <inertia-link
        v-else
        class="font-medium text-xl font-bold px-3 py-2 rounded hover:bg-purple-700 focus:bg-purple-900"
        href="#"
      >Login</inertia-link>
    </div>
    <div class="container mx-auto bg-white rounded p-8 shadow-md w-full sm:w-2/3">
      <slot></slot>
    </div>
    <footer class="bg-orange-500 text-white flex justify-center items-center h-20 mt-auto">
      <p class="text-xl">Made with 🧙‍♂️ in 🇩🇪</p>
    </footer>
  </div>
</template>

<script>
import { InertiaLink } from "inertia-vue";

export default {
  components: {
    InertiaLink
  },
  props: ["shared"],
  inject: ["page"]
};
</script>

