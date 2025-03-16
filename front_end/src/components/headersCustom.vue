
<template>
    <div>    
        <header class = "header">
            <h1>Header</h1>
            <div class="navbar">
                <div class = "container text-left">
                    <div class = "col">
                        <RouterLink to="/" @keyup = "Home" class = "terminal-nav-link"> [ Home ] </RouterLink>
                    </div>
                    <div class = "col">
                        <RouterLink to="/blog" class = "terminal-nav-link"> [ About ] </RouterLink>
                    </div>
                    <div class = "col">
                        <RouterLink to="/contact" class = "terminal-nav-link"> [ Contact ] </RouterLink>
                    </div>
                </div>
            </div>
        </header>
        
    </div>
</template>

<script>
export default{
    name: 'headersCustom'
}
</script>


<style scoped>
.terminal-header {
  background-color: #1a1a1a;
  color: #f8f8f2;
  padding: 10px 15px;
  display: flex;
  align-items: center;
  border-bottom: 1px solid #333;
  border-top-left-radius: 6px;
  border-top-right-radius: 6px;
}

.terminal-window-controls {
  display: flex;
  margin-right: 15px;
}

.control {
  width: 12px;
  height: 12px;
  border-radius: 50%;
  margin-right: 8px;
}

.close {
  background-color: #ff5f56;
}

.minimize {
  background-color: #ffbd2e;
}

.maximize {
  background-color: #27c93f;
}

.terminal-title {
  flex-grow: 1;
  font-family: 'Fira Code', monospace;
  font-size: 14px;
  color: #66d9ef;
}

.terminal-nav {
  display: flex;
  gap: 20px;
}

.terminal-nav-link {
  color: #a6e22e;
  text-decoration: none;
  font-family: 'Fira Code', monospace;
  font-size: 14px;
  padding: 4px 8px;
  border: none;
}

.terminal-nav-link:hover, .router-link-active {
  color: #f92672;
  background-color: rgba(255, 255, 255, 0.05);
  border-radius: 3px;
}
</style>