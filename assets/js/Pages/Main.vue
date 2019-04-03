<template>
  <Layout>
    <inertia-link href="/second">Second</inertia-link>
    <p>this would be awesome as ehll!!</p>
    <button class="button">Get started</button>
  </Layout>
</template>

<script>
import { InertiaLink } from "inertia-vue";
import Layout from "@/Components/Layout.vue";

export default {
  components: { Layout, InertiaLink }
};
</script>

