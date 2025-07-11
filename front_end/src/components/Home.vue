<template>
    <div>
    <img ref="gifImage" src="@/assets/2.gif" alt="into" style="width: 450px;height: 20px; background-blend-mode: darken;" @load="pauseGif">

</template>

<script>
export default {
    name: 'HomeCustom',
    methods: {
        pauseGif() {
            const img = this.$refs.gifImage;
            if (img) {
                const gifSrc = img.src;
                img.src = gifSrc;
            }
        }
    }
}
</script>
    <h1>Placeholder Home</h1>
    <p>Lorem ipsum dolor sit amet.</p>
    <p>Laboriosam, consequuntur nulla. Vel, voluptas.</p>
    <p>Vitae tempora veritatis ratione! Dolor!</p>
    <p>Alias debitis provident nam aliquam.</p>
    <p>Sunt, minima amet? Consectetur, ipsam.</p>
    <p>Odio ad voluptas laboriosam. Dignissimos!</p>
    <p>Temporibus porro consectetur consequuntur ipsum!</p>
    <p>Vel vero modi ex commodi.</p>
    <p>Totam, quo aperiam! Unde, non?</p>
    <p>Veniam cupiditate maiores sapiente impedit.</p>
    </div>
</template>

<script>
export default {
    name: 'HomeCustom'
}
</script>

<style scoped>
h1 {
    color: #333;
    font-size: 2em;
    margin-bottom: 0.5em;
}
</style>