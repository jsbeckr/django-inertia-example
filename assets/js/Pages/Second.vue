<template>
  <Layout>
    <inertia-link href="/">Home</inertia-link>
    <ul>
      <li>this</li>
      <li>is</li>
      <li>noice</li>
      <li>TEST: {{ test }}</li>
    </ul>
  </Layout>
</template>

<script>
import { InertiaLink } from "inertia-vue";
import Layout from "@/Components/Layout.vue";

export default {
  props: ['test'],
  components: { Layout, InertiaLink }
};
</script>

