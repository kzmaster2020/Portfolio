<template>
  <div class="home">
    <img alt="Vue logo" src="../assets/logo.png" />

    <div class="container" v-for='fighter in fighters' :key='fighter.pk'>
      <hr>
      <h2><router-link :to="{name: 'fighter', params: { first_name: fighter.id} }">{{fighter.first_name}} {{fighter.last_name}} <img v-if="!!fighter.picture" :src="fighter.picture" width="250px" style="border-radius:100%" /></router-link></h2>
      <p>{{fighter.id}}</p>
      <p>Weightclass: {{fighter.weight}}</p>
      <p>Created by: {{fighter.creator}}</p>
    </div>
    <div> 
      <p v-show="loadMore">...loading...</p>
      <button v-show="next" @click="getFighters" class="btn btn-sm btn-outline-success">Load More</button>
    </div>

  </div>
</template>

<script>
import { apiService } from "../common/api.service.js"; // Import your apiService
     // <img v-if="!!fighter.picture" :src="fighter.picture" width="250px" style="border-radius:100%" /> 


export default {
  name: "Home", // Give your file a name
  data(){
    return {
      fighters: [], // This is where your models will be stored. 
      next: null, 
      loadMore: false
    }
  },
  methods: {
    getFighters() {
      let endpoint = 'api/fightmanager/'; //The url where your models are coming from, refer to your urls.py 
      if (this.next) {
        endpoint = this.next;
      }
      this.loadMore = true
      apiService(endpoint)
        .then(data => {
          this.fighters.push(...data.results);
            this.loadMore = false;
          if (data.next) {
            this.next = data.next;
          } else {
            this.next = null;
          }
        })
    }
  },
  created() {
    this.getFighters()
    document.title = 'UFFC Roster'
  }
  
};
</script>
