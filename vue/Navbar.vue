<template>
    <nav class="navbar navbar-expand-lg navbar-light bg-light my-navbar">
        <div class="container">
                    <router-link :to="{ name: 'Home'}" class="navbar-brand">UFFC</router-link>

            <div class="collapse navbar-collapse" id="navbarSupportedContent">
                <ul class="navbar-nav mr-auto">
                <li class="nav-item active">
                    <router-link :to="{ name: 'Home'}" class="btn btn-small btn-success">Home</router-link>
                </li>
                <li class="nav-item">
                    <li class="nav-item active">
                    <router-link :to="{ name: 'FightCreator'}" class="btn btn-small btn-danger">Create Fighter</router-link>
                </li>
 
                <li class="nav-item dropdown">
                    <a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                    Rankings and Events
                    </a>
                    <div class="dropdown-menu" aria-labelledby="navbarDropdown">
                    <router-link :to="{ name: 'Lightweight_Rank'}"><a class="dropdown-item" href="#">Lightweight</a></router-link>
                    <router-link :to="{ name: 'Heavyweight_Rank'}"><a class="dropdown-item" href="#">Heavyweight</a></router-link>
                    <router-link :to="{ name: 'Titan'}"><a class="dropdown-item" href="#">Titan</a></router-link>

                    <div class="dropdown-divider"></div>
                   <router-link :to="{ name: 'Event_List'}"> <a class="dropdown-item" href="#">Events</a></router-link>
                    </div>
                </li>
                <li class="nav-item">
                    <a class="btn btn-small btn-outline-secondary" href="/accounts/logout/">Logout</a>
                </li>
                </ul>

            </div>
        </div>
</nav>
</template>
<script>

export default {
    
    name: 'NavbarComponent'
  
}
</script>
<style scoped>
    .my-navbar {
        border-bottom: 3px solid black;
    }
    .navbar-brand {
        font-weight: bold;
        font-size: 190%;

    }
    .navbar-brand:hover {
        color: yellow !important;
    }
</style>