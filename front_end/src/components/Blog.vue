<template>


    <div class="container">
        <div v-for="(blog_summary, index) in blog_list" :key="index">
            <div class="row border-success">
                <RouterLink :to="`/blog/${blog_summary.uid}`" class="link"><h3>{{ blog_summary.title }}</h3></RouterLink>
                <h6 v-html = "renderMD(blog_summary.content)"></h6>
            </div>
        </div>
    </div>

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
    name: 'BlogCustom',
    data(){
        return{
            blog_list: [],
            md: null,
            blog_url_list: []
        }
    },
    methods:{
        // fetch json look like this:
        // {
        //     "blog_list": [
                // {
                //     "title": "Blog 1",
                        // "uid": "1",
                //     "content_summary": "This is the content of blog 1"
                // },
                // {
                //     "title": "Blog 2",
                //      uid: "2",
                //     "content_seuumay": "This is the content of blog 2"
                // },
                // {
                //     "title": "Blog 3",
                //      uid: "3",
                //     "content_summary": "This is the content of blog 3"
                // }
        //}
        make_blog_url_list(){
            this.blog_list.forEach((blog) => {
                this.blog_url_list.push({
                    title: blog.title,
                    url: `/blog/${blog.uid}`
                })
            })
        },
        async getBlog(){
            fetch("https://api.4rc.in/api/blogs")
                .then(response => response.json())
                .then(data => this.blog_list = data)
                .catch(error => console.log(error))

            // this.blog_list = await new Promise((resolve)=> {
            //     setTimeout(()=>{
            //         resolve([
            //             {
            //                 title: "Blog 1",
            //                 content: `
            //                 $ sqrt() O(log_2(n)) $
            //                 `
            //             },
            //             {
            //                 title: "Blog 2",
            //                 content: "==Blog 2==\n\n :smile: This is~the~content of blog 2 $\\sqrt{3x-1} + (1+x)^2$"
            //             },
            //             {
            //                 title: "Blog 3",
            //                 content: "# Blog 3\n\nThis is the content of blog 3 Check out this website: ![test_img](https://www.gstatic.com/images/branding/googlelogo/svg/googlelogo_clr_74x24px.svg)"
            //             }
            //         ])
            //     }, 1000)
            // })
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
        this.md.use(sub)                                 // Subscript ~sub~
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
        this.make_blog_url_list()
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
.link{
    color: #ff7700;
    text-decoration: none;
    font-weight: bold;
}
.link:hover {
    color: #ff7711;
    transform: skewX(-10deg);
    transition: transform 0.1s ease-in-out, color 0.3s ease-in-out; /* Add transition */
}
</style>
                                                                                           