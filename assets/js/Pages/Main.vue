<template>
  <Layout>
    <h2>Contacts</h2>
    <ul>
      <li :key="contact.id" v-for="contact in contact_list">
        <inertia-link :href="'/second/' + contact.id">
          {{contact.name}}
        </inertia-link>
        </li>
    </ul>
  </Layout>
</template>

<script>
import { InertiaLink } from "inertia-vue";
import Layout from "@/Components/Layout.vue";

export default {
  props: ["contact_list"],
  components: { Layout, InertiaLink }
};
</script>

