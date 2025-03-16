<template>
    <div>
    <h1>Placeholder Blog</h1>
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

    <div class="container">
        <div v-for="(blog_summary, index) in blog_list" :key="index">
            <div class="row border-success">
                <h3>{{ blog_summary.title }}</h3>
                <h6 v-html = "renderMD(blog_summary.content)"></h6>
            </div>
        </div>
    </div>
    </div>
</template>

<script>

import MarkdownIt from 'markdown-it';
import {bare as emoji} from 'markdown-it-emoji';
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



export default {
    name: 'BlogCustom',
    data(){
        return{
            blog_list: [],
            md: null,
        }
    },
    methods:{
        async getBlog(){
            // blog_lst = fetch("https://api.placeholder.com/bloglist")
            // .then(response => response.json())
            // .then(data => this.blog = data)
            // .catch(error => console.log(error))
            this.blog_list = await new Promise((resolve)=> {
                setTimeout(()=>{
                    resolve([
                        {
                            title: "Blog 1",
                            content: `
                            ~ello~

                            \`\`\` ~python~
                            print("this is a test")
                            \`\`\`

                            `
                        },
                        {
                            title: "Blog 2",
                            content: "==Blog 2==\n\n :smile: This is~the~content of blog 2"
                        },
                        {
                            title: "Blog 3",
                            content: "# Blog 3\n\nThis is the content of blog 3 Check out this website: ![test_img](https://www.gstatic.com/images/branding/googlelogo/svg/googlelogo_clr_74x24px.svg)"
                        }
                    ])
                }, 1000)
            })
        },
        renderMD(content){
            return this.md?this.md.render(content):content
        }
    },
    created(){
        this.md = MarkdownIt({
            html: true,
            linkify: true,
            typographer: true,
        })
        this.md.use(emoji)                               // Emoji support :smile:
    .use(sub)                                 // Subscript ~sub~
    .use(sup)                                 // Superscript ^sup^
    .use(footnote)                            // Footnotes [^1]
    .use(deflist)                             // Definition lists
    .use(abbr)                                // Abbreviations
    .use(mark)                                // Marked text ==marked==
    .use(ins)                                 // Inserted text ++inserted++
    .use(tasklists, { enabled: true })        // Task lists [x]
    .use(katex)                               // KaTeX for math rendering
    .use(anchor, {                            // Add anchors to headers
      permalink: anchor.permalink.linkInsideHeader({
        symbol: '#',
        placement: 'before'
      })
    })
    .use(toc, {                               // Table of contents
      listType: 'ul',
      level: [1, 2, 3]
    });
        this.getBlog()
    }
}
</script>

<style scoped>
:deep(mark) {
    background-color: rgb(0, 0, 0); /* Remove default yellow highlight */
  color: #ff7700; /* Change text color to red (or any color you prefer) */
  font-weight: bold;
}
h1 {
    color: #333;
    font-size: 2em;
    margin-bottom: 0.5em;
}
</style>