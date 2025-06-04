<template>

    <h1>{{ this.title }}</h1>
    <div v-html="renderMD(content)"></div>

</template>

<script>

import MarkdownIt from 'markdown-it';
import sub from 'markdown-it-sub';
import sup from 'markdown-it-sup';
import footnote from 'markdown-it-footnote';
import deflist from 'markdown-it-deflist';
import abbr from 'markdown-it-abbr';
import mark from 'markdown-it-mark';
import ins from 'markdown-it-ins';
import anchor from 'markdown-it-anchor';
import toc from 'markdown-it-toc-done-right';
import tasklists from 'markdown-it-task-lists';
import katex from 'markdown-it-katex';
import 'katex/dist/katex.min.css';

export default {
    name: 'BlogView',
    parameters: {
        uid: {
            type: String,
        }
    },
    data(){
        return{
            title: "",
            content: "",
            md: null,
        }
    },
    methods:{
        renderMD(content){
            return this.md?this.md.render(content):content
        },
        fetchBlog(uid){
            /*
            the api returns blog as 
            {
                "title": "Blog Title",
                "content": "Blog content in markdown format"
            }
            */
            fetch("http://0.0.0.0:8000/api/blog/"+uid)
            .then(response => response.json())
            .then(data => {
                this.title = data.title;
                this.content = data.content;
            })
            .catch(error => {
                console.error("Error fetching blog:", error);
            });
        }
    },
    created() {
        this.md = new MarkdownIt()
            .use(sub)
            .use(sup)
            .use(footnote)
            .use(deflist)
            .use(abbr)
            .use(mark)
            .use(ins)
            .use(anchor)
            .use(toc)
            .use(tasklists)
            .use(katex);

        this.fetchBlog(this.$route.params.uid);
    }
}

</script>

