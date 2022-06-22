<template>
  <div class="container">
      <vs-button color="success" type="gradient" @click="addAction" style="margin-bottom:10px;margin-right:20px;">Add action</vs-button>
      <vs-button color="danger" type="gradient" @click="commitActions" style="margin-bottom:10px">Commit actions</vs-button>

    <vs-row vs-justify="center" v-if="toggleModal" class="add-action-modal">
  <vs-col type="flex" vs-justify="center" vs-align="center" vs-w="6">
    <vs-card>
      <div slot="header">
        <vs-row vs-justify="flex-end" vs-align="center">
        <h3 style="margin-right: 380px;">
          Add action
        </h3>
          <vs-button type="gradient" color="danger" icon="close" @click="closeModal"></vs-button>
        </vs-row>
      </div>
      <vs-row >
        <vs-col vs-type="flex" vs-justify="center">
         <vs-input class="inputx" placeholder="title" :danger="danger" danger-text="Cannot be empty" v-model="newActionTitle"/>
         </vs-col>
         <vs-col vs-type="flex" vs-justify="center">
         <vs-input class="inputx" placeholder="description" :danger="danger" danger-text="Cannot be empty" v-model="newActionDescription"/>
         </vs-col>
         <!-- <vs-col vs-type="flex" vs-justify="center">
         <vs-input class="inputx" placeholder="deadline" :danger="danger" danger-text="Cannot be empty" v-model="newActionDeadline"/>
         </vs-col> -->
         <vs-col style="margin-top: 20px;">
          <vs-button type="gradient" color="success" @click="createActionInBacklog">Submit</vs-button>

         </vs-col>
      </vs-row>
      <!-- <div slot="footer">
        <vs-row vs-justify="flex-start">
          <vs-button color="primary" icon="turned_in_not"></vs-button>
          <vs-button color="rgb(230,230,230)" color-text="rgb(50,50,50)" icon="settings"></vs-button>
        </vs-row>
      </div> -->
    </vs-card>
  </vs-col>
</vs-row>
    <vs-row vs-type=flex>
      <vs-col vs-type="flex" class="container-action">
        
      <!-- <vs-col style="border: 1px solid black;" v-for="category in categories" :key="category.id"> -->
          <vs-col  vs-justify="center" style="border: 1px solid black;border-radius:15px;">
            <h3>Backlog:</h3>
            <vs-divider></vs-divider>
          <draggable class="draggable-list" :list="actions" group="actions" :emptyInsertThreshold="500">
              <transition-group>
              <vs-row vs-type="flex" vs-justify="center" style="width:80%; margin:0 auto" v-for="(action, i) in actions" :key="action.title">
                  <vs-col vs-align="center" vs-justify="center" class="actions-wrapper" style="border: 1px dotted gray">
                      <p class="action-title">{{action.title}}</p><vs-button color="danger" type="flat" icon="delete" @click="removeAction(actions, action.title, 'actions')"></vs-button>
                      <vs-divider></vs-divider>

                      <p class="action-description">{{action.description}}</p>
                      <vs-divider></vs-divider>

                      <p class="action-deadline">Deadline placeholder	📅</p>
                </vs-col>
              </vs-row>
          </transition-group>
          </draggable>
          </vs-col>
          <!-- </vs-col> -->
        </vs-col>
        <vs-col vs-type="flex" class="container-action">
          <vs-col style="border: 1px solid black; border-radius:15px;">
          <h3>Todo:</h3>
            <vs-divider></vs-divider>

          <draggable class="draggable-list" :list="todoActions" group="actions" :emptyInsertThreshold="500">
              <transition-group>
              <vs-row vs-type="flex" style="width:80%; margin:0 auto"  v-for="(action, i) in todoActions" :key="action.title">
                  <vs-col class="actions-wrapper" style="border: 1px dotted gray">
                      <p class="action-title">{{action.title}}</p><vs-button color="danger" type="flat" icon="delete" @click="removeAction(todoActions, action.title, 'todoActions')"></vs-button>
            <vs-divider></vs-divider>

                      <p class="action-description">{{action.description}}</p>
            <vs-divider></vs-divider>

                      <p class="action-deadline">Deadline placeholder	📅</p>
                </vs-col>
              </vs-row>
          </transition-group>
          </draggable>
          </vs-col>
        </vs-col>
        <vs-col vs-type="flex" class="container-action">
          <vs-col style="border: 1px solid black;border-radius:15px;">
          <h3>Almost there:</h3>
            <vs-divider></vs-divider>

          <draggable class="draggable-list" :list="almostThereActions" group="actions" :emptyInsertThreshold="500">
              <transition-group>
              <vs-row vs-type="flex" style="width:80%; margin:0 auto" v-for="(action, i) in almostThereActions" :key="action.title">
                  <vs-col class="actions-wrapper" style="border: 1px dotted gray">
                      <p class="action-title">{{action.title}}</p><vs-button color="danger" type="flat" icon="delete" @click="removeAction(almostThereActions, action.title, 'almostThereActions')"></vs-button>
            <vs-divider></vs-divider>

                      <p class="action-description">{{action.description}}</p>
            <vs-divider></vs-divider>

                      <p class="action-deadline">Deadline placeholder	📅</p>
                </vs-col>
              </vs-row>
          </transition-group>
          </draggable>
          </vs-col>
        </vs-col>
        <vs-col vs-type="flex" class="container-action">
          <vs-col style="border: 1px solid black;border-radius:15px;">
          <h3>Done:</h3>
            <vs-divider></vs-divider>

          <draggable class="draggable-list" :list="doneActions" group="actions" :emptyInsertThreshold="500">
              <transition-group>
              <vs-row vs-type="flex" style="width:80%; margin:0 auto" v-for="(action, i) in doneActions" :key="action.title">
                  <vs-col class="actions-wrapper" style="border: 1px dotted gray">
                      <p class="action-title">{{action.title}}</p><vs-button color="danger" type="flat" icon="delete" @click="removeAction(doneActions, action.title, 'doneActions')"></vs-button>
            <vs-divider></vs-divider>

                      <p class="action-description">{{action.description}}</p>
            <vs-divider></vs-divider>

                      <p class="action-deadline">Deadline placeholder	📅</p>
                </vs-col>
              </vs-row>
          </transition-group>
          </draggable>
          </vs-col>
        </vs-col>
        <vs-col vs-type="flex" class="container-action">
          <vs-col style="border: 1px solid black;border-radius:15px;">
          <h3>Review:</h3>
            <vs-divider></vs-divider>

          <draggable class="draggable-list" :list="reviewActions" group="actions" :emptyInsertThreshold="500">
              <transition-group>
              <vs-row vs-type="flex" style="width:80%; margin:0 auto" v-for="(action, i) in reviewActions" :key="action.title">
                  <vs-col class="actions-wrapper" style="border: 1px dotted gray">
                      <p class="action-title">{{action.title}}</p><vs-button color="danger" type="flat" icon="delete" @click="removeAction(reviewActions, action.title, 'reviewActions')"></vs-button>
            <vs-divider></vs-divider>

                      <p class="action-description">{{action.description}}</p>
            <vs-divider></vs-divider>

                      <p class="action-deadline">Deadline placeholder	📅</p>
                </vs-col>
              </vs-row>
          </transition-group>
          </draggable>
          </vs-col>
        </vs-col>
        <vs-col vs-type="flex" class="container-action">
          <vs-col style="border: 1px solid black;border-radius:15px;">
          <h3>Refactor:</h3>
            <vs-divider></vs-divider>

          <draggable class="draggable-list" :list="refactorActions" group="actions" :emptyInsertThreshold="500">
              <transition-group>
              <vs-row vs-type="flex" style="width:80%; margin:0 auto; margin-bottom:10px;" v-for="(action, i) in refactorActions" :key="action.title">
                  <vs-col class="actions-wrapper" style="border: 1px dotted gray; margin-bottom: 10px;">
                      <p class="action-title">{{action.title}}</p><vs-button color="danger" type="flat" icon="delete" @click="removeAction(refactorActions,action.title, 'refactorActions')"></vs-button>
            <vs-divider></vs-divider>

                      <p class="action-description">{{action.description}}</p>
            <vs-divider></vs-divider>

                      <p class="action-deadline">Deadline placeholder 📅</p>
                </vs-col>
              </vs-row>
          </transition-group>
          </draggable>
          </vs-col>
        </vs-col>
        </vs-col>
      </vs-col>
    </vs-row>
  </div>
</template>

<script>
import draggable from "vuedraggable";
import {
  getCategoriesByUser,
  getActionsByUser,
  createActionByUser,
} from "../api/shortcuts";
import { mapGetters, mapMutations } from "vuex";
export default {
  components: {
    draggable,
  },
  data() {
    return {
      categories: [],
      actions: this.$store.getters.backlog,
      filteredActions: [],
      todoActions: this.$store.getters.todoActions,
      almostThereActions: this.$store.getters.almostThere,
      doneActions: this.$store.getters.doneActions,
      reviewActions: this.$store.getters.reviewActions,
      refactorActions: this.$store.getters.refactorActionsArray,
      toggleModal: false,
      newActionTitle: null,
      newActionDescription: null,
      newActionDeadline: null,
      // nestedActions: [
      //   this.todoActions,
      //   this.almostThereActions,
      //   this.doneActions,
      //   this.reviewActions,
      //   this.refactorActions,
      // ],
      danger: false,
    };
  },
  methods: {
    loadCategories() {
      getCategoriesByUser(this.currentUser.username).then(
        (response) => (this.categories = response.data)
      );
    },
    loadActions() {
      getActionsByUser(this.currentUser.username).then(
        (response) => (this.actions = response.data)
      );
    },
    filterActionsByCategory(categoryId, actionsArray) {
      console.log(this.actions);
      let result = actionsArray.filter(
        (action) => action.category_id === categoryId
      );
      this.filteredActions = result;
      return result;
    },
    addAction() {
      this.toggleModal = !this.toggleModal;
    },
    closeModal() {
      this.toggleModal = false;
    },
    createActionInBacklog() {
      if (this.newActionTitle === null || this.newActionDescription === null) {
        this.danger = true;
      } else {
        this.actions.push({
          title: this.newActionTitle,
          description: this.newActionDescription,
        });
        createActionByUser({
          title: this.newActionTitle,
          description: this.newActionDescription,
          created_by: this.currentUser.username,
          category_id: 3,
        });
        this.toggleModal = !this.toggleModal;
      }
    },
    removeAction(array, elementTitle, arrayName) {
      console.log(elementTitle);
      array.splice(
        array.findIndex((elem) => elem.title === elementTitle),
        1
      );
      if (arrayName === "actions") {
        this.$store.commit("setBacklog", array);
        // delete in db in backend
      } else if (arrayName === "todoActions") {
        this.$store.commit("setTodoActions", array);
      } else if (arrayName === "almostThereActions") {
        this.$store.commit("setAlmostThereActions", array);
      } else if (arrayName === "doneActions") {
        this.$store.commit("setDoneActions", array);
      } else if (arrayName === "reviewActions") {
        this.$store.commit("setReviewActions", array);
      } else if (arrayName === "refactorActions") {
        this.$store.commit("setRefactorActionsArray", array);
      }
    },
    commitActions() {
      this.$store.commit("setBacklog", this.actions);
      this.$store.commit("setTodoActions", this.todoActions);
      this.$store.commit("setAlmostThere", this.almostThereActions);
      this.$store.commit("setDoneActions", this.doneActions);
      this.$store.commit("setReviewActions", this.reviewActions);
      this.$store.commit("setRefactorActionsArray", this.refactorActions);
    },
    parseNewActions() {
      getActionsByUser(this.currentUser.username).then((response) => {
        this.$store.commit("setUsersActions", response.data);
      });
      this.$store.state.backlogArray = this.$store.state.usersActions;
    },
    // findNewUniqueActions(){
    //   this.
    // }
  },
  computed: {
    ...mapGetters(["currentUser", "usersActions"]),
    ...mapMutations([
      "setBacklog",
      "setTodoActions",
      "setAlmostThere",
      "setDoneActions",
      "setReviewActions",
      "setRefactorActionsArray",
      "setUsersActions",
    ]),
  },
  mounted() {
    this.loadCategories();
    // this.loadActions();
    this.parseNewActions();
  },
};
</script>

<style>
.container-action {
  min-height: 300px;
  width: 15% !important;
  margin-right: 15px;
  margin-left: 10px;
}
.actions-wrapper {
  border-radius: 15px;
  margin-bottom: 15px;
}
.add-action-modal {
  position: fixed;
  z-index: 9998;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.5);
  display: table;
  transition: opacity 0.3s ease;
  display: table-cell;
  vertical-align: middle;
  margin-top: 50px;
}
.action-title {
  font-weight: bold;
  font-size: 18px;
}
.action-description {
  font-style: italic;
}
</style>