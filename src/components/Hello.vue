<template>
  <div class="hello">
    <div class="jumbotron text-center">
      <h1>Bienvenue chez Torobhe Etoile</h1>
    </div>

    <div class="container">
      <div class="col-lg-6 col-lg-offset-3">
        <p class="h4"> Entrez vos noms d'utlisateur et mot de passe: </p>
      </div>
      <form>
        <div class="form-group">
          <div class="col-lg-6 col-lg-offset-3">
            <label for="email" class="h3">Adresse Email:</label>
            <input type="email" class="form-control" id="email">
          </div>
        </div>
        <div class="form-group">
          <div class="col-lg-6 col-lg-offset-3">
            <label for="pwd" class="h3">Mot de passe:</label>
            <input type="password" class="form-control" id="pwd">
          </div>
        </div>
        <div class="checkbox col-lg-6 col-lg-offset-3">
          <label><input type="checkbox" class="h3"> Se souvenir de moi</label>
        </div>
        <div class="col-lg-6 col-lg-offset-3">
          <button type="submit" class="btn btn-info">Ouvrir Session</button>
        </div>
      </form>
      <div class="col-lg-6 col-lg-offset-3">
        <p>En cas d'oubli de votre mot de passe il faut contacter l'administrateur</p>
      </div>
    </div>
  </div>

</template>

<script>
export default {
  name: 'hello',
  data () {
    return {
      msg: 'Welcome to Your Vue.js App'
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style>

</style>
