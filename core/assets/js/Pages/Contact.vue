<template>
  <Layout>
    <inertia-link href="/">Home</inertia-link>
    <h2 class="mb-4">{{contact.name}}, {{contact.first_name}}</h2>
    <p>Age: {{contact.age}}</p>
    <p>Test: {{test}}</p>
  </Layout>
</template>

<script>
import { InertiaLink } from "inertia-vue";
import Layout from "@/Components/Layout";

export default {
  props: ['contact', 'test'],
  components: { Layout, InertiaLink }
};
</script>

