<template>
    <div >
        <strong>{{this.data['comentario']}}</strong>
        <strong>{{this.data['dateCreated']}}</strong>
        <strong>{{this.data['likes']}}</strong>
        <div>
            <i class="fa-solid fa-thumbs-up"></i>
            <p>{{this.data['likes']}}</p>
        </div>
    </div>
</template>

<script setup>

const props = defineProps ({
    id: {
        type: String,
        required: true
    },
    data: {
        type: Object,
        required: true
    }
})
</script>

<style lang="scss" scoped>
i{
    color:rgb(180, 99, 99);
}
i:hover{
    color:rgb(202, 52, 52);
}
</style>