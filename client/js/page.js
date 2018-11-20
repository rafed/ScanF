
var pageVue = new Vue({
    el: '#pagePanel',

    data: {
        currentPage:0,
        pages: []
    },

    methods: {
        getPages: function (id) {
            this.currentPage = id
            axios.get(scanfUrl + "/page/" + id)
                .then((response) => {
                    this.pages = response.data
                }, (error) => {
                    alert("An error occured")
                })
        },
        
        deletePage: function(id){
            axios.delete(scanfUrl + "/page/" + id)
                .then((response) => {
                    this.getPages(this.currentPage)
                }, (error) => {
                    alert("An error occured")
                })
        },

        eventPageClick: function(page_id){
            globalVue.$emit('eventPageClick', page_id)
        }
    },

    mounted() {
        globalVue.$on('eventWebsiteClick', function(website_id) {
            pageVue.getPages(website_id);
        })

        globalVue.$on('eventWebsitesRefreshed', ()=>{
            pageVue.getPages(pageVue.currentPage);
        })
    }
})
