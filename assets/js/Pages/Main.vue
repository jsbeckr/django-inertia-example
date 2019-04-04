<template>
  <Layout>
    <h2 class="mb-4">Contacts</h2>
    <p>CSRF: {{csrf}}</p>
    <ul>
      <li :key="contact.id" v-for="contact in contact_list">
        <inertia-link :href="'/second/' + contact.id">
          {{contact.name}}.class
        </inertia-link>
        <span> - </span>
        <inertia-link :href="'/func/' + contact.id">
          {{contact.name}}.function
        </inertia-link>
        </li>
    </ul>
  </Layout>
</template>

<script>
import { InertiaLink } from "inertia-vue";
import Layout from "@/Components/Layout";

export default {
  props: ["contact_list", "csrf"],
  components: { Layout, InertiaLink }
};
</script>

