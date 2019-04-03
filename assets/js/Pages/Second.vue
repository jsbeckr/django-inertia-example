<template>
  <Layout>
    <inertia-link href="/">Home</inertia-link>
    <h2>{{contact.name}}, {{contact.first_name}}</h2>
    <p>Age: {{contact.age}}</p>
  </Layout>
</template>

<script>
import { InertiaLink } from "inertia-vue";
import Layout from "@/Components/Layout.vue";

export default {
  props: ['contact'],
  components: { Layout, InertiaLink }
};
</script>

