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
                .then((data) => data.movie)
                
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
})