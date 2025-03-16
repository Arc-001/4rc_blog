<template>
    <div>
        <header class = "header">
            <p>
                header test
            </p>
            <nav>
                <ul>
                    <li><RouterLink to="/" @keyup = "Home"> [ Home ] </RouterLink></li>
                    <li><RouterLink to="/blog"> [ About ] </RouterLink></li>
                    <li><RouterLink to="/contact"> [ Contact ] </RouterLink></li>
                </ul>
            </nav>
        </header>
        
    </div>
</template>

<script>
export default{
    name: 'headersCustom'
}
</script>

<style scoped>
.header{
    background-color: #000000;
    textcolor:green;
    text-align: center;
    padding: 10px;
}
</style>