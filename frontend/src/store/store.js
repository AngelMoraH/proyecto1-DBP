import { defineStore } from 'pinia'

// useStore could be anything like useUser, useCart
// the first argument is a unique id of the store across your application
const baseURL = "http://localhost:5000/";
export const moviesStore = defineStore('movies', {
    state: () => ({
        movies: [],
        loading: false,
        error: null,
        movie: {},
    }),
    actions: {
        async getMovies(page) {
            this.movies = []
            this.loading = true
            try {
                this.movies = await fetch(baseURL + 'movies?page=' + page)
                    .then((response) => response.json()).then((data) => data.movies)


            } catch (error) {
                this.error = error
            } finally {
                this.loading = false
            }
        },
        async searchMovie(title) {
            this.movies = [];
            this.loading = true;
            try {
                this.movies = await fetch(baseURL + `movies?search=${title}`)
                .then(response => response.json())
                .then((data) => data.movies)
            } catch (error) {
                this.error = error
            } finally {
                this.loading = false
            }
        },
        async getMovieById(id) {
            this.movie={};
            this.loading = true;
            try {
                this.movie = await fetch(baseURL + `movies/${id}`)
                .then(response => response.json())
                .then((data) => data.movie)
            } catch (error) {
                this.error = error
            } finally {
                this.loading = false
            }
        }
    }
});

export const comentariosStore = defineStore('comentarios',{
    state : () => ({
        comentarios : [],
        loadingComentario : false,
        errorComentario : null,
    }),
    actions : {
        async getComentarios(movie_id) {
            this.comentarios = [];
            this.loadingComentario = true;
            try {
                this.comentarios = await fetch(baseURL + `comentarios/${movie_id}`)
                .then(response => response.json())
                .then((data) => data.comentarios)
            } catch (error) {
                this.errorComentario = error
            } finally {
                this.loadingComentario = false
            }
        },
        async addComentario(comentario,idUser,idMovie) {
            this.loadingComentario = true;
            try {
                await fetch(baseURL + `comentarios`, {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({
                        "data": {
                            "comentario": comentario,
                            "idUser": idUser,
                            "idMovie": idMovie
                        }
                    })
                })
            } catch (error) {
                this.errorComentario = error
            } finally {
                this.getComentarios(idMovie);
                this.loadingComentario = false
            }
        }
    }
});

export const userStore = defineStore('user', {
    state: () => ({
        user: null,
        islogged: false,
        loadingUser: false,
        errorUser: null,
        messageUser: null
    }),
    actions: {
        async login(email, password) {
            this.loadingUser = true;
            try {
                this.user = await fetch(baseURL + 'login/', {
                    method: 'POST',
                    body: JSON.stringify({ email:email, password:password }),
                    headers: {
                        'Content-Type': 'application/json'
                    }
                }).then((response) => response.json()).then((data) => data.user).catch((error) => {
                    this.errorUser = error
                })
                this.islogged = true;
            } catch (error) {
                
            } finally {
                this.loadingUser = false;
            }
        },
        async register(name, email, password) {
            this.loadingUser = true;
            try {
                this.user = await fetch(baseURL + 'register', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({ 'userName':name, 'email':email, 'password':password })
                }).then((response) => response.json()).then((data) => {
                    this.messageUser=data.message;
                    return data.user;
                })
            } catch (error) {
                this.errorUser = error
            } finally {
                this.loadingUser = false;
            }
        },
        async logout() {
            this.loadingUser=true;
            try {
                fetch(baseURL + 'logout')
                this.user = null;
                this.islogged = false;
            } catch (error) {
                this.errorUser = error
            } finally {
                this.loadingUser = false;
            }
        }
    }

});