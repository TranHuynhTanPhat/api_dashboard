<template>
  <Transition name="modal">
    <div v-if="show" class="modal-mask">
      <div class="modal-wrapper">
        <div class="modal-container">
          <div class="modal-header">
            <label for="title" class="label-header">Register account</label>
          </div>

          <div class="modal-body">
            <label for="email" class="label">Email:</label>
            <input type="email" v-model="email" placeholder="Enter email" />
            <label for="password" class="label">Password:</label>
            <input
              type="password"
              v-model="password"
              placeholder="Enter password"
            />
            <label for="status" class="label">Status:</label>
            <input type="number" v-model="status" :placeholder="this.status" />
            <span id="messError"></span>
          </div>

          <div class="modal-footer-alert">
            <slot name="footer-alert">
              <button class="modal-right-button" @click="handleAdd">Add</button>
              <button class="modal-left-button" @click="handleCancel">
                Cancel
              </button>
            </slot>
          </div>
        </div>
      </div>
    </div>
  </Transition>
</template>
<script>
import axios from "axios";
import { REGISTER } from "@/axios";
export default {
  name: "AlertDialog",
  data() {
    return {
      email: "",
      password: "",
      status: 0,
    };
  },
  props: {
    show: Boolean,
  },
  methods: {
    async handleAdd() {
      if (this.email != "" && this.password != "") {
        await axios
          .post(REGISTER, {
            email: this.email,
            password: this.password,
            status: this.status,
          })
          .then((res) => {
            if (res.status == 200) {
              this.$emit("load-user");
              this.$emit("close");
            }
          })
          .catch((ex) => {
            if (ex.response.status == 409) {
              document.getElementById("messError").innerHTML =
                "Email already existed!";
            }
          });
      } else if (this.email == "") {
        document.getElementById("messError").innerHTML = "Enter email please!";
      } else if (this.password == "") {
        document.getElementById("messError").innerHTML =
          "Enter password please!";
      }
    },
    handleCancel() {
      this.$emit("close");
    },
  },
};
</script>

<style>
.modal-mask {
  position: fixed;
  z-index: 9998;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.5);
  display: table;
  transition: opacity 0.3s ease;

  padding: 20px;
}

.modal-wrapper {
  display: table-cell;
  vertical-align: middle;
}

.modal-container {
  width: 400px;
  height: auto;
  margin: 0px auto;
  padding: 50px 30px;
  background-color: #fff;
  border-radius: 15px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.33);
  transition: all 0.3s ease;
}

.modal-header .label-header {
  margin-top: 0;
  color: #3d5554;
  font-size: 18px;
  font-weight: 500;
}

.modal-body {
  margin: 20px 0;
}

.modal-body .label {
  margin-top: 0;
  color: #3d5554;
  font-size: 14px;
  font-weight: 500;
}

.modal-body input {
  width: 100%;
  margin-top: 5px;
  margin-bottom: 10px;
  padding: 10px 10px;
  border-radius: 10px;
  box-shadow: rgb(204, 219, 232) 3px 3px 6px 0px inset,
    rgba(255, 255, 255, 0.5) -3px -3px 6px 1px inset;
}

.modal-body #messError {
  color: red;
}

input:hover {
  border-color: #3d5554;
}

.modal-right-button {
  float: right;
  border-radius: 10px;
  background-color: rgb(0, 100, 154);
  padding: 10px 20px;

  color: #fff;
}

.modal-left-button {
  float: left;
  border-radius: 10px;
  background-color: rgba(0, 100, 154, 0.194);
  padding: 10px 20px;

  color: #000;
}

/*
 * The following styles are auto-applied to elements with
 * transition="modal" when their visibility is toggled
 * by Vue.js.
 *
 * You can easily play with the modal transition by editing
 * these styles.
 */

.modal-enter-from {
  opacity: 0;
}

.modal-leave-to {
  opacity: 0;
}

.modal-enter-from .modal-container,
.modal-leave-to .modal-container {
  -webkit-transform: scale(1.1);
  transform: scale(1.1);
}
</style>