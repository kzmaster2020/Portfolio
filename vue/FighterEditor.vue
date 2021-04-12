<template>
    <div>

        <button class="btn btn-sm btn-outline-danger" @click='deleteFighter'>Delete</button>
    </div>
    
</template>

<script>
import { apiService } from '../common/api.service';
export default {
    name: 'FighterEditor',
    props: {
        first_name: {
            type: String, 
            required: true
        }
    }, 
    methods: {
        async deleteFighter() {
            let endpoint = `/api/fightmanager/${this.first_name}/`;
            try {
                await apiService(endpoint, 'DELETE');
                this.$router.push('/')
            }
            catch(err) {
                console.log(err);
            }
        }
    }
}
</script>