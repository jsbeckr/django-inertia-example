import Inertia from "inertia-vue";
import Vue from "vue";
import axios from "axios";

axios.defaults.xsrfCookieName = "csrftoken";
axios.defaults.xsrfHeaderName = "X-CSRFToken";

Vue.config.productionTip = false;

Vue.use(Inertia)

const app = document.getElementById("app");
// we are getting the initialPage from a rendered json_script
const page = JSON.parse(document.getElementById("page").textContent);

new Vue({
  render: h =>
    h(Inertia, {
      props: {
        initialPage: page,
        resolveComponent: name =>
          import(`@/Pages/${name}`).then(module => module.default)
      }
    })
}).$mount(app);
